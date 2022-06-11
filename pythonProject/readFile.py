file = open('file.txt')

# Read all contents of file
# print(file.read())

#Read only specific content
# print(file.read(8))

#Read 1 single line at a time
# print(file.readline())
# print(file.readline())

#Print line by line using readline method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

# Read file from list ['apple', 'boy', 'cat', 'dog', 'elephant']
for line in file.readlines():
    print(line)

file.close()
