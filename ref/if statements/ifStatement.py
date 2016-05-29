#ifStatement.py
#Written by Jesse Gallarzo

#The script prompts the user for their age.
age = int(input('How old are you? '))

#The if statement compares the age against a predetermined value
if(age > 17):
    #If the age recorded is above 17...
    print('You are an adult, congradulations...now get a job!')
    #If the age recorded is 17 or below...
else:
    print('You are still a kid...now go to school!')
