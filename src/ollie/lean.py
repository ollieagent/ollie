from __future__ import annotations

import subprocess
from pathlib import Path

from ollie.config import OllieSettings
from ollie.types import LeanResult, ProofCandidate


class LeanVerifier:
    def __init__(self, settings: OllieSettings) -> None:
        self.settings = settings

    def verify(self, candidate: ProofCandidate) -> LeanResult:
        project = Path(self.settings.LEAN_PROJECT)
        tmp = project / "OllieCandidate.lean"
        tmp.write_text(candidate.lean_source, encoding="utf-8")
        try:
            proc = subprocess.run(
                ["lake", "build"],
                cwd=project,
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )
            return LeanResult(
                success=proc.returncode == 0,
                stdout=proc.stdout[-4000:],
                stderr=proc.stderr[-4000:],
            )
        except FileNotFoundError:
            return LeanResult(success=False, stdout="", stderr="lean/lake not installed")
        except subprocess.TimeoutExpired:
            return LeanResult(success=False, stdout="", stderr="lean build timeout")
