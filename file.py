import os

#Python comment
print("this is my first python programme")
print("this is the second line of my python programme")

#Declare variables and print them with concatenation
name = "Michael"

greet = "hello and welcome to the programme, "

print(greet + name)

#Open a file in the current directory and print it's contents
with open('file1.txt', 'r') as f:
	data = f.read()

print(data)

#Print the names of all the files in the current directory
files = os.scandir()

# for file in files:
# 	print(file.name)

#Create a new file in the current directory, create content for it, then print it
with open('programmeCreatedFile.txt', 'w') as f1:
	f1.write('the content of this file was created programatically')

with open('programmeCreatedFile.txt', 'r') as f2:
	contents = f2.read()

print(contents)
