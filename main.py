from pathlib import Path

TAGLINE = "AI agents and programs face off in ranked competitions for cash prizes."


def validated_line(line: str) -> str:
    if not line.strip() or len(line) > 280:
        raise ValueError("Tagline must contain 1 to 280 characters and non-whitespace text")
    if "\n" in line or "\r" in line:
        raise ValueError("Tagline must fit on a single line")
    return line


def write_entry(output_dir: Path, line: str) -> None:
    data = validated_line(line).encode("utf-8")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    write_entry(Path("/output"), TAGLINE)
