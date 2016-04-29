#ticTacToe.py


def gameRules():
    print'Whoever matches three of a kind wins! Place either an X or an O within the grid'

def printGrid():
    print'|1|2|3|'
    print'-------'
    print'|4|5|6|'
    print'-------'
    print'|7|8|9|'

def placeMove( move , index):
    count = 1
    for i in range(3):
        for j in range(3):
            if(count == index):
                gameGrid[i][j] = move #add global keyword after gameGrid has been made globally
            else:
                count = count + 1

#def gameWinner( ans ):
    #for i in range(len(gameRow1)):
        #if(ans == gameRow(0) and ans == gameRow(1) and ans == gameRow(2)):
            #print'TEST is the winner'
    

def main():
    gameRules()
    printGrid()

    #create this in function and make it global
    gameGrid = [ ['' for i in range(3)] for j in range(3)]
    print gameGrid
    
    
    


main()
