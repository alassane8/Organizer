import datetime
import shutil
from pathlib import Path

DOWNLOADS_FOLDER = Path.home() / "Downloads"

ORGANIZATION_RULES = {
    Path.home() / "Pictures":  ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    Path.home() / "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt'],
    Path.home() / "Videos":    ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    Path.home() / "Music":     ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
}

def get_file_date_creation(item):
    stat = item.stat()
    year_date = datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%Y')
    month_date = datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%m')
    
    return year_date, month_date

def map_file_to_corresponding_directory(item, year_date, month_date):
    file_extension = item.suffix.lower()
    destination_folder = None

    for folder_path, extensions in ORGANIZATION_RULES.items():
        if file_extension in extensions:
            destination_folder = folder_path
            break

    if not destination_folder:
        destination_folder = Path.home() / "Documents"

    destination_path = destination_folder / year_date / month_date

    if not destination_path.exists():
        destination_path.mkdir(parents=True)

    return destination_path

def get_unique_destination(destination_path, item):
    candidate = destination_path / item.name
    if not candidate.exists():
        return candidate

    stem = item.stem
    suffix = item.suffix
    counter = 1
    while True:
        candidate = destination_path / f"{stem} ({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1

def move_file_to_new_directory(item, destination_path):
    target = get_unique_destination(destination_path, item)
    shutil.move(str(item), str(target))
    print(f"Moved: {item.name} → {target}")

def move_files():
    for item in DOWNLOADS_FOLDER.iterdir():
        if item.is_file():
            year_date, month_date = get_file_date_creation(item)
            destination_path = map_file_to_corresponding_directory(item, year_date, month_date)
            move_file_to_new_directory(item, destination_path)