
import random
from collections import Sequence
from numbers import Number
import math


class Dice:

    def __init__(self, sides, numRolls=1, multiplier=1, addition=0):
        self.sides = sides
        self.numRolls = numRolls
        self.multiplier = multiplier
        self.addition = addition

    def Roll(self):
        res = []
        for i in range(0, self.numRolls):
            if isinstance(self.sides, Sequence):
                r = random.choice(self.sides)
                res.append(r)
            else:
                r = random.randint(1, self.sides)
                res.append(r)
        if all(isinstance(r, Number) for r in res):
            return (sum(res) + self.addition) * self.multiplier
        else:
            return res, self.multiplier, self.addition

    def RollMinimum(self):
        return 1 * self.numRolls * self.multiplier + self.addition

    def RollMaximum(self):
        return self.sides * self.numRolls * self.multiplier + self.addition

    def RollAverage(self):
        return math.ceil((self.sides+1)/2.0) * self.numRolls * self.multiplier + self.addition
