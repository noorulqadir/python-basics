# Average calculator: Ask for three numbers and print their average.
a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c  =int(input('Enter your third number: '))
avg = (a + b + c) / 3
print(f'Average: {avg}')

# optional exercise:
# Ask for a number of seconds and print how many minutes and leftover seconds that is.
s = int(input('Enter number of seconds: '))
print(f'This is  how many minutes are these {s} seconds: {s//60}minutes ')
print(f'This is the left over seconds: {s%60} sec')
