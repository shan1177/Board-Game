import random
x = str(input('Enter the name of Player 1: '))
y = str(input('Enter the name of Player 2: '))
z = str(input('Enter the name of Player 3: '))
print('\n')
temp = 1
txdice = 0
tydice = 0
tzdice = 0
while temp == 1:
    xdice = random.randint(1,6)
    ydice = random.randint(1,6)
    zdice = random.randint(1,6)
    print(x, 'rolled a', xdice)
    print(x, 'moves forward', xdice, 'spaces')
    txdice = txdice + xdice
    print(x, 'is at', txdice)
    print('\n')
    if txdice > 20:
        print(x, 'won the game, Congratulations')
        break
    print(y, 'rolled a', ydice)
    print(y, 'moves forward', ydice, 'spaces')
    tydice = tydice + ydice
    print(y, 'is at', tydice)
    print('\n')
    if tydice > 20:
        print(y, 'won the game, Congratulations')
        break
    print(z, 'rolled a', zdice)
    print(z, 'moves forward', zdice, 'spaces')
    tzdice = tzdice + zdice
    print(z, 'is at', tzdice)
    print('\n')
    if tzdice > 20:
        print(z, 'won the game, Congratulations')
        break