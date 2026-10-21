# Downloads Organizer

A Python automation that organizes downloaded files into folders by extension.

## Requirements

- Python 3.14 or later
- Windows for the planned Task Scheduler integration

## Usage

Run from the project directory:

```powershell
py .\organize.py
```

The script reads files directly inside `test-downloads`.
Supported files are moved into category folders under
`test-downloads/automatic organization`.

Create `test-downloads` before running the script.
Subfolders are not scanned.

## Supported categories

| Folder | Extensions |
| --- | --- |
| PDFs | .pdf |
| Text | .txt |
| Documents | .doc, .docx, .odt, .rtf |
| Spreadsheets | .xls, .xlsx, .csv, .ods |
| Presentations | .ppt, .pptx, .odp |
| Images | .jpg, .jpeg, .png, .gif, .webp, .svg, .bmp, .heic |
| Archives | .zip, .rar, .7z, .gz, .tar |
| Audio | .mp3, .wav, .flac, .m4a, .ogg |
| Videos | .mp4, .mkv, .avi, .mov, .webm |
| Installers | .exe, .msi, .msix |

## Current behavior

- Extensions are matched without case sensitivity.
- Files with unsupported extensions remain in the source folder.
- Files are skipped when the destination path already exists.
- Only the final extension is used: `backup.tar.gz` matches `.gz`.
- Local test files are excluded from Git.

## Planned improvements

- Handle file operation errors.
- Detect incomplete or active downloads.
- Configure the source folder.
- Run automatically with Windows Task Scheduler.
