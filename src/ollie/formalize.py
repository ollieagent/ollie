from __future__ import annotations

import hashlib
import re

from ollie.types import FormalProblem


class Formalizer:
    def formalize(self, informal: str) -> FormalProblem:
        pid = hashlib.sha256(informal.encode()).hexdigest()[:10]
        cleaned = re.sub(r"\s+", " ", informal.strip())
        return FormalProblem(
            problem_id=f"prb_{pid}",
            informal=cleaned,
            formal_statement=f"theorem ollie_{pid} : True := by sorry -- scaffold from: {cleaned[:80]}",
            assumptions=["standard axioms"],
            goal=cleaned,
        )
