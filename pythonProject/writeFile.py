# Read the file and store all the lines in the list
# Reverse the list
# Write the reverse list back to the file

with open('file.txt', 'r') as reader:
    content = reader.readlines()  # ['apple', 'boy', 'cat', 'dog', 'elephant']
    reversed(content)  # ['elephant', 'dog','cat', 'boy', 'apple']
    with open('file.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
