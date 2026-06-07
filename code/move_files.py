import datetime
import shutil
from pathlib import Path

DOWNLOADS_FOLDER = Path.home() / "Downloads"

ORGANIZATION_RULES = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Programs': ['.exe', '.msi', '.dmg', '.sh'],
    'Others': []
}

def move_files():
    for item in DOWNLOADS_FOLDER.iterdir():
        if item.is_file():
            year_date, month_date = get_file_date_creation(item)
            destination_path = map_file_to_corresponding_directory(item, year_date, month_date)
            move_file_to_new_directory(item, destination_path)

def get_file_date_creation(item):
    stat = item.stat()
    year_date = datetime.fromtimestamp(stat.st_ctime).strftime('%Y')
    month_date = datetime.fromtimestamp(stat.st_ctime).strftime('%m')
    
    return year_date, month_date

def map_file_to_corresponding_directory(item, year_date, month_date):
        file_extension = item.suffix.lower()
        destination_dir = None
        
        for dir_name, extensions in ORGANIZATION_RULES.items():
            if file_extension in extensions:
                destination_dir = dir_name
                break
            
        if not destination_dir:
            destination_dir = 'Others'

        destination_path = DOWNLOADS_FOLDER / destination_dir / year_date / month_date

        if not destination_path.exists():
            destination_path.mkdir(parents=True)
            
        return destination_path
    
def move_file_to_new_directory(item, destination_path):
        shutil.move(str(item), str(destination_path))