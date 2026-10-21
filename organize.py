import logging
from pathlib import Path


SOURCE_PATH = Path(r"C:\Users\paulo\Downloads")
OUTPUT_PATH = Path(r"C:\Users\paulo\Documents\! Automatic Organization")

RULES = {
    ".pdf": "PDFs",
    ".txt": "Text",

    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",

    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",

    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".odp": "Presentations",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".bmp": "Images",
    ".heic": "Images",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".gz": "Archives",
    ".tar": "Archives",

    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".m4a": "Audio",
    ".ogg": "Audio",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",

    ".exe": "Installers",
    ".msi": "Installers",
    ".msix": "Installers",
}

TEMPORARY_EXTENSIONS = {".crdownload", ".part", ".partial", ".tmp"}


def main():
    if not SOURCE_PATH.is_dir():
        raise FileNotFoundError(f"Source folder not found: {SOURCE_PATH}")

    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=OUTPUT_PATH / "organizer.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8",
    )

    logging.info("Run started.")

    for file in sorted(SOURCE_PATH.iterdir()):
        try:
            if not file.is_file():
                continue

            extension = file.suffix.lower()

            if extension in TEMPORARY_EXTENSIONS:
                logging.info("Skipped temporary file: %s", file.name)
                continue

            folder_name = RULES.get(extension)

            if folder_name is None:
                logging.info("Skipped unsupported file: %s", file.name)
                continue

            destination_path = OUTPUT_PATH / folder_name
            target_path = destination_path / file.name

            if target_path.exists():
                logging.info("Skipped existing destination: %s", file.name)
                continue

            destination_path.mkdir(parents=True, exist_ok=True)

            # On Windows, rename fails if the destination already exists.
            file.rename(target_path)
            logging.info("Moved: %s -> %s", file.name, folder_name)

        except OSError:
            logging.exception("Could not organize: %s", file.name)

    logging.info("Run finished.")


if __name__ == "__main__":
    main()

