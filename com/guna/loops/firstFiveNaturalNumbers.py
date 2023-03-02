# first five natural numbers
natural_list = []
for i in range(1, 6):
    natural_list.append(i)

print("The first five {} Natural numbers".format(natural_list))

# sum of first five natural numbers
sum_of_natural_numbers = 0
for i in range(1, 6):
    sum_of_natural_numbers = i + sum_of_natural_numbers
    print(sum_of_natural_numbers)

print("sum of first five natural numbers is {} ".format(sum_of_natural_numbers))
