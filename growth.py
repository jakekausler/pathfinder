
import config

import random


def GetGrowthString(n):
    if n == config.GROWTH_SLOW:
        return 'Slow'
    if n == config.GROWTH_MEDIUM:
        return 'Medium'
    if n == config.GROWTH_FAST:
        return 'Fast'
    return ''


def GetLevel(rate, experience):
    for i in range(len(config.Experience[rate])):
        if i < len(config.Experience[rate]) - 1 and experience >= config.Experience[rate-1][i] and experience < config.Experience[rate-1][i+1]:
            return i + 1
    return len(config.Experience[rate-1])


def GetStartingExperienceForLevel(rate, level):
    return config.Experience[rate-1][level-1]


def RandomRate():
    return random.choice([config.GROWTH_SLOW, config.GROWTH_MEDIUM, config.GROWTH_FAST])
