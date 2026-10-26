def is_even(n):
    return n % 2 == 0
if __name__  == "__main__":
    print(is_even(46))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

if __name__ == "__main__":
    print(factorial(5))


def count_vowels(sentence):
    count = 0
    for char in sentence:
        if char in "aeiou":
            count += 1
    return count

if __name__ == "__main__":
    print(count_vowels("hello world"))