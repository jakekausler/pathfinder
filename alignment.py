
import config

import random


def GetAlignmentName(lc, ge):
    if lc == config.ALIGNMENT_LAWFUL:
        lc = 'Lawful'
    elif lc == config.ALIGNMENT_CHAOTIC:
        lc = 'Chaotic'
    else:
        lc = 'Neutral'
    if ge == config.ALIGNMENT_GOOD:
        ge = 'Good'
    elif ge == config.ALIGNMENT_EVIL:
        ge = 'Evil'
    else:
        ge = 'Neutral'
    return lc + ' ' + ge


class Alignment:

    def __init__(self, lc=config.ALIGNMENT_NEUTRAL, ge=config.ALIGNMENT_NEUTRAL):
        self.GoodEvil = ge
        self.LawfulChaotic = lc

    def ToJson(self):
        return GetAlignmentName(self.LawfulChaotic, self.GoodEvil)

    def __str__(self):
        s = ""
        if self.LawfulChaotic == config.ALIGNMENT_LAWFUL:
            s += "L"
        elif self.LawfulChaotic == config.ALIGNMENT_NEUTRAL:
            s += "N"
        else:
            s += "C"
        if self.GoodEvil == config.ALIGNMENT_GOOD:
            s += "G"
        elif self.GoodEvil == config.ALIGNMENT_NEUTRAL:
            s += "N"
        else:
            s += "E"
        return s


def Random():
    a = Alignment()
    a.GoodEvil = random.choice([config.ALIGNMENT_GOOD, config.ALIGNMENT_NEUTRAL, config.ALIGNMENT_EVIL])
    a.LawfulChaotic = random.choice([config.ALIGNMENT_LAWFUL, config.ALIGNMENT_NEUTRAL, config.ALIGNMENT_CHAOTIC])
    return a
