import os
from pathlib import PurePosixPath

#Python comment
print("this is my first python programme")
print("this is the second line of my python programme")

#Declare variables and print them with concatenation
name = "Michael"

greet = "hello and welcome to the programme, "

print(greet + name)

# #Open a file in the current directory and print it's contents
# with open('file1.txt', 'r') as f:
# 	data = f.read()

# print(data)

# #Print the names of all the files in the current directory
# files = os.scandir()

# for file in files:
# 	print(file.name)

# #Create a new file in the current directory, create content for it, then print it
# with open('programmeCreatedFile.txt', 'w') as f1:
# 	f1.write('the content of this file was created programatically')

# with open('programmeCreatedFile.txt', 'r') as f2:
# 	contents = f2.read()

# print(contents)

srcFolder = "/Users/admin/Downloads"
documentsDir = "/Users/admin/Documents/Test Files/Documents"
picturesDir = "/Users/admin/Documents/Test Files/Pictures"
moviesDir = "/Users/admin/Documents/Test Files/Movies"
miscDir = "/Users/admin/Documents/Test Files/Misc"

def isDoc(fileExt):
  if fileExt == ".txt" or fileExt == ".pdf" or fileExt == ".xlsx" or fileExt == ".epub" or fileExt == ".docx":
    return True

def isVideo(fileExt):
  #many movie downloads will be in a folder - need to handle this.
  if fileExt == ".mp4" or fileExt == ".mkv":
    return True

def isImage(fileExt):
  if fileExt == ".jpg" or fileExt == ".png" or fileExt == ".heic":
    return True

def arrangeFiles():
  list = os.listdir(srcFolder)

  for file in list:
    isDir = os.path.isdir(srcFolder + "/" + file)
    fileExt = PurePosixPath(file).suffix.lower()

    if isDir:
      continue

    if isDoc(fileExt):
      # print("file is a document")
      # os.rename(srcFolder + "/" + file, documentsDir + "/" + file)
      continue


    if isImage(fileExt):
      # print("file is an image")
      # os.rename(srcFolder + "/" + file, picturesDir + "/" + file)
      continue

    if isVideo(fileExt):
      # print("file is a video")
      # os.rename(srcFolder + "/" + file, moviesDir + "/" + file)
      continue

    else:
      print("file is not recognized")
      print(file)
      os.rename(srcFolder + "/" + file, miscDir + "/" + file)


arrangeFiles()