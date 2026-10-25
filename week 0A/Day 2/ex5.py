# Sum to n: Ask for a number n and print the sum of 1 + 2 + ... + n. For n = 10 the answer is 55.
number = int(input('Enter a number: '))
total = 0
for i in range(1, number + 1):
    total = total + i
print(total)