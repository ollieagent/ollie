from ollie.ledger import ResearchLedger
from ollie.types import ProofCandidate


def test_ledger_chain():
    ledger = ResearchLedger()
    c = ProofCandidate("p1", "prb_1", "theorem t : True := by trivial", "", 1.0)
    ledger.publish("prb_1", c, "candidate")
    ledger.publish("prb_1", c, "lean_verified")
    assert ledger.verify_chain()
