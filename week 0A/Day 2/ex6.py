# Number-guessing game: The program picks a secret number from 1 to 10. The user keeps guessing until correct. After each wrong guess, say “Too high” or “Too low”. At the end, print how many guesses it took.
import random
secret = random.randint(1, 10)
guesses = 0
while True:
    password = int(input('Enter your secret key from 1 to 10:'))
    guesses = guesses + 1
    
    if password == secret:
        print('Got It!')
        break
    elif password > secret:
        print('Too High')
    else:
        print('Too Low')

print("total guesses:", guesses)


#Bonus exercise
# Print a multiplication table for a number the user enters (for 3: 3 x 1 = 3 up to 3 x 10 = 30).
n = int(input('Enter you number: '))
for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')