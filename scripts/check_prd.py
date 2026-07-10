from pathlib import Path
import sys


REQUIRED_SECTIONS = [
    "需求背景",
    "目标用户",
    "需求描述",
    "验收标准",
    "风险",
]


def find_prd_files() -> list[Path]:
    """查找仓库中的 PRD Markdown 文件。"""
    candidate_directories = [
        Path("docs"),
        Path("prd"),
        Path("requirements"),
    ]

    prd_files: list[Path] = []

    for directory in candidate_directories:
        if directory.exists():
            prd_files.extend(directory.rglob("*.md"))

    return [
        file
        for file in prd_files
        if "prd" in file.name.lower()
        or "requirement" in file.name.lower()
        or "需求" in file.name
    ]


def validate_prd(file_path: Path) -> list[str]:
    """检查单个 PRD 是否包含标准章节。"""
    content = file_path.read_text(encoding="utf-8")
    errors: list[str] = []

    if len(content.strip()) < 100:
        errors.append("文档内容过短，至少应填写 100 个字符。")

    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"缺少章节：{section}")

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
