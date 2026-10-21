# Downloads Organizer

Organize Windows downloads into category folders using Python.

## Requirements

- Windows
- Python 3.14 or later
- Windows PowerShell 5.1 or later for task installation

## Paths

Source:

`C:\Users\paulo\Downloads`

Destination:

`C:\Users\paulo\Documents\! Automatic Organization`

These paths are configured in `organize.py`.

## Run manually

```powershell
py .\organize.py
```

Running the script moves supported files from the source folder.

## Install automatic execution

From the project directory:

```powershell
.\install.ps1
```

The Windows scheduled task runs once at each logon of the user who
installed it. It runs without a terminal window and does not continuously
monitor Downloads.

Keep the project and Python installation at their current locations.
Run the installer again if either location changes.

## Remove automatic execution

```powershell
.\uninstall.ps1
```

Removing the scheduled task does not delete or move organized files.

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

Category folders are created as needed.

## Behavior

- Only files directly inside Downloads are scanned.
- Subfolders are not scanned or moved.
- Existing destination files are preserved.
- Unsupported files remain in Downloads.
- Files ending in .crdownload, .part, .partial or .tmp are skipped.
- Active downloads using their final extension are not detected.
- File operation errors are logged, and processing continues.
- Only the final extension is matched.
- Extension matching is case-insensitive.

## Execution log

The log is stored at:

`C:\Users\paulo\Documents\! Automatic Organization\organizer.log`

