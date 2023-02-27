# numeric data types
"""
- int
- float
- complex
"""
# String data type - str
# List is mutable
list_example1 = [1, 2, "Java", "Docker"]
# Index starts from zero
# if you want to fetch the values from list then we will use index or slicing
print(list_example1[3])   # Docker
print(list_example1[-1])  # you will get the last value

# slicing
slicing_values = list_example1[1:3]
print(slicing_values)  # here last value or item is exclusive

# insert method
list_example1.insert(2, "Python")
print(list_example1)

# update values in a list
list_example1[0] = 11
list_example1[1] = 12
print(list_example1)

# deleting
del list_example1[-1]
print(list_example1)

# append
list_example1.append("GSS")
print(list_example1)

# tuple is immutable
tuple_example = ("Python", "GSS", "RGS", 76)
tuple_example1 = tuple_example
print(tuple_example1)

# dictionary
dictionary_example = {"name": "GSS", 24: "age"}
dictionary_example["name"] = "RGSGSS"
print(dictionary_example)
dictionary_example1 = dictionary_example
print(dictionary_example1)

# empty dict
empty_dict = {}
empty_dict["last_name"] = 'Sekhar'
empty_dict["first_n"] = 'GSS'
print(empty_dict)