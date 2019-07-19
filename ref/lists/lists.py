#lists.py
#Written by Jesse Gallarzo
#run in Python3 otherwise change input to raw_input for python2

listOfNames = []

#A for loop that runs five times.
#For every iteration, the name variable gets added to the list until the loop stops.
for num in range(5):
    name = input('Enter a name: ')
    listOfNames.append(name)

print(listOfNames)

#For every value(num) within the list 'listOfNames'
#print out a specific value from the list in the index denoted by 'num'.
for num in range(len(listOfNames)):
    print(listOfNames[num])

#Below is a 3 dimentional list.
#The 3x3 list serves as an example to demonstrate how to create lists within lists, how to iterate through a 3 dimentional list
# and how to print out its content.
threeThreeGrid = [[' ' for i in range(3)] for j in range(3)]

for i in range(3):
    for j in range(3):
            name = input('Enter a name: ')
            threeThreeGrid[i][j] = name

print(threeThreeGrid)
