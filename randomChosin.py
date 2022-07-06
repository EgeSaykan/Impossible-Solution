from random import random, shuffle #shuffles the list

# the function to simulate the chosing process for 100 prisoners
# by randomly chosing boxes
# the function returns a list of 2 variables
# first variable is a list with 2 variables, first variables is wins out of 100, and second one is losses our of 100
# the second one is if the prisoners have survived or not (true or false)
def winOrLoseWhenRandomised():
    # keeps a track of how many wins and losses there has been
    winsAndLosses = [0, 0]

    # randomly genarated list that represents the boxes with numbers in them
    chestList = [i for i in range(100)]
    shuffle(chestList)
    chestList = set(chestList)  # sets are significantly faster when checking if an element exists in the array

    # loops through each prisoner
    for prisoner in range(100):

        chosenNumbers = set()   # records the numbers that already been chosen
        found = False           # true if the prisoner finds their number
        
        # loops through each box
        for i in range(50):
            
            # chose a random box
            randomNumber = random()
            while randomNumber in chosenNumbers: randomNumber = random()

            # check if the prisoner has found their number
            if randomNumber == prisoner:
                found = True
            
            # record which boxes have been opened
            chosenNumbers.add(randomNumber)

        # increment wins or losses
        if found: winsAndLosses[0] += 1
        else: winsAndLosses[1] += 1
    
    # return wins or losses
    return ([winsAndLosses, winsAndLosses[0] == 100])
