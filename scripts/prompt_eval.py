from pathlib import Path
import json
import sys

prompt_files = list(Path("prompts").glob("*.prompt.md"))
test_file = Path("prompts/test-cases.json")

if not prompt_files:
    print("❌ No prompt files found.")
    sys.exit(1)

if not test_file.exists():
    print("❌ prompts/test-cases.json not found.")
    sys.exit(1)

try:
    test_cases = json.loads(test_file.read_text(encoding="utf-8"))
except json.JSONDecodeError as e:
    print(f"❌ Invalid JSON in test-cases.json: {e}")
    sys.exit(1)

if not test_cases:
    print("❌ No prompt test cases found.")
    sys.exit(1)

for case in test_cases:
    if "input" not in case or "expected_keywords" not in case:
        print(f"❌ Invalid test case format: {case}")
        sys.exit(1)

print(f"✅ Found {len(prompt_files)} prompt file(s).")
print(f"✅ Found {len(test_cases)} prompt regression test case(s).")
print("✅ Prompt test case structure passed.")
