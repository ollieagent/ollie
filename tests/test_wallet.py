from ollie.config import OllieSettings
from ollie.wallet import BountyIntent, BountyWallet


def test_wallet_requires_reproduction():
    w = BountyWallet(OllieSettings())
    r = w.release(BountyIntent("led_1", "reviewer_alpha", 0.1, "review"), reproduced=False)
    assert r["released"] is False
