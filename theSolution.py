from random import shuffle  #shuffles the list

# the function to simulate the chosing process for 100 prisoners
# using the looping technique
# the function returns a list of 2 variables
# first variable is a list with 2 variables, first variables is wins out of 100, and second one is losses our of 100
# the second one is if the prisoners have survived or not (true or false)
def winOrLoseWhenInALoop():
    
    # keeps a track of how many wins and losses there has been
    winsAndLosses = [0, 0]

    # randomly genarated list that represents the boxes with numbers in them
    chestList = [i for i in range(100)]
    shuffle(chestList)

    # loops through each prisoner
    for prisoner in range(100):
        index = prisoner    # the index of next box to check
        found = False       # true if the prisoner finds their number

        # loops through each box
        for i in range(50):

            # check the number in the box numbered index, set found true if the numbers match
            if chestList[index] == prisoner:
                found = True
                break
            
            # set the next box index to number that was in the box that was just checked
            index = chestList[index]
        
        # increment wins or losses
        if not found: winsAndLosses[1] += 1
        else: winsAndLosses[0] += 1

    # return wins or losses
    return([winsAndLosses, winsAndLosses[0] == 100])
