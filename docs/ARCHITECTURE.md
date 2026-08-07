# Ollie architecture

Ollie enforces a strict epistemic pipeline: **no solved theorem without Lean + human + reproduction**.

## Claim lifecycle

```
conjecture → candidate → lean_verified → human_accepted → reproduced → bounty_eligible
```

Backward transitions (e.g. `lean_verified` → `refuted`) are recorded explicitly in the ledger.

## Components

| Layer | Responsibility |
|-------|----------------|
| Astra reasoning | Proof search, disproof search, literature synthesis |
| Formalization | Map natural language to Lean-ready statements |
| Lean runner | Subprocess `lake build` / `#eval` checks |
| Sandbox | CPU-bound experiments without network egress |
| Challenge | Reviewer tokens, reproduction attestations |
| Ledger | Hash-chained public record |
| Wallet | Policy-gated bounty disbursement |

## On-chain vs off-chain

| Off-chain | On-chain (optional) |
|-----------|------------------------|
| Full proof artifacts | Claim hash + status |
| Lean source | Reviewer attestation hash |
| Simulation logs | Bounty payout receipt |

## Wallet rules

- Allowlisted reviewer addresses
- Cap per claim and per day
- Mainnet disabled by default
- Payout only in `reproduced` state
