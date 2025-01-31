import shutil

#to copy file
#shutil.copy("data.csv", "backup.csv")
#print("File copied successfully")

#shutil.copy2("file1.txt", "file2.txt")

#Copies the content of src to dst. If dst exists, it will be overwritten
#shutil.copyfile("source.txt", "destination.txt")

#Moves a file or directory from src to dst. If dst is a directory, src is moved into it.
#shutil.move("source.txt", "destination.txt")

#Deleting a file
#shutil.remove("file_to_delete.txt")

#Deleting an entire directory
#shutil.rmtree("folder_to_remove")

#Create an archive (zip)
#shutil.make_archive("backup", "zip", "folder_to_backup")

#Extract archive (zip)
#shutil.unpack_archive("backup.zip", "destination_folder")