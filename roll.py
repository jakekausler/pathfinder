
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

    def Copy(self):
        return Dice(self.sides, self.numRolls, self.multiplier, self.addition)

    def __eq__(self, other):
        return (
            self.sides == other.sides and
            self.numRolls == other.numRolls and
            self.multiplier == other.multiplier and
            self.addition == other.addition
            )

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.ToJson())

    def ToJson(self):
        base = str(self.numRolls) + "d" + str(self.sides)
        if base.startswith("0d"):
            base = ""
        extra = str(self.addition)
        if extra == "0":
            extra = ""
        if extra == "":
            return base
        if base == "":
            return extra
        return base + "+" + extra
