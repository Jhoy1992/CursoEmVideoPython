from random import randint
from time import sleep

computer = randint(1,3)
chose = ['', 'Rock', 'Paper', 'Scissors']
print('Rock = 1\nPaper = 2\nScissors = 3')
user = int(input('Choose one: \n'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if user == computer:
    print('You drew, there is no winner.')
elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
    print('Congratulations, {} beats {}. You won!'.format(chose[user], chose[computer]))
else:
    print('Sorry, {} beats {}. You lose!'.format(chose[computer], chose[user]))
