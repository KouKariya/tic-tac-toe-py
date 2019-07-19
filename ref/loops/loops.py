#loops.py
#Written by Jesse Gallarzo

#The script prompts the user for their age.
#age is the integer variable used for the for loop
#age2 is the integer variable used for the while loop
#adult is the boolean variable used for the while loop 
age = int(input('How old are you? '))
age2 = age
adult = False



#This is an exampe of a for loop:
#For every value between the age variable and 19, print your age.
#Print contents of the 'else' statement once num reaches 18
for num in range(age,19):
	if(num <= 17):
		print('I am sorry, you are still '+str(num)+ ' years old..')
	else:
		print('You are all grown up now!')
		print('\n')



        
#This is an example of a while loop.
#So long as the adult variable is 'false', run the if-statement to check your age
while(adult is False):
	if(age2 <= 17):
		print('I am sorry, you are still '+str(age2)+ ' years old..')
		age2 += 1 #Here we are incrementing the value of the 'age2' variable for every loop iteration
	else:
		adult = True
#Once the value of age2 is greater than 17, the adult variable becomes 'true' and breaks the for loop.
print('You are all grown up now!')
