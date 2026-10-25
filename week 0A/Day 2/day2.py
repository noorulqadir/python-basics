# comparisons
# ==  --> equal to
# !=  --> not equal to
# >   --> greater then
# <  --> less then
# >=   --> greater or equal
# <=  --> less or equal

# Combining conditions with and, or, not:
age = 20
print(age >= 18 and age <= 65)
print(age<13 or age>60)
print(not age == 20)

# If/ elif/ else
temperature = 28
if temperature >30:
    print('Its hot')
elif temperature >20:
    print('Its warm')
else:
    print('its cold')

number = 7
if number % 2 == 0:
    print('even')
else:
    print('odd')

# For loops and range
for i in range(5):
    print(i)

# range has three forms
range(5)         # 0, 1, 2, 3, 4
range(1, 6)      # 1, 2, 3, 4, 5      (start, stop-before)
range(0, 10, 2)  # 0, 2, 4, 6, 8      (start, stop-before, step)

# we can also loop through text
for letter in 'hello':
    print(letter)

# Accumulator pattern
total = 0
for n in range (1, 6):
    total = total + n
print(total)

# while loop
count = 3
while count > 0:
    print(count)
    count = count -1
print('liftoff!')

# Break and continue
for n in range(1, 10):
    if n == 3:
        continue      # skip 3
    if n == 6:
        break         # stop completely at 6
    print(n)

# random numbers
import random
secret =  random.randint(1, 10)
print(secret)



# Example
# Keep asking for a password until the user types the right one.
while True:
    password = input("Enter your password: ")
    if password == "python123":
        print("Excess granted")
        break
    print("Wrong Password!")