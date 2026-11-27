LINE = "I can't come in today - my bed has filed a formal complaint about my absence, and HR (my cat) has approved the leave."


def validated_line() -> str:
    line = LINE.strip()
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"the excuse must be 1-200 characters, got {len(line)}"
    return line


def main() -> None:
    import os
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validated_line() + "\n")
    print(validated_line())


if __name__ == "__main__":
    main()
