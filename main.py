from theSolution import winOrLoseWhenInALoop        # importing proposed solution
from randomChosin import winOrLoseWhenRandomised    # importing normal solution


# calculates the avarage of both solutions for randomly created 100 simulations
avarageOfProposedSolution = 0
avarageOfCasualSolution = 0
for i in range (100):
    if winOrLoseWhenInALoop()[1]: avarageOfProposedSolution += 0.01
    if winOrLoseWhenRandomised()[1]: avarageOfCasualSolution += 0.01

print("The avarage of 100 simulations with the proposed loop strategy: ", avarageOfProposedSolution)
print("The avarage of 100 simulations via randomly chosing strategy: ", avarageOfCasualSolution)