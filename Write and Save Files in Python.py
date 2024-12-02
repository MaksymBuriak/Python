# Write and Save Files in Python

separation_line = '-------------------------'
# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

print(separation_line)

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
print(Lines)

print(separation_line)

# Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

print(separation_line)

# Verify if writing to file is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

print(separation_line)

with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

print(separation_line)

# Write a new line to text file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

print(separation_line)

# Verify if the new line is in the text file
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

print(separation_line)

#Additional modes

# a+ : Appending and Reading. Creates a new file, if none exists.
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()))

print(separation_line)

# Difference between w+ and r+: 
# Both of these modes allow access to read and write methods; however, opening a file in w+ overwrites it and deletes all pre-existing data
with open('Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0,0)
    print(testwritefile.read())

print(separation_line)

# To work with a file on existing data, use **r+** and **a+**. While using **r+**, it can be useful to add a 
# .truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows
with open('Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())

#Copy a File

# Copy file to another
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

print(separation_line)

# Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())

print(separation_line)

# Given the file `currentMem`, each member is removed if there is a 'no' in their Active column.
# Keeping the track of each of the removed members and append them to the `exMem` file. The format of the original files in preserved.

from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee = ('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))

genFiles(memReg,exReg)

# The two arguments for this function are the files:
#   - currentMem: File containing list of current members
#   - exMem: File containing list of old members

def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
            members.pop(0)
                
            inactive = [member for member in members if ('no' in member)]

            #go to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()
                
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)

# code to help you see the files

headers = "Membership No  Date Joined  Active  \n"

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())


    
