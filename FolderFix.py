from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_tracked):
            src = folder_tracked + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)
            return folder_tracked


folder_tracked = "F:\Downloads\practice"
folder_destination = "F:\Downloads\Programs\practice"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_tracked, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
        print("works")

except KeyboardInterrupt:
    observer.stop()
observer.join()

