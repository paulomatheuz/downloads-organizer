from pathlib import Path


source_path = Path(__file__).resolve().parent / "test-downloads"

for file in sorted(source_path.iterdir()):
    if file.is_file():
        print(f"File: {file.name} | Extension: {file.suffix}")
