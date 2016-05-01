#ticTacToe.py
#by Jesse Gallarzo

gameGrid = [[' ' for i in range(3)] for j in range(3)]
gameOver = False
answer = str()

def gameRules():
    print'Whoever matches three of a kind wins! Place either an X or an O within the grid'

def printGrid():
    print'|'+gameGrid[0][0]+'|'+gameGrid[0][1]+'|'+gameGrid[0][2]+'|'
    print'-------'
    print'|'+gameGrid[1][0]+'|'+gameGrid[1][1]+'|'+gameGrid[1][2]+'|'
    print'-------'
    print'|'+gameGrid[2][0]+'|'+gameGrid[2][1]+'|'+gameGrid[2][2]+'|'

def placeMove():
    global answer
    global gameOver
    global gameGrid
    ans = raw_input('Xs or Os? ')
    index = int(input('What position? '))
    count = 1
    for i in range(3):
        for j in range(3):
            if count == index:
                gameGrid[i][j] = ans
                answer = ans
                return
            else:
                count += 1

def gameWinner():
    global gameOver
    for i in range(3):
        if answer == gameGrid[i][0] and answer == gameGrid[i][1] and answer == gameGrid[i][2]:
            print answer + 's are the winner'
            gameOver = True

    for j in range(3):
        if answer == gameGrid[0][j] and answer == gameGrid[1][j] and answer == gameGrid[2][j]:
            print answer + 's are the winner'
            gameOver = True

def main():
    gameRules()
    global gameOver
    while gameOver != True:
        printGrid()
        placeMove()
        gameWinner()

    printGrid()
    print 'Game over...'
    
    
main()
