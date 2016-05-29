#loops.py
#Written by Jesse Gallarzo

#The script prompts the user for their age.
age = int(input('How old are you? '))

#the following line creates a for loop
#for every value 'num' in range of 5 e.i. this for loop happens 5 times
for num in range(5):
    #Check to see if the value of age is greater than 17
    #If it is, print the statement below and 'break' from the loop
    if(age > 17):
        print('You are all grown up now!')
        break;
    #Else, if the age variable is not high enough...
    #print the statement below and increment the value of 'age' by 1
    #str(age) converts the integer variable 'age' into a string in order to
    #concantenate the value into our sentence.
    else:
        print('I am sorry, you are still '+str(age)+ ' years old..')
        age += 1