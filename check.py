#!/usr/bin/env python3
"""Compare your predictions in predictions.py against what the code does.

A prediction that does not match is a finding, not a failure. Run this as
often as you like.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "app"))

import orders  # noqa: E402  (must follow the sys.path line above)
from predictions import PREDICTIONS  # noqa: E402


def run(call):
    return eval(call, vars(orders).copy())  # noqa: S307 — our own fixed strings


def main():
    filled = {c: p for c, p in PREDICTIONS.items() if p is not None}
    matched, rows = 0, []

    for call, predicted in PREDICTIONS.items():
        try:
            actual = run(call)
        except Exception as error:
            actual = f"{type(error).__name__}: {error}"
        if predicted is None:
            rows.append((call, "not filled in", actual, " "))
        elif predicted == actual:
            matched += 1
            rows.append((call, predicted, actual, "match"))
        else:
            rows.append((call, predicted, actual, "FINDING"))

    width = max(len(c) for c in PREDICTIONS)
    print(f"\n{'call':<{width}}  {'you said':>22}  {'actually':>22}  result")
    print("-" * (width + 58))
    for call, predicted, actual, verdict in rows:
        print(f"{call:<{width}}  {str(predicted):>22}  {str(actual):>22}  {verdict}")

    print(f"\n{len(filled)}/{len(PREDICTIONS)} filled in, {matched} matched.")
    if len(filled) == len(PREDICTIONS):
        print(f"{len(PREDICTIONS) - matched} finding(s) to write about.")
    else:
        print("Fill in every prediction before you run the code.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
