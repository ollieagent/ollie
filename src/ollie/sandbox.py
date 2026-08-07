from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass


@dataclass
class ExperimentResult:
    experiment_id: str
    stdout: str
    success: bool


class ComputeSandbox:
    """Isolated numeric experiments — no network."""

    def run(self, code: str, inputs: dict) -> ExperimentResult:
        # Safe subset: evaluate arithmetic expressions only (demo scaffold)
        expr = str(inputs.get("expr", "1+1"))
        allowed = set("0123456789+-*/(). ")
        if not set(expr) <= allowed:
            return ExperimentResult("exp_fail", "disallowed expression", False)
        try:
            val = eval(expr, {"__builtins__": {}}, {})  # noqa: S307 demo only
            return ExperimentResult(
                f"exp_{hashlib.sha256(code.encode()).hexdigest()[:8]}",
                json.dumps({"result": val}),
                True,
            )
        except Exception as e:  # noqa: BLE001
            return ExperimentResult("exp_err", str(e), False)
