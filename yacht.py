"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8 #3 of one face and 2 of another
FOUR_OF_A_KIND = 9 #At least four dice showing the same face
LITTLE_STRAIGHT = 10 #1-2-3-4-5
BIG_STRAIGHT = 11 #2-3-4-5-6
CHOICE = 12 #Sum of the dice

def freq(dice):
    #Return array of 6 elements
    #First element is number of 1s in dice
    f = [0, 0, 0, 0, 0, 0]
    for i in dice:
        f[i-1] += 1
    return f

def score(dice, category):
    result = 0
    #First work out what values the dice are
    #Score determined on which category is chosen
    if category == YACHT: #All the same and yacht category selected
        f = freq(dice)
        for i in f:
            if f[i-1] == 5:
                result += 50
                break
            else:
                result = 0
    elif category == FULL_HOUSE:
        f = freq(dice)
        count = 0
        threecounted = False
        twocounted = False
        for i in f:
            print(f">>>>>>>>>>{f}<<<<<<<<<<<<<")
            print(f">>>>>>>>>>{f[i-1]}<<<<<<<<<<<<<")
            if i == 3 and threecounted != True:
                threecounted = True
                count += 1
            if i == 2 and twocounted != True:
                twocounted = True
                count += 1
        if count == 2:
            #Total of the dice
            for i in dice:
                result += i
    elif category == ONES:
        #return result of 2 * number of fives in dice
        faces = []
        for i in dice:
            if i == 1:
                faces.append(i)
        if faces != []:
            result += 1 * len(faces)
    elif category == TWOS:
        #return result of 2 * number of fives in dice
        faces = []
        for i in dice:
            if i == 2:
                faces.append(i)
        if faces != []:
            result += 2 * len(faces)
    elif category == THREES:
        #return result of 2 * number of fives in dice
        faces = []
        for i in dice:
            if i == 3:
                faces.append(i)
        if faces != []:
            print(f">>>>>>>{faces}<<<<<<<")
            result += 3 * len(faces)
    elif category == FOURS:
        #return result of 2 * number of fives in dice
        faces = []
        for i in dice:
            if i == 4:
                faces.append(i)
        if faces != []:
            result += 4 * len(faces)
    elif category == FIVES:
        #return result of 2 * number of fives in dice
        faces = []
        for i in dice:
            if i == 5:
                faces.append(i)
        if faces != []:
            print(f">>>>>>>{faces}<<<<<<<")
            result += 5 * len(faces)
    elif category == SIXES:
        #return result of 2 * number of fives in dice
        faces = []
        for i in dice:
            if i == 6:
                faces.append(i)
        if faces != []:
            result += 6 * len(faces)
    return result
