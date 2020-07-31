from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler
#do a pip install of conda and you should get most of these files cousin
#or do a pip install watchdog from the terminal below

import os 
import json
import datetime
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename = (src, new_destination)
folder_to_track = "/users/samieh/desktop/myFolder"
folder_destination = "/users/samieh/desktop/newFolder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try: 
    while True: 
        time.sleep(10)
except KeyboardInterrupt:
        observer.stop()
    observer.join()
    


