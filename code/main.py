from code import create_directories, move_files
from datetime import time
from move_files import DOWNLOADS_FOLDER, ORGANIZATION_RULES

if __name__ == "__main__":
    while True:
        create_directories(DOWNLOADS_FOLDER, ORGANIZATION_RULES.keys())
        move_files()
        time.sleep(600)