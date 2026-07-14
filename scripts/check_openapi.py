from pathlib import Path
import yaml
import sys

openapi_file = Path("api/openapi.yaml")

if not openapi_file.exists():
    print("❌ api/openapi.yaml not found.")
    sys.exit(1)

try:
    data = yaml.safe_load(openapi_file.read_text(encoding="utf-8"))
except Exception as e:
    print(f"❌ Failed to parse OpenAPI YAML: {e}")
    sys.exit(1)

required_keys = ["openapi", "info", "paths"]

for key in required_keys:
    if key not in data:
        print(f"❌ Missing OpenAPI key: {key}")
        sys.exit(1)

print("✅ OpenAPI document passed basic validation.")
