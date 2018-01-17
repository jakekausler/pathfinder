
import config

# TODO: Add effect classes, effect names, effect types (for stacking),
# and a dict of effect name to effect class
# Effect classes will have the type and a function for turning on/off the
# effect, which raises/lowers the appropriate stats of a given player


class Effect(object):

    def __init__(self):
        self.Type = config.EFFECT_UNTYPED
        self.Active = False
        return

    def ShouldBeActive(self, character):
        return False

    def GetEffectValue(self):
        return 0

    def Stackable(self):
        return self.Type in config.StackableTypes


class nonlethal_staggered(Effect):

    def __init__(self):
        super(nonlethal_staggered, self).__init__()


class nonlethal_unconsious(Effect):

    def __init__(self):
        super(nonlethal_unconsious, self).__init__()


class damage_disabled(Effect):

    def __init__(self):
        super(damage_disabled, self).__init__()


class damage_unconsious(Effect):

    def __init__(self):
        super(damage_unconsious, self).__init__()


class damage_dying(Effect):

    def __init__(self):
        super(damage_dying, self).__init__()


class no_speed_penalty_from_armor_or_encumbrance(Effect):

    def __init__(self):
        super(no_speed_penalty_from_armor_or_encumbrance, self).__init__()


EffectClasses = {
    config.EFFECT_NONLETHAL_STAGGERED: nonlethal_staggered,
    config.EFFECT_NONLETHAL_UNCONSIOUS: nonlethal_unconsious,
    config.EFFECT_DAMAGE_DISABLED: damage_disabled,
    config.EFFECT_DAMAGE_UNCONSIOUS: damage_unconsious,
    config.EFFECT_DAMAGE_DYING: damage_dying
}
