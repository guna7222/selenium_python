# reading and writing file using with keyword
with open('python_notes.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('python_notes.txt', 'w') as writer:
       for lines in reversed(content):
           writer.write(lines)



