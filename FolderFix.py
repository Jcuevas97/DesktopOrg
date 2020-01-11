from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in os.listdir(folder_tracked):
            src = folder_tracked + "\\" + filename
            if filename.endswith(".exe"):
                new_destination = folder_tracked + "\\Programs\\" + filename
            elif filename.endswith(".rmskin"):
                new_destination = folder_tracked + "\\Rainmeter Skins\\" + filename
            elif filename.endswith(tuple([".pdf", ".doc", ".docx", ".txt"])):
                new_destination = folder_tracked + "\\Documents\\" + filename
            elif filename.endswith(tuple([".mp4", ".wav", ".flac", ".mp3"])):
                new_destination = folder_tracked + "\\Music\\" + filename
            else:
                continue
            try:
                file_mover(src, new_destination)
            except FileExistsError:
                change = new_destination.split(".")
                file_mover(src, change[0] + " copy" + change[1])


def file_mover(src, destination):
    os.rename(src, destination)


folder_tracked = "F:\\Downloads"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_tracked, recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()
observer.join()

