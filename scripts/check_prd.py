from pathlib import Path
import sys


REQUIRED_SECTION_ALIASES = {
    "需求背景 / Background": (
        "需求背景",
        "business background",
        "background",
    ),
    "目标用户 / User Story": (
        "目标用户",
        "target user",
        "target users",
        "user story",
    ),
    "需求描述 / Scope": (
        "需求描述",
        "feature description",
        "scope",
    ),
    "验收标准 / Acceptance Criteria": (
        "验收标准",
        "acceptance criteria",
    ),
    "风险 / Risks": (
        "风险",
        "risk",
        "risks",
    ),
}


def find_prd_files() -> list[Path]:
    """只查找明确存放 PRD 的目录，避免误查知识库。"""
    candidate_directories = [
        Path("docs/prd"),
        Path(".github/docs/prd"),
        Path("prd"),
        Path("requirements"),
    ]

    prd_files: list[Path] = []

    for directory in candidate_directories:
        if directory.exists():
            prd_files.extend(directory.rglob("*.md"))

    return sorted(set(prd_files))


def validate_prd(file_path: Path) -> list[str]:
    """检查单个 PRD 是否包含必需结构。"""
    content = file_path.read_text(encoding="utf-8")
    normalised_content = content.casefold()
    errors: list[str] = []

    if len(content.strip()) < 100:
        errors.append("文档内容过短，至少应填写 100 个字符。")

    for section_name, aliases in REQUIRED_SECTION_ALIASES.items():
        if not any(
            alias.casefold() in normalised_content
            for alias in aliases
        ):
            errors.append(f"缺少章节：{section_name}")

    return errors


def main() -> int:
    prd_files = find_prd_files()

    if not prd_files:
        print("未发现需要检查的 PRD 文件，本次检查跳过。")
        return 0

    all_errors: list[str] = []

    for file_path in prd_files:
        errors = validate_prd(file_path)

        if errors:
            print(f"\n❌ PRD 检查未通过：{file_path}")

            for error in errors:
                print(f"  - {error}")
                all_errors.append(f"{file_path}: {error}")
        else:
            print(f"✅ PRD 检查通过：{file_path}")

    if all_errors:
        print(f"\n共发现 {len(all_errors)} 个问题。")
        return 1

    print("\n所有 PRD 文件检查通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
