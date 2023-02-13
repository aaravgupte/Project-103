import os
import shutil
import sys
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/HP/Pictures/Saved Pictures/C102_assets-main"
to_dir="C:/Users/HP/Desktop/WhiteHat Jr"


# Event Hanlder Class

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")     

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()        

    
