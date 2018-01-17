
import config

import random


class Color:

    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def ToJson(self):
        j = {}
        j['Name'] = self.name
        j['r'] = self.r
        j['g'] = self.g
        j['b'] = self.b
        return j


def GetColorNames():
    return [
        "Red",
        "Green",
        "Yellow",
        "Blue",
        "Orange",
        "Purple",
        "Cyan",
        "Magenta",
        "Lime",
        "Pink",
        "Teal",
        "Lavender",
        "Brown",
        "Beige",
        "Maroon",
        "Mint",
        "Olive",
        "Coral",
        "Navy",
        "Grey",
        "White",
        "Black"
    ]


def Random():
    return random.choice([
                            config.COLOR_RED,
                            config.COLOR_GREEN,
                            config.COLOR_YELLOW,
                            config.COLOR_BLUE,
                            config.COLOR_ORANGE,
                            config.COLOR_PURPLE,
                            config.COLOR_CYAN,
                            config.COLOR_MAGENTA,
                            config.COLOR_LIME,
                            config.COLOR_PINK,
                            config.COLOR_TEAL,
                            config.COLOR_LAVENDER,
                            config.COLOR_BROWN,
                            config.COLOR_BEIGE,
                            config.COLOR_MAROON,
                            config.COLOR_MINT,
                            config.COLOR_OLIVE,
                            config.COLOR_CORAL,
                            config.COLOR_NAVY,
                            config.COLOR_GREY,
                            config.COLOR_WHITE,
                            config.COLOR_BLACK
                        ])
