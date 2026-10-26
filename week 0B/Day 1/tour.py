from math import sqrt
import datetime
import os
import random as rnd

files = os.listdir(".")
today = datetime.date.today()
print(sqrt(144))
print(today.strftime("%A, %d %B %Y"))
print(rnd.randint(1, 100))
print(len(files))