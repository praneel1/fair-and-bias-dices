import random as r



def fairDiceThrow():    #Fair Dice (Equal chances of all numbers)
    fairOutput = r.choice([1,2,3,4,5,6])
    # print(fairOutput)
    return fairOutput


def moreSixThrow():    #10 times more chances of 6
    moreSixOutput = r.choice([1,2,3,4,5,6,6,6,6,6,6,6,6,6,6])
    # print(moreSixOutput)
    return moreSixOutput


def lessSixThrow():   #10 times less chances of 6
    lessSixOutput = r.choice([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6])
    # print(lessSixOutput)
    return lessSixOutput


NumUp = [];
for x in range(10):                          #Change the range for more observations
    NumUp.append(moreSixThrow())             #Change the append name for checking p(e) of other dices

# print(NumUp)

# diceChosen = "Fair Dice"
diceChosen = "More 6 Dice"
# diceChosen = "Less 6 Dice"

probablity = NumUp.count(6)/ len(NumUp)
print("Probablity for", diceChosen, "is", probablity)
