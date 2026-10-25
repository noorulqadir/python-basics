# Fizzbuzz from 1 to 100
for n in range(1, 101):
    if n % 3 == 0  and n % 5 == 0:
        print(n, "FizzBuzz")
    elif n % 3 == 0:
        print(n, "Fizz")
    elif n % 5 == 0:
        print(n, "Buzz")


# count_vowels(text), returning the number of vowels. Test it with "Hello World" (should give 3).
def count_vowels(text):
    count = 0
    for letter in text:
        if letter in "aeiou":
            count =  count + 1
    return count
print(count_vowels("Hello World"))


# word_count(sentence), returning a dictionary of how often each word appears. Test it with "the cat and the hat".
def word_count(sentence):
    words = sentence.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print(word_count("the cat and the hat"))