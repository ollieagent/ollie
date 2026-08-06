from ollie.formalize import Formalizer


def test_formalize_produces_theorem():
    p = Formalizer().formalize("Test conjecture")
    assert p.problem_id.startswith("prb_")
    assert "theorem" in p.formal_statement
