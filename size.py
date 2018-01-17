
import config


class Size:
    Name = ""
    ArmorClass = 0
    CMB = 0
    FlySkill = 0
    StealthSkill = 0
    CarryingCapacity = 0.0


class Fine(Size):
    Name = "Fine"
    ArmorClass = 8
    CMB = -8
    FlySkill = 8
    StealthSkill = 16
    CarryingCapacity = 0.125


class Diminutive(Size):
    Name = "Diminutive"
    ArmorClass = 4
    CMB = -4
    FlySkill = 6
    StealthSkill = 12
    CarryingCapacity = 0.25


class Tiny(Size):
    Name = "Tiny"
    ArmorClass = 2
    CMB = -2
    FlySkill = 4
    StealthSkill = 8
    CarryingCapacity = 0.5


class Small(Size):
    Name = "Small"
    ArmorClass = 1
    CMB = -1
    FlySkill = 2
    StealthSkill = 4
    CarryingCapacity = 0.75


class Medium(Size):
    Name = "Medium"
    ArmorClass = 0
    CMB = 0
    FlySkill = 0
    StealthSkill = 0
    CarryingCapacity = 1.0


class Large(Size):
    Name = "Large"
    ArmorClass = -1
    CMB = 1
    FlySkill = -2
    StealthSkill = -4
    CarryingCapacity = 2.0


class Huge(Size):
    Name = "Huge"
    ArmorClass = -2
    CMB = 2
    FlySkill = -4
    StealthSkill = -8
    CarryingCapacity = 4.0


class Gargantuan(Size):
    Name = "Gargantuan"
    ArmorClass = -4
    CMB = 4
    FlySkill = -6
    StealthSkill = -12
    CarryingCapacity = 8.0


class Colossal(Size):
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
