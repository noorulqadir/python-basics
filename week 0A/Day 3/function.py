# is_even(n): returns True if n is even, otherwise False.
# Test: is_even(4), is_even(7), is_even(0). Hint: use % and return the comparison directly.

def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(7))
print(is_even(0))


# count_vowels(text): returns how many vowels (a, e, i, o, u) are in the text.
# Test: count_vowels("Hello World") should give 3. Hint: loop through the letters, and use in "aeiou" to check. Convert to lowercase first with text.lower() so capital letters count too.

def count_vowels(text):
    text = text.lower()
    count = 0
    
    for letter in text:
        if letter in "aeiou":
            count = count + 1
    return count

print(count_vowels('Hello World'))


# factorial(n): returns n! (for example, factorial(5) = 5 × 4 × 3 × 2 × 1 = 120).
# Test: factorial(5) gives 120, and factorial(1) gives 1. Hint: start a result at 1 and multiply it by each number from 1 to n.

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i
    return result
print(factorial(5))
print(factorial(1))

# Bonus
# is_palindrome(word) returns True if the word reads the same backward. "level" is True, "hello" is False. Hint: a string can be reversed with word[::-1].
def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome("level"))
print(is_palindrome("hello"))


# Rewrite your Day 2 FizzBuzz as a function fizzbuzz(n) that returns the correct text for one number ("Fizz", "Buzz", "FizzBuzz", or the number), then loop 1-100 and print(fizzbuzz(i)).
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

for i in range(1, 101):
    print(fizzbuzz(i))

