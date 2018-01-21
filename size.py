
import config


class Size:
    ID = config.NONE
    Name = ""
    ArmorClass = 0
    CMB = 0
    FlySkill = 0
    StealthSkill = 0
    CarryingCapacity = 0.0


class Fine(Size):
    ID = config.SIZE_FINE
    Name = "Fine"
    ArmorClass = 8
    CMB = -8
    FlySkill = 8
    StealthSkill = 16
    CarryingCapacity = 0.125


class Diminutive(Size):
    ID = config.SIZE_DIMINUTIVE
    Name = "Diminutive"
    ArmorClass = 4
    CMB = -4
    FlySkill = 6
    StealthSkill = 12
    CarryingCapacity = 0.25


class Tiny(Size):
    ID = config.SIZE_TINY
    Name = "Tiny"
    ArmorClass = 2
    CMB = -2
    FlySkill = 4
    StealthSkill = 8
    CarryingCapacity = 0.5


class Small(Size):
    ID = config.SIZE_SMALL
    Name = "Small"
    ArmorClass = 1
    CMB = -1
    FlySkill = 2
    StealthSkill = 4
    CarryingCapacity = 0.75


class Medium(Size):
    ID = config.SIZE_MEDIUM
    Name = "Medium"
    ArmorClass = 0
    CMB = 0
    FlySkill = 0
    StealthSkill = 0
    CarryingCapacity = 1.0


class Large(Size):
    ID = config.SIZE_LARGE
    Name = "Large"
    ArmorClass = -1
    CMB = 1
    FlySkill = -2
    StealthSkill = -4
    CarryingCapacity = 2.0


class Huge(Size):
    ID = config.SIZE_HUGE
    Name = "Huge"
    ArmorClass = -2
    CMB = 2
    FlySkill = -4
    StealthSkill = -8
    CarryingCapacity = 4.0


class Gargantuan(Size):
    ID = config.SIZE_GARGANTUAN
    Name = "Gargantuan"
    ArmorClass = -4
    CMB = 4
    FlySkill = -6
    StealthSkill = -12
    CarryingCapacity = 8.0


class Colossal(Size):
    ID = config.SIZE_COLOSSAL
    Name = "Colossal"
    ArmorClass = -8
    CMB = 8
    FlySkill = -8
    StealthSkill = -16
    CarryingCapacity = 16.0

sizeDict = {
    config.SIZE_FINE: Fine,
    config.SIZE_DIMINUTIVE: Diminutive,
    config.SIZE_TINY: Tiny,
    config.SIZE_SMALL: Small,
    config.SIZE_MEDIUM: Medium,
    config.SIZE_LARGE: Large,
    config.SIZE_HUGE: Huge,
    config.SIZE_GARGANTUAN: Gargantuan,
    config.SIZE_COLOSSAL: Colossal
}
