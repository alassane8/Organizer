from watchdog.observers import Observer
from download_hander import DownloadsHandler
from move_files import move_files, DOWNLOADS_FOLDER
import time


if __name__ == "__main__":
    print("Sorting existing files in Downloads...")
    move_files()
    print("Done.")

    event_handler = DownloadsHandler()
    observer = Observer()
    observer.schedule(event_handler, str(DOWNLOADS_FOLDER), recursive=False)
    observer.start()
    print(f"Watching {DOWNLOADS_FOLDER} for new files...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()