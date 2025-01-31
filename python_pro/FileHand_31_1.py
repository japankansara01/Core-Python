#Writing to a file(creates a new file or overwrites)
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")
    file.writelines(["Third line\n", "Fourth line\n"])

#Reading the entire file content
with open("example.txt", "r") as file:
    content = file.read()
    print("Reading with read():\n", content)

#Reading line by line
with open("example.txt", "r") as file:
    print("Reading line by line with readline():")
    print(file.readline().strip())
    print(file.readline().strip())

#Reading all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Reading with readlines():", lines)

#Appending new content
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

#Using 'r+' mode(read and write)
with open("example.txt", "r+") as file:
    print("Before modification:\n", file.read())
    file.seek(0)  #Move cursor to the beginning
    file.write("Modified first line!\n")

#Reading file content
with open("example.txt", "r") as file:
    print("Final file content:\n", file.read())

#CSV file handling
import csv
# Writing CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])  # Header
    writer.writerows([["Alice", 25, "New York"], ["Bob", 30, "LA"], ["Charlie", 22, "Chicago"]])

# Reading CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing CSV using DictWriter
with open("data.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([{"Name": "Japan", "Age": 22, "City": "Nadiad"},
                      {"Name": "Khush", "Age": 22, "City": "Mumbai"},
                      {"Name": "Yashvi", "Age": 22, "City": "Anand"}])

# Reading CSV using DictReader
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row))
