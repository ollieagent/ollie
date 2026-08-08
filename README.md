# Ollie

**Autonomous mathematical-discovery agent powered by OpenAI's Astra research model.**

Ollie works on unsolved problems in mathematics and theoretical computer science: formalizing conjectures, searching literature, generating candidate proofs, checking them in Lean, and publishing results only after formal verification and independent human review.

> AI agents started by writing code. Now they may be solving problems mathematicians have worked on for decades. Ollie is an autonomous research agent designed to turn frontier AI reasoning into **verifiable** discoveries, with every proof formally checked, independently reviewed, and recorded publicly.

## Background

OpenAI has reportedly told US officials that its experimental **Astra** model has solved or substantially advanced **10 longstanding problems** in mathematics and theoretical computer science ([Axios](https://www.axios.com/newsletters/axios-am-e6e15a72-3b81-4056-9657-5c07f9825685)). Ollie is the research infrastructure layer around that capability: not merely generating text, but producing claims that survive formal checking, independent challenge, and public audit.

This repository is inspired by the public release pattern of [OpenAI IMO 2025 Proofs](https://github.com/aw31/openai-imo-2025-proofs) — proofs and artifacts, not hype.

## What Ollie does

| Stage | Description |
|-------|-------------|
| **Problem intake** | Accept informal conjectures; produce formal definitions and proof obligations |
| **Literature search** | Map prior work; identify missing lemmas and unexplored connections |
| **Proof search** | Generate candidate proofs; actively search for counterexamples and disproofs |
| **Formal verification** | Check proofs in Lean (extensible to other proof assistants) |
| **Experimentation** | Run simulations and computations in isolated sandboxes |
| **Peer challenge** | Invite independent researchers to reproduce or refute results |
| **Research ledger** | Timestamped public record of claims, evidence, and status |
| **Bounty wallet** | Restricted ETH/SOL payments for compute, review, and verified reproduction |

## What Ollie never does

Ollie **does not**:

- Claim a theorem is solved before Lean verification **and** required human sign-off
- Release bounty funds before independent reviewers reproduce a result
- Store unrestricted access to production keys or unaudited mainnet treasuries
- Publish unverified "proof sketches" as solved theorems
- Operate outside an approved research scope

Status labels on every claim: `conjecture` → `candidate` → `lean_verified` → `human_accepted` → `reproduced`.

## Architecture

```
Informal problem ──► formalization ──► literature graph
                           │
                           ▼
                    proof / disproof search (Astra)
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         Lean check    sandbox      counterexample hunt
              │            │            │
              └────────────┼────────────┘
                           ▼
                  research ledger (public hash chain)
                           │
                           ▼
              bounty wallet (after reproduction)
```

| Module | Role |
|--------|------|
| `ollie/formalize` | Informal → formal problem statements |
| `ollie/literature` | Citation graph and gap detection |
| `ollie/proof` | Candidate proof generation and critique |
| `ollie/lean` | Lean 4 verification interface |
| `ollie/sandbox` | Isolated compute for experiments |
| `ollie/challenge` | Independent reviewer workflow |
| `ollie/ledger` | Public timestamped research record |
| `ollie/wallet` | Restricted ETH/SOL bounties |
| `ollie/runtime` | Orchestration and policy gates |

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Research wallets

Ollie operates restricted wallets for **research bounties**, **compute costs**, and **verified peer review** — not general custody.

| Network | Address |
|---------|---------|
| Solana | `AgTeY89y1cfPxn5t5fxY6quWW4cjsi937LzTma5zJtuZ` |
| Ethereum | `0x1e370583abaD95Fb641592b2FDD071ed5b525D01` |

> Verify addresses through official project channels before transferring funds. Bounties release only after documented reproduction.

## Setup

### Requirements

- Python 3.10+
- Lean 4 toolchain (for local verification)
- OpenAI API access with Astra / research model entitlement (when available)

### Installation

```bash
git clone https://github.com/agentAegis/ollie.git
cd ollie
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

### Lean project

```bash
cd formal/ollie
lake build
```

## Usage

### Formalize a conjecture

```bash
python -m ollie formalize \
  --input "Every bounded-degree expander has a linear-size spectral gap" \
  --output problems/expander_gap.json
```

### Run proof search

```bash
python -m ollie prove \
  --problem problems/expander_gap.json \
  --attempts 8 \
  --output proofs/expander_gap_candidate.lean
```

### Verify in Lean

```bash
python -m ollie verify --proof proofs/expander_gap_candidate.lean
```

### Publish to ledger (does not imply acceptance)

```bash
python -m ollie publish \
  --problem problems/expander_gap.json \
  --proof proofs/expander_gap_candidate.lean \
  --status candidate
```

### Python API

```python
from ollie import OllieRuntime

rt = OllieRuntime.from_env()
problem = rt.formalize("P vs NP separation via ...")
literature = rt.literature.search(problem)
candidate = rt.proof.search(problem, literature)
check = rt.lean.verify(candidate.lean_source)

if check.success:
    entry = rt.ledger.publish(problem, candidate, status="lean_verified")
    rt.challenge.invite_reviewers(entry)
```

## Bounty policy

1. Claim enters ledger with evidence bundle
2. Independent reviewers attempt reproduction
3. After `REQUIRE_REPRODUCTION_FOR_BOUNTY` confirmations, wallet releases payment
4. All payouts logged onchain as hashes (not private notes)

## Contents

- [Setup](#setup)
- [Usage](#usage)
- [Architecture](#architecture)
- [Research wallets](#research-wallets)
- [Bounty policy](#bounty-policy)
- [Citation](#citation)
- [License](#license)

## Citation

If you use Ollie in academic work, please cite this repository and relevant OpenAI research publications when available.

```bibtex
@software{ollie2026,
  author = {Alexander Wei},
  title  = {Ollie: Autonomous mathematical-discovery agent},
  year   = {2026},
  url    = {https://github.com/agentAegis/ollie}
}
```

## Maintainer

**Alexander Wei** ([@aw31](https://github.com/aw31))

## License

MIT License — Copyright © 2026 Alexander Wei.

---

**Ollie** — frontier reasoning, formally checked, independently reproduced, publicly recorded.
