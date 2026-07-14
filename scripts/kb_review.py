def main():
    if not KB_DIR.exists():
        add_issue(
            KB_DIR,
            "docs/knowledge-base directory does not exist."
        )
        write_reports()
        sys.exit(1)

    files = sorted(KB_DIR.rglob("*.md"))

    if not files:
        add_issue(
            KB_DIR,
            "No markdown files found in docs/knowledge-base."
        )
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
                add_issue(
                    file_path,
                    f"Duplicate title with {titles[title]}: {title}"
                )
            else:
                titles[title] = str(file_path)

    write_reports()

    if issues:
        print(
            f"❌ Knowledge base review failed "
            f"with {len(issues)} issue(s)."
        )

        for item in issues:
            print(f"- {item['file']}: {item['message']}")

        sys.exit(1)

    print("✅ Knowledge base review passed.")
