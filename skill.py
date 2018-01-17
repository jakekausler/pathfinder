
import config
import urllib2
from bs4 import BeautifulSoup
import os

# TODO: Add ability to see what actions can be done with a skill, and the chance that the action will succeed


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
    WebName = ""

    def __init__(self, key):
        self.Key = key
        self.Actions = {}  # Dictionary of action name to {subaction: score}
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

    def GetChanceOfSuccess(self, character, mainAction, subAction):
        if self.GetSkillCheck(character, mainAction, subAction) == config.INFINITY:
            return 1
        return 1 - (self.GetSkillCheck(mainAction, subAction) - self.GetTotal(character)) / 20.0

    # Return INFINITY if no check is needed
    def GetSkillCheck(self, character, mainAction, subAction):
        check = self.Actions[mainAction][subAction]
        for key in self.ActiveModifiers:
            if self.ActiveModifiers[key]:
                check += self.ModifierAmounts[key]
        return check

    def ActivateModifer(self, modifer):
        self.ActiveModifiers[modifer] = True

    def DeactivateModifer(self, modifer):
        self.ActiveModifiers[modifer] = False

    def GetWebInfo(self):
        if os.path.isfile(self.WebName + ".skl"):
            with open(self.WebName + ".skl") as f:
                return f.read()
        else:
            data = urllib2.urlopen("http://www.d20pfsrd.com/skills/" + self.WebName)
            data = data.read()
            soup = BeautifulSoup(data, 'html.parser')
            soup = soup.main
            [x.extract() for x in soup.findAll('script')]
            [x.extract() for x in soup.findAll('a', {'class': 'bread-parent'})]
            [x.extract() for x in soup.findAll('div', {'class': 'page-widget'})]
            [x.extract() for x in soup.findAll('div', {'class': 'product-right'})]
            REMOVE_ATTRIBUTES = ['border', 'cellpadding']
            for tag in soup.recursiveChildGenerator():
                if hasattr(tag, 'attrs'):
                    tag.attrs = {key: value for key, value in tag.attrs.iteritems() if key not in REMOVE_ATTRIBUTES}
            return str(soup)


class acrobatics(Skill):
    Name = "Acrobatics"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True
    WebName = "acrobatics"

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
        self.ModifierAmounts['Long Pole'] = 2
        self.ActiveModifiers['Long Pole'] = False
        self.ModifierAmounts['Move at full speed on narrow or uneven surfaces'] = 5
        self.ActiveModifiers['Move at full speed on narrow or uneven surfaces'] = False
        self.Actions['Cross Narrow Surface/Uneven Ground'] = {
            '>3 ft wide': 0,
            '1-3 ft wide': 5,
            '7-11 in wide': 10,
            '2-6 in wide': 15,
            '< 2 in wide': 20
        }
        self.Actions['Long Jump'] = {
        }

    def GetSkillCheck(self, character, mainAction, subAction):
        check = super(acrobatics, self).GetSkillCheck(character, mainAction, subAction)
        if check < 10 and mainAction == 'Move at full speed on narrow or uneven surfaces' and subAction in [
                    '> 3 ft wide',
                    '1-3 ft wide'
                ]:
            return config.INFINITY


class appraise(Skill):
    WebName = "appraise"
    Name = "Appraise"
    Ability = config.ABILITY_INTELLIGENCE

    def __init__(self, key):
        super(appraise, self).__init__(key)


class bluff(Skill):
    WebName = "bluff"
    Name = "Bluff"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(bluff, self).__init__(key)


class climb(Skill):
    WebName = "climb"
    Name = "Climb"
    Ability = config.ABILITY_STRENGTH
    UseACP = True

    def __init__(self, key):
        super(climb, self).__init__(key)


class craft1(Skill):
    WebName = "craft"
    Name = "Craft1"
    Ability = config.ABILITY_INTELLIGENCE

    def __init__(self, key):
        super(craft1, self).__init__(key)


class craft2(Skill):
    WebName = "craft"
    Name = "Craft2"
    Ability = config.ABILITY_INTELLIGENCE

    def __init__(self, key):
        super(craft2, self).__init__(key)


class diplomacy(Skill):
    WebName = "diplomacy"
    Name = "Diplomacy"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(diplomacy, self).__init__(key)


class disable_device(Skill):
    WebName = "disable-device"
    Name = "Disable Device"
    Ability = config.ABILITY_DEXTERITY
    IsTrained = True
    UseACP = True

    def __init__(self, key):
        super(disable_device, self).__init__(key)


class disguise(Skill):
    WebName = "disguise"
    Name = "Disguise"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(disguise, self).__init__(key)


class escape_artist(Skill):
    WebName = "escape-artist"
    Name = "Escape Artist"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(escape_artist, self).__init__(key)


class fly(Skill):
    WebName = "fly"
    Name = "Fly"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(fly, self).__init__(key)


class handle_animal(Skill):
    WebName = "handle-animal"
    Name = "Handle Animal"
    Ability = config.ABILITY_CHARISMA
    IsTrained = True

    def __init__(self, key):
        super(handle_animal, self).__init__(key)


class heal(Skill):
    WebName = "heal"
    Name = "Heal"
    Ability = config.ABILITY_WISDOM

    def __init__(self, key):
        super(heal, self).__init__(key)


class intimidate(Skill):
    WebName = "intimidate"
    Name = "Intimidate"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(intimidate, self).__init__(key)


class knowledge_arcana(Skill):
    WebName = "knowledge"
    Name = "Knowledge Arcana"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_arcana, self).__init__(key)


class knowledge_dungeoneering(Skill):
    WebName = "knowledge"
    Name = "Knowledge Dungeoneering"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_dungeoneering, self).__init__(key)


class knowledge_engineering(Skill):
    WebName = "knowledge"
    Name = "Knowledge Engineering"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_engineering, self).__init__(key)


class knowledge_geography(Skill):
    WebName = "knowledge"
    Name = "Knowledge Geography"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_geography, self).__init__(key)


class knowledge_history(Skill):
    WebName = "knowledge"
    Name = "Knowledge History"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_history, self).__init__(key)


class knowledge_local(Skill):
    WebName = "knowledge"
    Name = "Knowledge Local"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_local, self).__init__(key)


class knowledge_nature(Skill):
    WebName = "knowledge"
    Name = "Knowledge Nature"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_nature, self).__init__(key)


class knowledge_nobility(Skill):
    WebName = "knowledge"
    Name = "Knowledge Nobility"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_nobility, self).__init__(key)


class knowledge_planes(Skill):
    WebName = "knowledge"
    Name = "Knowledge Planes"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_planes, self).__init__(key)


class knowledge_religion(Skill):
    WebName = "knowledge"
    Name = "Knowledge Religion"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(knowledge_religion, self).__init__(key)


class linguistics(Skill):
    WebName = "linguistics"
    Name = "Linguistics"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(linguistics, self).__init__(key)


class perception(Skill):
    WebName = "perception"
    Name = "Perception"
    Ability = config.ABILITY_WISDOM

    def __init__(self, key):
        super(perception, self).__init__(key)


class perform1(Skill):
    WebName = "perform"
    Name = "Perform1"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(perform1, self).__init__(key)


class perform2(Skill):
    WebName = "perform"
    Name = "Perform2"
    Ability = config.ABILITY_CHARISMA

    def __init__(self, key):
        super(perform2, self).__init__(key)


class prof1(Skill):
    WebName = "profession"
    Name = "Prof1"
    Ability = config.ABILITY_WISDOM
    IsTrained = True

    def __init__(self, key):
        super(prof1, self).__init__(key)


class prof2(Skill):
    WebName = "profession"
    Name = "Prof2"
    Ability = config.ABILITY_WISDOM
    IsTrained = True

    def __init__(self, key):
        super(prof2, self).__init__(key)


class ride(Skill):
    WebName = "ride"
    Name = "Ride"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(ride, self).__init__(key)


class sense_motive(Skill):
    WebName = "sense-motive"
    Name = "Sense Motive"
    Ability = config.ABILITY_WISDOM

    def __init__(self, key):
        super(sense_motive, self).__init__(key)


class sleight_of_hand(Skill):
    WebName = "sleight-of-hand"
    Name = "Sleight Of Hand"
    Ability = config.ABILITY_DEXTERITY
    IsTrained = True
    UseACP = True

    def __init__(self, key):
        super(sleight_of_hand, self).__init__(key)


class spellcraft(Skill):
    WebName = "spellcraft"
    Name = "Spellcraft"
    Ability = config.ABILITY_INTELLIGENCE
    IsTrained = True

    def __init__(self, key):
        super(spellcraft, self).__init__(key)


class stealth(Skill):
    WebName = "stealth"
    Name = "Stealth"
    Ability = config.ABILITY_DEXTERITY
    UseACP = True

    def __init__(self, key):
        super(stealth, self).__init__(key)


class survival(Skill):
    WebName = "survival"
    Name = "Survival"
    Ability = config.ABILITY_WISDOM

    def __init__(self, key):
        super(survival, self).__init__(key)


class swim(Skill):
    WebName = "swim"
    Name = "Swim"
    Ability = config.ABILITY_STRENGTH
    UseACP = True

    def __init__(self, key):
        super(swim, self).__init__(key)


class use_magic_device(Skill):
    WebName = "use-magic-device"
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

def saveWebInfo():
    for skill in SkillClasses:
        s = SkillClasses[skill](skill)
        data = s.GetWebInfo()
        with open(s.WebName + '.skl', 'w') as f:
            f.write(data)
