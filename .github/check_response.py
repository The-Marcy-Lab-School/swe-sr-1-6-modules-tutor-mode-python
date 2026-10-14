"""Report whether the predictions were filled in and a response was written.

This does NOT grade the writing, and it does NOT grade whether the predictions
were right. Objective 10.4 asks a student to predict, then check, and treat a
wrong prediction as a finding — so being wrong is the exercise working. What
is checked is that they did it: every prediction filled in, and a response
written.

Posts the same `marcy/score` status the coding assignments use, so one
gradebook reads every repo.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESPONSE = ROOT / "short_response.md"
PLACEHOLDER = "Your response here"
MIN_WORDS = 40


def predictions_filled():
    """How many predictions have a value, and how many there are."""
    sys.path.insert(0, str(ROOT))
    try:
        from predictions import PREDICTIONS
    except Exception:
        return 0, 0
    return sum(1 for v in PREDICTIONS.values() if v is not None), len(PREDICTIONS)


def matched():
    """How many predictions match what the code does. Reported, never required."""
    result = subprocess.run([sys.executable, "check.py"], cwd=ROOT,
                            capture_output=True, text=True)
    found = re.search(r"(\d+) matched", result.stdout)
    return int(found.group(1)) if found else 0


def words_written(text):
    body = re.split(r"^###\s+Response.*$", text, flags=re.M)
    body = body[-1] if len(body) > 1 else text
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    return len(re.sub(r"[#*_>`\[\]()-]", " ", body).split())


def main():
    filled, total = predictions_filled()
    text = RESPONSE.read_text(encoding="utf-8") if RESPONSE.is_file() else ""
    count = words_written(text)
    written = PLACEHOLDER.lower() not in text.lower() and count >= MIN_WORDS

    hits = matched() if filled == total and total else 0
    done = filled == total and total > 0 and written

    lines = [
        "| Check | |",
        "| --- | --- |",
        f"| Predictions filled in | {filled}/{total} |",
        f"| Matched what the code does | {hits}/{total} |",
        f"| Response written | {count} words |",
        "",
    ]
    if done:
        findings = total - hits
        lines.append(
            f"Submitted. {findings} prediction(s) did not match, and those are "
            f"your findings." if findings else
            "Submitted. Every prediction matched, so say what made this program "
            "predictable."
        )
    elif filled < total:
        lines.append(f"Fill in all {total} predictions in `predictions.py`, then "
                     f"run `python3 check.py`.")
    else:
        lines.append(f"Write your response in `short_response.md`. At least "
                     f"{MIN_WORDS} words.")

    summary = "## Short response\n\n" + "\n".join(lines) + "\n"
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(summary)
    else:
        print(summary)

    repo, sha = os.environ.get("REPO"), os.environ.get("SHA")
    if not (repo and sha):
        return
    detail = (f"submitted ({filled}/{total} predicted, {count} words)" if done
              else f"not finished ({filled}/{total} predicted, {count} words)")
    subprocess.run(
        ["gh", "api", "-X", "POST", f"repos/{repo}/statuses/{sha}",
         "-f", f"state={'success' if done else 'pending'}",
         "-f", "context=marcy/score",
         "-f", f"description={int(done)}/1 ({int(done) * 100}%) {detail}"[:140]],
        check=False, capture_output=True)


if __name__ == "__main__":
    main()
