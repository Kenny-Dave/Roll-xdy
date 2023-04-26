#Roll.py
import random

inputString ="!roll 3D3".lower()
rollSum=0

def Roll(inputString):

        nums = inputString.lstrip("!roll ")
        numList=nums.split("d")
        
        rollSum=0

        if len(numList) !=2:
            return
        else:

            for r in range(1, int(numList[0])+1):
                roll = random.choice(range(1, int(numList[1])+1))
                print("roll: ", str(r), "Outcome: ",roll)
                rollSum =rollSum+roll

            return rollSum

if inputString.startswith("!") ==False:
    pass
elif inputString.startswith("!roll") ==True:

    if inputString.endswith("d3"):
        print("LOL. Ok Satan.")
    else:
        rollSum = Roll(inputString)

        if rollSum!=0:
            print("With \""+inputString+"\" you rolled "+str(rollSum)+".")
        else:
            pass #error
        rollSum=0