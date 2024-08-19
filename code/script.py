import time
import shutil
from datetime import datetime
from pathlib import Path

########################################################################################################################

# Define the path to the Downloads folder
DOWNLOADS_FOLDER = Path.home() / "Downloads"

# Define the directories for file organization
ORGANIZATION_RULES = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Programs': ['.exe', '.msi', '.dmg', '.sh'],
    'Others': []
}

########################################################################################################################

# Function to create directories if they do not exist
def create_directories(base_path, directories):
    for directory in directories:
        dir_path = base_path / directory
        if not dir_path.exists():
            dir_path.mkdir()
            print(f"Created directory: {dir_path}")

########################################################################################################################

# Function to move files to appropriate directories
def move_files():
    for item in DOWNLOADS_FOLDER.iterdir():
        if item.is_file():

            # Get file's Year and Month of creation
            stat = item.stat()
            year_date = datetime.fromtimestamp(stat.st_ctime).strftime('%Y')
            month_date = datetime.fromtimestamp(stat.st_ctime).strftime('%m')

            # Get the file extension and map to the corresponding directory
            file_extension = item.suffix.lower()
            destination_dir = None
            for dir_name, extensions in ORGANIZATION_RULES.items():
                if file_extension in extensions:
                    destination_dir = dir_name
                    break

            # If the file type doesn't match any rule
            if not destination_dir:
                destination_dir = 'Others'

            # Define the destination path
            destination_path = DOWNLOADS_FOLDER / destination_dir / year_date / month_date

            if not destination_path.exists():
                destination_path.mkdir(parents=True)

            # Move the file
            shutil.move(str(item), str(destination_path))
            print(f"Moved {item.name} to {destination_path}")

########################################################################################################################

if __name__ == "__main__":
    while True:
        # Create directories based on rules
        create_directories(DOWNLOADS_FOLDER, ORGANIZATION_RULES.keys())

        # Move files into their respective folders
        move_files()

        # Wait 10 minutes before doing organisation again
        time.sleep(600)