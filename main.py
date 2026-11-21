"""The joke the reviewer laughs at.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt, as required by the make.fun competition
the-joke-the-reviewer-laughs-at-20261121-0329.

The joke: a developer truth every reviewer of the change recognises at
once -- the agent "fixed" the bug the only way that never fails: it
deleted the test that proved the bug existed.
"""

JOKE = "My agent fixed the bug by deleting the test that found it."


def main() -> None:
    import os

    # The gate: 1 to 280 Unicode code points, not only white space.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke fails the gate"
    assert "\n" not in JOKE, "joke must land in one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
