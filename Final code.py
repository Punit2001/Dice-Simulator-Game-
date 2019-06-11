import time
from random import randint


def roll():
    dice_reps = ("",
                 "  _ _ _ \n |     |\n |  .  |\n |_ _ _|\n ",
                 "  _ _ _ \n |     |\n | . . |\n |_ _ _|\n ",
                 "  _ _ _ \n |     |\n | ... |\n |_ _ _|\n ",
                 "  _ _ _ \n | . . |\n | . . |\n |_ _ _|\n ",
                 "  _ _ _ \n | . . |\n | .`. |\n |_ _ _|\n ",
                 "  _ _ _ \n | ... |\n | ... |\n |_ _ _|\n ")
    value = randint(1, 6)
    print (dice_reps[value])
    return value

answer = input('Roll the dice? [Y/n]\n> ')

while answer.lower() in ('', 'y', 'yes', 'k', 'ok'):
    answer2 = input('How many times? [1-5]\n> ')
    total = 0
    for x in range(int(answer2)):
        total += roll()
    print ("Total =", total, "\n")
    answer = input('Again? [Y/n]\n> ')

print ('Thanks for playing!')
time.sleep(3)
