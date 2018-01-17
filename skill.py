
import config

# TODO: Add ability to see what actions can be done with a skill, and the chance that the action will succeed

config.SKILL_ACROBATICS = 1
config.SKILL_APPRAISE = 2
config.SKILL_BLUFF = 3
config.SKILL_CLIMB = 4
config.SKILL_CRAFT1 = 5
config.SKILL_CRAFT2 = 6
config.SKILL_DIPLOMACY = 7
config.SKILL_DISABLE_DEVICE = 8
config.SKILL_DISGUISE = 9
config.SKILL_ESCAPE_ARTIST = 10
config.SKILL_FLY = 11
config.SKILL_HANDLE_ANIMAL = 12
config.SKILL_HEAL = 13
config.SKILL_INTIMIDATE = 14
config.SKILL_KNOWLEDGE_ARCANA = 15
config.SKILL_KNOWLEDGE_DUNGEONEERING = 16
config.SKILL_KNOWLEDGE_ENGINEERING = 17
config.SKILL_KNOWLEDGE_GEOGRAPHY = 18
config.SKILL_KNOWLEDGE_HISTORY = 19
config.SKILL_KNOWLEDGE_LOCAL = 20
config.SKILL_KNOWLEDGE_NATURE = 21
config.SKILL_KNOWLEDGE_NOBILITY = 22
config.SKILL_KNOWLEDGE_PLANES = 23
config.SKILL_KNOWLEDGE_RELIGION = 24
config.SKILL_LINGUISTICS = 25
config.SKILL_PERCEPTION = 26
config.SKILL_PERFORM1 = 27
config.SKILL_PERFORM2 = 28
config.SKILL_PROF1 = 29
config.SKILL_PROF2 = 30
config.SKILL_RIDE = 31
config.SKILL_SENSE_MOTIVE = 32
config.SKILL_SLEIGHT_OF_HAND = 33
config.SKILL_SPELLCRAFT = 34
config.SKILL_STEALTH = 35
config.SKILL_SURVIVAL = 36
config.SKILL_SWIM = 37
config.SKILL_USE_MAGIC_DEVICE = 38


def GetSkillName(n):
    if n == config.SKILL_ACROBATICS:
        return 'Acrobatics'
    if n == config.SKILL_APPRAISE:
        return 'Appraise'
    if n == config.SKILL_BLUFF:
        return 'Bluff'
    if n == config.SKILL_CLIMB:
        return 'Climb'
    if n == config.SKILL_CRAFT1:
        return 'Craft1'
    if n == config.SKILL_CRAFT2:
        return 'Craft2'
    if n == config.SKILL_DIPLOMACY:
        return 'Diplomacy'
    if n == config.SKILL_DISABLE_DEVICE:
        return 'Disable Device'
    if n == config.SKILL_DISGUISE:
        return 'Disguise'
    if n == config.SKILL_ESCAPE_ARTIST:
        return 'Escape Artist'
    if n == config.SKILL_FLY:
        return 'Fly'
    if n == config.SKILL_HANDLE_ANIMAL:
        return 'Handle Animal'
    if n == config.SKILL_HEAL:
        return 'Heal'
    if n == config.SKILL_INTIMIDATE:
        return 'Intimidate'
    if n == config.SKILL_KNOWLEDGE_ARCANA:
        return 'Kn. Arcana'
    if n == config.SKILL_KNOWLEDGE_DUNGEONEERING:
        return 'Kn. Dungeoneering'
    if n == config.SKILL_KNOWLEDGE_ENGINEERING:
        return 'Kn. Engineering'
    if n == config.SKILL_KNOWLEDGE_GEOGRAPHY:
        return 'Kn. Geography'
    if n == config.SKILL_KNOWLEDGE_HISTORY:
        return 'Kn. History'
    if n == config.SKILL_KNOWLEDGE_LOCAL:
        return 'Kn. Local'
    if n == config.SKILL_KNOWLEDGE_NATURE:
        return 'Kn. Nature'
    if n == config.SKILL_KNOWLEDGE_NOBILITY:
        return 'Kn. Nobility'
    if n == config.SKILL_KNOWLEDGE_PLANES:
        return 'Kn. Planes'
    if n == config.SKILL_KNOWLEDGE_RELIGION:
        return 'Kn. Religion'
    if n == config.SKILL_LINGUISTICS:
        return 'Linguistics'
    if n == config.SKILL_PERCEPTION:
        return 'Perception'
    if n == config.SKILL_PERFORM1:
        return 'Perform1'
    if n == config.SKILL_PERFORM2:
        return 'Perform2'
    if n == config.SKILL_PROF1:
        return 'Prof1'
    if n == config.SKILL_PROF2:
        return 'Prof2'
    if n == config.SKILL_RIDE:
        return 'Ride'
    if n == config.SKILL_SENSE_MOTIVE:
        return 'Sense Motive'
    if n == config.SKILL_SLEIGHT_OF_HAND:
        return 'Sleight of Hand'
    if n == config.SKILL_SPELLCRAFT:
        return 'Spellcraft'
    if n == config.SKILL_STEALTH:
        return 'Stealth'
    if n == config.SKILL_SURVIVAL:
        return 'Survival'
    if n == config.SKILL_SWIM:
        return 'Swim'
    if n == config.SKILL_USE_MAGIC_DEVICE:
        return 'Use Magic Device'
    return ''


def GetSkillNames():
    return [
        config.SKILL_ACROBATICS,
        config.SKILL_APPRAISE,
        config.SKILL_BLUFF,
        config.SKILL_CLIMB,
        config.SKILL_CRAFT1,
        config.SKILL_CRAFT2,
        config.SKILL_DIPLOMACY,
        config.SKILL_DISABLE_DEVICE,
        config.SKILL_DISGUISE,
        config.SKILL_ESCAPE_ARTIST,
        config.SKILL_FLY,
        config.SKILL_HANDLE_ANIMAL,
        config.SKILL_HEAL,
        config.SKILL_INTIMIDATE,
        config.SKILL_KNOWLEDGE_ARCANA,
        config.SKILL_KNOWLEDGE_DUNGEONEERING,
        config.SKILL_KNOWLEDGE_ENGINEERING,
        config.SKILL_KNOWLEDGE_GEOGRAPHY,
        config.SKILL_KNOWLEDGE_HISTORY,
        config.SKILL_KNOWLEDGE_LOCAL,
        config.SKILL_KNOWLEDGE_NATURE,
        config.SKILL_KNOWLEDGE_NOBILITY,
        config.SKILL_KNOWLEDGE_PLANES,
        config.SKILL_KNOWLEDGE_RELIGION,
        config.SKILL_LINGUISTICS,
        config.SKILL_PERCEPTION,
        config.SKILL_PERFORM1,
        config.SKILL_PERFORM2,
        config.SKILL_PROF1,
        config.SKILL_PROF2,
        config.SKILL_RIDE,
        config.SKILL_SENSE_MOTIVE,
        config.SKILL_SLEIGHT_OF_HAND,
        config.SKILL_SPELLCRAFT,
        config.SKILL_STEALTH,
        config.SKILL_SURVIVAL,
        config.SKILL_SWIM,
        config.SKILL_USE_MAGIC_DEVICE
    ]


class Skill(object):
    Name = "Skill"
    Ability = config.ABILITY_STRENGTH
    IsTrained = False
    UseACP = False

    def __init__(self, key):
        self.Key = key
        self.Actions = {}  # Dictionary of action name to check amount
        self.ActiveModifiers = {}  # Dictionary of Modifier name to bool
        self.ModifierAmounts = {}  # Dictionary of Modifier name to amount

    def GetTotal(self, character):
        ret = 0
        if not self.IsTrained or character.Skills[self.Key][0] > 0:
            ret += character.Skills[self.Key][0]
            if character.IsClassSkill(self.Key) and character.Skills[self.Key][0] > 0:
                ret += 3
            if self.Key == config.SKILL_FLY:
                ret += character.Size().FlySkill
            elif self.Key == config.SKILL_STEALTH:
                ret += character.Size().StealthSkill
            if self.UseACP:
                ret += character.ArmorCheckPenalty()
            ret += character.AbilityModifiers()[self.Ability]
            ret += (character.CalculateEffects(character.EffectSkillCheckAll) +
                            character.CalculateEffects(character.EffectSkillCheck[self.Key]) +
                            character.FeatSkills[self.Key] +
                            character.MiscSkills[self.Key] +
                            character.FCSkills[self.Key] +
                            character.Race.RacialSkills[self.Key])
        return ret

    def IsAvailable(self, character):
        return not self.IsTrained or character.Skills[self.Key][0] > 0

    def GetChanceOfSuccess(self, character, action):
        if self.GetSkillCheck(character, action) == config.INFINITY:
            return 1
        return 1 - (self.GetSkillCheck(action) - self.GetTotal(character)) / 20.0

    # Return INFINITY if no check is needed
    def GetSkillCheck(self, character, action):
        check = self.Actions[action]
        for key in self.ActiveModifiers:
            if self.ActiveModifiers[key]:
                check += self.ModifierAmounts[key]
        return check

    def ActivateModifer(self, modifer):
        self.ActiveModifiers[modifer] = True

    def DeactivateModifer(self, modifer):
        self.ActiveModifiers[modifer] = False


class acrobatics(Skill):
    Name = "Acrobatics"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(acrobatics, self).__init__(key)
        self.ModifierAmounts['Lightly Obstructed'] = 2
        self.ActiveModifiers['Lightly Obstructed'] = False
        self.ModifierAmounts['Severely Obstructed'] = 5
        self.ActiveModifiers['Severely Obstructed'] = False
        self.ModifierAmounts['Slightly Slippery'] = 2
        self.ActiveModifiers['Slightly Slippery'] = False
        self.ModifierAmounts['Severely Slippery'] = 5
        self.ActiveModifiers['Severely Slippery'] = False
        self.ModifierAmounts['Slightly Sloped'] = 2
        self.ActiveModifiers['Slightly Sloped'] = False
        self.ModifierAmounts['Severely Sloped'] = 5
        self.ActiveModifiers['Severely Sloped'] = False
        self.ModifierAmounts['Slightly Unsteady'] = 2
        self.ActiveModifiers['Slightly Unsteady'] = False
        self.ModifierAmounts['Mildly Unsteady'] = 5
        self.ActiveModifiers['Mildly Unsteady'] = False
        self.ModifierAmounts['Severely Unsteady'] = 10
        self.ActiveModifiers['Severely Unsteady'] = False
        self.ModifierAmounts['Balancing Pole'] = 1
        self.ActiveModifiers['Balancing Pole'] = False
        self.ModifierAmounts['Move at full speed on narrow or uneven surfaces'] = 5
        self.ActiveModifiers['Move at full speed on narrow or uneven surfaces'] = False
        self.Actions['Cross Narrow Surface/Uneven Ground (> 3 ft wide)'] = 0
        self.Actions['Cross Narrow Surface/Uneven Ground (1-3 ft wide)'] = 5
        self.Actions['Cross Narrow Surface/Uneven Ground (7-11 in wide)'] = 10
        self.Actions['Cross Narrow Surface/Uneven Ground (2-6 in wide)'] = 15
        self.Actions['Cross Narrow Surface/Uneven Ground (< 2 in wide)'] = 20

    def GetSkillCheck(self, character, action):
        check = super(acrobatics, self).GetSkillCheck(character, action)
        if check < 10 and action in ['Cross Narrow Surface/Uneven Ground (> 3 ft wide)',
                    'Cross Narrow Surface/Uneven Ground (1-3 ft wide)',
                    'Cross Narrow Surface/Uneven Ground (7-11 in wide)',
                    'Cross Narrow Surface/Uneven Ground (2-6 in wide)',
                    'Cross Narrow Surface/Uneven Ground (< 2 in wide)']:
            return config.INFINITY


class appraise(Skill):
    Name = "Appraise"
    Ability = config.ABILITY_INTELLIGENCE

    def __init__(self, key):
        super(appraise, self).__init__(key)


class bluff(Skill):
    Name = "Bluff"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(bluff, self).__init__(key)


class climb(Skill):
    Name = "Climb"
    Ability = config.ABILITY_STRENGTH
    UseACP = True

    def __init__(self, key):
        super(climb, self).__init__(key)


class craft1(Skill):
    Name = "Craft1"
    Ability = config.ABILITY_INTELLIGENCE

    def __init__(self, key):
        super(craft1, self).__init__(key)


class craft2(Skill):
    Name = "Craft2"
    Ability = config.ABILITY_INTELLIGENCE

    def __init__(self, key):
        super(craft2, self).__init__(key)


class diplomacy(Skill):
    Name = "Diplomacy"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(diplomacy, self).__init__(key)


class disable_device(Skill):
    Name = "Disable Device"
    Ability = config.ABILITY_DEXTERITY
    IsTrained = True
    UseACP = True

    def __init__(self, key):
        super(disable_device, self).__init__(key)


class disguise(Skill):
    Name = "Disguise"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(disguise, self).__init__(key)


class escape_artist(Skill):
    Name = "Escape Artist"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(escape_artist, self).__init__(key)


class fly(Skill):
    Name = "Fly"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(fly, self).__init__(key)


class handle_animal(Skill):
    Name = "Handle Animal"
    Ability = config.ABILITY_CHARISMA
    IsTrained = True

    def __init__(self, key):
        super(handle_animal, self).__init__(key)


class heal(Skill):
    Name = "Heal"
    Ability = config.ABILITY_WISDOM

    def __init__(self, key):
        super(heal, self).__init__(key)


class intimidate(Skill):
    Name = "Intimidate"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(intimidate, self).__init__(key)


class knowledge_arcana(Skill):
    Name = "Knowledge Arcana"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_arcana, self).__init__(key)


class knowledge_dungeoneering(Skill):
    Name = "Knowledge Dungeoneering"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_dungeoneering, self).__init__(key)


class knowledge_engineering(Skill):
    Name = "Knowledge Engineering"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_engineering, self).__init__(key)


class knowledge_geography(Skill):
    Name = "Knowledge Geography"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_geography, self).__init__(key)


class knowledge_history(Skill):
    Name = "Knowledge History"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_history, self).__init__(key)


class knowledge_local(Skill):
    Name = "Knowledge Local"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_local, self).__init__(key)


class knowledge_nature(Skill):
    Name = "Knowledge Nature"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_nature, self).__init__(key)


class knowledge_nobility(Skill):
    Name = "Knowledge Nobility"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_nobility, self).__init__(key)


class knowledge_planes(Skill):
    Name = "Knowledge Planes"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_planes, self).__init__(key)


class knowledge_religion(Skill):
    Name = "Knowledge Religion"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_religion, self).__init__(key)


class linguistics(Skill):
    Name = "Linguistics"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(linguistics, self).__init__(key)


class perception(Skill):
    Name = "Perception"
    Ability = config.ABILITY_WISDOM

    def __init__(self, key):
        super(perception, self).__init__(key)


class perform1(Skill):
    Name = "Perform1"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(perform1, self).__init__(key)


class perform2(Skill):
    Name = "Perform2"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(perform2, self).__init__(key)


class prof1(Skill):
    Name = "Prof1"
    Ability = config.ABILITY_WISDOM
    IsTrained = True

    def __init__(self, key):
        super(prof1, self).__init__(key)


class prof2(Skill):
    Name = "Prof2"
    Ability = config.ABILITY_WISDOM
    IsTrained = True

    def __init__(self, key):
        super(prof2, self).__init__(key)


class ride(Skill):
    Name = "Ride"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(ride, self).__init__(key)


class sense_motive(Skill):
    Name = "Sense Motive"
    Ability = config.ABILITY_WISDOM

    def __init__(self, key):
        super(sense_motive, self).__init__(key)


class sleight_of_hand(Skill):
    Name = "Sleight Of Hand"
    Ability = config.ABILITY_DEXTERITY
    IsTrained = True
    UseACP = True

    def __init__(self, key):
        super(sleight_of_hand, self).__init__(key)


class spellcraft(Skill):
    Name = "Spellcraft"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(spellcraft, self).__init__(key)


class stealth(Skill):
    Name = "Stealth"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(stealth, self).__init__(key)


class survival(Skill):
    Name = "Survival"
    Ability = config.ABILITY_WISDOM

    def __init__(self, key):
        super(survival, self).__init__(key)


class swim(Skill):
    Name = "Swim"
    Ability = config.ABILITY_STRENGTH
    UseACP = True

    def __init__(self, key):
        super(swim, self).__init__(key)


class use_magic_device(Skill):
    Name = "Use Magic Device"
    Ability = config.ABILITY_CHARISMA
    IsTrained = True

    def __init__(self, key):
        super(use_magic_device, self).__init__(key)


SkillClasses = {
    config.SKILL_ACROBATICS: acrobatics,
    config.SKILL_APPRAISE: appraise,
    config.SKILL_BLUFF: bluff,
    config.SKILL_CLIMB: climb,
    config.SKILL_CRAFT1: craft1,
    config.SKILL_CRAFT2: craft2,
    config.SKILL_DIPLOMACY: diplomacy,
    config.SKILL_DISABLE_DEVICE: disable_device,
    config.SKILL_DISGUISE: disguise,
    config.SKILL_ESCAPE_ARTIST: escape_artist,
    config.SKILL_FLY: fly,
    config.SKILL_HANDLE_ANIMAL: handle_animal,
    config.SKILL_HEAL: heal,
    config.SKILL_INTIMIDATE: intimidate,
    config.SKILL_KNOWLEDGE_ARCANA: knowledge_arcana,
    config.SKILL_KNOWLEDGE_DUNGEONEERING: knowledge_dungeoneering,
    config.SKILL_KNOWLEDGE_ENGINEERING: knowledge_engineering,
    config.SKILL_KNOWLEDGE_GEOGRAPHY: knowledge_geography,
    config.SKILL_KNOWLEDGE_HISTORY: knowledge_history,
    config.SKILL_KNOWLEDGE_LOCAL: knowledge_local,
    config.SKILL_KNOWLEDGE_NATURE: knowledge_nature,
    config.SKILL_KNOWLEDGE_NOBILITY: knowledge_nobility,
    config.SKILL_KNOWLEDGE_PLANES: knowledge_planes,
    config.SKILL_KNOWLEDGE_RELIGION: knowledge_religion,
    config.SKILL_LINGUISTICS: linguistics,
    config.SKILL_PERCEPTION: perception,
    config.SKILL_PERFORM1: perform1,
    config.SKILL_PERFORM2: perform2,
    config.SKILL_PROF1: prof1,
    config.SKILL_PROF2: prof2,
    config.SKILL_RIDE: ride,
    config.SKILL_SENSE_MOTIVE: sense_motive,
    config.SKILL_SLEIGHT_OF_HAND: sleight_of_hand,
    config.SKILL_SPELLCRAFT: spellcraft,
    config.SKILL_STEALTH: stealth,
    config.SKILL_SURVIVAL: survival,
    config.SKILL_SWIM: swim,
    config.SKILL_USE_MAGIC_DEVICE: use_magic_device
}
