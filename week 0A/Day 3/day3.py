# functions
def greet():
    print("Hello!")
    print("Welcome to Python!")

greet()
greet()


#  Parameters
def greet(name):
    print(f'Hello, {name}!')

greet('Sara')
greet('Ali')

def add(a, b):
    print(a+b)

add(3, 4)

# Return
def add(a, b):
    return a + b
result = add(3, 4)
print(result)
print(add(10, 5) * 2)

def add_bad(a, b):
    print(a + b)
x = add_bad(3, 4)
print(x)

# Returning True/False
def is_adult(age):
    return age >= 18
print(is_adult(20))
print(is_adult(15))

if is_adult(20):
    print('You can Vote!')

# Default Arguments
def power(base, exponent = 2):
    return base**exponent
print(power(5))
print(power(5, 3))

# Variable scope
def make_total():
    total = 100
    return total
make_total()
# print(total) # NameError: total doesn't exist out here

# Functin calling function
def square(n):
    return n*n

def sum_of_square(a, b):
    return square(a) + square(b)

print(sum_of_square(3, 4))


# Example
# Write a function that counts how many numbers in a range are divisible by 3.
def count_divisible_by_3(n):
    count = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            count = count + 1
    return count

print(count_divisible_by_3(10))