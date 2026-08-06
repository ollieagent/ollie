from __future__ import annotations

from ollie.types import FormalProblem, LiteratureHit


class LiteratureSearch:
    def search(self, problem: FormalProblem, limit: int = 5) -> list[LiteratureHit]:
        seed = problem.problem_id
        return [
            LiteratureHit(
                title=f"Related work on {problem.goal[:40]}",
                authors=["Author A", "Author B"],
                year=2024,
                relevance=0.81,
                missing_connection="No prior reduction to spectral gap bound",
            ),
            LiteratureHit(
                title="Foundations reference",
                authors=["Classic Source"],
                year=2010,
                relevance=0.55,
            ),
        ][:limit]
