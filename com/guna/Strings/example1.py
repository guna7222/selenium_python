# String is sequence of characters
str = 'Guna_Sekhar_Raghavaraju'
str1 = 'Guna'
# if you want to check certain sequence is present in the string or not
print(str1 in str) #True
# how to access the element in the String
first_name = str[0:4]
print(first_name)

last_character = str[-1]
print(last_character)

second_name = str[5:]
print(second_name)

for i in str:
    print(i)

str3 = "guna, sekhar, raghavaraju"
split_method = str3.split(",")
print(split_method)

str4 = "   remove spaces at beg and end      "
strip_method = str4.strip()
print(strip_method)

