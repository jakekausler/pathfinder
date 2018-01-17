
import config

import random


def String(g):
    if g == config.GENDER_MALE:
        return "Male"
    elif g == config.GENDER_FEMALE:
        return "Female"
    elif g == config.GENDER_GENDERLESS:
        return "Genderless"
    elif g == config.GENDER_BOTH:
        return "Both"


def Random(use_genderless=False, use_both=False):
    choices = [config.GENDER_MALE, config.GENDER_FEMALE]
    if use_genderless:
        choices.append(config.GENDER_GENDERLESS)
    if use_both:
        choices.append(config.GENDER_BOTH)
    return random.choice(choices)
