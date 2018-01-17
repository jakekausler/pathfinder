
import roll
import config

import random


def RandomAbilityCalculationMethod():
    return random.choice([config.ABILITY_CALCULATION_STANDARD,
                          config.ABILITY_CALCULATION_CLASSIC,
                          config.ABILITY_CALCULATION_HEROIC,
                          config.ABILITY_CALCULATION_DICEPOOL,
                          config.ABILITY_CALCULATION_PURCHASE])


def GetAbilityName(a):
    if a == config.ABILITY_STRENGTH:
        return 'Strength'
    if a == config.ABILITY_DEXTERITY:
        return 'Dexterity'
    if a == config.ABILITY_CONSTITUTION:
        return 'Constitution'
    if a == config.ABILITY_INTELLIGENCE:
        return 'Intelligence'
    if a == config.ABILITY_WISDOM:
        return 'Wisdom'
    if a == config.ABILITY_CHARISMA:
        return 'Charisma'


def GetAbilityNames():
    return [config.ABILITY_STRENGTH, config.ABILITY_DEXTERITY, config.ABILITY_CONSTITUTION, config.ABILITY_INTELLIGENCE, config.ABILITY_WISDOM, config.ABILITY_CHARISMA]


def GenerateRandomBase(baseDict, method=config.ABILITY_CALCULATION_STANDARD, numDice=24, minDice=3, points=15):
    if method == config.ABILITY_CALCULATION_STANDARD:
        GenerateRandomBaseStandard(baseDict)
    if method == config.ABILITY_CALCULATION_CLASSIC:
        GenerateRandomBaseClassic(baseDict)
    if method == config.ABILITY_CALCULATION_HEROIC:
        GenerateRandomBaseHerioic(baseDict)
    if method == config.ABILITY_CALCULATION_DICEPOOL:
        GenerateRandomBaseDicePool(baseDict, numDice, minDice)
    if method == config.ABILITY_CALCULATION_PURCHASE:
        GenerateRandomBasePurchase(baseDict, points)


def GenerateRandomBaseStandard(baseDict):
    dice = roll.Dice(6)
    results = [sum(sorted([dice.Roll() for i in range(4)])[1:]) for i in range(6)]
    for i in range(len(baseDict.keys())):
        baseDict[baseDict.keys()[i]] = results[i]


def GenerateRandomBaseClassic(baseDict):
    dice = roll.Dice(6, 3)
    results = [dice.Roll() for i in range(6)]
    for i in range(len(baseDict.keys())):
        baseDict[baseDict.keys()[i]] = results[i]


def GenerateRandomBaseHerioic(baseDict):
    dice = roll.Dice(6, 2, 1, 6)
    results = [dice.Roll() for i in range(6)]
    for i in range(len(baseDict.keys())):
        baseDict[baseDict.keys()[i]] = results[i]


def GenerateRandomBaseDicePool(baseDict, numDice=24, minDice=3):
    dice = roll.Dice(6)
    abilities = GetAbilityNames()
    scores = {}
    for key in abilities:
        scores[key] = sum([dice.Roll() for i in range(minDice)])
        numDice -= minDice
    while numDice > 0:
        scores[scores.keys()[random.randint(0, len(abilities)-1)]] += dice.Roll()
        numDice -= 1


def GenerateRandomBasePurchase(baseDict, points):
    abilities = GetAbilityNames()
    for key in abilities:
        baseDict[key] = 10
    while points > 0:
        s = baseDict.keys()[random.randint(0, len(abilities)-1)]
        old = baseDict[s]
        new = baseDict[s] + random.randint(-2, 2)
        if new in config.AbilityScoreCosts and config.AbilityScoreCosts[new] - config.AbilityScoreCosts[old] <= points:
            baseDict[s] = new
            points -= config.AbilityScoreCosts[new] - config.AbilityScoreCosts[old]


def RandomMethod():
    return random.choice([config.ABILITY_CALCULATION_STANDARD,
                          config.ABILITY_CALCULATION_CLASSIC,
                          config.ABILITY_CALCULATION_HEROIC,
                          config.ABILITY_CALCULATION_DICEPOOL,
                          config.ABILITY_CALCULATION_PURCHASE])
