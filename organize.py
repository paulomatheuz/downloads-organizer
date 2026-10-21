from pathlib import Path


source_path = Path(__file__).resolve().parent / "test-downloads"
output_path = source_path / "automatic organization"

rules = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".txt": "Text",
}

for file in sorted(source_path.iterdir()):
    if not file.is_file():
        continue

    extension = file.suffix.lower()

    if extension not in rules:
        print(f"Skipped: {file.name} - no matching rule.")
        continue

    folder_name = rules[extension]
    destination_path = output_path / folder_name
    target_path = destination_path / file.name

    if target_path.exists():
        print(f"Skipped: {file.name} - destination already exists.")
        continue

    destination_path.mkdir(parents=True, exist_ok=True)

    file.rename(target_path)
    print(f"Moved: {file.name} -> automatic organization/{folder_name}")
