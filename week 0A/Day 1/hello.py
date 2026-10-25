# first python program
print('hello, world!')


# variable and types
name = 'Alice'  # string
age = 30        # integer
height = 5.5   # float
is_student = True  # boolean
print('Name:', name)
print('Age:', age)
# for checking a value's type
print(type(age))
print(type(height))

# Math operators
print(7+2)  # addition
print(7-2)  # subtraction
print(7*2)  # multiplication
print(7/2)  # division
print(7//2) # floor division
print(7%2)  # modulus
print(7**2) # exponentiation

# Getting input
name = input('what is your name? ')
print('nice to meet you!', name)

# input always return a string so for numbers:
age = int(input("enter your age: "))
print(age + 1)
#use float() when you expect decimals

#f-strings
name = 'Ali'
age = 20
print(f'{name} is {age} years old.')
print(f'next year the {name} will be {age + 1} years old.')

# example use case:
# Ask for a length and width of a rectangle and prints its area.
length = float(input('length: '))
width = float(input('width: '))
area = length * width
print(f'The rectangle has {length} length and {width} width, so the area will be {area}')