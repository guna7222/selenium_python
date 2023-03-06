file = open('python_notes.txt')

# using for loop
# for files in file:
#     print(file.readline())
#
# file.close()

# using while loop
while file:
    line = file.readline()
    print(line)
    if line == "":
        break
file.close()
print("579521640")