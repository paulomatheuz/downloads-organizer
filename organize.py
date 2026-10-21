from pathlib import Path


source_path = Path(__file__).resolve().parent / "test-downloads"
destination_path = source_path / "PDFs"

destination_path.mkdir(exist_ok=True)

for file in sorted(source_path.iterdir()):
    if not file.is_file() or file.suffix.lower() != ".pdf":
        continue

    target_path = destination_path / file.name

    if target_path.exists():
        print(f"Skipped: {file.name} - destination already exists.")
        continue

    file.rename(target_path)
    print(f"Moved: {file.name} -> PDFs")
