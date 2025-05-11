import math
import threading
import asyncio

# 1. Variables and Data Types
x = 10  # Integer
y = 3.14  # Float
name = "Python"  # String
is_active = True  # Boolean

# 2. Data Structures
my_list = [1, 2, 3]  # List
my_tuple = (4, 5, 6)  # Tuple
my_set = {7, 8, 9}  # Set
my_dict = {"key1": "value1", "key2": "value2"}  # Dictionary

# 3. Control Flow
for i in range(3):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# 4. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

# 5. Classes and Objects
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

dog = Animal("Dog")
print(dog.speak())

# 6. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# 7. File Handling
with open("example.txt", "w") as file:
    file.write("Hello, File!")

# 8. Modules and Libraries
print(math.sqrt(16))

# 9. List Comprehensions
squares = [x**2 for x in range(5)]
print(squares)

# 10. Generators
def my_generator():
    for i in range(3):
        yield i

for value in my_generator():
    print(value)

# 11. Decorators
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# 12. Lambda Functions
add = lambda a, b: a + b
print(add(5, 7))

# 13. Multithreading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# 14. Asynchronous Programming

async def async_hello():
    await asyncio.sleep(1)
    print("Hello, Async!")

asyncio.run(async_hello())

# 15. Context Managers
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContextManager() as cm:
    print("Inside context")

# 16. Type Hinting
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(3, 4))
