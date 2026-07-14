from pathlib import Path
from datetime import date

release_dir = Path("docs/release-notes")
release_dir.mkdir(parents=True, exist_ok=True)

file = release_dir / f"release-draft-{date.today().isoformat()}.md"

content = f"""# Release Draft - {date.today().isoformat()}

## Summary

Describe the main product changes in this release.

## Features

- 

## Prompt Changes

- 

## API Changes

- 

## UAT Result

- Pending

## Risks

- 

## Rollback Plan

- 

## Post-release Metrics

- 

"""

file.write_text(content, encoding="utf-8")

print(f"✅ Release note draft generated: {file}")
