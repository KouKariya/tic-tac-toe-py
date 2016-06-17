#functions.py
#Written by Jesse Gallarzo

#Add code here

def functionOne():
    name = input('What is your name? ')
    print('Hello, ' +name+ ' nice to meet you!')

def functionTwo():
    #We are asking for a number for the variable age
    age = int(input('How old are you? '))
    print('I cannot believe that you are '+str(age)+ ' years old!')
    #'str(age)' is casting the integer variable into a string in order to use it in the print statement above.

def functionThree():
    print('It does not matter in what order the functions are written.')
    print('The only order that matters is WHEN the functions are called')

#The main function
def main():
    #Below are the functions that are defined above.
    #Changing the order of functions below will change what gets displayed.
    functionOne()
    functionTwo()
    functionThree()

#The main fucntion needs to be called in order for the functions above to be called.
main()
