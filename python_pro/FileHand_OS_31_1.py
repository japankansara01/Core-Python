import os

# List all files in the current directory
files = os.listdir(".")
print(files)

#check for existing file
if os.path.exists("abc.txt"):
    print("File exists")
else:
    print("File not found")

#create new dir
os.mkdir("new_folder")
print("Directory created")
#remove empty dir
os.rmdir("new_folder")
print("Directory removed")

#delete file
#os.remove("example.txt")
#print("File deleted")