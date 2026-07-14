from pathlib import Path
from datetime import date, datetime
import json
import re
import sys

KB_DIR = Path("docs/knowledge-base")
ARTIFACT_DIR = Path("artifacts")
ARTIFACT_DIR.mkdir(exist_ok=True)

REQUIRED_FRONT_MATTER_KEYS = [
    "title",
    "owner",
    "product_area",
    "status",
    "last_reviewed",
]

REQUIRED_SECTIONS = [
    "## 适用范围",
    "## 标准答案",
    "## 关键规则",
    "## 示例",
    "## 相关链接",
]

MAX_FILE_CHARS = 12000
MAX_DAYS_SINCE_REVIEW = 180

issues = []
warnings = []
passed_files = []


def add_issue(file_path, message):
    issues.append({
        "file": str(file_path),
        "message": message
    })


def add_warning(file_path, message):
    warnings.append({
        "file": str(file_path),
        "message": message
    })


def parse_front_matter(content):
    if not content.startswith("---"):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    front_matter_text = parts[1].strip()
    data = {}

    for line in front_matter_text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()

    return data


def check_relative_links(file_path, content):
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", content)

    for link in links:
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue

        target = (file_path.parent / link).resolve()

        if not target.exists():
            add_warning(file_path, f"Relative link may be broken: {link}")


def check_last_reviewed(file_path, value):
    try:
        reviewed_date = datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        add_issue(file_path, "last_reviewed must use YYYY-MM-DD format.")
        return

    days = (date.today() - reviewed_date).days

    if days > MAX_DAYS_SINCE_REVIEW:
        add_warning(
            file_path,
            f"Knowledge base has not been reviewed for {days} days."
        )


def review_file(file_path):
    content = file_path.read_text(encoding="utf-8")

    if len(content.strip()) == 0:
        add_issue(file_path, "File is empty.")
        return

    if len(content) > MAX_FILE_CHARS:
        add_warning(
            file_path,
            f"File is too long: {len(content)} characters. Consider splitting it."
        )

    if "TODO" in content or "FIXME" in content:
        add_issue(file_path, "File contains TODO or FIXME.")

    front_matter = parse_front_matter(content)

    for key in REQUIRED_FRONT_MATTER_KEYS:
        if key not in front_matter or not front_matter[key]:
            add_issue(file_path, f"Missing front matter key: {key}")

    if "last_reviewed" in front_matter:
        check_last_reviewed(file_path, front_matter["last_reviewed"])

    for section in REQUIRED_SECTIONS:
        if section not in content:
            add_issue(file_path, f"Missing required section: {section}")

    check_relative_links(file_path, content)

    passed_files.append(str(file_path))


def write_reports():
    result = {
        "passed_files": passed_files,
        "issues": issues,
        "warnings": warnings,
        "issue_count": len(issues),
        "warning_count": len(warnings),
    }

    json_path = ARTIFACT_DIR / "kb-review-results.json"
    json_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    md_lines = [
        "# Knowledge Base Review Summary",
        "",
        f"- Checked files: {len(passed_files)}",
        f"- Issues: {len(issues)}",
        f"- Warnings: {len(warnings)}",
        "",
    ]

    if issues:
        md_lines.append("## Issues")
        for item in issues:
            md_lines.append(f"- ❌ `{item['file']}`: {item['message']}")
        md_lines.append("")

    if warnings:
        md_lines.append("## Warnings")
        for item in warnings:
            md_lines.append(f"- ⚠️ `{item['file']}`: {item['message']}")
        md_lines.append("")

    if not issues:
        md_lines.append("✅ Knowledge base review passed.")

    md_path = ARTIFACT_DIR / "kb-review-summary.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")


def main():
    if not KB_DIR.exists():
        add_issue(KB_DIR, "docs/knowledge-base directory does not exist.")
        write_reports()
        sys.exit(1)

    files = list(KB_DIR.glob("*.md"))

    if not files:
        add_issue(KB_DIR, "No markdown files found in docs/knowledge-base.")
        write_reports()
        sys.exit(1)

    titles = {}

    for file_path in files:
        review_file(file_path)

        content = file_path.read_text(encoding="utf-8")
        front_matter = parse_front_matter(content)
        title = front_matter.get("title")

        if title:
            if title in titles:
                add_issue(file_path, f"Duplicate title with {titles[title]}: {title}")
            else:
                titles[title] = str(file_path)

    write_reports()

    if issues:
        print(f"❌ Knowledge base review failed with {len(issues)} issue(s).")
        for item in issues:
            print(f"- {item['file']}: {item['message']}")
        sys.exit(1)

    print("✅ Knowledge base review passed.")


if __name__ == "__main__":
    main()
