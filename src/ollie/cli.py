from __future__ import annotations

import argparse
import json

from ollie.runtime import OllieRuntime


def main() -> None:
    parser = argparse.ArgumentParser(prog="ollie")
    sub = parser.add_subparsers(dest="cmd")

    p_f = sub.add_parser("formalize")
    p_f.add_argument("--input", required=True)
    p_f.add_argument("--output", required=True)

    p_p = sub.add_parser("prove")
    p_p.add_argument("--problem", required=True)
    p_p.add_argument("--output", required=True)

    p_v = sub.add_parser("verify")
    p_v.add_argument("--proof", required=True)

    p_pub = sub.add_parser("publish")
    p_pub.add_argument("--problem", required=True)
    p_pub.add_argument("--proof", required=True)
    p_pub.add_argument("--status", default="candidate")

    args = parser.parse_args()
    rt = OllieRuntime.from_env()

    if args.cmd == "formalize":
        prob = rt.formalize(args.input)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(prob.__dict__, f, indent=2)
    elif args.cmd == "prove":
        with open(args.problem, encoding="utf-8") as f:
            data = json.load(f)
        from ollie.types import FormalProblem

        prob = FormalProblem(**data)
        lit = rt.literature.search(prob)
        cand = rt.proof.generate(prob, lit)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(cand.lean_source)
    elif args.cmd == "verify":
        from pathlib import Path
        from ollie.types import ProofCandidate

        text = Path(args.proof).read_text(encoding="utf-8")
        cand = ProofCandidate("manual", "manual", text, "", 0.0)
        result = rt.lean.verify(cand)
        print(json.dumps(result.__dict__, indent=2))
    elif args.cmd == "publish":
        print("Use runtime API for ledger publish in this scaffold")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
