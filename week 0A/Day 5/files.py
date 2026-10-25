# Task
# save_note(text): appends the text as a new line to notes.txt. Call it three times with different text, then open notes.txt in VS Code to check.
def save_note(text):
    with open("notes.txt", "a") as file:
        file.write(text + "\n")
save_note("Review the project structure.")
save_note("Check pending tasks.")
save_note("Verify the changes.")


# count_lines(filename): returns the number of lines in a file, or 0 if the file doesn’t exist.
# Hint: try/except FileNotFoundError, and loop with a counter.
def count_lines(filename):
    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                count += 1
            return count
    except FileNotFoundError:
        print("File does not exist")

print(count_lines('notes.txt'))


# safe_divide(): asks for two numbers and prints the result of dividing the first by the second. It must not crash if the user types text or enters 0 as the second number.
# Hint: one try with two except blocks, except ValueError: and except ZeroDivisionError:.
def safe_divide():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter your second number: "))
        result = a / b
        print("Result: ", result)
    except ValueError:
        print("Enter a valid name.")
    except ZeroDivisionError:
        print("Enter a non zero number.")

safe_divide()