import random
print('Number guessing game')
num = random.randint(1,9)
chances = 0
print('Guess a number between 1 to 9:')
while chances<5:
    guess = int(input())
    if guess == num:
        print('Congrats, you win')
        break
    elif guess < num:
        print('Your guess was too low: guess a number higher than',guess)
    else:
        print('Your guess was too high: guess a number lower than',guess)
    chances += 1
if not chances < 5:
    print('You lose ..the number is', num)