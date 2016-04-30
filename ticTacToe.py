#ticTacToe.py

gameGrid = [ [' ' for i in range(3)] for j in range(3)]
gameWon = False
gameOver = False

def gameRules():
    print'Whoever matches three of a kind wins! Place either an X or an O within the grid'

def printGrid():
    print'|'+gameGrid[0][0]+'|'+gameGrid[0][1]+'|'+gameGrid[0][2]+'|'
    print'-------'
    print'|'+gameGrid[1][0]+'|'+gameGrid[1][1]+'|'+gameGrid[1][2]+'|'
    print'-------'
    print'|'+gameGrid[2][0]+'|'+gameGrid[2][1]+'|'+gameGrid[2][2]+'|'

def placeMove(move,index):
    print move
    x = move
    global gameGrid
    count = 1
    for i in range(3):
        for j in range(3):
            if(count == index):
                print move
                gameGrid[i][j] = x
            else:
                count = count + 1

#def gameWinner( ans ):
    #for i in range(len(gameRow1)):
        #if(ans == gameRow(0) and ans == gameRow(1) and ans == gameRow(2)):
            #print'TEST is the winner'
    

def main():
    gameRules()
    #printGrid()
    while(gameWon != True or gameOver != True):
        printGrid()
        a = raw_input('Xs or Os?')
        b = raw_input('Where?...')
        placeMove(a,b)
        gameGrid[2][2] = 'x' #TEST

    #create this in function and make it global
    
    
    


main()
