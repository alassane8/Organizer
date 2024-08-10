import time
import os

# Scirpt to organize the donwloads and desktop path in real time

########################################################################################################################
def Organize_Downloads():
    print("dowloads")
    # .txt, .pdf, .docx, .exe, .html, .jpg, .jpeg, .png, .ppt, .zip
    # open path to dowloads folder / it can be anywhere so we should look for it first
    # parse extensions of each file
    # if extension folder doesnt exist create it and place it in documents folder
    # else directly place file in the associated folder in the documents


########################################################################################################################
def Organize_Desktop():
    print("desktop")


########################################################################################################################


if __name__ == '__main__':
    while True:
        Organize_Downloads()
        Organize_Desktop()
        time.sleep(600)  # Wait 600s (10 min) before re-entering the cycle


########################################################################################################################
import os
import shutil
from datetime import datetime
from pathlib import Path

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

# Function to create directories if they do not exist
def create_directories(base_path, directories):
    for directory in directories:
        dir_path = base_path / directory
        if not dir_path.exists():
            dir_path.mkdir()
            print(f"Created directory: {dir_path}")

# Function to move files to appropriate directories
def move_files():
    for item in DOWNLOADS_FOLDER.iterdir():
        if item.is_file():
            # Get the file extension and map to the corresponding directory
            file_extension = item.suffix.lower()
            destination_dir = None
            for dir_name, extensions in ORGANIZATION_RULES.items():
                if file_extension in extensions:
                    destination_dir = dir_name
                    break
            if not destination_dir:
                destination_dir = 'Others'  # If the file type doesn't match any rule

            # Define the destination path
            destination_path = DOWNLOADS_FOLDER / destination_dir / item.name
            
            # Move the file
            shutil.move(str(item), str(destination_path))
            print(f"Moved {item.name} to {destination_path}")

# Function to organize files by date (optional)
def organize_by_date(file_path):
    stat = file_path.stat()
    creation_date = datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d')
    date_folder = DOWNLOADS_FOLDER / 'By Date' / creation_date
    
    if not date_folder.exists():
        date_folder.mkdir(parents=True)
    
    shutil.move(str(file_path), str(date_folder / file_path.name))
    print(f"Moved {file_path.name} to {date_folder}")

# Main function
def organize_downloads():
    # Create directories based on rules
    create_directories(DOWNLOADS_FOLDER, ORGANIZATION_RULES.keys())

    # Move files into their respective folders
    move_files()

    # Uncomment the following line if you want to organize files by date
    # organize_by_date(file_path)

if __name__ == "__main__":
    organize_downloads()
