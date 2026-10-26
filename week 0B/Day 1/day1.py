# modules
import math
print(math.sqrt(16))
print(math.pi)
print(math.ceil(4.2))

# other ways to import
from math import sqrt, pi
print(sqrt(25))

import random as rnd
print(rnd.randint(1, 6))

import datetime
today = datetime.date.today()
print(today)
print(today.year)
print(today.strftime("%A, %d %B %Y"))

# own module helpers.py
import helpers
print(helpers.is_even(22))
print(helpers.factorial(4))

# Packages and pips
# Beyond the standard library, other people publish code you can install. These are packages, shared through PyPI (the Python Package Index), and pip is the tool that installs them.


# virtual environment
# The problem: Project A needs version 1.0 of a package, and Project B needs version 2.0. If you install everything into one global place, they fight, and you can break your system’s own Python tools.

# The solution: a virtual environment (venv) is a private, isolated copy of Python for one project. Each project gets its own packages.


# example
import requests
response = requests.get("https://www.python.org")
print(response.status_code)
print(len(response.text))