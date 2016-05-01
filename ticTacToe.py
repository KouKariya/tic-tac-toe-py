#ticTacToe.py

gameGrid = [ [' ' for i in range(3)] for j in range(3)]
gameWon = False
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
    ans = raw_input('Xs or Os?')
    index = int(input('What position?'))
    count = 1
    for i in range(3):
        for j in range(3):
            if(count == index):
                gameGrid[i][j] = ans
                answer = ans
                break
            elif(count > 9):
                gameOver = True
            else:
                count = count + 1
        #if(count == index): break #TEST

def gameWinner():
    global gameWon
    for i in range(3):
        if(answer == gameGrid[i][0] and answer == gameGrid[i][1] and answer == gameGrid[i][2]):
            print'TEST is the winner'
    

def main():
    gameRules()
    #printGrid()
    while(gameWon != True or gameOver != True):
        printGrid()
        placeMove()
        gameWinner()
    
    
main()
