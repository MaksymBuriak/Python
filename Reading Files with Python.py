# Reading Files with Python
import urllib.request

separation_line = '-------------------------------------------'

# Download Data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'example1.txt'
urllib.request.urlretrieve(url, filename)


# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")

# Print the path of file
print(file1.name)
print(separation_line)

# Print the mode of file, either 'r' or 'w'
print(file1.mode)
print(separation_line)

# Read the file
FileContent = file1.read()
print(FileContent)
print(separation_line)

# Print the file with '\n' as a new line
print(FileContent)
print(separation_line)

# Type of file content
print(type(FileContent))
print(separation_line)

# Close file after finish
file1.close()
print(separation_line)

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
file1.closed

# See the content of file
print(FileContent)
print(separation_line)

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))

print(separation_line)

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

print(separation_line)

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

print(separation_line)

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

print(separation_line)

# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

print(separation_line)

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

print(separation_line)

# Print the first line
print(FileasList[0])
# Print the second line
print(FileasList[1])
# Print the third line
print(FileasList[2])

print('Finished')



