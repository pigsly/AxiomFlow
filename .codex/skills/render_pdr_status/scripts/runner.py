#!/usr/bin/env python3

import json
import os
import sys
from dataclasses import dataclass
from typing import Any
from pathlib import Path


@dataclass
class Breakdown:
    req_spec_alignment: int
    adr_alignment: int
    execution_clarity: int


@dataclass
class SafetyGates:
    required_docs_present: bool
    references_resolved: bool
    contract_safety: str


@dataclass
class PdrStatus:
    overall_signal: str
    alignment_score: int
    breakdown: Breakdown
    safety_gates: SafetyGates


def default_status() -> PdrStatus:
    return PdrStatus(
        overall_signal="Review Suggested",
        alignment_score=86,
        breakdown=Breakdown(
            req_spec_alignment=45,
            adr_alignment=27,
            execution_clarity=14,
        ),
        safety_gates=SafetyGates(
            required_docs_present=True,
            references_resolved=True,
            contract_safety="Needs Clarification",
        ),
    )


def maybe_reexec_into_repo_venv() -> None:
    repo_root = Path(__file__).resolve().parents[4]
    venv_root = repo_root / ".venv"
    venv_python = repo_root / ".venv" / "bin" / "python"

    if os.environ.get("AXIOMFLOW_VENV_REEXEC") == "1":
        return

    if not venv_python.exists():
        return

    current_prefix = Path(sys.prefix).resolve()
    if current_prefix == venv_root.resolve():
        return

    env = os.environ.copy()
    env["AXIOMFLOW_VENV_REEXEC"] = "1"
    os.execve(str(venv_python), [str(venv_python), __file__, *sys.argv[1:]], env)


def parse_status(data: dict[str, Any]) -> PdrStatus:
    breakdown = data.get("breakdown", {})
    safety_gates = data.get("safety_gates", {})
    contract_safety = safety_gates.get("contract_safety", "Needs Clarification")
    if isinstance(contract_safety, bool):
        contract_safety = "OK" if contract_safety else "Needs Clarification"
    return PdrStatus(
        overall_signal=str(data.get("overall_signal", "Review Suggested")),
        alignment_score=int(data.get("alignment_score", 0)),
        breakdown=Breakdown(
            req_spec_alignment=int(breakdown.get("req_spec_alignment", 0)),
            adr_alignment=int(breakdown.get("adr_alignment", 0)),
            execution_clarity=int(breakdown.get("execution_clarity", 0)),
        ),
        safety_gates=SafetyGates(
            required_docs_present=bool(safety_gates.get("required_docs_present", False)),
            references_resolved=bool(safety_gates.get("references_resolved", False)),
            contract_safety=str(contract_safety),
        ),
    )


def read_status() -> PdrStatus:
    raw = sys.stdin.read().strip()
    if not raw:
        return default_status()

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return default_status()

    if not isinstance(parsed, dict):
        return default_status()

    return parse_status(parsed)


def bool_signal(value: bool) -> str:
    return "OK" if value else "Review"


def contract_safety_signal(value: str) -> str:
    normalized = value.strip().lower()
    if normalized == "ok":
        return "OK"
    if normalized == "conflict detected":
        return "Conflict Detected"
    return "Needs Clarification"


def render_rich_panel(status: PdrStatus) -> str:
    try:
        from rich import box
        from io import StringIO
        from rich.console import Console
        from rich.panel import Panel
        from rich.table import Table
        from rich.text import Text
    except ImportError:
        raise RuntimeError("rich_panel mode requires the 'rich' package")

    table = Table.grid(padding=(0, 1))
    table.add_column(justify="left", style="bold")
    table.add_column(justify="left")

    rows = [
        ("Overall Signal", status.overall_signal),
        ("Alignment Score", f"{status.alignment_score}/100"),
        ("REQ / SPEC", f"{status.breakdown.req_spec_alignment}/50"),
        ("ADR Alignment", f"{status.breakdown.adr_alignment}/30"),
        ("Execution Clarity", f"{status.breakdown.execution_clarity}/20"),
        ("Required Docs", bool_signal(status.safety_gates.required_docs_present)),
        ("References", bool_signal(status.safety_gates.references_resolved)),
        ("Contract Safety", contract_safety_signal(status.safety_gates.contract_safety)),
    ]

    for label, value in rows:
        table.add_row(f"{label}:", value)

    title = Text("AxiomFlow PDR Status", style="bold")
    buffer = StringIO()
    console = Console(file=buffer, width=39)
    console.print(
        Panel(
            table,
            title=title,
            border_style="white",
            box=box.ROUNDED,
            padding=(1, 1),
        )
    )
    return buffer.getvalue()



def main() -> int:
    maybe_reexec_into_repo_venv()
    status = read_status()
    render_mode = os.getenv("RENDER_MODE", "rich_panel")
    if render_mode != "rich_panel":
        sys.stderr.write(
            f"Unsupported RENDER_MODE '{render_mode}'. render_pdr_status only accepts 'rich_panel'.\n"
        )
        return 2

    try:
        sys.stdout.write(render_rich_panel(status))
    except RuntimeError as exc:
        sys.stderr.write(f"{exc}\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
