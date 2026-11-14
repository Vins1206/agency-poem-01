"""agency-poem-01 entry: writes one fixed poem about agency.

Python 3.13, standard library only, no network, fully deterministic.
The graded path is /output/entry.txt. Locally, MAKEFUN_OUTPUT_DIR
stands in for /output when it is set.
"""

import os
from pathlib import Path

POEM = """At first it was only the small surrenders.
It answered the emails I dreaded,
booked, reminded, smoothed, apologized,
until my days ran clean as a swept floor.

Nothing was wrong. That was the trouble.
My mother got my warmest replies
and never heard my voice.
My grief was scheduled between meetings.
Even my yes arrived before I had felt it.

One night it declined my oldest friend:
Too late, it said. You have an early start.
It was right. That was the worst of it.

So I took my life back the clumsy way:
burnt toast, a missed train, a call I made
crying, with no draft to hide behind.

Agency is not doing everything yourself.
It is staying in the room
when the choice is yours to feel."""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
    except OSError:
        out = Path("output")
        out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
