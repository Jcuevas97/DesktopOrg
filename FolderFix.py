from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, shutil, time, datetime

oneday = 86400
programs = "G:\\Computer Files\\Programs\\"
documents = "C:\\Users\\johnn\\OneDrive\\Documents\\"
music = "F:\\Music\\"

class MyHandler(FileSystemEventHandler):
    folder = ""

    def on_any_event(self, event):
        file_mover(self.folder)

    def folderassign(self, dire):
        self.folder = dire


def file_mover(location):
    for filename in os.listdir(location):
        src = location + "\\" + filename
        other = location + "\\misc\\"
        if time.time() - os.path.getmtime(src) >= 4*oneday:
            if filename.endswith(tuple([".exe", ".msi"])):
                dest = programs + filename
            elif filename.endswith(tuple([".pdf", ".doc", ".docx", ".txt"])):
                dest = documents + filename
            elif filename.endswith(tuple([".mp4", ".wav", ".flac", ".mp3"])):
                dest = music + filename
            elif os.path.isfile(src):
                dest = other + filename
            else:
                continue
            try:
                if src.split(":",1)[0] == dest.split(":", 1)[0]:
                    os.rename(src, dest)
                else:
                    shutil.move(src, dest)
                with open('log.txt', 'a') as file:
                    file.write(datetime.datetime.now().strftime("%x")+": "+src + "-" * ((175 - len(src+dest)) if (175 - len(src+dest)) > 0 else 0) + ">" + dest + '\n')
            except FileExistsError:
                change = dest.split(".")
                os.rename(src, change[0] + " copy" + change[1])
            except FileNotFoundError:
                os.mkdir(dest.rsplit('\\', 1)[0])


def main():
    folders = {"downloads": "F:\\Downloads", "desktop": "C:\\Users\\johnn\\OneDrive\\Desktop"}
    observer = Observer()
    observers = []
    for key in folders:
        event_handler = MyHandler()
        event_handler.folderassign(folders[key])
        observer.schedule(event_handler, folders[key])
        observers.append(observer)
    observer.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        for o in observers:
            o.unschedule_all()
            o.stop()
    for o in observers:
        o.join()


main()