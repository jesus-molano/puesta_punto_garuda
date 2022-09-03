#! python3
# Convert images to webp format
import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image

pathToConvert = "/home/jesus/Pictures/toConvert/"
pathConverted = "/home/jesus/Pictures/converted/"

def convert_to_webp(filename, path=pathToConvert):
  extension = filename.split(".")[-1]
  fname = filename.split(".")[0]
  image = Image.open(path + filename)

  if extension == "png":
    image.save(pathConverted + fname + ".webp", "webp", lossless=True)
  elif extension == "jpg" or extension == "jpeg":
    image.save(pathConverted + fname + ".webp", "webp", quality=75)
    

class FileHandle(FileSystemEventHandler):
  def on_modified(self, event):
    with os.scandir(pathToConvert) as entries:
      for entry in entries:
        fileName = entry.name
        if(fileName.endswith(".png") or fileName.endswith(".jpg") or fileName.endswith(".jpeg")):
          convert_to_webp(fileName)


if __name__ == "__main__":
  event_handler = FileHandle()
  observer = Observer()
  path = pathToConvert
  observer.schedule(event_handler, path, recursive=False)
  observer.start()
  try:
    print("Watching for changes...")
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
    print("Done")
  observer.join()