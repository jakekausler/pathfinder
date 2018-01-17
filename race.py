
import config
import size
import skill
import ability
import roll

import random


def RandomAgeMethod():
    return random.choice([
                            config.AGE_INTUITIVE,
                            config.AGE_SELF_TAUGHT,
                            config.AGE_TRAINED
                         ])


class Race:

    def __init__(self):
        self.Name = ""
        self.AbilityScoreModifiers = {}
        for abil in ability.GetAbilityNames():
            self.AbilityScoreModifiers[abil] = 0
        self.Size = size.Size()
        self.Type = Type()
        self.SubTypes = []
        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0
        self.Speed = 0  # In feet
        self.StartingLanguages = ['Common']  # List of language names
        self.PossibleLanguages = []  # Other possible languages
        self.DefensiveTraits = []  # List of traits
        self.OffensiveTraits = []  # List of traits
        self.Feats = []  # List of feats
        self.SpecialAbilities = []  # List of spell.SpAbility and spell.SuAbility
        self.RacePoints = 0
        self.AgeProperties = []  # List of Starting Age indexed by age type
        self.AgeModifer = []  # List of roll type, indexed by age method
        self.BaseHeight = []  # List of Height (in inches), indexed by gender
        self.HeightModifier = []  # List of roll type, indexed by gender
        self.BaseWeight = []  # List of Weight (in pounds), indexed by gender
        self.WeightModifier = []  # List of roll type, indexed by gender
        self.WeaponProficiencies = []  # TODO
        self.WeaponProficienciesNamed = []  # TODO

    def SetEffects(self, character):
        return

    def Senses(self):
        s = list(set(self.Type.Senses))
        for i in self.SubTypes:
            s.Add(i.Senses)
        return s

    def BaseAttackBonus(self):
        return self.Type.BaseAttackBonus

    def HitDie(self):
        return self.Type.HitDie

    def AgeType(self, age):
        j = len(self.AgeProperties)-1
        for i in reversed(self.AgeProperties):
            if age > i:
                return j
            j -= 1
        return config.AGE_CHILD

    def RandomAge(self, method, baseAge=-1):
        if baseAge == -1:
            if config.AGE_ADULT < len(self.AgeProperties):
                baseAge = self.AgeProperties[config.AGE_ADULT]
            else:
                baseAge = 0
        if method < len(self.AgeModifer):
            return baseAge + self.AgeModifer[method].Roll()
        return baseAge

    def RandomHeight(self, gender):
        base = 0
        if gender < len(self.BaseHeight):
            base = self.BaseHeight[gender]
        if gender < len(self.HeightModifier):
            return base + self.HeightModifier[gender].Roll()
        return base

    def RandomWeight(self, gender):
        base = 0
        if gender < len(self.BaseWeight):
            base = self.BaseWeight[gender]
        if gender < len(self.WeightModifier):
            return base + self.WeightModifier[gender].Roll()
        return base

    def GetAgeAbilityModifiers(self, age):
        abilities = {}
        for abil in ability.GetAbilityNames():
            abilities[abil] = 0
        at = self.AgeType(age)
        if at == config.AGE_MIDDLE_AGE:
            abilities[config.ABILITY_STRENGTH] = -1
            abilities[config.ABILITY_DEXTERITY] = -1
            abilities[config.ABILITY_CONSTITUTION] = -1
            abilities[config.ABILITY_INTELLIGENCE] = 1
            abilities[config.ABILITY_WISDOM] = 1
            abilities[config.ABILITY_CHARISMA] = 1
        elif at == config.AGE_OLD:
            abilities[config.ABILITY_STRENGTH] = -2
            abilities[config.ABILITY_DEXTERITY] = -2
            abilities[config.ABILITY_CONSTITUTION] = -2
            abilities[config.ABILITY_INTELLIGENCE] = 1
            abilities[config.ABILITY_WISDOM] = 1
            abilities[config.ABILITY_CHARISMA] = 1
        elif at == config.AGE_VENERABLE:
            abilities[config.ABILITY_STRENGTH] = -3
            abilities[config.ABILITY_DEXTERITY] = -3
            abilities[config.ABILITY_CONSTITUTION] = -3
            abilities[config.ABILITY_INTELLIGENCE] = 1
            abilities[config.ABILITY_WISDOM] = 1
            abilities[config.ABILITY_CHARISMA] = 1
        return abilities


class Dwarf(Race):

    def __init__(self):
        self.Name = "Dwarf"
        self.AbilityScoreModifiers = {}
        for abil in ability.GetAbilityNames():
            self.AbilityScoreModifiers[abil] = 0
        self.AbilityScoreModifiers[config.ABILITY_CONSTITUTION] = 2
        self.AbilityScoreModifiers[config.ABILITY_WISDOM] = 2
        self.AbilityScoreModifiers[config.ABILITY_CHARISMA] = -2
        self.Size = size.Medium()
        self.Type = Type()  # TODO
        self.SubTypes = []  # TODO
        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0
        self.Speed = 20
        self.StartingLanguages = ['Common', 'Dwarven']  # List of language names
        self.PossibleLanguages = ['Giant', 'Gnome', 'Goblin', 'Orc', 'Terran', 'Undercommon']  # Other possible languages
        self.DefensiveTraits = []  # List of traits
        self.OffensiveTraits = []  # List of traits
        self.Feats = []  # List of feats
        self.SpecialAbilities = []  # List of spell.SpAbility and spell.SuAbility
        self.RacePoints = 0
        self.AgeProperties = [0, 40, 125, 188, 250]  # List of Starting Age indexed by age type
        self.AgeModifer = [roll.Dice(6, 3), roll.Dice(6, 5), roll.Dice(6, 7)]  # List of roll type, indexed by age method
        self.BaseHeight = [45, 43]  # List of Height (in inches), indexed by gender
        self.HeightModifier = [roll.Dice(4, 2), roll.Dice(4, 2)]  # List of roll type, indexed by gender
        self.BaseWeight = [150, 120]  # List of Weight (in pounds), indexed by gender
        self.WeightModifier = [roll.Dice(4, 2, 7), roll.Dice(4, 2, 7)]  # List of roll type, indexed by gender

    def SetEffects(self, character):
        return


class Elf(Race):

    def __init__(self):
        self.Name = "Elf"
        self.AbilityScoreModifiers = {}
        for abil in ability.GetAbilityNames():
            self.AbilityScoreModifiers[abil] = 0
        self.Size = size.Size()
        self.Type = Type()
        self.SubTypes = []
        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0
        self.Speed = 0  # In feet
        self.StartingLanguages = ['Common']  # List of language names
        self.PossibleLanguages = []  # Other possible languages
        self.DefensiveTraits = []  # List of traits
        self.OffensiveTraits = []  # List of traits
        self.Feats = []  # List of feats
        self.SpecialAbilities = []  # List of spell.SpAbility and spell.SuAbility
        self.RacePoints = 0
        self.AgeProperties = []  # List of Starting Age indexed by age type
        self.AgeModifer = []  # List of roll type, indexed by age method
        self.BaseHeight = []  # List of Height (in inches), indexed by gender
        self.HeightModifier = []  # List of roll type, indexed by gender
        self.BaseWeight = []  # List of Weight (in pounds), indexed by gender
        self.WeightModifier = []  # List of roll type, indexed by gender


class Gnome(Race):

    def __init__(self, UseSkillPointOnCraft1=True, UseSkillPointOnCraft2=False, UseSkillPointOnPerform1=True, UseSkillPointOnPerform2=False):
        self.Name = "Gnome"
        self.AbilityScoreModifiers = {}
        for abil in ability.GetAbilityNames():
            self.AbilityScoreModifiers[abil] = 0
        self.AbilityScoreModifiers[config.ABILITY_STRENGTH] = -2
        self.AbilityScoreModifiers[config.ABILITY_CONSTITUTION] = 2
        self.AbilityScoreModifiers[config.ABILITY_CHARISMA] = 2
        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0
        self.RacialSkills[config.SKILL_PERCEPTION] = 2
        if UseSkillPointOnCraft1:
            self.RacialSkills[config.SKILL_CRAFT1] = 2
        elif UseSkillPointOnCraft1:
            self.RacialSkills[config.SKILL_CRAFT2] = 2
        elif UseSkillPointOnCraft1:
            self.RacialSkills[config.SKILL_PERFORM1] = 2
        elif UseSkillPointOnCraft1:
            self.RacialSkills[config.SKILL_PERFORM2] = 2
        else:
            self.RacialSkills[config.SKILL_CRAFT1] = 2
        self.Size = size.Small()
        self.Type = Type()
        self.SubTypes = []
        self.Speed = 20  # In feet
        self.StartingLanguages = ['Common', 'Gnome', 'Sylvan']  # List of language names
        self.PossibleLanguages = []  # Other possible languages
        self.DefensiveTraits = []  # List of traits
        self.OffensiveTraits = []  # List of traits
        self.Feats = []  # List of feats
        self.SpecialAbilities = []  # List of spell.SpAbility and spell.SuAbility
        self.RacePoints = 0
        self.AgeProperties = []  # List of Starting Age indexed by age type
        self.AgeModifer = []  # List of roll type, indexed by age method
        self.BaseHeight = []  # List of Height (in inches), indexed by gender
        self.HeightModifier = []  # List of roll type, indexed by gender
        self.BaseWeight = []  # List of Weight (in pounds), indexed by gender
        self.WeightModifier = []  # List of roll type, indexed by gender


class HalfElf(Race):

    def __init__(self):
        self.Name = "HalfElf"
        self.AbilityScoreModifiers = {}
        for abil in ability.GetAbilityNames():
            self.AbilityScoreModifiers[abil] = 0
        self.Size = size.Size()
        self.Type = Type()
        self.SubTypes = []
        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0
        self.Speed = 0  # In feet
        self.StartingLanguages = ['Common']  # List of language names
        self.PossibleLanguages = []  # Other possible languages
        self.DefensiveTraits = []  # List of traits
        self.OffensiveTraits = []  # List of traits
        self.Feats = []  # List of feats
        self.SpecialAbilities = []  # List of spell.SpAbility and spell.SuAbility
        self.RacePoints = 0
        self.AgeProperties = []  # List of Starting Age indexed by age type
        self.AgeModifer = []  # List of roll type, indexed by age method
        self.BaseHeight = []  # List of Height (in inches), indexed by gender
        self.HeightModifier = []  # List of roll type, indexed by gender
        self.BaseWeight = []  # List of Weight (in pounds), indexed by gender
        self.WeightModifier = []  # List of roll type, indexed by gender


class HalfOrc(Race):

    def __init__(self):
        self.Name = "HalfOrc"
        self.AbilityScoreModifiers = {}
        for abil in ability.GetAbilityNames():
            self.AbilityScoreModifiers[abil] = 0
        self.Size = size.Size()
        self.Type = Type()
        self.SubTypes = []
        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0
        self.Speed = 0  # In feet
        self.StartingLanguages = ['Common']  # List of language names
        self.PossibleLanguages = []  # Other possible languages
        self.DefensiveTraits = []  # List of traits
        self.OffensiveTraits = []  # List of traits
        self.Feats = []  # List of feats
        self.SpecialAbilities = []  # List of spell.SpAbility and spell.SuAbility
        self.RacePoints = 0
        self.AgeProperties = []  # List of Starting Age indexed by age type
        self.AgeModifer = []  # List of roll type, indexed by age method
        self.BaseHeight = []  # List of Height (in inches), indexed by gender
        self.HeightModifier = []  # List of roll type, indexed by gender
        self.BaseWeight = []  # List of Weight (in pounds), indexed by gender
        self.WeightModifier = []  # List of roll type, indexed by gender


class Halfling(Race):

    def __init__(self):
        self.Name = "Halfling"
        self.AbilityScoreModifiers = {}
        for abil in ability.GetAbilityNames():
            self.AbilityScoreModifiers[abil] = 0
        self.Size = size.Size()
        self.Type = Type()
        self.SubTypes = []
        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0
        self.Speed = 0  # In feet
        self.StartingLanguages = ['Common']  # List of language names
        self.PossibleLanguages = []  # Other possible languages
        self.DefensiveTraits = []  # List of traits
        self.OffensiveTraits = []  # List of traits
        self.Feats = []  # List of feats
        self.SpecialAbilities = []  # List of spell.SpAbility and spell.SuAbility
        self.RacePoints = 0
        self.AgeProperties = []  # List of Starting Age indexed by age type
        self.AgeModifer = []  # List of roll type, indexed by age method
        self.BaseHeight = []  # List of Height (in inches), indexed by gender
        self.HeightModifier = []  # List of roll type, indexed by gender
        self.BaseWeight = []  # List of Weight (in pounds), indexed by gender
        self.WeightModifier = []  # List of roll type, indexed by gender


class Human(Race):

    def __init__(self):
        self.Name = "Human"
        self.AbilityScoreModifiers = {}
        for abil in ability.GetAbilityNames():
            self.AbilityScoreModifiers[abil] = 0
        self.Size = size.Size()
        self.Type = Type()
        self.SubTypes = []
        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0
        self.Speed = 0  # In feet
        self.StartingLanguages = ['Common']  # List of language names
        self.PossibleLanguages = []  # Other possible languages
        self.DefensiveTraits = []  # List of traits
        self.OffensiveTraits = []  # List of traits
        self.Feats = []  # List of feats
        self.SpecialAbilities = []  # List of spell.SpAbility and spell.SuAbility
        self.RacePoints = 0
        self.AgeProperties = []  # List of Starting Age indexed by age type
        self.AgeModifer = []  # List of roll type, indexed by age method
        self.BaseHeight = []  # List of Height (in inches), indexed by gender
        self.HeightModifier = []  # List of roll type, indexed by gender
        self.BaseWeight = []  # List of Weight (in pounds), indexed by gender
        self.WeightModifier = []  # List of roll type, indexed by gender

RaceDict = {
    config.RACE_DWARF: Dwarf,
    config.RACE_ELF: Elf,
    config.RACE_GNOME: Gnome,
    config.RACE_HALF_ELF: HalfElf,
    config.RACE_HALF_ORC: HalfOrc,
    config.RACE_HALFLING: Halfling,
    config.RACE_HUMAN: Human
}


def GetRaceNames():
    return [
        'Dwarf',
        'Elf',
        'Gnome',
        'Half Elf',
        'Half Orc',
        'Halfling',
        'Human'
    ]


def RandomRace():
    return RaceDict[random.randint(1, 7)]


# Race type (humanoid, etc)
class Type:
    def __init__(self):
        # TODO
        return


# TODO: Add other race types


class SubType:
    def __init__(self):
        # TODO
        return


# TODO: Add other race subtypes


class Trait:
    def __init__(self):
        self.Bonuses = {}  # Dict of bonus.Type: value
