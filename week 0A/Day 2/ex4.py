#  FizzBuzz: For numbers 1 to 100, print the number, but:
# print Fizz if divisible by 3
# print Buzz if divisible by 5
# print FizzBuzz if divisible by both

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print(number, 'FizzBuzz')
    elif number % 3 == 0:
        print(number, 'Fizz')
    elif number % 5 == 0:
        print(number, 'Buzz')