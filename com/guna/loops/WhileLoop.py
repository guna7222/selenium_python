# taking age as a input from user
number = 10
while number < 20:
    print(number)
    print("lesser")
    number = number + 3

print("completed while loop")

# break
number1 = 15
while number1 < 20:
    if number1 == 17:
        break
    print(number1)
    number1 += 1

print("if condition match then it will break the while loop ")

# continue
number1 = 15
while number1 < 20:
    if number1 == 17:
        number1 += 1
        continue
    print(number1)
    number1 += 1
print("continue")

