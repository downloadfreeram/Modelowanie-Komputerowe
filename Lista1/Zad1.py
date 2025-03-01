import random
import matplotlib.pyplot as plt

def diceThrow():
    '''
    Generate a number being result of a throw of two dices
    '''
    return random.randint(1,6) + random.randint(1,6)

def game(n):
    '''
    Generate a game with n-dice throws and print the result of numbers of visits of each place in a dictionary
    '''
    # Player starts at first element
    pos = 0
    
    # Board for the game
    board = {}
    for i in range(40):
        board[i] = 0

    for i in range(n):
        pos += diceThrow()
        if(pos >= 40):
            pos = pos - 40
        board[pos] += 1
    print("for ",n," throws")
    print(board)
    # Plot the result
    plt.plot(board.keys(),[i/n for i in board.values()], "--bo")
    plt.xlabel("Pole (i)")
    plt.ylabel("p")
    plt.title(f"Rozklad prawdopodobienstwa p(i) dla {n} rzutów")
    plt.show()

def game_with_prison(n):
    '''
    Generate a game with n-dice throws and print the result of numbers of visits of each place in a dictionary, including the prison tile, where if the player stands on a field 30, then is moved on a field 10
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
        # Whenever Player steps on the prison, go back to field 10
        if(pos == 30):
            pos = 10
            a[pos] += 1
    print("for ",n," throws")
    print(a)
    # Plot the result
    plt.plot(a.keys(),[i/n for i in a.values()], "--bo",)
    plt.xlabel("Pole (i)")
    plt.ylabel("p")
    plt.title(f"Rozklad prawdopodobienstwa p(i) dla {n} rzutów z uwzglednieniem pola 'wiezienie'")
    plt.show()


# test cases
game(100)

game(1000000)

game_with_prison(100)

game_with_prison(1000000)
