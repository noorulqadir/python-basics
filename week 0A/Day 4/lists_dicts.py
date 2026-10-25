# Task 1
# min_max(numbers): returns the smallest and largest numbers without using min() or max()..
# Test: min_max([4, 9, 1, 7]) should give 1 and 9. Hint: use the “start with the first item” pattern twice, or in one loop with two variables. To return two values, write return smallest, largest, and receive them with low, high = min_max(...).
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
        elif n < smallest:
            smallest = n
    return smallest, largest
low, high = min_max([4, 9, 1, 7])
print(low)
print(high)




# Task 2
# word_count(sentence): returns a dictionary of how many times each word appears.
# Test: word_count("the cat and the hat") gives {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}. Hint: .split(), then the counting pattern. Convert to lowercase first so “The” and “the” count together.
def word_count(sentence):
    words = sentence.lower().split()
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(word_count("the cat and the hat"))



# Task 3
# remove_duplicates(items): returns a new list with duplicates removed, keeping the original order..
# Test: remove_duplicates([1, 2, 2, 3, 1, 4]) gives [1, 2, 3, 4]. Hint: build an empty result list, and only append an item if it’s not in result already.
def remove_dupplicates(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)
    return result
print(remove_dupplicates([1, 2, 2, 3, 1, 4]))


# Bonus 1
# second_largest(numbers) returns the second-largest value. Assume at least two different numbers.
def second_largest(numbers):
    largest = 0
    second = 0

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num < largest:
            second = num
    return second
print(second_largest([4, 9, 1, 7]))


# Bonus 2
# Write a function that takes a list of expense dictionaries (like the example above) and returns the total of all the amount values. This is a preview of tomorrow’s project.
expenses = [
    {"amount": 12.5, "category": "food", "description": "lunch"},
    {"amount": 40.0, "category": "transport", "description": "taxi"},
]
def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]
    return total
print(total_expenses(expenses))

