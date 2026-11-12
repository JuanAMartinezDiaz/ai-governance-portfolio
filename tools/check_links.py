"""Check local Markdown/HTML link target existence; no network or anchor claims."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", "venv", "__pycache__", "node_modules", "tmp", ".tmp", "build"}
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\((<?[^\s)]+>?)(?:\s+[^)]*)?\)")
HTML_LINK = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)


def check_links(root=ROOT):
    errors, checked = [], 0
    for source in sorted(root.rglob("*.md")):
        if any(part in SKIP for part in source.relative_to(root).parts):
            continue
        content = source.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK.findall(content) + HTML_LINK.findall(content):
            raw = raw.strip("<>")
            parts = urlsplit(raw)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = (root / unquote(parts.path).lstrip("/")) if parts.path.startswith("/") else (source.parent / unquote(parts.path))
            target = target.resolve()
            checked += 1
            if not target.is_relative_to(root.resolve()):
                errors.append(f"{source.relative_to(root)}: target leaves repository: {raw}")
            elif not target.exists():
                errors.append(f"{source.relative_to(root)}: missing target: {raw}")
    return checked, errors


if __name__ == "__main__":
    count, errors = check_links()
    for error in errors:
        print("FAIL", error)
    if not errors:
        print(f"PASS: {count} local linked-file targets exist (binary files supported; remote URLs and anchor names not tested)")
    raise SystemExit(bool(errors))
