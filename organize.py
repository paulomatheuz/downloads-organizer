from pathlib import Path


source_path = Path(__file__).resolve().parent / "test-downloads"
output_path = source_path / "automatic organization"

rules = {
    # PDF files
    ".pdf": "PDFs",

    # Plain text files
    ".txt": "Text",

    # Documents
    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".odp": "Presentations",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".bmp": "Images",
    ".heic": "Images",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".gz": "Archives",
    ".tar": "Archives",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".m4a": "Audio",
    ".ogg": "Audio",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",

    # Installers and executables
    ".exe": "Installers",
    ".msi": "Installers",
    ".msix": "Installers",
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
