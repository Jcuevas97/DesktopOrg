from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in os.listdir(downloads):
            src = downloads + "\\" + filename
            if filename.endswith(tuple([".exe", ".msi"])):
                new_destination = downloads + "\\Programs\\" + filename
            elif filename.endswith(".rmskin"):
                new_destination = downloads + "\\Rainmeter Skins\\" + filename
            elif filename.endswith(tuple([".pdf", ".doc", ".docx", ".txt"])):
                new_destination = downloads + "\\Documents\\" + filename
            elif filename.endswith(tuple([".mp4", ".wav", ".flac", ".mp3"])):
                new_destination = downloads + "\\Music\\" + filename
            else:
                continue
            try:
                file_mover(src, new_destination)
            except FileExistsError:
                change = new_destination.split(".")
                file_mover(src, change[0] + " copy" + change[1])


def file_mover(src, destination):
    os.rename(src, destination)


downloads = "F:\\Downloads"
desktop = "C:\\Users\\%username%\\OneDrive\\Desktop"
event_handler = MyHandler()
observerDownloads = Observer()
observerDownloads.schedule(event_handler, downloads, recursive=True)


observerDownloads.start()

try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    observerDownloads.stop()
observerDownloads.join()

