def is_even(n):
    return n % 2 == 0
if __name__ == "__main__":
    print(is_even(20))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result