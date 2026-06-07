<h1 align="center">
Alassane WADE — File Organizer
</h1>

<h2 align="center">
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿"
</h2>

Python script that automatically organizes files from the Downloads folder into native Windows folders (Pictures, Documents, Videos, Music) sorted by year and month.

## How it works

1. On startup, the script sorts all files already present in Downloads
2. Then it watches the Downloads folder continuously
3. Any new file downloaded is automatically moved to the right folder

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/alassane8/Organizer.git
```

### 2. Install dependencies
```bash
pip install watchdog
```

### 3. Run at Windows startup

Open the startup folder:
```
Win + R → shell:startup → Enter
```

Then:
- Move the `code/` folder into `shell:startup`
- Place `launcher.bat` directly in `shell:startup`

```
shell:startup/
├── launcher.bat
└── code/
    ├── main.py
    ├── move_files.py
    └── download_handler.py
```

The script will now launch silently in the background every time Windows starts.

## File categorization

| Destination         | Extensions                                              |
|---------------------|---------------------------------------------------------|
| `~/Pictures`        | `.jpeg` `.jpg` `.png` `.gif` `.bmp` `.tiff` `.svg`     |
| `~/Documents`       | `.pdf` `.doc` `.docx` `.txt` `.xls` `.xlsx` `.ppt` `.pptx` `.odt` |
| `~/Videos`          | `.mp4` `.mov` `.avi` `.mkv` `.flv` `.wmv`              |
| `~/Music`           | `.mp3` `.wav` `.aac` `.flac` `.ogg`                    |
| `~/Desktop`         | Everything else                                         |

## Directory structure

Files are sorted by year and month inside each native folder:

```
Pictures/
└── 2026/
    └── 06/
        └── photo.png

Documents/
└── 2026/
    └── 06/
        └── report.pdf
```

## Area for improvement
Here you can find features currently being worked on.

- [ ] System tray icon to show the script is running
- [ ] Logs file to track all moved files
- [ ] Config file to customize rules without touching the code
- [ ] Support for additional file types