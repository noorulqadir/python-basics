# writing to a file
with open("notes.txt", "w") as file:
    file.write("Hello file\n")
    file.write("second line\n")
    file.write("Third line\n")

# Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
print(content)
# more often line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Handling errors with try/except
# amount = float(input("Amount: "))   #it will crash if you enter a string
try:
    amount = float(input("Amount: "))
    print(f'You entered this {amount}')
except ValueError:
    print("That was not a valid number")

# Common error types
# ValueError
# FileNotFoundError
# ZeroDivisionError
# KeyError
# IndexError


# example
def get_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")
get_amount()

# The first run problem
def load_lines():
    try:
        with open("expenses.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

print(load_lines())

# worked example
# A tiny to-do saver. Add a task to a file, then show all tasks.
def add_task(task):
    with open("task.txt", "a") as file:
        file.write(task + "\n")

def show_tasks():
    try:
        with open("task.txt", "r") as file:
            for number, line in enumerate(file, start=1):
                print(f'{number}. {line.strip()}')
    except FileNotFoundError:
        print("No task yet.")

add_task("Buy milk")
add_task("Finish Day 5")
show_tasks()

