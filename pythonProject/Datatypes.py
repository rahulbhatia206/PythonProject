# List Datatype Examples -->
values = [1, 2, "rahul", 3, 4, 5]

print(values[2])  # Output is rahul
print(values[1])  # Output is 2
print(values[-1])  # last-index #Output is 5

print(values[1:3])  # Output is [2, 'rahul']

values.insert(3, "bhatiya")
print(values)  # Output is [1, 2, 'rahul', 'bhatiya', 3, 4, 5]

values.append("End")
print(values)  # Output is [1, 2, 'rahul', 'bhatiya', 3, 4, 5, 'End']

values[2] = "RAHUL"
values[6] = 6
del values[0]

print(values)  # Output is [2, 'RAHUL', 'bhatiya', 3, 4, 6, 'End']


# Tuple Datatype Examples -->
# Same as List but immutable (not changeable)
tup = (1, 2, "rahul", 4.5)
print(tup[3])


# Dictionary Datatype Examples -->
dict = {"a": 2, 4: "bcd", "c": "Hello world"}

print(dict[4])  # Output is bcd
print(dict["c"])  # Output is Hello world


# Add dictionary key and values at Runtime
oxford = {}

oxford["fname"] = "Rahul"
oxford["lname"] = "Bhatiya"
oxford["sex"] = "Male"

print(oxford)
print(oxford["lname"])
