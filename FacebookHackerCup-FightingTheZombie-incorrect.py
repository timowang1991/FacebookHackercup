import sys
import numpy as np

dp = {} #key : faces of dice   # value : dp array

def getProbArray(diceFace, numOfRolls):
    if numOfRolls == 1:
        dp[diceFace] = [0, [1.0/diceFace] * diceFace]
        return dp[diceFace][numOfRolls]

    if diceFace in dp and len(dp[diceFace]) > numOfRolls:
        return dp[diceFace][numOfRolls]

    lastRollProb = getProbArray(diceFace, numOfRolls - 1)
    thisRollProb = np.convolve(lastRollProb, [1.0/diceFace] * diceFace)
    dp[diceFace].append(thisRollProb)
    return thisRollProb
    

with open(sys.argv[1]) as inFile:
    next(inFile)
    for i, line in enumerate(inFile, 1):
        zombieLife = int(line[:-1].split(' ')[0])
        spells = next(inFile)[:-1].split(' ')
        maxProb = 0
        for spell in spells:
            z = 0
            numOfRolls = 0
            diceFace = 0
            if '+' in spell:
                spellSplit = spell.split('+')
                z = int(spellSplit[1])
                numOfRolls = int(spellSplit[0].split('d')[0])
                diceFace = int(spellSplit[0].split('d')[1])
            elif '-' in spell:
                spellSplit = spell.split('-')
                z = -int(spellSplit[1])
                numOfRolls = int(spellSplit[0].split('d')[0])
                diceFace = int(spellSplit[0].split('d')[1])
            else:
                numOfRolls = int(spell.split('d')[0])
                diceFace = int(spell.split('d')[1])

            probArr = getProbArray(diceFace, numOfRolls)
            try:
                maxProb = max(maxProb, sum(probArr[(zombieLife - z - numOfRolls):]))
            except Exception as e:
                pass
        print "Case #{}: {:.6f}".format(i, maxProb)