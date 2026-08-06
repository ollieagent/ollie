from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

ClaimStatus = Literal[
    "conjecture",
    "candidate",
    "lean_verified",
    "human_accepted",
    "reproduced",
    "refuted",
]


@dataclass
class FormalProblem:
    problem_id: str
    informal: str
    formal_statement: str
    assumptions: list[str] = field(default_factory=list)
    goal: str = ""


@dataclass
class LiteratureHit:
    title: str
    authors: list[str]
    year: int
    relevance: float
    missing_connection: str | None = None


@dataclass
class ProofCandidate:
    proof_id: str
    problem_id: str
    lean_source: str
    sketch: str
    confidence: float


@dataclass
class LeanResult:
    success: bool
    stdout: str
    stderr: str


@dataclass
class LedgerEntry:
    entry_id: str
    problem_id: str
    status: ClaimStatus
    proof_hash: str
    timestamp: str
    prev_hash: str
    record_hash: str
