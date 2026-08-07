from __future__ import annotations

from dataclasses import dataclass

from ollie.config import OllieSettings


@dataclass
class BountyIntent:
    claim_id: str
    reviewer: str
    amount_eth: float
    reason: str


class BountyWallet:
    ALLOWED_REVIEWERS = {"reviewer_alpha", "reviewer_beta", "reviewer_gamma"}

    def __init__(self, settings: OllieSettings) -> None:
        self.settings = settings
        self.released_eth = 0.0
        self.cap_eth = 10.0

    def addresses(self) -> dict[str, str]:
        return {
            "solana": self.settings.OLLIE_SOLANA_ADDRESS,
            "ethereum": self.settings.OLLIE_EVM_ADDRESS,
        }

    def release(self, intent: BountyIntent, reproduced: bool) -> dict:
        if not reproduced:
            return {"released": False, "reason": "reproduction not confirmed"}
        if intent.reviewer not in self.ALLOWED_REVIEWERS:
            return {"released": False, "reason": "reviewer not allowlisted"}
        if self.released_eth + intent.amount_eth > self.cap_eth:
            return {"released": False, "reason": "bounty cap exceeded"}
        if not self.settings.REQUIRE_REPRODUCTION_FOR_BOUNTY:
            return {"released": False, "reason": "policy requires reproduction"}
        self.released_eth += intent.amount_eth
        mode = "testnet" if not self.settings.MAINNET_ENABLED else "mainnet_pending_approval"
        return {"released": True, "mode": mode, "intent": intent}
