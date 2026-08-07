from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone

from ollie.types import ClaimStatus, LedgerEntry, ProofCandidate


class ResearchLedger:
    def __init__(self) -> None:
        self.entries: list[LedgerEntry] = []

    @staticmethod
    def hash_proof(candidate: ProofCandidate) -> str:
        return "sha256:" + hashlib.sha256(candidate.lean_source.encode()).hexdigest()

    def publish(self, problem_id: str, candidate: ProofCandidate, status: ClaimStatus) -> LedgerEntry:
        prev = self.entries[-1].record_hash if self.entries else "genesis"
        body = {
            "problem_id": problem_id,
            "status": status,
            "proof_hash": self.hash_proof(candidate),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "prev_hash": prev,
        }
        record_hash = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
        entry = LedgerEntry(
            entry_id=f"led_{len(self.entries)+1}",
            problem_id=problem_id,
            status=status,
            proof_hash=body["proof_hash"],
            timestamp=body["timestamp"],
            prev_hash=prev,
            record_hash=record_hash,
        )
        self.entries.append(entry)
        return entry

    def verify_chain(self) -> bool:
        for i, e in enumerate(self.entries):
            expected = self.entries[i - 1].record_hash if i else "genesis"
            if e.prev_hash != expected:
                return False
        return True
