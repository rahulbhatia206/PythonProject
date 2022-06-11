
try:
    with open('NoFile.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)
    print("We reached here because there is Failure in Try Block, We got No such file Exception !!!!!")

finally:
    print("This will print everytime !!!!")
