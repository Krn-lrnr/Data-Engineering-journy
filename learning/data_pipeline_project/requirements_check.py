import importlib

required_packages = [
    "pandas",
    "requests",
    "sqlite3"
]

missing_packages = []

for package in required_packages:
    try:
        importlib.import_module(package)
    except ImportError:
        missing_packages.append(package)

if missing_packages:
    print("Missing packages:")
    for package in missing_packages:
        print(f"- {package}")
else:
    print("All required packages are installed")