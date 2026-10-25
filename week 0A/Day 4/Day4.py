# List
fruits = ['apples', 'banana', 'cherry']
numbers = [10, 20, 30, 40]
mixed = ["Ali", 25, True]
empty = []

# indexing
print(fruits[0])    # apple
print(fruits[2])    # cherry
print(fruits[-1])   # cherry  (negative counts from the end)
print(len(fruits))  # 3       (how many items)

# slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:2])    # [10, 20]       (from the start)
print(numbers[3:])    # [40, 50]       (to the end)

# changing in lists
fruits.append("mango")        # add to the end
fruits.insert(1, "kiwi")      # insert at position 1
fruits.remove("banana")       # remove by value
last = fruits.pop()           # remove and return the last item
fruits[0] = "pear"            # replace an item

# built-ins
nums = [3, 1, 4, 1, 5]
print(sum(nums))
print('apple' in fruits)
nums.sort()
print(sorted(nums, reverse=True))


# looping over lists
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i, fruits[i])

for i, fruit in enumerate(fruits):
    print(i, fruit)

# building a new list while looping
evens = []
for n in range(1, 11):
    if n % 2 == 0:
        evens.append(n)
print(evens)

# dictionaries
person = {"name": "Sara", "age": 25, "city": "Lahore"}

print(person["name"])
print(person["age"])

# changes in dictionaries
person["job"] = "student"     # add a new key
person["age"] = 26            # update an existing key
del person["city"]            # delete a key
print(person)

# checking and access
print("name" in person)           # True  (checks keys)
print(person.get("email"))        # None  (no crash if missing)
print(person.get("email", "n/a")) # n/a   (custom default)

# looping in dictionaries
for key in person:
    print(key)

for key, value in person.items():
    print(f'{key}, {value}')


# counting pattern
text = "apple banana apple cherry banana apple"
words = text.split()          # split text into a list of words
counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts)   # {'apple': 3, 'banana': 2, 'cherry': 1}

# shorter version
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

# example
# Write a function that returns the second-largest number in a list.
def find_largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest
print(find_largest([3, 9, 2, 10, 7]))

