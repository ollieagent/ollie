from __future__ import annotations

from ollie.challenge import ChallengeBoard
from ollie.config import OllieSettings, load_settings
from ollie.formalize import Formalizer
from ollie.lean import LeanVerifier
from ollie.ledger import ResearchLedger
from ollie.literature import LiteratureSearch
from ollie.proof import ProofSearch
from ollie.sandbox import ComputeSandbox
from ollie.types import ClaimStatus
from ollie.wallet import BountyWallet


class OllieRuntime:
    def __init__(self, settings: OllieSettings | None = None) -> None:
        self.settings = settings or load_settings()
        self.formalize_engine = Formalizer()
        self.literature = LiteratureSearch()
        self.proof = ProofSearch()
        self.lean = LeanVerifier(self.settings)
        self.sandbox = ComputeSandbox()
        self.challenge = ChallengeBoard()
        self.ledger = ResearchLedger()
        self.wallet = BountyWallet(self.settings)

    @classmethod
    def from_env(cls) -> "OllieRuntime":
        return cls(load_settings())

    def formalize(self, informal: str):
        return self.formalize_engine.formalize(informal)

    def publish_claim(self, problem, candidate, lean_ok: bool, human_ok: bool = False) -> ClaimStatus:
        if not lean_ok:
            status: ClaimStatus = "candidate"
        elif not human_ok:
            status = "lean_verified"
        else:
            status = "human_accepted"
        if self.settings.REQUIRE_LEAN_VERIFICATION and not lean_ok and status != "candidate":
            status = "candidate"
        self.ledger.publish(problem.problem_id, candidate, status)
        return status
