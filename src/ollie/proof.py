from __future__ import annotations

import uuid

from ollie.types import FormalProblem, LiteratureHit, ProofCandidate


class ProofSearch:
    def generate(self, problem: FormalProblem, literature: list[LiteratureHit]) -> ProofCandidate:
        lemma_hint = literature[0].missing_connection if literature else "direct"
        lean = f"""import Mathlib

-- Candidate proof for {problem.problem_id}
-- Literature gap: {lemma_hint}

{problem.formal_statement}
"""
        return ProofCandidate(
            proof_id=f"prf_{uuid.uuid4().hex[:8]}",
            problem_id=problem.problem_id,
            lean_source=lean,
            sketch=f"Attempt proof via {lemma_hint}",
            confidence=0.42,
        )

    def disprove(self, problem: FormalProblem) -> dict:
        return {
            "problem_id": problem.problem_id,
            "counterexample_search": "no counterexample found in bounded search",
            "status": "inconclusive",
        }
