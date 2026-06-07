
from datetime import time
from watchdog.events import FileSystemEventHandler
from code import move_files

class DownloadsHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"New file detected: {event.src_path}")
        time.sleep(1)
        move_files()
