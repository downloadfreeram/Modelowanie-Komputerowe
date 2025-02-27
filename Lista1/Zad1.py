import numpy
import random
import matplotlib.pyplot as plt

def diceThrow():
    '''
    Generate a number being result of two dice throws
    '''
    return random.randint(1,6) + random.randint(1,6)

def game(n):
    '''
    Generate a game with n-dice throws and print the result of numbers of visits of each place in a dictionary
    '''
    # Player starts at first element
    pos = 0
    
    # Board for the game
    a = {}
    for i in range(40):
        a[i] = 0

    for i in range(n):
        pos += diceThrow()
        if(pos >= 40):
            pos = pos - 40
        a[pos] += 1
    for i in a.values():
        i = i/n
        print(i)
    print("for ",n," throws")
    print(a)
    plt.plot(a.keys(),[i/n for i in a.values()])
    plt.title(f"Rozklad prawdopodobienstwa p(i) dla {n} rzutów")
    plt.show()

game(100)

game(1000000)
