# If Loop Example -->
greeting = "Good Morning"
num = 4

if greeting == "Good Morning" and num > 3:
    print("condition matches")
    print("2nd Line")
else:
    print("condition do not match")
print("Outside if else loop")

# For Loop Example -->
obj = [2, 4, 6, 8, 10]

for i in obj:
    print(i)
print("For Loop completed")

# Print sum of first five natural numbers
summation = 0
for i in range(1, 6):
    summation = summation + i
print(summation)

print("**********************")
for j in range(1, 10, 2):
    print(j)

print("-------Skipping 1st Index ----------")
for k in range(10):
    print(k)

print("######## While Loop Example ######")
# While Loop Example -->
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

print("While Loop completed !!")
