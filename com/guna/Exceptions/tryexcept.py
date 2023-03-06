# if you though this will raise the exception then you can put that code in try and catch the exception in except block
try:
    with open('hello.txt') as reader:
        reader.read()
except Exception as e:
    print(e)

# finally block should use along with try and except
# finally blocks executes in all the cases.
finally:
    print("close all resources")
