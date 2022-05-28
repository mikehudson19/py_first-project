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

srcFolder = "/Users/admin/Documents/Test Files"
documentsDir = "/Users/admin/Documents/Test Files/Documents"
picturesDir = "/Users/admin/Documents/Test Files/Pictures"
moviesDir = "/Users/admin/Documents/Test Files/Movies"
miscDir = "/Users/admin/Documents/Test Files/Misc"

list = os.listdir(srcFolder)

for file in list:
  fileExt = PurePosixPath(file).suffix
  isDir = os.path.isdir(srcFolder + "/" + file)
  isDoc = fileExt == ".txt"

  if isDir:
    continue

  if isDoc:
    print("file is a document")
    # os.rename(srcFolder + "/" + file, documentsDir + "/" + file)
    continue


  if fileExt == ".jpg" or fileExt == ".JPG":
    print("file is an image")
    # os.rename(srcFolder + "/" + file, picturesDir + "/" + file)
    continue

  if fileExt == ".mp4":
    print("file is a video")
    # os.rename(srcFolder + "/" + file, moviesDir + "/" + file)
    continue

  else:
    print("file is not recognized")
    print(file)
    # os.rename(srcFolder + "/" + file, miscDir + "/" + file)




  # Get the source directory
  # Get each respective target directory
  # Get all the files
  # Iterate through all the files
  # Dependent on file extension, move file to correct target dir 
