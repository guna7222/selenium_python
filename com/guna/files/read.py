# open function is used to read the text files
file = open('python_notes.txt')
content_from_the_txt_file = file.read()
print(content_from_the_txt_file)

print(file.readline())  # it will print only first line

file.close()
