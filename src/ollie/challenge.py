from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ReviewChallenge:
    challenge_id: str
    entry_id: str
    reviewers: list[str] = field(default_factory=list)
    reproductions: list[str] = field(default_factory=list)


class ChallengeBoard:
    def __init__(self, required_reproductions: int = 2) -> None:
        self.required = required_reproductions
        self.challenges: dict[str, ReviewChallenge] = {}

    def invite(self, entry_id: str, reviewers: list[str]) -> ReviewChallenge:
        ch = ReviewChallenge(challenge_id=f"chl_{len(self.challenges)+1}", entry_id=entry_id, reviewers=reviewers)
        self.challenges[ch.challenge_id] = ch
        return ch

    def record_reproduction(self, challenge_id: str, reviewer: str) -> bool:
        ch = self.challenges[challenge_id]
        if reviewer not in ch.reproductions:
            ch.reproductions.append(reviewer)
        return len(ch.reproductions) >= self.required
