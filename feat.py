
# TODO: Feat Classes

import config

import skill
import json

featData = []
namesToIds = {}


def LoadFeatDatabase(fn='feats.json'):
    global featData
    with open(fn) as f:
        featData = json.loads(f.read())
        for i in range(len(featData)):
            namesToIds[featData[i]['name']] = i


def LoadFeatByName(name):
    global featData
    if not featData:
        LoadFeatDatabase()
    ret = Feat()
    if featData and name in namesToIds:
        ret = FeatClasses[namesToIds[name]](featData[namesToIds[name]])
    return ret


def LoadFeatById(id):
    global featData
    if not featData:
        LoadFeatDatabase()
    ret = Feat()
    if featData and id > 0 and id <= len(featData):
        ret = FeatClasses[id - 1](featData[id - 1])
    return ret


def GetValidFeats(char):
    global featData
    if not featData:
        LoadFeatDatabase()
    ret = []
    for feat in featData:
        if Feat(feat).CanLearnFeat(char):
            ret.append(Feat(feat))
    return ret


class Feat(object):

    def __init__(self, data=None):
        self.ID = 0
        self.Name = ""
        self.Type = ""
        self.Description = ""
        self.Prerequisites = ""
        self.PrerequisitesFeats = ""
        self.Benefit = ""
        self.Normal = ""
        self.Special = ""
        self.Source = ""
        self.Fulltext = ""
        self.Critical = ""
        self.Grit = ""
        self.Style = ""
        self.Performance = ""
        self.Racial = ""
        self.CompanionFamiliar = ""
        self.RaceName = ""
        self.Note = ""
        self.Goal = ""
        self.CompletionBenefit = ""
        self.Multiples = ""
        self.SuggestedTraits = ""
        if data:
            self.ParseData(data)

    def AddEffect(self, character):
        return

    def RemoveEffect(self, character):
        return

    def ParseData(self, data):
        self.ID = data['id']
        self.Name = data['name']
        self.Type = data['type']
        self.Description = data['description']
        self.Prerequisites = data['prerequisites']
        self.PrerequisitesFeats = data['prerequisites_feats']
        self.Benefit = data['benefit']
        self.Normal = data['normal']
        self.Special = data['special']
        self.Source = data['source']
        self.Fulltext = data['fulltext']
        self.Critical = data['critical']
        self.Grit = data['grit']
        self.Style = data['style']
        self.Performance = data['performance']
        self.Racial = data['racial']
        self.CompanionFamiliar = data['companion_familiar']
        self.RaceName = data['race_name']
        self.Note = data['note']
        self.Goal = data['goal']
        self.CompletionBenefit = data['completion_benefit']
        self.Multiples = data['multiples']
        self.SuggestedTraits = data['suggested_traits']

    def CanLearnFeat(self, char):
        return True

    def ToJson(self):
        return {
            'ID': self.ID,
            'Name': self.Name,
            'Type': self.Type,
            'Description': self.Description,
            'Prerequisites': self.Prerequisites,
            'PrerequisitesFeats': self.PrerequisitesFeats,
            'Benefit': self.Benefit,
            'Normal': self.Normal,
            'Special': self.Special,
            'Source': self.Source,
            'Fulltext': self.Fulltext,
            'Critical': self.Critical,
            'Grit': self.Grit,
            'Style': self.Style,
            'Performance': self.Performance,
            'Racial': self.Racial,
            'CompanionFamiliar': self.CompanionFamiliar,
            'RaceName': self.RaceName,
            'Note': self.Note,
            'Goal': self.Goal,
            'CompletionBenefit': self.CompletionBenefit,
            'Multiples': self.Multiples,
            'SuggestedTraits': self.SuggestedTraits
        }


class Acrobatic(Feat):

    def __init__(self, data=None):
        super(Acrobatic, self).__init__(data)

    def AddEffect(self, character):
        super(Acrobatic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Acrobatic, self).RemoveEffect(character)


class AcrobaticSteps(Feat):

    def __init__(self, data=None):
        super(AcrobaticSteps, self).__init__(data)

    def AddEffect(self, character):
        super(AcrobaticSteps, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AcrobaticSteps, self).RemoveEffect(character)


class AgileManeuvers(Feat):

    def __init__(self, data=None):
        super(AgileManeuvers, self).__init__(data)

    def AddEffect(self, character):
        super(AgileManeuvers, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AgileManeuvers, self).RemoveEffect(character)


class Alertness(Feat):

    def __init__(self, data=None):
        super(Alertness, self).__init__(data)

    def AddEffect(self, character):
        super(Alertness, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Alertness, self).RemoveEffect(character)


class AlignmentChannel(Feat):

    def __init__(self, data=None):
        super(AlignmentChannel, self).__init__(data)

    def AddEffect(self, character):
        super(AlignmentChannel, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AlignmentChannel, self).RemoveEffect(character)


class AnimalAffinity(Feat):

    def __init__(self, data=None):
        super(AnimalAffinity, self).__init__(data)
        self.AddedRide = 0
        self.AddedHandleAnimal = 0

    def AddEffect(self, character):
        super(AnimalAffinity, self).AddEffect(character)
        character.FeatSkills[skill.RIDE] += 2
        self.AddedRide += 2
        if character.Skills[skill.RIDE][0] >= 10:
            character.FeatSkills[skill.RIDE] += 2
            self.AddedRide += 2
        character.FeatSkills[skill.HANDLE_ANIMAL] += 2
        self.AddedHandleAnimal += 2
        if character.Skills[skill.HANDLE_ANIMAL][0] >= 10:
            character.FeatSkills[skill.HANDLE_ANIMAL] += 2
            self.AddedHandleAnimal += 2

    def RemoveEffect(self, character):
        super(AnimalAffinity, self).RemoveEffect(character)
        character.FeatSkills[skill.RIDE] -= self.AddedRide
        self.AddedRide = 0
        character.FeatSkills[skill.HANDLE_ANIMAL] -= self.AddedHandleAnimal
        self.AddedHandleAnimal = 0


class ArcaneArmorMastery(Feat):

    def __init__(self, data=None):
        super(ArcaneArmorMastery, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneArmorMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneArmorMastery, self).RemoveEffect(character)


class ArcaneArmorTraining(Feat):

    def __init__(self, data=None):
        super(ArcaneArmorTraining, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneArmorTraining, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneArmorTraining, self).RemoveEffect(character)


class ArcaneStrike(Feat):

    def __init__(self, data=None):
        super(ArcaneStrike, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneStrike, self).RemoveEffect(character)


class HeavyArmorProficiency(Feat):

    def __init__(self, data=None):
        super(HeavyArmorProficiency, self).__init__(data)

    def AddEffect(self, character):
        super(HeavyArmorProficiency, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HeavyArmorProficiency, self).RemoveEffect(character)


class LightArmorProficiency(Feat):

    def __init__(self, data=None):
        super(LightArmorProficiency, self).__init__(data)

    def AddEffect(self, character):
        super(LightArmorProficiency, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LightArmorProficiency, self).RemoveEffect(character)


class MediumArmorProficiency(Feat):

    def __init__(self, data=None):
        super(MediumArmorProficiency, self).__init__(data)

    def AddEffect(self, character):
        super(MediumArmorProficiency, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MediumArmorProficiency, self).RemoveEffect(character)


class Athletic(Feat):

    def __init__(self, data=None):
        super(Athletic, self).__init__(data)

    def AddEffect(self, character):
        super(Athletic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Athletic, self).RemoveEffect(character)


class AugmentSummoning(Feat):

    def __init__(self, data=None):
        super(AugmentSummoning, self).__init__(data)

    def AddEffect(self, character):
        super(AugmentSummoning, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AugmentSummoning, self).RemoveEffect(character)


class BleedingCritical(Feat):

    def __init__(self, data=None):
        super(BleedingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(BleedingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BleedingCritical, self).RemoveEffect(character)


class BlindFight(Feat):

    def __init__(self, data=None):
        super(BlindFight, self).__init__(data)

    def AddEffect(self, character):
        super(BlindFight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlindFight, self).RemoveEffect(character)


class BlindingCritical(Feat):

    def __init__(self, data=None):
        super(BlindingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(BlindingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlindingCritical, self).RemoveEffect(character)


class BrewPotion(Feat):

    def __init__(self, data=None):
        super(BrewPotion, self).__init__(data)

    def AddEffect(self, character):
        super(BrewPotion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BrewPotion, self).RemoveEffect(character)


class CatchOffGuard(Feat):

    def __init__(self, data=None):
        super(CatchOffGuard, self).__init__(data)

    def AddEffect(self, character):
        super(CatchOffGuard, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CatchOffGuard, self).RemoveEffect(character)


class ChannelSmite(Feat):

    def __init__(self, data=None):
        super(ChannelSmite, self).__init__(data)

    def AddEffect(self, character):
        super(ChannelSmite, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ChannelSmite, self).RemoveEffect(character)


class Cleave(Feat):

    def __init__(self, data=None):
        super(Cleave, self).__init__(data)

    def AddEffect(self, character):
        super(Cleave, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Cleave, self).RemoveEffect(character)


class CombatCasting(Feat):

    def __init__(self, data=None):
        super(CombatCasting, self).__init__(data)

    def AddEffect(self, character):
        super(CombatCasting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CombatCasting, self).RemoveEffect(character)


class CombatExpertise(Feat):

    def __init__(self, data=None):
        super(CombatExpertise, self).__init__(data)

    def AddEffect(self, character):
        super(CombatExpertise, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CombatExpertise, self).RemoveEffect(character)


class CombatReflexes(Feat):

    def __init__(self, data=None):
        super(CombatReflexes, self).__init__(data)

    def AddEffect(self, character):
        super(CombatReflexes, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CombatReflexes, self).RemoveEffect(character)


class CommandUndead(Feat):

    def __init__(self, data=None):
        super(CommandUndead, self).__init__(data)

    def AddEffect(self, character):
        super(CommandUndead, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CommandUndead, self).RemoveEffect(character)


class CraftMagicArmsAndArmor(Feat):

    def __init__(self, data=None):
        super(CraftMagicArmsAndArmor, self).__init__(data)

    def AddEffect(self, character):
        super(CraftMagicArmsAndArmor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraftMagicArmsAndArmor, self).RemoveEffect(character)


class CraftRod(Feat):

    def __init__(self, data=None):
        super(CraftRod, self).__init__(data)

    def AddEffect(self, character):
        super(CraftRod, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraftRod, self).RemoveEffect(character)


class CraftWand(Feat):

    def __init__(self, data=None):
        super(CraftWand, self).__init__(data)

    def AddEffect(self, character):
        super(CraftWand, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraftWand, self).RemoveEffect(character)


class CraftStaff(Feat):

    def __init__(self, data=None):
        super(CraftStaff, self).__init__(data)

    def AddEffect(self, character):
        super(CraftStaff, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraftStaff, self).RemoveEffect(character)


class CraftWondrousItem(Feat):

    def __init__(self, data=None):
        super(CraftWondrousItem, self).__init__(data)

    def AddEffect(self, character):
        super(CraftWondrousItem, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraftWondrousItem, self).RemoveEffect(character)


class CriticalFocus(Feat):

    def __init__(self, data=None):
        super(CriticalFocus, self).__init__(data)

    def AddEffect(self, character):
        super(CriticalFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CriticalFocus, self).RemoveEffect(character)


class CriticalMastery(Feat):

    def __init__(self, data=None):
        super(CriticalMastery, self).__init__(data)

    def AddEffect(self, character):
        super(CriticalMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CriticalMastery, self).RemoveEffect(character)


class DazzlingDisplay(Feat):

    def __init__(self, data=None):
        super(DazzlingDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(DazzlingDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DazzlingDisplay, self).RemoveEffect(character)


class DeadlyAim(Feat):

    def __init__(self, data=None):
        super(DeadlyAim, self).__init__(data)

    def AddEffect(self, character):
        super(DeadlyAim, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeadlyAim, self).RemoveEffect(character)


class DeadlyStroke(Feat):

    def __init__(self, data=None):
        super(DeadlyStroke, self).__init__(data)

    def AddEffect(self, character):
        super(DeadlyStroke, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeadlyStroke, self).RemoveEffect(character)


class DeafeningCritical(Feat):

    def __init__(self, data=None):
        super(DeafeningCritical, self).__init__(data)

    def AddEffect(self, character):
        super(DeafeningCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeafeningCritical, self).RemoveEffect(character)


class Deceitful(Feat):

    def __init__(self, data=None):
        super(Deceitful, self).__init__(data)

    def AddEffect(self, character):
        super(Deceitful, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Deceitful, self).RemoveEffect(character)


class DefensiveCombatTraining(Feat):

    def __init__(self, data=None):
        super(DefensiveCombatTraining, self).__init__(data)

    def AddEffect(self, character):
        super(DefensiveCombatTraining, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DefensiveCombatTraining, self).RemoveEffect(character)


class DeflectArrows(Feat):

    def __init__(self, data=None):
        super(DeflectArrows, self).__init__(data)

    def AddEffect(self, character):
        super(DeflectArrows, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeflectArrows, self).RemoveEffect(character)


class DeftHands(Feat):

    def __init__(self, data=None):
        super(DeftHands, self).__init__(data)

    def AddEffect(self, character):
        super(DeftHands, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeftHands, self).RemoveEffect(character)


class Diehard(Feat):

    def __init__(self, data=None):
        super(Diehard, self).__init__(data)

    def AddEffect(self, character):
        super(Diehard, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Diehard, self).RemoveEffect(character)


class Disruptive(Feat):

    def __init__(self, data=None):
        super(Disruptive, self).__init__(data)

    def AddEffect(self, character):
        super(Disruptive, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Disruptive, self).RemoveEffect(character)


class Dodge(Feat):

    def __init__(self, data=None):
        super(Dodge, self).__init__(data)

    def AddEffect(self, character):
        super(Dodge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Dodge, self).RemoveEffect(character)


class DoubleSlice(Feat):

    def __init__(self, data=None):
        super(DoubleSlice, self).__init__(data)

    def AddEffect(self, character):
        super(DoubleSlice, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DoubleSlice, self).RemoveEffect(character)


class ElementalChannel(Feat):

    def __init__(self, data=None):
        super(ElementalChannel, self).__init__(data)

    def AddEffect(self, character):
        super(ElementalChannel, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElementalChannel, self).RemoveEffect(character)


class EmpowerSpell(Feat):

    def __init__(self, data=None):
        super(EmpowerSpell, self).__init__(data)

    def AddEffect(self, character):
        super(EmpowerSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EmpowerSpell, self).RemoveEffect(character)


class Endurance(Feat):

    def __init__(self, data=None):
        super(Endurance, self).__init__(data)

    def AddEffect(self, character):
        super(Endurance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Endurance, self).RemoveEffect(character)


class EnlargeSpell(Feat):

    def __init__(self, data=None):
        super(EnlargeSpell, self).__init__(data)

    def AddEffect(self, character):
        super(EnlargeSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EnlargeSpell, self).RemoveEffect(character)


class EschewMaterials(Feat):

    def __init__(self, data=None):
        super(EschewMaterials, self).__init__(data)

    def AddEffect(self, character):
        super(EschewMaterials, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EschewMaterials, self).RemoveEffect(character)


class ExhaustingCritical(Feat):

    def __init__(self, data=None):
        super(ExhaustingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(ExhaustingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExhaustingCritical, self).RemoveEffect(character)


class ExoticWeaponProficiency(Feat):

    def __init__(self, data=None):
        super(ExoticWeaponProficiency, self).__init__(data)

    def AddEffect(self, character):
        super(ExoticWeaponProficiency, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExoticWeaponProficiency, self).RemoveEffect(character)


class ExtendSpell(Feat):

    def __init__(self, data=None):
        super(ExtendSpell, self).__init__(data)

    def AddEffect(self, character):
        super(ExtendSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtendSpell, self).RemoveEffect(character)


class ExtraChannel(Feat):

    def __init__(self, data=None):
        super(ExtraChannel, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraChannel, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraChannel, self).RemoveEffect(character)


class ExtraKi(Feat):

    def __init__(self, data=None):
        super(ExtraKi, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraKi, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraKi, self).RemoveEffect(character)


class ExtraLayOnHands(Feat):

    def __init__(self, data=None):
        super(ExtraLayOnHands, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraLayOnHands, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraLayOnHands, self).RemoveEffect(character)


class ExtraMercy(Feat):

    def __init__(self, data=None):
        super(ExtraMercy, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraMercy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraMercy, self).RemoveEffect(character)


class ExtraPerformance(Feat):

    def __init__(self, data=None):
        super(ExtraPerformance, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraPerformance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraPerformance, self).RemoveEffect(character)


class ExtraRage(Feat):

    def __init__(self, data=None):
        super(ExtraRage, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraRage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraRage, self).RemoveEffect(character)


class FarShot(Feat):

    def __init__(self, data=None):
        super(FarShot, self).__init__(data)

    def AddEffect(self, character):
        super(FarShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FarShot, self).RemoveEffect(character)


class Fleet(Feat):

    def __init__(self, data=None):
        super(Fleet, self).__init__(data)

    def AddEffect(self, character):
        super(Fleet, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Fleet, self).RemoveEffect(character)


class ForgeRing(Feat):

    def __init__(self, data=None):
        super(ForgeRing, self).__init__(data)

    def AddEffect(self, character):
        super(ForgeRing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ForgeRing, self).RemoveEffect(character)


class GorgonSFist(Feat):

    def __init__(self, data=None):
        super(GorgonSFist, self).__init__(data)

    def AddEffect(self, character):
        super(GorgonSFist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GorgonSFist, self).RemoveEffect(character)


class GreatCleave(Feat):

    def __init__(self, data=None):
        super(GreatCleave, self).__init__(data)

    def AddEffect(self, character):
        super(GreatCleave, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreatCleave, self).RemoveEffect(character)


class GreatFortitude(Feat):

    def __init__(self, data=None):
        super(GreatFortitude, self).__init__(data)

    def AddEffect(self, character):
        super(GreatFortitude, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreatFortitude, self).RemoveEffect(character)


class GreaterBullRush(Feat):

    def __init__(self, data=None):
        super(GreaterBullRush, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterBullRush, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterBullRush, self).RemoveEffect(character)


class GreaterDisarm(Feat):

    def __init__(self, data=None):
        super(GreaterDisarm, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterDisarm, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterDisarm, self).RemoveEffect(character)


class GreaterFeint(Feat):

    def __init__(self, data=None):
        super(GreaterFeint, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterFeint, self).RemoveEffect(character)


class GreaterGrapple(Feat):

    def __init__(self, data=None):
        super(GreaterGrapple, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterGrapple, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterGrapple, self).RemoveEffect(character)


class GreaterOverrun(Feat):

    def __init__(self, data=None):
        super(GreaterOverrun, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterOverrun, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterOverrun, self).RemoveEffect(character)


class GreaterPenetratingStrike(Feat):

    def __init__(self, data=None):
        super(GreaterPenetratingStrike, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterPenetratingStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterPenetratingStrike, self).RemoveEffect(character)


class GreaterShieldFocus(Feat):

    def __init__(self, data=None):
        super(GreaterShieldFocus, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterShieldFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterShieldFocus, self).RemoveEffect(character)


class GreaterSpellFocus(Feat):

    def __init__(self, data=None):
        super(GreaterSpellFocus, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterSpellFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterSpellFocus, self).RemoveEffect(character)


class GreaterSpellPenetration(Feat):

    def __init__(self, data=None):
        super(GreaterSpellPenetration, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterSpellPenetration, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterSpellPenetration, self).RemoveEffect(character)


class GreaterSunder(Feat):

    def __init__(self, data=None):
        super(GreaterSunder, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterSunder, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterSunder, self).RemoveEffect(character)


class GreaterTrip(Feat):

    def __init__(self, data=None):
        super(GreaterTrip, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterTrip, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterTrip, self).RemoveEffect(character)


class GreaterTwoWeaponFighting(Feat):

    def __init__(self, data=None):
        super(GreaterTwoWeaponFighting, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterTwoWeaponFighting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterTwoWeaponFighting, self).RemoveEffect(character)


class GreaterVitalStrike(Feat):

    def __init__(self, data=None):
        super(GreaterVitalStrike, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterVitalStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterVitalStrike, self).RemoveEffect(character)


class GreaterWeaponFocus(Feat):

    def __init__(self, data=None):
        super(GreaterWeaponFocus, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterWeaponFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterWeaponFocus, self).RemoveEffect(character)


class GreaterWeaponSpecialization(Feat):

    def __init__(self, data=None):
        super(GreaterWeaponSpecialization, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterWeaponSpecialization, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterWeaponSpecialization, self).RemoveEffect(character)


class HeightenSpell(Feat):

    def __init__(self, data=None):
        super(HeightenSpell, self).__init__(data)

    def AddEffect(self, character):
        super(HeightenSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HeightenSpell, self).RemoveEffect(character)


class ImprovedBullRush(Feat):

    def __init__(self, data=None):
        super(ImprovedBullRush, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedBullRush, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedBullRush, self).RemoveEffect(character)


class ImprovedChannel(Feat):

    def __init__(self, data=None):
        super(ImprovedChannel, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedChannel, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedChannel, self).RemoveEffect(character)


class ImprovedCounterspell(Feat):

    def __init__(self, data=None):
        super(ImprovedCounterspell, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedCounterspell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedCounterspell, self).RemoveEffect(character)


class ImprovedCritical(Feat):

    def __init__(self, data=None):
        super(ImprovedCritical, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedCritical, self).RemoveEffect(character)


class ImprovedDisarm(Feat):

    def __init__(self, data=None):
        super(ImprovedDisarm, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedDisarm, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedDisarm, self).RemoveEffect(character)


class ImprovedFamiliar(Feat):

    def __init__(self, data=None):
        super(ImprovedFamiliar, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedFamiliar, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedFamiliar, self).RemoveEffect(character)


class ImprovedFeint(Feat):

    def __init__(self, data=None):
        super(ImprovedFeint, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedFeint, self).RemoveEffect(character)


class ImprovedGrapple(Feat):

    def __init__(self, data=None):
        super(ImprovedGrapple, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedGrapple, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedGrapple, self).RemoveEffect(character)


class ImprovedGreatFortitude(Feat):

    def __init__(self, data=None):
        super(ImprovedGreatFortitude, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedGreatFortitude, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedGreatFortitude, self).RemoveEffect(character)


class ImprovedInitiative(Feat):

    def __init__(self, data=None):
        super(ImprovedInitiative, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedInitiative, self).AddEffect(character)
        character.MiscInitiative += 4

    def RemoveEffect(self, character):
        super(ImprovedInitiative, self).RemoveEffect(character)
        character.MiscInitiative -= 4


class ImprovedIronWill(Feat):

    def __init__(self, data=None):
        super(ImprovedIronWill, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedIronWill, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedIronWill, self).RemoveEffect(character)


class ImprovedLightningReflexes(Feat):

    def __init__(self, data=None):
        super(ImprovedLightningReflexes, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedLightningReflexes, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedLightningReflexes, self).RemoveEffect(character)


class ImprovedOverrun(Feat):

    def __init__(self, data=None):
        super(ImprovedOverrun, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedOverrun, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedOverrun, self).RemoveEffect(character)


class ImprovedPreciseShot(Feat):

    def __init__(self, data=None):
        super(ImprovedPreciseShot, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedPreciseShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedPreciseShot, self).RemoveEffect(character)


class ImprovedShieldBash(Feat):

    def __init__(self, data=None):
        super(ImprovedShieldBash, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedShieldBash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedShieldBash, self).RemoveEffect(character)


class ImprovedSunder(Feat):

    def __init__(self, data=None):
        super(ImprovedSunder, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedSunder, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedSunder, self).RemoveEffect(character)


class ImprovedTrip(Feat):

    def __init__(self, data=None):
        super(ImprovedTrip, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedTrip, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedTrip, self).RemoveEffect(character)


class ImprovedTwoWeaponFighting(Feat):

    def __init__(self, data=None):
        super(ImprovedTwoWeaponFighting, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedTwoWeaponFighting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedTwoWeaponFighting, self).RemoveEffect(character)


class ImprovedUnarmedStrike(Feat):

    def __init__(self, data=None):
        super(ImprovedUnarmedStrike, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedUnarmedStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedUnarmedStrike, self).RemoveEffect(character)


class ImprovedVitalStrike(Feat):

    def __init__(self, data=None):
        super(ImprovedVitalStrike, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedVitalStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedVitalStrike, self).RemoveEffect(character)


class ImprovisedWeaponMastery(Feat):

    def __init__(self, data=None):
        super(ImprovisedWeaponMastery, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovisedWeaponMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovisedWeaponMastery, self).RemoveEffect(character)


class IntimidatingProwess(Feat):

    def __init__(self, data=None):
        super(IntimidatingProwess, self).__init__(data)

    def AddEffect(self, character):
        super(IntimidatingProwess, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(IntimidatingProwess, self).RemoveEffect(character)


class IronWill(Feat):

    def __init__(self, data=None):
        super(IronWill, self).__init__(data)

    def AddEffect(self, character):
        super(IronWill, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(IronWill, self).RemoveEffect(character)


class Leadership(Feat):

    def __init__(self, data=None):
        super(Leadership, self).__init__(data)

    def AddEffect(self, character):
        super(Leadership, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Leadership, self).RemoveEffect(character)


class LightningReflexes(Feat):

    def __init__(self, data=None):
        super(LightningReflexes, self).__init__(data)

    def AddEffect(self, character):
        super(LightningReflexes, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LightningReflexes, self).RemoveEffect(character)


class LightningStance(Feat):

    def __init__(self, data=None):
        super(LightningStance, self).__init__(data)

    def AddEffect(self, character):
        super(LightningStance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LightningStance, self).RemoveEffect(character)


class Lunge(Feat):

    def __init__(self, data=None):
        super(Lunge, self).__init__(data)

    def AddEffect(self, character):
        super(Lunge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Lunge, self).RemoveEffect(character)


class MagicalAptitude(Feat):

    def __init__(self, data=None):
        super(MagicalAptitude, self).__init__(data)

    def AddEffect(self, character):
        super(MagicalAptitude, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MagicalAptitude, self).RemoveEffect(character)


class Manyshot(Feat):

    def __init__(self, data=None):
        super(Manyshot, self).__init__(data)

    def AddEffect(self, character):
        super(Manyshot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Manyshot, self).RemoveEffect(character)


class MartialWeaponProficiency(Feat):

    def __init__(self, data=None):
        super(MartialWeaponProficiency, self).__init__(data)

    def AddEffect(self, character):
        super(MartialWeaponProficiency, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MartialWeaponProficiency, self).RemoveEffect(character)


class MasterCraftsman(Feat):

    def __init__(self, data=None):
        super(MasterCraftsman, self).__init__(data)

    def AddEffect(self, character):
        super(MasterCraftsman, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MasterCraftsman, self).RemoveEffect(character)


class MaximizeSpell(Feat):

    def __init__(self, data=None):
        super(MaximizeSpell, self).__init__(data)

    def AddEffect(self, character):
        super(MaximizeSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MaximizeSpell, self).RemoveEffect(character)


class MedusaSWrath(Feat):

    def __init__(self, data=None):
        super(MedusaSWrath, self).__init__(data)

    def AddEffect(self, character):
        super(MedusaSWrath, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MedusaSWrath, self).RemoveEffect(character)


class Mobility(Feat):

    def __init__(self, data=None):
        super(Mobility, self).__init__(data)

    def AddEffect(self, character):
        super(Mobility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Mobility, self).RemoveEffect(character)


class MountedArchery(Feat):

    def __init__(self, data=None):
        super(MountedArchery, self).__init__(data)

    def AddEffect(self, character):
        super(MountedArchery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MountedArchery, self).RemoveEffect(character)


class MountedCombat(Feat):

    def __init__(self, data=None):
        super(MountedCombat, self).__init__(data)

    def AddEffect(self, character):
        super(MountedCombat, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MountedCombat, self).RemoveEffect(character)


class NaturalSpell(Feat):

    def __init__(self, data=None):
        super(NaturalSpell, self).__init__(data)

    def AddEffect(self, character):
        super(NaturalSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NaturalSpell, self).RemoveEffect(character)


class NimbleMoves(Feat):

    def __init__(self, data=None):
        super(NimbleMoves, self).__init__(data)

    def AddEffect(self, character):
        super(NimbleMoves, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NimbleMoves, self).RemoveEffect(character)


class PenetratingStrike(Feat):

    def __init__(self, data=None):
        super(PenetratingStrike, self).__init__(data)

    def AddEffect(self, character):
        super(PenetratingStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PenetratingStrike, self).RemoveEffect(character)


class Persuasive(Feat):

    def __init__(self, data=None):
        super(Persuasive, self).__init__(data)
        self.AddedDiplomacy = 0
        self.AddedIntimidate = 0

    def AddEffect(self, character):
        super(Persuasive, self).AddEffect(character)
        character.FeatSkills[skill.DIPLOMACY] += 2
        self.AddedDiplomacy += 2
        if character.Skills[skill.DIPLOMACY][0] >= 10:
            character.FeatSkills[skill.DIPLOMACY] += 2
            self.AddedDiplomacy += 2
        character.FeatSkills[skill.INTIMIDATE] += 2
        self.AddedIntimidate += 2
        if character.Skills[skill.INTIMIDATE][0] >= 10:
            character.FeatSkills[skill.INTIMIDATE] += 2
            self.AddedIntimidate += 2

    def RemoveEffect(self, character):
        super(Persuasive, self).RemoveEffect(character)
        character.FeatSkills[skill.DIPLOMACY] -= self.AddedDiplomacy
        self.AddedDiplomacy = 0
        character.FeatSkills[skill.INTIMIDATE] -= self.AddedIntimidate
        self.AddedIntimidate = 0


class PinpointTargeting(Feat):

    def __init__(self, data=None):
        super(PinpointTargeting, self).__init__(data)

    def AddEffect(self, character):
        super(PinpointTargeting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PinpointTargeting, self).RemoveEffect(character)


class PointBlankShot(Feat):

    def __init__(self, data=None):
        super(PointBlankShot, self).__init__(data)

    def AddEffect(self, character):
        super(PointBlankShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PointBlankShot, self).RemoveEffect(character)


class PowerAttack(Feat):

    def __init__(self, data=None):
        super(PowerAttack, self).__init__(data)

    def AddEffect(self, character):
        super(PowerAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PowerAttack, self).RemoveEffect(character)


class PreciseShot(Feat):

    def __init__(self, data=None):
        super(PreciseShot, self).__init__(data)

    def AddEffect(self, character):
        super(PreciseShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PreciseShot, self).RemoveEffect(character)


class QuickDraw(Feat):

    def __init__(self, data=None):
        super(QuickDraw, self).__init__(data)

    def AddEffect(self, character):
        super(QuickDraw, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickDraw, self).RemoveEffect(character)


class QuickenSpell(Feat):

    def __init__(self, data=None):
        super(QuickenSpell, self).__init__(data)

    def AddEffect(self, character):
        super(QuickenSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickenSpell, self).RemoveEffect(character)


class RapidShot(Feat):

    def __init__(self, data=None):
        super(RapidShot, self).__init__(data)

    def AddEffect(self, character):
        super(RapidShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RapidShot, self).RemoveEffect(character)


class RideByAttack(Feat):

    def __init__(self, data=None):
        super(RideByAttack, self).__init__(data)

    def AddEffect(self, character):
        super(RideByAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RideByAttack, self).RemoveEffect(character)


class Run(Feat):

    def __init__(self, data=None):
        super(Run, self).__init__(data)

    def AddEffect(self, character):
        super(Run, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Run, self).RemoveEffect(character)


class ScorpionStyle(Feat):

    def __init__(self, data=None):
        super(ScorpionStyle, self).__init__(data)

    def AddEffect(self, character):
        super(ScorpionStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ScorpionStyle, self).RemoveEffect(character)


class ScribeScroll(Feat):

    def __init__(self, data=None):
        super(ScribeScroll, self).__init__(data)

    def AddEffect(self, character):
        super(ScribeScroll, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ScribeScroll, self).RemoveEffect(character)


class SelectiveChanneling(Feat):

    def __init__(self, data=None):
        super(SelectiveChanneling, self).__init__(data)

    def AddEffect(self, character):
        super(SelectiveChanneling, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SelectiveChanneling, self).RemoveEffect(character)


class SelfSufficient(Feat):

    def __init__(self, data=None):
        super(SelfSufficient, self).__init__(data)

    def AddEffect(self, character):
        super(SelfSufficient, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SelfSufficient, self).RemoveEffect(character)


class ShatterDefenses(Feat):

    def __init__(self, data=None):
        super(ShatterDefenses, self).__init__(data)

    def AddEffect(self, character):
        super(ShatterDefenses, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShatterDefenses, self).RemoveEffect(character)


class ShieldFocus(Feat):

    def __init__(self, data=None):
        super(ShieldFocus, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldFocus, self).RemoveEffect(character)


class ShieldProficiency(Feat):

    def __init__(self, data=None):
        super(ShieldProficiency, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldProficiency, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldProficiency, self).RemoveEffect(character)


class ShieldSlam(Feat):

    def __init__(self, data=None):
        super(ShieldSlam, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldSlam, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldSlam, self).RemoveEffect(character)


class ShotOnTheRun(Feat):

    def __init__(self, data=None):
        super(ShotOnTheRun, self).__init__(data)

    def AddEffect(self, character):
        super(ShotOnTheRun, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShotOnTheRun, self).RemoveEffect(character)


class SickeningCritical(Feat):

    def __init__(self, data=None):
        super(SickeningCritical, self).__init__(data)

    def AddEffect(self, character):
        super(SickeningCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SickeningCritical, self).RemoveEffect(character)


class SilentSpell(Feat):

    def __init__(self, data=None):
        super(SilentSpell, self).__init__(data)

    def AddEffect(self, character):
        super(SilentSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SilentSpell, self).RemoveEffect(character)


class SimpleWeaponProficiency(Feat):

    def __init__(self, data=None):
        super(SimpleWeaponProficiency, self).__init__(data)

    def AddEffect(self, character):
        super(SimpleWeaponProficiency, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SimpleWeaponProficiency, self).RemoveEffect(character)


class SkillFocus(Feat):

    def __init__(self, data=None):
        super(SkillFocus, self).__init__(data)

    def AddEffect(self, character):
        super(SkillFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SkillFocus, self).RemoveEffect(character)


class SnatchArrows(Feat):

    def __init__(self, data=None):
        super(SnatchArrows, self).__init__(data)

    def AddEffect(self, character):
        super(SnatchArrows, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SnatchArrows, self).RemoveEffect(character)


class SpellFocus(Feat):

    def __init__(self, data=None):
        super(SpellFocus, self).__init__(data)

    def AddEffect(self, character):
        super(SpellFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellFocus, self).RemoveEffect(character)


class SpellMastery(Feat):

    def __init__(self, data=None):
        super(SpellMastery, self).__init__(data)

    def AddEffect(self, character):
        super(SpellMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellMastery, self).RemoveEffect(character)


class SpellPenetration(Feat):

    def __init__(self, data=None):
        super(SpellPenetration, self).__init__(data)

    def AddEffect(self, character):
        super(SpellPenetration, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellPenetration, self).RemoveEffect(character)


class Spellbreaker(Feat):

    def __init__(self, data=None):
        super(Spellbreaker, self).__init__(data)

    def AddEffect(self, character):
        super(Spellbreaker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Spellbreaker, self).RemoveEffect(character)


class SpiritedCharge(Feat):

    def __init__(self, data=None):
        super(SpiritedCharge, self).__init__(data)

    def AddEffect(self, character):
        super(SpiritedCharge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpiritedCharge, self).RemoveEffect(character)


class SpringAttack(Feat):

    def __init__(self, data=None):
        super(SpringAttack, self).__init__(data)

    def AddEffect(self, character):
        super(SpringAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpringAttack, self).RemoveEffect(character)


class StaggeringCritical(Feat):

    def __init__(self, data=None):
        super(StaggeringCritical, self).__init__(data)

    def AddEffect(self, character):
        super(StaggeringCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StaggeringCritical, self).RemoveEffect(character)


class StandStill(Feat):

    def __init__(self, data=None):
        super(StandStill, self).__init__(data)

    def AddEffect(self, character):
        super(StandStill, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StandStill, self).RemoveEffect(character)


class Stealthy(Feat):

    def __init__(self, data=None):
        super(Stealthy, self).__init__(data)

    def AddEffect(self, character):
        super(Stealthy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Stealthy, self).RemoveEffect(character)


class StepUp(Feat):

    def __init__(self, data=None):
        super(StepUp, self).__init__(data)

    def AddEffect(self, character):
        super(StepUp, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StepUp, self).RemoveEffect(character)


class StillSpell(Feat):

    def __init__(self, data=None):
        super(StillSpell, self).__init__(data)

    def AddEffect(self, character):
        super(StillSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StillSpell, self).RemoveEffect(character)


class StrikeBack(Feat):

    def __init__(self, data=None):
        super(StrikeBack, self).__init__(data)

    def AddEffect(self, character):
        super(StrikeBack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StrikeBack, self).RemoveEffect(character)


class StunningCritical(Feat):

    def __init__(self, data=None):
        super(StunningCritical, self).__init__(data)

    def AddEffect(self, character):
        super(StunningCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StunningCritical, self).RemoveEffect(character)


class StunningFist(Feat):

    def __init__(self, data=None):
        super(StunningFist, self).__init__(data)

    def AddEffect(self, character):
        super(StunningFist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StunningFist, self).RemoveEffect(character)


class ThrowAnything(Feat):

    def __init__(self, data=None):
        super(ThrowAnything, self).__init__(data)

    def AddEffect(self, character):
        super(ThrowAnything, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThrowAnything, self).RemoveEffect(character)


class TiringCritical(Feat):

    def __init__(self, data=None):
        super(TiringCritical, self).__init__(data)

    def AddEffect(self, character):
        super(TiringCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TiringCritical, self).RemoveEffect(character)


class Toughness(Feat):

    def __init__(self, data=None):
        super(Toughness, self).__init__(data)

    def AddEffect(self, character):
        super(Toughness, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Toughness, self).RemoveEffect(character)


class TowerShieldProficiency(Feat):

    def __init__(self, data=None):
        super(TowerShieldProficiency, self).__init__(data)

    def AddEffect(self, character):
        super(TowerShieldProficiency, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TowerShieldProficiency, self).RemoveEffect(character)


class Trample(Feat):

    def __init__(self, data=None):
        super(Trample, self).__init__(data)

    def AddEffect(self, character):
        super(Trample, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Trample, self).RemoveEffect(character)


class TurnUndead(Feat):

    def __init__(self, data=None):
        super(TurnUndead, self).__init__(data)

    def AddEffect(self, character):
        super(TurnUndead, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TurnUndead, self).RemoveEffect(character)


class TwoWeaponDefense(Feat):

    def __init__(self, data=None):
        super(TwoWeaponDefense, self).__init__(data)

    def AddEffect(self, character):
        super(TwoWeaponDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwoWeaponDefense, self).RemoveEffect(character)


class TwoWeaponFighting(Feat):

    def __init__(self, data=None):
        super(TwoWeaponFighting, self).__init__(data)

    def AddEffect(self, character):
        super(TwoWeaponFighting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwoWeaponFighting, self).RemoveEffect(character)


class TwoWeaponRend(Feat):

    def __init__(self, data=None):
        super(TwoWeaponRend, self).__init__(data)

    def AddEffect(self, character):
        super(TwoWeaponRend, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwoWeaponRend, self).RemoveEffect(character)


class Unseat(Feat):

    def __init__(self, data=None):
        super(Unseat, self).__init__(data)

    def AddEffect(self, character):
        super(Unseat, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Unseat, self).RemoveEffect(character)


class VitalStrike(Feat):

    def __init__(self, data=None):
        super(VitalStrike, self).__init__(data)

    def AddEffect(self, character):
        super(VitalStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VitalStrike, self).RemoveEffect(character)


class WeaponFinesse(Feat):

    def __init__(self, data=None):
        super(WeaponFinesse, self).__init__(data)

    def AddEffect(self, character):
        super(WeaponFinesse, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WeaponFinesse, self).RemoveEffect(character)


class WeaponFocus(Feat):

    def __init__(self, data=None):
        super(WeaponFocus, self).__init__(data)

    def AddEffect(self, character):
        super(WeaponFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WeaponFocus, self).RemoveEffect(character)


class WeaponSpecialization(Feat):

    def __init__(self, data=None):
        super(WeaponSpecialization, self).__init__(data)

    def AddEffect(self, character):
        super(WeaponSpecialization, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WeaponSpecialization, self).RemoveEffect(character)


class WhirlwindAttack(Feat):

    def __init__(self, data=None):
        super(WhirlwindAttack, self).__init__(data)

    def AddEffect(self, character):
        super(WhirlwindAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WhirlwindAttack, self).RemoveEffect(character)


class WidenSpell(Feat):

    def __init__(self, data=None):
        super(WidenSpell, self).__init__(data)

    def AddEffect(self, character):
        super(WidenSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WidenSpell, self).RemoveEffect(character)


class WindStance(Feat):

    def __init__(self, data=None):
        super(WindStance, self).__init__(data)

    def AddEffect(self, character):
        super(WindStance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WindStance, self).RemoveEffect(character)


class AdditionalTraits(Feat):

    def __init__(self, data=None):
        super(AdditionalTraits, self).__init__(data)

    def AddEffect(self, character):
        super(AdditionalTraits, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AdditionalTraits, self).RemoveEffect(character)


class AbilityFocus(Feat):

    def __init__(self, data=None):
        super(AbilityFocus, self).__init__(data)

    def AddEffect(self, character):
        super(AbilityFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AbilityFocus, self).RemoveEffect(character)


class AwesomeBlow(Feat):

    def __init__(self, data=None):
        super(AwesomeBlow, self).__init__(data)

    def AddEffect(self, character):
        super(AwesomeBlow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AwesomeBlow, self).RemoveEffect(character)


class CraftConstruct(Feat):

    def __init__(self, data=None):
        super(CraftConstruct, self).__init__(data)

    def AddEffect(self, character):
        super(CraftConstruct, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraftConstruct, self).RemoveEffect(character)


class EmpowerSpellLikeAbility(Feat):

    def __init__(self, data=None):
        super(EmpowerSpellLikeAbility, self).__init__(data)

    def AddEffect(self, character):
        super(EmpowerSpellLikeAbility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EmpowerSpellLikeAbility, self).RemoveEffect(character)


class FlybyAttack(Feat):

    def __init__(self, data=None):
        super(FlybyAttack, self).__init__(data)

    def AddEffect(self, character):
        super(FlybyAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FlybyAttack, self).RemoveEffect(character)


class Hover(Feat):

    def __init__(self, data=None):
        super(Hover, self).__init__(data)

    def AddEffect(self, character):
        super(Hover, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Hover, self).RemoveEffect(character)


class ImprovedNaturalArmor(Feat):

    def __init__(self, data=None):
        super(ImprovedNaturalArmor, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedNaturalArmor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedNaturalArmor, self).RemoveEffect(character)


class ImprovedNaturalAttack(Feat):

    def __init__(self, data=None):
        super(ImprovedNaturalAttack, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedNaturalAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedNaturalAttack, self).RemoveEffect(character)


class Multiattack(Feat):

    def __init__(self, data=None):
        super(Multiattack, self).__init__(data)

    def AddEffect(self, character):
        super(Multiattack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Multiattack, self).RemoveEffect(character)


class QuickenSpellLikeAbility(Feat):

    def __init__(self, data=None):
        super(QuickenSpellLikeAbility, self).__init__(data)

    def AddEffect(self, character):
        super(QuickenSpellLikeAbility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickenSpellLikeAbility, self).RemoveEffect(character)


class Snatch(Feat):

    def __init__(self, data=None):
        super(Snatch, self).__init__(data)

    def AddEffect(self, character):
        super(Snatch, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Snatch, self).RemoveEffect(character)


class Wingover(Feat):

    def __init__(self, data=None):
        super(Wingover, self).__init__(data)

    def AddEffect(self, character):
        super(Wingover, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Wingover, self).RemoveEffect(character)


class AlliedSpellcaster(Feat):

    def __init__(self, data=None):
        super(AlliedSpellcaster, self).__init__(data)

    def AddEffect(self, character):
        super(AlliedSpellcaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AlliedSpellcaster, self).RemoveEffect(character)


class ArcaneBlast(Feat):

    def __init__(self, data=None):
        super(ArcaneBlast, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneBlast, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneBlast, self).RemoveEffect(character)


class ArcaneShield(Feat):

    def __init__(self, data=None):
        super(ArcaneShield, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneShield, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneShield, self).RemoveEffect(character)


class ArcaneTalent(Feat):

    def __init__(self, data=None):
        super(ArcaneTalent, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneTalent, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneTalent, self).RemoveEffect(character)


class AspectOfTheBeast(Feat):

    def __init__(self, data=None):
        super(AspectOfTheBeast, self).__init__(data)

    def AddEffect(self, character):
        super(AspectOfTheBeast, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AspectOfTheBeast, self).RemoveEffect(character)


class BashingFinish(Feat):

    def __init__(self, data=None):
        super(BashingFinish, self).__init__(data)

    def AddEffect(self, character):
        super(BashingFinish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BashingFinish, self).RemoveEffect(character)


class BloodyAssault(Feat):

    def __init__(self, data=None):
        super(BloodyAssault, self).__init__(data)

    def AddEffect(self, character):
        super(BloodyAssault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodyAssault, self).RemoveEffect(character)


class Bodyguard(Feat):

    def __init__(self, data=None):
        super(Bodyguard, self).__init__(data)

    def AddEffect(self, character):
        super(Bodyguard, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Bodyguard, self).RemoveEffect(character)


class BouncingSpell(Feat):

    def __init__(self, data=None):
        super(BouncingSpell, self).__init__(data)

    def AddEffect(self, character):
        super(BouncingSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BouncingSpell, self).RemoveEffect(character)


class BreadthOfExperience(Feat):

    def __init__(self, data=None):
        super(BreadthOfExperience, self).__init__(data)

    def AddEffect(self, character):
        super(BreadthOfExperience, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BreadthOfExperience, self).RemoveEffect(character)


class BullRushStrike(Feat):

    def __init__(self, data=None):
        super(BullRushStrike, self).__init__(data)

    def AddEffect(self, character):
        super(BullRushStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BullRushStrike, self).RemoveEffect(character)


class ChargeThrough(Feat):

    def __init__(self, data=None):
        super(ChargeThrough, self).__init__(data)

    def AddEffect(self, character):
        super(ChargeThrough, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ChargeThrough, self).RemoveEffect(character)


class Childlike(Feat):

    def __init__(self, data=None):
        super(Childlike, self).__init__(data)

    def AddEffect(self, character):
        super(Childlike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Childlike, self).RemoveEffect(character)


class CloudStep(Feat):

    def __init__(self, data=None):
        super(CloudStep, self).__init__(data)

    def AddEffect(self, character):
        super(CloudStep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CloudStep, self).RemoveEffect(character)


class CockatriceStrike(Feat):

    def __init__(self, data=None):
        super(CockatriceStrike, self).__init__(data)

    def AddEffect(self, character):
        super(CockatriceStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CockatriceStrike, self).RemoveEffect(character)


class CombatPatrol(Feat):

    def __init__(self, data=None):
        super(CombatPatrol, self).__init__(data)

    def AddEffect(self, character):
        super(CombatPatrol, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CombatPatrol, self).RemoveEffect(character)


class CooperativeCrafting(Feat):

    def __init__(self, data=None):
        super(CooperativeCrafting, self).__init__(data)

    def AddEffect(self, character):
        super(CooperativeCrafting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CooperativeCrafting, self).RemoveEffect(character)


class CoordinatedDefense(Feat):

    def __init__(self, data=None):
        super(CoordinatedDefense, self).__init__(data)

    def AddEffect(self, character):
        super(CoordinatedDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CoordinatedDefense, self).RemoveEffect(character)


class CoordinatedManeuvers(Feat):

    def __init__(self, data=None):
        super(CoordinatedManeuvers, self).__init__(data)

    def AddEffect(self, character):
        super(CoordinatedManeuvers, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CoordinatedManeuvers, self).RemoveEffect(character)


class Cosmopolitan(Feat):

    def __init__(self, data=None):
        super(Cosmopolitan, self).__init__(data)

    def AddEffect(self, character):
        super(Cosmopolitan, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Cosmopolitan, self).RemoveEffect(character)


class CoveringDefense(Feat):

    def __init__(self, data=None):
        super(CoveringDefense, self).__init__(data)

    def AddEffect(self, character):
        super(CoveringDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CoveringDefense, self).RemoveEffect(character)


class CripplingCritical(Feat):

    def __init__(self, data=None):
        super(CripplingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(CripplingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CripplingCritical, self).RemoveEffect(character)


class CrossbowMastery(Feat):

    def __init__(self, data=None):
        super(CrossbowMastery, self).__init__(data)

    def AddEffect(self, character):
        super(CrossbowMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CrossbowMastery, self).RemoveEffect(character)


class DastardlyFinish(Feat):

    def __init__(self, data=None):
        super(DastardlyFinish, self).__init__(data)

    def AddEffect(self, character):
        super(DastardlyFinish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DastardlyFinish, self).RemoveEffect(character)


class DazingAssault(Feat):

    def __init__(self, data=None):
        super(DazingAssault, self).__init__(data)

    def AddEffect(self, character):
        super(DazingAssault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DazingAssault, self).RemoveEffect(character)


class DazingSpell(Feat):

    def __init__(self, data=None):
        super(DazingSpell, self).__init__(data)

    def AddEffect(self, character):
        super(DazingSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DazingSpell, self).RemoveEffect(character)


class DeepDrinker(Feat):

    def __init__(self, data=None):
        super(DeepDrinker, self).__init__(data)

    def AddEffect(self, character):
        super(DeepDrinker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeepDrinker, self).RemoveEffect(character)


class Deepsight(Feat):

    def __init__(self, data=None):
        super(Deepsight, self).__init__(data)

    def AddEffect(self, character):
        super(Deepsight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Deepsight, self).RemoveEffect(character)


class DisarmingStrike(Feat):

    def __init__(self, data=None):
        super(DisarmingStrike, self).__init__(data)

    def AddEffect(self, character):
        super(DisarmingStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisarmingStrike, self).RemoveEffect(character)


class DisruptingShot(Feat):

    def __init__(self, data=None):
        super(DisruptingShot, self).__init__(data)

    def AddEffect(self, character):
        super(DisruptingShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisruptingShot, self).RemoveEffect(character)


class DisruptiveSpell(Feat):

    def __init__(self, data=None):
        super(DisruptiveSpell, self).__init__(data)

    def AddEffect(self, character):
        super(DisruptiveSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisruptiveSpell, self).RemoveEffect(character)


class DivinerSDelving(Feat):

    def __init__(self, data=None):
        super(DivinerSDelving, self).__init__(data)

    def AddEffect(self, character):
        super(DivinerSDelving, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DivinerSDelving, self).RemoveEffect(character)


class DreadfulCarnage(Feat):

    def __init__(self, data=None):
        super(DreadfulCarnage, self).__init__(data)

    def AddEffect(self, character):
        super(DreadfulCarnage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DreadfulCarnage, self).RemoveEffect(character)


class DuckAndCover(Feat):

    def __init__(self, data=None):
        super(DuckAndCover, self).__init__(data)

    def AddEffect(self, character):
        super(DuckAndCover, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DuckAndCover, self).RemoveEffect(character)


class EagleEyes(Feat):

    def __init__(self, data=None):
        super(EagleEyes, self).__init__(data)

    def AddEffect(self, character):
        super(EagleEyes, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EagleEyes, self).RemoveEffect(character)


class Eclectic(Feat):

    def __init__(self, data=None):
        super(Eclectic, self).__init__(data)

    def AddEffect(self, character):
        super(Eclectic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Eclectic, self).RemoveEffect(character)


class EctoplasmicSpell(Feat):

    def __init__(self, data=None):
        super(EctoplasmicSpell, self).__init__(data)

    def AddEffect(self, character):
        super(EctoplasmicSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EctoplasmicSpell, self).RemoveEffect(character)


class EldritchClaws(Feat):

    def __init__(self, data=None):
        super(EldritchClaws, self).__init__(data)

    def AddEffect(self, character):
        super(EldritchClaws, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EldritchClaws, self).RemoveEffect(character)


class ElementalFist(Feat):

    def __init__(self, data=None):
        super(ElementalFist, self).__init__(data)

    def AddEffect(self, character):
        super(ElementalFist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElementalFist, self).RemoveEffect(character)


class ElementalFocus(Feat):

    def __init__(self, data=None):
        super(ElementalFocus, self).__init__(data)

    def AddEffect(self, character):
        super(ElementalFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElementalFocus, self).RemoveEffect(character)


class ElementalSpell(Feat):

    def __init__(self, data=None):
        super(ElementalSpell, self).__init__(data)

    def AddEffect(self, character):
        super(ElementalSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElementalSpell, self).RemoveEffect(character)


class ElvenAccuracy(Feat):

    def __init__(self, data=None):
        super(ElvenAccuracy, self).__init__(data)

    def AddEffect(self, character):
        super(ElvenAccuracy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElvenAccuracy, self).RemoveEffect(character)


class Enforcer(Feat):

    def __init__(self, data=None):
        super(Enforcer, self).__init__(data)

    def AddEffect(self, character):
        super(Enforcer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Enforcer, self).RemoveEffect(character)


class ExpandedArcana(Feat):

    def __init__(self, data=None):
        super(ExpandedArcana, self).__init__(data)

    def AddEffect(self, character):
        super(ExpandedArcana, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExpandedArcana, self).RemoveEffect(character)


class ExtraBombs(Feat):

    def __init__(self, data=None):
        super(ExtraBombs, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraBombs, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraBombs, self).RemoveEffect(character)


class ExtraDiscovery(Feat):

    def __init__(self, data=None):
        super(ExtraDiscovery, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraDiscovery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraDiscovery, self).RemoveEffect(character)


class ExtraHex(Feat):

    def __init__(self, data=None):
        super(ExtraHex, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraHex, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraHex, self).RemoveEffect(character)


class ExtraRagePower(Feat):

    def __init__(self, data=None):
        super(ExtraRagePower, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraRagePower, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraRagePower, self).RemoveEffect(character)


class ExtraRevelation(Feat):

    def __init__(self, data=None):
        super(ExtraRevelation, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraRevelation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraRevelation, self).RemoveEffect(character)


class ExtraRogueTalent(Feat):

    def __init__(self, data=None):
        super(ExtraRogueTalent, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraRogueTalent, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraRogueTalent, self).RemoveEffect(character)


class FastDrinker(Feat):

    def __init__(self, data=None):
        super(FastDrinker, self).__init__(data)

    def AddEffect(self, character):
        super(FastDrinker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FastDrinker, self).RemoveEffect(character)


class FastHealer(Feat):

    def __init__(self, data=None):
        super(FastHealer, self).__init__(data)

    def AddEffect(self, character):
        super(FastHealer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FastHealer, self).RemoveEffect(character)


class FavoredDefense(Feat):

    def __init__(self, data=None):
        super(FavoredDefense, self).__init__(data)

    def AddEffect(self, character):
        super(FavoredDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FavoredDefense, self).RemoveEffect(character)


class FightOn(Feat):

    def __init__(self, data=None):
        super(FightOn, self).__init__(data)

    def AddEffect(self, character):
        super(FightOn, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FightOn, self).RemoveEffect(character)


class FocusedShot(Feat):

    def __init__(self, data=None):
        super(FocusedShot, self).__init__(data)

    def AddEffect(self, character):
        super(FocusedShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FocusedShot, self).RemoveEffect(character)


class FocusedSpell(Feat):

    def __init__(self, data=None):
        super(FocusedSpell, self).__init__(data)

    def AddEffect(self, character):
        super(FocusedSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FocusedSpell, self).RemoveEffect(character)


class FollowingStep(Feat):

    def __init__(self, data=None):
        super(FollowingStep, self).__init__(data)

    def AddEffect(self, character):
        super(FollowingStep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FollowingStep, self).RemoveEffect(character)


class FuriousFocus(Feat):

    def __init__(self, data=None):
        super(FuriousFocus, self).__init__(data)

    def AddEffect(self, character):
        super(FuriousFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FuriousFocus, self).RemoveEffect(character)


class GangUp(Feat):

    def __init__(self, data=None):
        super(GangUp, self).__init__(data)

    def AddEffect(self, character):
        super(GangUp, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GangUp, self).RemoveEffect(character)


class GnomeTrickster(Feat):

    def __init__(self, data=None):
        super(GnomeTrickster, self).__init__(data)

    def AddEffect(self, character):
        super(GnomeTrickster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GnomeTrickster, self).RemoveEffect(character)


class GoUnnoticed(Feat):

    def __init__(self, data=None):
        super(GoUnnoticed, self).__init__(data)

    def AddEffect(self, character):
        super(GoUnnoticed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GoUnnoticed, self).RemoveEffect(character)


class GreaterBlindFight(Feat):

    def __init__(self, data=None):
        super(GreaterBlindFight, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterBlindFight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterBlindFight, self).RemoveEffect(character)


class GreaterDirtyTrick(Feat):

    def __init__(self, data=None):
        super(GreaterDirtyTrick, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterDirtyTrick, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterDirtyTrick, self).RemoveEffect(character)


class GreaterDrag(Feat):

    def __init__(self, data=None):
        super(GreaterDrag, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterDrag, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterDrag, self).RemoveEffect(character)


class GreaterElementalFocus(Feat):

    def __init__(self, data=None):
        super(GreaterElementalFocus, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterElementalFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterElementalFocus, self).RemoveEffect(character)


class GreaterReposition(Feat):

    def __init__(self, data=None):
        super(GreaterReposition, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterReposition, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterReposition, self).RemoveEffect(character)


class GreaterShieldSpecialization(Feat):

    def __init__(self, data=None):
        super(GreaterShieldSpecialization, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterShieldSpecialization, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterShieldSpecialization, self).RemoveEffect(character)


class GreaterSteal(Feat):

    def __init__(self, data=None):
        super(GreaterSteal, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterSteal, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterSteal, self).RemoveEffect(character)


class Groundling(Feat):

    def __init__(self, data=None):
        super(Groundling, self).__init__(data)

    def AddEffect(self, character):
        super(Groundling, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Groundling, self).RemoveEffect(character)


class HeroicDefiance(Feat):

    def __init__(self, data=None):
        super(HeroicDefiance, self).__init__(data)

    def AddEffect(self, character):
        super(HeroicDefiance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HeroicDefiance, self).RemoveEffect(character)


class HeroicRecovery(Feat):

    def __init__(self, data=None):
        super(HeroicRecovery, self).__init__(data)

    def AddEffect(self, character):
        super(HeroicRecovery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HeroicRecovery, self).RemoveEffect(character)


class ImprovedBlindFight(Feat):

    def __init__(self, data=None):
        super(ImprovedBlindFight, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedBlindFight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedBlindFight, self).RemoveEffect(character)


class ImprovedDirtyTrick(Feat):

    def __init__(self, data=None):
        super(ImprovedDirtyTrick, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedDirtyTrick, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedDirtyTrick, self).RemoveEffect(character)


class ImprovedDrag(Feat):

    def __init__(self, data=None):
        super(ImprovedDrag, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedDrag, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedDrag, self).RemoveEffect(character)


class ImprovedKiThrow(Feat):

    def __init__(self, data=None):
        super(ImprovedKiThrow, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedKiThrow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedKiThrow, self).RemoveEffect(character)


class ImprovedReposition(Feat):

    def __init__(self, data=None):
        super(ImprovedReposition, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedReposition, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedReposition, self).RemoveEffect(character)


class ImprovedSecondChance(Feat):

    def __init__(self, data=None):
        super(ImprovedSecondChance, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedSecondChance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedSecondChance, self).RemoveEffect(character)


class ImprovedShareSpells(Feat):

    def __init__(self, data=None):
        super(ImprovedShareSpells, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedShareSpells, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedShareSpells, self).RemoveEffect(character)


class ImprovedSidestep(Feat):

    def __init__(self, data=None):
        super(ImprovedSidestep, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedSidestep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedSidestep, self).RemoveEffect(character)


class ImprovedSteal(Feat):

    def __init__(self, data=None):
        super(ImprovedSteal, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedSteal, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedSteal, self).RemoveEffect(character)


class ImprovedStonecunning(Feat):

    def __init__(self, data=None):
        super(ImprovedStonecunning, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedStonecunning, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedStonecunning, self).RemoveEffect(character)


class IntensifiedSpell(Feat):

    def __init__(self, data=None):
        super(IntensifiedSpell, self).__init__(data)

    def AddEffect(self, character):
        super(IntensifiedSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(IntensifiedSpell, self).RemoveEffect(character)


class InHarmSWay(Feat):

    def __init__(self, data=None):
        super(InHarmSWay, self).__init__(data)

    def AddEffect(self, character):
        super(InHarmSWay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InHarmSWay, self).RemoveEffect(character)


class Ironguts(Feat):

    def __init__(self, data=None):
        super(Ironguts, self).__init__(data)

    def AddEffect(self, character):
        super(Ironguts, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Ironguts, self).RemoveEffect(character)


class Ironhide(Feat):

    def __init__(self, data=None):
        super(Ironhide, self).__init__(data)

    def AddEffect(self, character):
        super(Ironhide, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Ironhide, self).RemoveEffect(character)


class KeenScent(Feat):

    def __init__(self, data=None):
        super(KeenScent, self).__init__(data)

    def AddEffect(self, character):
        super(KeenScent, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KeenScent, self).RemoveEffect(character)


class KiThrow(Feat):

    def __init__(self, data=None):
        super(KiThrow, self).__init__(data)

    def AddEffect(self, character):
        super(KiThrow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KiThrow, self).RemoveEffect(character)


class LeafSinger(Feat):

    def __init__(self, data=None):
        super(LeafSinger, self).__init__(data)

    def AddEffect(self, character):
        super(LeafSinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LeafSinger, self).RemoveEffect(character)


class LightStep(Feat):

    def __init__(self, data=None):
        super(LightStep, self).__init__(data)

    def AddEffect(self, character):
        super(LightStep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LightStep, self).RemoveEffect(character)


class LingeringPerformance(Feat):

    def __init__(self, data=None):
        super(LingeringPerformance, self).__init__(data)

    def AddEffect(self, character):
        super(LingeringPerformance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LingeringPerformance, self).RemoveEffect(character)


class LingeringSpell(Feat):

    def __init__(self, data=None):
        super(LingeringSpell, self).__init__(data)

    def AddEffect(self, character):
        super(LingeringSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LingeringSpell, self).RemoveEffect(character)


class Lookout(Feat):

    def __init__(self, data=None):
        super(Lookout, self).__init__(data)

    def AddEffect(self, character):
        super(Lookout, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Lookout, self).RemoveEffect(character)


class LowProfile(Feat):

    def __init__(self, data=None):
        super(LowProfile, self).__init__(data)

    def AddEffect(self, character):
        super(LowProfile, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LowProfile, self).RemoveEffect(character)


class LuckyHalfling(Feat):

    def __init__(self, data=None):
        super(LuckyHalfling, self).__init__(data)

    def AddEffect(self, character):
        super(LuckyHalfling, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LuckyHalfling, self).RemoveEffect(character)


class MajorSpellExpertise(Feat):

    def __init__(self, data=None):
        super(MajorSpellExpertise, self).__init__(data)

    def AddEffect(self, character):
        super(MajorSpellExpertise, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MajorSpellExpertise, self).RemoveEffect(character)


class MasterAlchemist(Feat):

    def __init__(self, data=None):
        super(MasterAlchemist, self).__init__(data)

    def AddEffect(self, character):
        super(MasterAlchemist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MasterAlchemist, self).RemoveEffect(character)


class MercifulSpell(Feat):

    def __init__(self, data=None):
        super(MercifulSpell, self).__init__(data)

    def AddEffect(self, character):
        super(MercifulSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MercifulSpell, self).RemoveEffect(character)


class MinorSpellExpertise(Feat):

    def __init__(self, data=None):
        super(MinorSpellExpertise, self).__init__(data)

    def AddEffect(self, character):
        super(MinorSpellExpertise, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MinorSpellExpertise, self).RemoveEffect(character)


class MissileShield(Feat):

    def __init__(self, data=None):
        super(MissileShield, self).__init__(data)

    def AddEffect(self, character):
        super(MissileShield, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MissileShield, self).RemoveEffect(character)


class MountedShield(Feat):

    def __init__(self, data=None):
        super(MountedShield, self).__init__(data)

    def AddEffect(self, character):
        super(MountedShield, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MountedShield, self).RemoveEffect(character)


class MountedSkirmisher(Feat):

    def __init__(self, data=None):
        super(MountedSkirmisher, self).__init__(data)

    def AddEffect(self, character):
        super(MountedSkirmisher, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MountedSkirmisher, self).RemoveEffect(character)


class Outflank(Feat):

    def __init__(self, data=None):
        super(Outflank, self).__init__(data)

    def AddEffect(self, character):
        super(Outflank, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Outflank, self).RemoveEffect(character)


class PairedOpportunists(Feat):

    def __init__(self, data=None):
        super(PairedOpportunists, self).__init__(data)

    def AddEffect(self, character):
        super(PairedOpportunists, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PairedOpportunists, self).RemoveEffect(character)


class ParrySpell(Feat):

    def __init__(self, data=None):
        super(ParrySpell, self).__init__(data)

    def AddEffect(self, character):
        super(ParrySpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ParrySpell, self).RemoveEffect(character)


class PartingShot(Feat):

    def __init__(self, data=None):
        super(PartingShot, self).__init__(data)

    def AddEffect(self, character):
        super(PartingShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PartingShot, self).RemoveEffect(character)


class PassForHuman(Feat):

    def __init__(self, data=None):
        super(PassForHuman, self).__init__(data)

    def AddEffect(self, character):
        super(PassForHuman, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PassForHuman, self).RemoveEffect(character)


class PerfectStrike(Feat):

    def __init__(self, data=None):
        super(PerfectStrike, self).__init__(data)

    def AddEffect(self, character):
        super(PerfectStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PerfectStrike, self).RemoveEffect(character)


class PersistentSpell(Feat):

    def __init__(self, data=None):
        super(PersistentSpell, self).__init__(data)

    def AddEffect(self, character):
        super(PersistentSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PersistentSpell, self).RemoveEffect(character)


class PointBlankMaster(Feat):

    def __init__(self, data=None):
        super(PointBlankMaster, self).__init__(data)

    def AddEffect(self, character):
        super(PointBlankMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PointBlankMaster, self).RemoveEffect(character)


class PracticedTactician(Feat):

    def __init__(self, data=None):
        super(PracticedTactician, self).__init__(data)

    def AddEffect(self, character):
        super(PracticedTactician, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PracticedTactician, self).RemoveEffect(character)


class PreciseStrike(Feat):

    def __init__(self, data=None):
        super(PreciseStrike, self).__init__(data)

    def AddEffect(self, character):
        super(PreciseStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PreciseStrike, self).RemoveEffect(character)


class PreferredSpell(Feat):

    def __init__(self, data=None):
        super(PreferredSpell, self).__init__(data)

    def AddEffect(self, character):
        super(PreferredSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PreferredSpell, self).RemoveEffect(character)


class PunishingKick(Feat):

    def __init__(self, data=None):
        super(PunishingKick, self).__init__(data)

    def AddEffect(self, character):
        super(PunishingKick, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PunishingKick, self).RemoveEffect(character)


class PushingAssault(Feat):

    def __init__(self, data=None):
        super(PushingAssault, self).__init__(data)

    def AddEffect(self, character):
        super(PushingAssault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PushingAssault, self).RemoveEffect(character)


class RacialHeritage(Feat):

    def __init__(self, data=None):
        super(RacialHeritage, self).__init__(data)

    def AddEffect(self, character):
        super(RacialHeritage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RacialHeritage, self).RemoveEffect(character)


class RagingVitality(Feat):

    def __init__(self, data=None):
        super(RagingVitality, self).__init__(data)

    def AddEffect(self, character):
        super(RagingVitality, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RagingVitality, self).RemoveEffect(character)


class RayShield(Feat):

    def __init__(self, data=None):
        super(RayShield, self).__init__(data)

    def AddEffect(self, character):
        super(RayShield, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RayShield, self).RemoveEffect(character)


class Razortusk(Feat):

    def __init__(self, data=None):
        super(Razortusk, self).__init__(data)

    def AddEffect(self, character):
        super(Razortusk, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Razortusk, self).RemoveEffect(character)


class ReachSpell(Feat):

    def __init__(self, data=None):
        super(ReachSpell, self).__init__(data)

    def AddEffect(self, character):
        super(ReachSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ReachSpell, self).RemoveEffect(character)


class RendingClaws(Feat):

    def __init__(self, data=None):
        super(RendingClaws, self).__init__(data)

    def AddEffect(self, character):
        super(RendingClaws, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RendingClaws, self).RemoveEffect(character)


class RepositioningStrike(Feat):

    def __init__(self, data=None):
        super(RepositioningStrike, self).__init__(data)

    def AddEffect(self, character):
        super(RepositioningStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RepositioningStrike, self).RemoveEffect(character)


class SavingShield(Feat):

    def __init__(self, data=None):
        super(SavingShield, self).__init__(data)

    def AddEffect(self, character):
        super(SavingShield, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SavingShield, self).RemoveEffect(character)


class SecondChance(Feat):

    def __init__(self, data=None):
        super(SecondChance, self).__init__(data)

    def AddEffect(self, character):
        super(SecondChance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SecondChance, self).RemoveEffect(character)


class SelectiveSpell(Feat):

    def __init__(self, data=None):
        super(SelectiveSpell, self).__init__(data)

    def AddEffect(self, character):
        super(SelectiveSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SelectiveSpell, self).RemoveEffect(character)


class ShadowStrike(Feat):

    def __init__(self, data=None):
        super(ShadowStrike, self).__init__(data)

    def AddEffect(self, character):
        super(ShadowStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadowStrike, self).RemoveEffect(character)


class SharedInsight(Feat):

    def __init__(self, data=None):
        super(SharedInsight, self).__init__(data)

    def AddEffect(self, character):
        super(SharedInsight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SharedInsight, self).RemoveEffect(character)


class SharpSenses(Feat):

    def __init__(self, data=None):
        super(SharpSenses, self).__init__(data)

    def AddEffect(self, character):
        super(SharpSenses, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SharpSenses, self).RemoveEffect(character)


class ShieldOfSwings(Feat):

    def __init__(self, data=None):
        super(ShieldOfSwings, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldOfSwings, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldOfSwings, self).RemoveEffect(character)


class ShieldSpecialization(Feat):

    def __init__(self, data=None):
        super(ShieldSpecialization, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldSpecialization, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldSpecialization, self).RemoveEffect(character)


class ShieldWall(Feat):

    def __init__(self, data=None):
        super(ShieldWall, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldWall, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldWall, self).RemoveEffect(character)


class ShieldedCaster(Feat):

    def __init__(self, data=None):
        super(ShieldedCaster, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldedCaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldedCaster, self).RemoveEffect(character)


class SickeningSpell(Feat):

    def __init__(self, data=None):
        super(SickeningSpell, self).__init__(data)

    def AddEffect(self, character):
        super(SickeningSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SickeningSpell, self).RemoveEffect(character)


class Sidestep(Feat):

    def __init__(self, data=None):
        super(Sidestep, self).__init__(data)

    def AddEffect(self, character):
        super(Sidestep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Sidestep, self).RemoveEffect(character)


class Smash(Feat):

    def __init__(self, data=None):
        super(Smash, self).__init__(data)

    def AddEffect(self, character):
        super(Smash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Smash, self).RemoveEffect(character)


class SmellFear(Feat):

    def __init__(self, data=None):
        super(SmellFear, self).__init__(data)

    def AddEffect(self, character):
        super(SmellFear, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SmellFear, self).RemoveEffect(character)


class Sociable(Feat):

    def __init__(self, data=None):
        super(Sociable, self).__init__(data)

    def AddEffect(self, character):
        super(Sociable, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Sociable, self).RemoveEffect(character)


class SpellPerfection(Feat):

    def __init__(self, data=None):
        super(SpellPerfection, self).__init__(data)

    def AddEffect(self, character):
        super(SpellPerfection, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellPerfection, self).RemoveEffect(character)


class SpiderStep(Feat):

    def __init__(self, data=None):
        super(SpiderStep, self).__init__(data)

    def AddEffect(self, character):
        super(SpiderStep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpiderStep, self).RemoveEffect(character)


class StabbingShot(Feat):

    def __init__(self, data=None):
        super(StabbingShot, self).__init__(data)

    def AddEffect(self, character):
        super(StabbingShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StabbingShot, self).RemoveEffect(character)


class SteelSoul(Feat):

    def __init__(self, data=None):
        super(SteelSoul, self).__init__(data)

    def AddEffect(self, character):
        super(SteelSoul, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SteelSoul, self).RemoveEffect(character)


class StepUpAndStrike(Feat):

    def __init__(self, data=None):
        super(StepUpAndStrike, self).__init__(data)

    def AddEffect(self, character):
        super(StepUpAndStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StepUpAndStrike, self).RemoveEffect(character)


class StoneFaced(Feat):

    def __init__(self, data=None):
        super(StoneFaced, self).__init__(data)

    def AddEffect(self, character):
        super(StoneFaced, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StoneFaced, self).RemoveEffect(character)


class StoneSense(Feat):

    def __init__(self, data=None):
        super(StoneSense, self).__init__(data)

    def AddEffect(self, character):
        super(StoneSense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StoneSense, self).RemoveEffect(character)


class StoneSinger(Feat):

    def __init__(self, data=None):
        super(StoneSinger, self).__init__(data)

    def AddEffect(self, character):
        super(StoneSinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StoneSinger, self).RemoveEffect(character)


class StunningAssault(Feat):

    def __init__(self, data=None):
        super(StunningAssault, self).__init__(data)

    def AddEffect(self, character):
        super(StunningAssault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StunningAssault, self).RemoveEffect(character)


class SummonerSCall(Feat):

    def __init__(self, data=None):
        super(SummonerSCall, self).__init__(data)

    def AddEffect(self, character):
        super(SummonerSCall, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SummonerSCall, self).RemoveEffect(character)


class SunderingStrike(Feat):

    def __init__(self, data=None):
        super(SunderingStrike, self).__init__(data)

    def AddEffect(self, character):
        super(SunderingStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SunderingStrike, self).RemoveEffect(character)


class SwapPlaces(Feat):

    def __init__(self, data=None):
        super(SwapPlaces, self).__init__(data)

    def AddEffect(self, character):
        super(SwapPlaces, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SwapPlaces, self).RemoveEffect(character)


class SwiftAid(Feat):

    def __init__(self, data=None):
        super(SwiftAid, self).__init__(data)

    def AddEffect(self, character):
        super(SwiftAid, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SwiftAid, self).RemoveEffect(character)


class Taunt(Feat):

    def __init__(self, data=None):
        super(Taunt, self).__init__(data)

    def AddEffect(self, character):
        super(Taunt, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Taunt, self).RemoveEffect(character)


class TeamUp(Feat):

    def __init__(self, data=None):
        super(TeamUp, self).__init__(data)

    def AddEffect(self, character):
        super(TeamUp, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TeamUp, self).RemoveEffect(character)


class TeleportTactician(Feat):

    def __init__(self, data=None):
        super(TeleportTactician, self).__init__(data)

    def AddEffect(self, character):
        super(TeleportTactician, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TeleportTactician, self).RemoveEffect(character)


class TenaciousTransmutation(Feat):

    def __init__(self, data=None):
        super(TenaciousTransmutation, self).__init__(data)

    def AddEffect(self, character):
        super(TenaciousTransmutation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TenaciousTransmutation, self).RemoveEffect(character)


class ThunderingSpell(Feat):

    def __init__(self, data=None):
        super(ThunderingSpell, self).__init__(data)

    def AddEffect(self, character):
        super(ThunderingSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThunderingSpell, self).RemoveEffect(character)


class TouchOfSerenity(Feat):

    def __init__(self, data=None):
        super(TouchOfSerenity, self).__init__(data)

    def AddEffect(self, character):
        super(TouchOfSerenity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TouchOfSerenity, self).RemoveEffect(character)


class TrickRiding(Feat):

    def __init__(self, data=None):
        super(TrickRiding, self).__init__(data)

    def AddEffect(self, character):
        super(TrickRiding, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TrickRiding, self).RemoveEffect(character)


class TrippingStrike(Feat):

    def __init__(self, data=None):
        super(TrippingStrike, self).__init__(data)

    def AddEffect(self, character):
        super(TrippingStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TrippingStrike, self).RemoveEffect(character)


class UnderAndOver(Feat):

    def __init__(self, data=None):
        super(UnderAndOver, self).__init__(data)

    def AddEffect(self, character):
        super(UnderAndOver, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UnderAndOver, self).RemoveEffect(character)


class Underfoot(Feat):

    def __init__(self, data=None):
        super(Underfoot, self).__init__(data)

    def AddEffect(self, character):
        super(Underfoot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Underfoot, self).RemoveEffect(character)


class VerminHeart(Feat):

    def __init__(self, data=None):
        super(VerminHeart, self).__init__(data)

    def AddEffect(self, character):
        super(VerminHeart, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VerminHeart, self).RemoveEffect(character)


class WarSinger(Feat):

    def __init__(self, data=None):
        super(WarSinger, self).__init__(data)

    def AddEffect(self, character):
        super(WarSinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WarSinger, self).RemoveEffect(character)


class WellPrepared(Feat):

    def __init__(self, data=None):
        super(WellPrepared, self).__init__(data)

    def AddEffect(self, character):
        super(WellPrepared, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WellPrepared, self).RemoveEffect(character)


class AdderStrike(Feat):

    def __init__(self, data=None):
        super(AdderStrike, self).__init__(data)

    def AddEffect(self, character):
        super(AdderStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AdderStrike, self).RemoveEffect(character)


class AdeptChampion(Feat):

    def __init__(self, data=None):
        super(AdeptChampion, self).__init__(data)

    def AddEffect(self, character):
        super(AdeptChampion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AdeptChampion, self).RemoveEffect(character)


class AmateurGunslinger(Feat):

    def __init__(self, data=None):
        super(AmateurGunslinger, self).__init__(data)

    def AddEffect(self, character):
        super(AmateurGunslinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AmateurGunslinger, self).RemoveEffect(character)


class ArcSlinger(Feat):

    def __init__(self, data=None):
        super(ArcSlinger, self).__init__(data)

    def AddEffect(self, character):
        super(ArcSlinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcSlinger, self).RemoveEffect(character)


class BackToBack(Feat):

    def __init__(self, data=None):
        super(BackToBack, self).__init__(data)

    def AddEffect(self, character):
        super(BackToBack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BackToBack, self).RemoveEffect(character)


class Betrayer(Feat):

    def __init__(self, data=None):
        super(Betrayer, self).__init__(data)

    def AddEffect(self, character):
        super(Betrayer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Betrayer, self).RemoveEffect(character)


class BindingThrow(Feat):

    def __init__(self, data=None):
        super(BindingThrow, self).__init__(data)

    def AddEffect(self, character):
        super(BindingThrow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BindingThrow, self).RemoveEffect(character)


class Bludgeoner(Feat):

    def __init__(self, data=None):
        super(Bludgeoner, self).__init__(data)

    def AddEffect(self, character):
        super(Bludgeoner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Bludgeoner, self).RemoveEffect(character)


class BoarFerocity(Feat):

    def __init__(self, data=None):
        super(BoarFerocity, self).__init__(data)

    def AddEffect(self, character):
        super(BoarFerocity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BoarFerocity, self).RemoveEffect(character)


class BoarShred(Feat):

    def __init__(self, data=None):
        super(BoarShred, self).__init__(data)

    def AddEffect(self, character):
        super(BoarShred, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BoarShred, self).RemoveEffect(character)


class BoarStyle(Feat):

    def __init__(self, data=None):
        super(BoarStyle, self).__init__(data)

    def AddEffect(self, character):
        super(BoarStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BoarStyle, self).RemoveEffect(character)


class BodyShield(Feat):

    def __init__(self, data=None):
        super(BodyShield, self).__init__(data)

    def AddEffect(self, character):
        super(BodyShield, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BodyShield, self).RemoveEffect(character)


class BolsteredResilience(Feat):

    def __init__(self, data=None):
        super(BolsteredResilience, self).__init__(data)

    def AddEffect(self, character):
        super(BolsteredResilience, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BolsteredResilience, self).RemoveEffect(character)


class Bonebreaker(Feat):

    def __init__(self, data=None):
        super(Bonebreaker, self).__init__(data)

    def AddEffect(self, character):
        super(Bonebreaker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Bonebreaker, self).RemoveEffect(character)


class BrandedForRetribution(Feat):

    def __init__(self, data=None):
        super(BrandedForRetribution, self).__init__(data)

    def AddEffect(self, character):
        super(BrandedForRetribution, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BrandedForRetribution, self).RemoveEffect(character)


class BreakGuard(Feat):

    def __init__(self, data=None):
        super(BreakGuard, self).__init__(data)

    def AddEffect(self, character):
        super(BreakGuard, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BreakGuard, self).RemoveEffect(character)


class BrokenWingGambit(Feat):

    def __init__(self, data=None):
        super(BrokenWingGambit, self).__init__(data)

    def AddEffect(self, character):
        super(BrokenWingGambit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BrokenWingGambit, self).RemoveEffect(character)


class CartwheelDodge(Feat):

    def __init__(self, data=None):
        super(CartwheelDodge, self).__init__(data)

    def AddEffect(self, character):
        super(CartwheelDodge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CartwheelDodge, self).RemoveEffect(character)


class CavalryFormation(Feat):

    def __init__(self, data=None):
        super(CavalryFormation, self).__init__(data)

    def AddEffect(self, character):
        super(CavalryFormation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CavalryFormation, self).RemoveEffect(character)


class ChanneledRevival(Feat):

    def __init__(self, data=None):
        super(ChanneledRevival, self).__init__(data)

    def AddEffect(self, character):
        super(ChanneledRevival, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ChanneledRevival, self).RemoveEffect(character)


class ChannelingScourge(Feat):

    def __init__(self, data=None):
        super(ChannelingScourge, self).__init__(data)

    def AddEffect(self, character):
        super(ChannelingScourge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ChannelingScourge, self).RemoveEffect(character)


class ChargingHurler(Feat):

    def __init__(self, data=None):
        super(ChargingHurler, self).__init__(data)

    def AddEffect(self, character):
        super(ChargingHurler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ChargingHurler, self).RemoveEffect(character)


class Chokehold(Feat):

    def __init__(self, data=None):
        super(Chokehold, self).__init__(data)

    def AddEffect(self, character):
        super(Chokehold, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Chokehold, self).RemoveEffect(character)


class CleavingFinish(Feat):

    def __init__(self, data=None):
        super(CleavingFinish, self).__init__(data)

    def AddEffect(self, character):
        super(CleavingFinish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CleavingFinish, self).RemoveEffect(character)


class CloseQuartersThrower(Feat):

    def __init__(self, data=None):
        super(CloseQuartersThrower, self).__init__(data)

    def AddEffect(self, character):
        super(CloseQuartersThrower, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CloseQuartersThrower, self).RemoveEffect(character)


class ClusteredShots(Feat):

    def __init__(self, data=None):
        super(ClusteredShots, self).__init__(data)

    def AddEffect(self, character):
        super(ClusteredShots, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ClusteredShots, self).RemoveEffect(character)


class CombatMedic(Feat):

    def __init__(self, data=None):
        super(CombatMedic, self).__init__(data)

    def AddEffect(self, character):
        super(CombatMedic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CombatMedic, self).RemoveEffect(character)


class CombatStyleMaster(Feat):

    def __init__(self, data=None):
        super(CombatStyleMaster, self).__init__(data)

    def AddEffect(self, character):
        super(CombatStyleMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CombatStyleMaster, self).RemoveEffect(character)


class ContingentChanneling(Feat):

    def __init__(self, data=None):
        super(ContingentChanneling, self).__init__(data)

    def AddEffect(self, character):
        super(ContingentChanneling, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ContingentChanneling, self).RemoveEffect(character)


class CoordinatedCharge(Feat):

    def __init__(self, data=None):
        super(CoordinatedCharge, self).__init__(data)

    def AddEffect(self, character):
        super(CoordinatedCharge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CoordinatedCharge, self).RemoveEffect(character)


class CraneRiposte(Feat):

    def __init__(self, data=None):
        super(CraneRiposte, self).__init__(data)

    def AddEffect(self, character):
        super(CraneRiposte, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraneRiposte, self).RemoveEffect(character)


class CraneStyle(Feat):

    def __init__(self, data=None):
        super(CraneStyle, self).__init__(data)

    def AddEffect(self, character):
        super(CraneStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraneStyle, self).RemoveEffect(character)


class CraneWing(Feat):

    def __init__(self, data=None):
        super(CraneWing, self).__init__(data)

    def AddEffect(self, character):
        super(CraneWing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CraneWing, self).RemoveEffect(character)


class CrusaderSFist(Feat):

    def __init__(self, data=None):
        super(CrusaderSFist, self).__init__(data)

    def AddEffect(self, character):
        super(CrusaderSFist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CrusaderSFist, self).RemoveEffect(character)


class CrusaderSFlurry(Feat):

    def __init__(self, data=None):
        super(CrusaderSFlurry, self).__init__(data)

    def AddEffect(self, character):
        super(CrusaderSFlurry, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CrusaderSFlurry, self).RemoveEffect(character)


class CrushingBlow(Feat):

    def __init__(self, data=None):
        super(CrushingBlow, self).__init__(data)

    def AddEffect(self, character):
        super(CrushingBlow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CrushingBlow, self).RemoveEffect(character)


class DeadlyFinish(Feat):

    def __init__(self, data=None):
        super(DeadlyFinish, self).__init__(data)

    def AddEffect(self, character):
        super(DeadlyFinish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeadlyFinish, self).RemoveEffect(character)


class DeathFromAbove(Feat):

    def __init__(self, data=None):
        super(DeathFromAbove, self).__init__(data)

    def AddEffect(self, character):
        super(DeathFromAbove, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeathFromAbove, self).RemoveEffect(character)


class DeathOrGlory(Feat):

    def __init__(self, data=None):
        super(DeathOrGlory, self).__init__(data)

    def AddEffect(self, character):
        super(DeathOrGlory, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeathOrGlory, self).RemoveEffect(character)


class DeathlessInitiate(Feat):

    def __init__(self, data=None):
        super(DeathlessInitiate, self).__init__(data)

    def AddEffect(self, character):
        super(DeathlessInitiate, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeathlessInitiate, self).RemoveEffect(character)


class DeathlessMaster(Feat):

    def __init__(self, data=None):
        super(DeathlessMaster, self).__init__(data)

    def AddEffect(self, character):
        super(DeathlessMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeathlessMaster, self).RemoveEffect(character)


class DeathlessZealot(Feat):

    def __init__(self, data=None):
        super(DeathlessZealot, self).__init__(data)

    def AddEffect(self, character):
        super(DeathlessZealot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeathlessZealot, self).RemoveEffect(character)


class DeceptiveExchange(Feat):

    def __init__(self, data=None):
        super(DeceptiveExchange, self).__init__(data)

    def AddEffect(self, character):
        super(DeceptiveExchange, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeceptiveExchange, self).RemoveEffect(character)


class DefensiveWeaponTraining(Feat):

    def __init__(self, data=None):
        super(DefensiveWeaponTraining, self).__init__(data)

    def AddEffect(self, character):
        super(DefensiveWeaponTraining, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DefensiveWeaponTraining, self).RemoveEffect(character)


class DeftShootistDeed(Feat):

    def __init__(self, data=None):
        super(DeftShootistDeed, self).__init__(data)

    def AddEffect(self, character):
        super(DeftShootistDeed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeftShootistDeed, self).RemoveEffect(character)


class DestructiveDispel(Feat):

    def __init__(self, data=None):
        super(DestructiveDispel, self).__init__(data)

    def AddEffect(self, character):
        super(DestructiveDispel, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DestructiveDispel, self).RemoveEffect(character)


class DevastatingStrike(Feat):

    def __init__(self, data=None):
        super(DevastatingStrike, self).__init__(data)

    def AddEffect(self, character):
        super(DevastatingStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DevastatingStrike, self).RemoveEffect(character)


class DimensionalAgility(Feat):

    def __init__(self, data=None):
        super(DimensionalAgility, self).__init__(data)

    def AddEffect(self, character):
        super(DimensionalAgility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DimensionalAgility, self).RemoveEffect(character)


class DimensionalAssault(Feat):

    def __init__(self, data=None):
        super(DimensionalAssault, self).__init__(data)

    def AddEffect(self, character):
        super(DimensionalAssault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DimensionalAssault, self).RemoveEffect(character)


class DimensionalDervish(Feat):

    def __init__(self, data=None):
        super(DimensionalDervish, self).__init__(data)

    def AddEffect(self, character):
        super(DimensionalDervish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DimensionalDervish, self).RemoveEffect(character)


class DimensionalManeuvers(Feat):

    def __init__(self, data=None):
        super(DimensionalManeuvers, self).__init__(data)

    def AddEffect(self, character):
        super(DimensionalManeuvers, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DimensionalManeuvers, self).RemoveEffect(character)


class DimensionalSavant(Feat):

    def __init__(self, data=None):
        super(DimensionalSavant, self).__init__(data)

    def AddEffect(self, character):
        super(DimensionalSavant, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DimensionalSavant, self).RemoveEffect(character)


class DiscordantVoice(Feat):

    def __init__(self, data=None):
        super(DiscordantVoice, self).__init__(data)

    def AddEffect(self, character):
        super(DiscordantVoice, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DiscordantVoice, self).RemoveEffect(character)


class DisengagingFeint(Feat):

    def __init__(self, data=None):
        super(DisengagingFeint, self).__init__(data)

    def AddEffect(self, character):
        super(DisengagingFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisengagingFeint, self).RemoveEffect(character)


class DisengagingFlourish(Feat):

    def __init__(self, data=None):
        super(DisengagingFlourish, self).__init__(data)

    def AddEffect(self, character):
        super(DisengagingFlourish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisengagingFlourish, self).RemoveEffect(character)


class DisengagingShot(Feat):

    def __init__(self, data=None):
        super(DisengagingShot, self).__init__(data)

    def AddEffect(self, character):
        super(DisengagingShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisengagingShot, self).RemoveEffect(character)


class DisorientingManeuver(Feat):

    def __init__(self, data=None):
        super(DisorientingManeuver, self).__init__(data)

    def AddEffect(self, character):
        super(DisorientingManeuver, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisorientingManeuver, self).RemoveEffect(character)


class DispelSynergy(Feat):

    def __init__(self, data=None):
        super(DispelSynergy, self).__init__(data)

    def AddEffect(self, character):
        super(DispelSynergy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DispelSynergy, self).RemoveEffect(character)


class DispellingCritical(Feat):

    def __init__(self, data=None):
        super(DispellingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(DispellingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DispellingCritical, self).RemoveEffect(character)


class DispellingFist(Feat):

    def __init__(self, data=None):
        super(DispellingFist, self).__init__(data)

    def AddEffect(self, character):
        super(DispellingFist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DispellingFist, self).RemoveEffect(character)


class DisposableWeapon(Feat):

    def __init__(self, data=None):
        super(DisposableWeapon, self).__init__(data)

    def AddEffect(self, character):
        super(DisposableWeapon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisposableWeapon, self).RemoveEffect(character)


class DisruptiveRecall(Feat):

    def __init__(self, data=None):
        super(DisruptiveRecall, self).__init__(data)

    def AddEffect(self, character):
        super(DisruptiveRecall, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisruptiveRecall, self).RemoveEffect(character)


class DistanceThrower(Feat):

    def __init__(self, data=None):
        super(DistanceThrower, self).__init__(data)

    def AddEffect(self, character):
        super(DistanceThrower, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DistanceThrower, self).RemoveEffect(character)


class DjinniSpin(Feat):

    def __init__(self, data=None):
        super(DjinniSpin, self).__init__(data)

    def AddEffect(self, character):
        super(DjinniSpin, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DjinniSpin, self).RemoveEffect(character)


class DjinniSpirit(Feat):

    def __init__(self, data=None):
        super(DjinniSpirit, self).__init__(data)

    def AddEffect(self, character):
        super(DjinniSpirit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DjinniSpirit, self).RemoveEffect(character)


class DjinniStyle(Feat):

    def __init__(self, data=None):
        super(DjinniStyle, self).__init__(data)

    def AddEffect(self, character):
        super(DjinniStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DjinniStyle, self).RemoveEffect(character)


class DomainStrike(Feat):

    def __init__(self, data=None):
        super(DomainStrike, self).__init__(data)

    def AddEffect(self, character):
        super(DomainStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DomainStrike, self).RemoveEffect(character)


class DoubleBane(Feat):

    def __init__(self, data=None):
        super(DoubleBane, self).__init__(data)

    def AddEffect(self, character):
        super(DoubleBane, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DoubleBane, self).RemoveEffect(character)


class DragDown(Feat):

    def __init__(self, data=None):
        super(DragDown, self).__init__(data)

    def AddEffect(self, character):
        super(DragDown, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DragDown, self).RemoveEffect(character)


class DragonFerocity(Feat):

    def __init__(self, data=None):
        super(DragonFerocity, self).__init__(data)

    def AddEffect(self, character):
        super(DragonFerocity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DragonFerocity, self).RemoveEffect(character)


class DragonRoar(Feat):

    def __init__(self, data=None):
        super(DragonRoar, self).__init__(data)

    def AddEffect(self, character):
        super(DragonRoar, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DragonRoar, self).RemoveEffect(character)


class DragonStyle(Feat):

    def __init__(self, data=None):
        super(DragonStyle, self).__init__(data)

    def AddEffect(self, character):
        super(DragonStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DragonStyle, self).RemoveEffect(character)


class DramaticDisplay(Feat):

    def __init__(self, data=None):
        super(DramaticDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(DramaticDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DramaticDisplay, self).RemoveEffect(character)


class EarthChildBinder(Feat):

    def __init__(self, data=None):
        super(EarthChildBinder, self).__init__(data)

    def AddEffect(self, character):
        super(EarthChildBinder, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EarthChildBinder, self).RemoveEffect(character)


class EarthChildStyle(Feat):

    def __init__(self, data=None):
        super(EarthChildStyle, self).__init__(data)

    def AddEffect(self, character):
        super(EarthChildStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EarthChildStyle, self).RemoveEffect(character)


class EarthChildTopple(Feat):

    def __init__(self, data=None):
        super(EarthChildTopple, self).__init__(data)

    def AddEffect(self, character):
        super(EarthChildTopple, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EarthChildTopple, self).RemoveEffect(character)


class EfreetiStance(Feat):

    def __init__(self, data=None):
        super(EfreetiStance, self).__init__(data)

    def AddEffect(self, character):
        super(EfreetiStance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EfreetiStance, self).RemoveEffect(character)


class EfreetiStyle(Feat):

    def __init__(self, data=None):
        super(EfreetiStyle, self).__init__(data)

    def AddEffect(self, character):
        super(EfreetiStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EfreetiStyle, self).RemoveEffect(character)


class EfreetiTouch(Feat):

    def __init__(self, data=None):
        super(EfreetiTouch, self).__init__(data)

    def AddEffect(self, character):
        super(EfreetiTouch, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EfreetiTouch, self).RemoveEffect(character)


class ElusiveRedirection(Feat):

    def __init__(self, data=None):
        super(ElusiveRedirection, self).__init__(data)

    def AddEffect(self, character):
        super(ElusiveRedirection, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElusiveRedirection, self).RemoveEffect(character)


class EnfiladingFire(Feat):

    def __init__(self, data=None):
        super(EnfiladingFire, self).__init__(data)

    def AddEffect(self, character):
        super(EnfiladingFire, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EnfiladingFire, self).RemoveEffect(character)


class EscapeRoute(Feat):

    def __init__(self, data=None):
        super(EscapeRoute, self).__init__(data)

    def AddEffect(self, character):
        super(EscapeRoute, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EscapeRoute, self).RemoveEffect(character)


class ExpertDriver(Feat):

    def __init__(self, data=None):
        super(ExpertDriver, self).__init__(data)

    def AddEffect(self, character):
        super(ExpertDriver, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExpertDriver, self).RemoveEffect(character)


class ExtraBane(Feat):

    def __init__(self, data=None):
        super(ExtraBane, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraBane, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraBane, self).RemoveEffect(character)


class ExtraGrit(Feat):

    def __init__(self, data=None):
        super(ExtraGrit, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraGrit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraGrit, self).RemoveEffect(character)


class FalseOpening(Feat):

    def __init__(self, data=None):
        super(FalseOpening, self).__init__(data)

    def AddEffect(self, character):
        super(FalseOpening, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FalseOpening, self).RemoveEffect(character)


class FeintPartner(Feat):

    def __init__(self, data=None):
        super(FeintPartner, self).__init__(data)

    def AddEffect(self, character):
        super(FeintPartner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FeintPartner, self).RemoveEffect(character)


class FellingEscape(Feat):

    def __init__(self, data=None):
        super(FellingEscape, self).__init__(data)

    def AddEffect(self, character):
        super(FellingEscape, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FellingEscape, self).RemoveEffect(character)


class FellingSmash(Feat):

    def __init__(self, data=None):
        super(FellingSmash, self).__init__(data)

    def AddEffect(self, character):
        super(FellingSmash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FellingSmash, self).RemoveEffect(character)


class FeralCombatTraining(Feat):

    def __init__(self, data=None):
        super(FeralCombatTraining, self).__init__(data)

    def AddEffect(self, character):
        super(FeralCombatTraining, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FeralCombatTraining, self).RemoveEffect(character)


class FieldRepair(Feat):

    def __init__(self, data=None):
        super(FieldRepair, self).__init__(data)

    def AddEffect(self, character):
        super(FieldRepair, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FieldRepair, self).RemoveEffect(character)


class FinalEmbrace(Feat):

    def __init__(self, data=None):
        super(FinalEmbrace, self).__init__(data)

    def AddEffect(self, character):
        super(FinalEmbrace, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FinalEmbrace, self).RemoveEffect(character)


class FinalEmbraceHorror(Feat):

    def __init__(self, data=None):
        super(FinalEmbraceHorror, self).__init__(data)

    def AddEffect(self, character):
        super(FinalEmbraceHorror, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FinalEmbraceHorror, self).RemoveEffect(character)


class FinalEmbraceMaster(Feat):

    def __init__(self, data=None):
        super(FinalEmbraceMaster, self).__init__(data)

    def AddEffect(self, character):
        super(FinalEmbraceMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FinalEmbraceMaster, self).RemoveEffect(character)


class FlankingFoil(Feat):

    def __init__(self, data=None):
        super(FlankingFoil, self).__init__(data)

    def AddEffect(self, character):
        super(FlankingFoil, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FlankingFoil, self).RemoveEffect(character)


class FortifiedArmorTraining(Feat):

    def __init__(self, data=None):
        super(FortifiedArmorTraining, self).__init__(data)

    def AddEffect(self, character):
        super(FortifiedArmorTraining, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FortifiedArmorTraining, self).RemoveEffect(character)


class FuriousFinish(Feat):

    def __init__(self, data=None):
        super(FuriousFinish, self).__init__(data)

    def AddEffect(self, character):
        super(FuriousFinish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FuriousFinish, self).RemoveEffect(character)


class GoryFinish(Feat):

    def __init__(self, data=None):
        super(GoryFinish, self).__init__(data)

    def AddEffect(self, character):
        super(GoryFinish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GoryFinish, self).RemoveEffect(character)


class GreaterChannelSmite(Feat):

    def __init__(self, data=None):
        super(GreaterChannelSmite, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterChannelSmite, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterChannelSmite, self).RemoveEffect(character)


class GreaterRendingFury(Feat):

    def __init__(self, data=None):
        super(GreaterRendingFury, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterRendingFury, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterRendingFury, self).RemoveEffect(character)


class GreaterSnapShot(Feat):

    def __init__(self, data=None):
        super(GreaterSnapShot, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterSnapShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterSnapShot, self).RemoveEffect(character)


class GreaterWhipMastery(Feat):

    def __init__(self, data=None):
        super(GreaterWhipMastery, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterWhipMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterWhipMastery, self).RemoveEffect(character)


class GuidedHand(Feat):

    def __init__(self, data=None):
        super(GuidedHand, self).__init__(data)

    def AddEffect(self, character):
        super(GuidedHand, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GuidedHand, self).RemoveEffect(character)


class Gunsmithing(Feat):

    def __init__(self, data=None):
        super(Gunsmithing, self).__init__(data)

    def AddEffect(self, character):
        super(Gunsmithing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Gunsmithing, self).RemoveEffect(character)


class HammerTheGap(Feat):

    def __init__(self, data=None):
        super(HammerTheGap, self).__init__(data)

    def AddEffect(self, character):
        super(HammerTheGap, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HammerTheGap, self).RemoveEffect(character)


class HarmonicSage(Feat):

    def __init__(self, data=None):
        super(HarmonicSage, self).__init__(data)

    def AddEffect(self, character):
        super(HarmonicSage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HarmonicSage, self).RemoveEffect(character)


class HauntedGnome(Feat):

    def __init__(self, data=None):
        super(HauntedGnome, self).__init__(data)

    def AddEffect(self, character):
        super(HauntedGnome, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HauntedGnome, self).RemoveEffect(character)


class HauntedGnomeAssault(Feat):

    def __init__(self, data=None):
        super(HauntedGnomeAssault, self).__init__(data)

    def AddEffect(self, character):
        super(HauntedGnomeAssault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HauntedGnomeAssault, self).RemoveEffect(character)


class HauntedGnomeShroud(Feat):

    def __init__(self, data=None):
        super(HauntedGnomeShroud, self).__init__(data)

    def AddEffect(self, character):
        super(HauntedGnomeShroud, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HauntedGnomeShroud, self).RemoveEffect(character)


class HeroSDisplay(Feat):

    def __init__(self, data=None):
        super(HeroSDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(HeroSDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HeroSDisplay, self).RemoveEffect(character)


class HexStrike(Feat):

    def __init__(self, data=None):
        super(HexStrike, self).__init__(data)

    def AddEffect(self, character):
        super(HexStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HexStrike, self).RemoveEffect(character)


class HorseMaster(Feat):

    def __init__(self, data=None):
        super(HorseMaster, self).__init__(data)

    def AddEffect(self, character):
        super(HorseMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HorseMaster, self).RemoveEffect(character)


class ImpactCriticalShot(Feat):

    def __init__(self, data=None):
        super(ImpactCriticalShot, self).__init__(data)

    def AddEffect(self, character):
        super(ImpactCriticalShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImpactCriticalShot, self).RemoveEffect(character)


class ImpalingCritical(Feat):

    def __init__(self, data=None):
        super(ImpalingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(ImpalingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImpalingCritical, self).RemoveEffect(character)


class ImprovedBackToBack(Feat):

    def __init__(self, data=None):
        super(ImprovedBackToBack, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedBackToBack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedBackToBack, self).RemoveEffect(character)


class ImprovedChargingHurler(Feat):

    def __init__(self, data=None):
        super(ImprovedChargingHurler, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedChargingHurler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedChargingHurler, self).RemoveEffect(character)


class ImprovedCleavingFinish(Feat):

    def __init__(self, data=None):
        super(ImprovedCleavingFinish, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedCleavingFinish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedCleavingFinish, self).RemoveEffect(character)


class ImprovedDevastatingStrike(Feat):

    def __init__(self, data=None):
        super(ImprovedDevastatingStrike, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedDevastatingStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedDevastatingStrike, self).RemoveEffect(character)


class ImprovedFeintPartner(Feat):

    def __init__(self, data=None):
        super(ImprovedFeintPartner, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedFeintPartner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedFeintPartner, self).RemoveEffect(character)


class ImprovedImpalingCritical(Feat):

    def __init__(self, data=None):
        super(ImprovedImpalingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedImpalingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedImpalingCritical, self).RemoveEffect(character)


class ImprovedRendingFury(Feat):

    def __init__(self, data=None):
        super(ImprovedRendingFury, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedRendingFury, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedRendingFury, self).RemoveEffect(character)


class ImprovedSnapShot(Feat):

    def __init__(self, data=None):
        super(ImprovedSnapShot, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedSnapShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedSnapShot, self).RemoveEffect(character)


class ImprovedStalwart(Feat):

    def __init__(self, data=None):
        super(ImprovedStalwart, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedStalwart, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedStalwart, self).RemoveEffect(character)


class ImprovedTwoWeaponFeint(Feat):

    def __init__(self, data=None):
        super(ImprovedTwoWeaponFeint, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedTwoWeaponFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedTwoWeaponFeint, self).RemoveEffect(character)


class ImprovedWhipMastery(Feat):

    def __init__(self, data=None):
        super(ImprovedWhipMastery, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedWhipMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedWhipMastery, self).RemoveEffect(character)


class InstantJudgment(Feat):

    def __init__(self, data=None):
        super(InstantJudgment, self).__init__(data)

    def AddEffect(self, character):
        super(InstantJudgment, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InstantJudgment, self).RemoveEffect(character)


class IntimidatingBane(Feat):

    def __init__(self, data=None):
        super(IntimidatingBane, self).__init__(data)

    def AddEffect(self, character):
        super(IntimidatingBane, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(IntimidatingBane, self).RemoveEffect(character)


class JanniRush(Feat):

    def __init__(self, data=None):
        super(JanniRush, self).__init__(data)

    def AddEffect(self, character):
        super(JanniRush, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(JanniRush, self).RemoveEffect(character)


class JanniStyle(Feat):

    def __init__(self, data=None):
        super(JanniStyle, self).__init__(data)

    def AddEffect(self, character):
        super(JanniStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(JanniStyle, self).RemoveEffect(character)


class JanniTempest(Feat):

    def __init__(self, data=None):
        super(JanniTempest, self).__init__(data)

    def AddEffect(self, character):
        super(JanniTempest, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(JanniTempest, self).RemoveEffect(character)


class Jawbreaker(Feat):

    def __init__(self, data=None):
        super(Jawbreaker, self).__init__(data)

    def AddEffect(self, character):
        super(Jawbreaker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Jawbreaker, self).RemoveEffect(character)


class KirinPath(Feat):

    def __init__(self, data=None):
        super(KirinPath, self).__init__(data)

    def AddEffect(self, character):
        super(KirinPath, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KirinPath, self).RemoveEffect(character)


class KirinStrike(Feat):

    def __init__(self, data=None):
        super(KirinStrike, self).__init__(data)

    def AddEffect(self, character):
        super(KirinStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KirinStrike, self).RemoveEffect(character)


class KirinStyle(Feat):

    def __init__(self, data=None):
        super(KirinStyle, self).__init__(data)

    def AddEffect(self, character):
        super(KirinStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KirinStyle, self).RemoveEffect(character)


class KnockoutArtist(Feat):

    def __init__(self, data=None):
        super(KnockoutArtist, self).__init__(data)

    def AddEffect(self, character):
        super(KnockoutArtist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KnockoutArtist, self).RemoveEffect(character)


class LandingRoll(Feat):

    def __init__(self, data=None):
        super(LandingRoll, self).__init__(data)

    def AddEffect(self, character):
        super(LandingRoll, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LandingRoll, self).RemoveEffect(character)


class LeapingShotDeed(Feat):

    def __init__(self, data=None):
        super(LeapingShotDeed, self).__init__(data)

    def AddEffect(self, character):
        super(LeapingShotDeed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LeapingShotDeed, self).RemoveEffect(character)


class MantisStyle(Feat):

    def __init__(self, data=None):
        super(MantisStyle, self).__init__(data)

    def AddEffect(self, character):
        super(MantisStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MantisStyle, self).RemoveEffect(character)


class MantisTorment(Feat):

    def __init__(self, data=None):
        super(MantisTorment, self).__init__(data)

    def AddEffect(self, character):
        super(MantisTorment, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MantisTorment, self).RemoveEffect(character)


class MantisWisdom(Feat):

    def __init__(self, data=None):
        super(MantisWisdom, self).__init__(data)

    def AddEffect(self, character):
        super(MantisWisdom, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MantisWisdom, self).RemoveEffect(character)


class MaridColdsnap(Feat):

    def __init__(self, data=None):
        super(MaridColdsnap, self).__init__(data)

    def AddEffect(self, character):
        super(MaridColdsnap, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MaridColdsnap, self).RemoveEffect(character)


class MaridSpirit(Feat):

    def __init__(self, data=None):
        super(MaridSpirit, self).__init__(data)

    def AddEffect(self, character):
        super(MaridSpirit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MaridSpirit, self).RemoveEffect(character)


class MaridStyle(Feat):

    def __init__(self, data=None):
        super(MaridStyle, self).__init__(data)

    def AddEffect(self, character):
        super(MaridStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MaridStyle, self).RemoveEffect(character)


class MasterCombatPerformer(Feat):

    def __init__(self, data=None):
        super(MasterCombatPerformer, self).__init__(data)

    def AddEffect(self, character):
        super(MasterCombatPerformer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MasterCombatPerformer, self).RemoveEffect(character)


class MasterSiegeEngineer(Feat):

    def __init__(self, data=None):
        super(MasterSiegeEngineer, self).__init__(data)

    def AddEffect(self, character):
        super(MasterSiegeEngineer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MasterSiegeEngineer, self).RemoveEffect(character)


class MasterfulDisplay(Feat):

    def __init__(self, data=None):
        super(MasterfulDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(MasterfulDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MasterfulDisplay, self).RemoveEffect(character)


class MaximizedSpellstrike(Feat):

    def __init__(self, data=None):
        super(MaximizedSpellstrike, self).__init__(data)

    def AddEffect(self, character):
        super(MaximizedSpellstrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MaximizedSpellstrike, self).RemoveEffect(character)


class MenacingBane(Feat):

    def __init__(self, data=None):
        super(MenacingBane, self).__init__(data)

    def AddEffect(self, character):
        super(MenacingBane, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MenacingBane, self).RemoveEffect(character)


class MercifulBane(Feat):

    def __init__(self, data=None):
        super(MercifulBane, self).__init__(data)

    def AddEffect(self, character):
        super(MercifulBane, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MercifulBane, self).RemoveEffect(character)


class MockingDance(Feat):

    def __init__(self, data=None):
        super(MockingDance, self).__init__(data)

    def AddEffect(self, character):
        super(MockingDance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MockingDance, self).RemoveEffect(character)


class MonasticLegacy(Feat):

    def __init__(self, data=None):
        super(MonasticLegacy, self).__init__(data)

    def AddEffect(self, character):
        super(MonasticLegacy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MonasticLegacy, self).RemoveEffect(character)


class MonkeyMoves(Feat):

    def __init__(self, data=None):
        super(MonkeyMoves, self).__init__(data)

    def AddEffect(self, character):
        super(MonkeyMoves, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MonkeyMoves, self).RemoveEffect(character)


class MonkeyShine(Feat):

    def __init__(self, data=None):
        super(MonkeyShine, self).__init__(data)

    def AddEffect(self, character):
        super(MonkeyShine, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MonkeyShine, self).RemoveEffect(character)


class MonkeyStyle(Feat):

    def __init__(self, data=None):
        super(MonkeyStyle, self).__init__(data)

    def AddEffect(self, character):
        super(MonkeyStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MonkeyStyle, self).RemoveEffect(character)


class MoonlightStalker(Feat):

    def __init__(self, data=None):
        super(MoonlightStalker, self).__init__(data)

    def AddEffect(self, character):
        super(MoonlightStalker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MoonlightStalker, self).RemoveEffect(character)


class MoonlightStalkerFeint(Feat):

    def __init__(self, data=None):
        super(MoonlightStalkerFeint, self).__init__(data)

    def AddEffect(self, character):
        super(MoonlightStalkerFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MoonlightStalkerFeint, self).RemoveEffect(character)


class MoonlightStalkerMaster(Feat):

    def __init__(self, data=None):
        super(MoonlightStalkerMaster, self).__init__(data)

    def AddEffect(self, character):
        super(MoonlightStalkerMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MoonlightStalkerMaster, self).RemoveEffect(character)


class MurdererSCircle(Feat):

    def __init__(self, data=None):
        super(MurdererSCircle, self).__init__(data)

    def AddEffect(self, character):
        super(MurdererSCircle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MurdererSCircle, self).RemoveEffect(character)


class Neckbreaker(Feat):

    def __init__(self, data=None):
        super(Neckbreaker, self).__init__(data)

    def AddEffect(self, character):
        super(Neckbreaker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Neckbreaker, self).RemoveEffect(character)


class NetAdept(Feat):

    def __init__(self, data=None):
        super(NetAdept, self).__init__(data)

    def AddEffect(self, character):
        super(NetAdept, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NetAdept, self).RemoveEffect(character)


class NetAndTrident(Feat):

    def __init__(self, data=None):
        super(NetAndTrident, self).__init__(data)

    def AddEffect(self, character):
        super(NetAndTrident, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NetAndTrident, self).RemoveEffect(character)


class NetManeuvering(Feat):

    def __init__(self, data=None):
        super(NetManeuvering, self).__init__(data)

    def AddEffect(self, character):
        super(NetManeuvering, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NetManeuvering, self).RemoveEffect(character)


class NetTrickery(Feat):

    def __init__(self, data=None):
        super(NetTrickery, self).__init__(data)

    def AddEffect(self, character):
        super(NetTrickery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NetTrickery, self).RemoveEffect(character)


class NightmareFist(Feat):

    def __init__(self, data=None):
        super(NightmareFist, self).__init__(data)

    def AddEffect(self, character):
        super(NightmareFist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NightmareFist, self).RemoveEffect(character)


class NightmareStriker(Feat):

    def __init__(self, data=None):
        super(NightmareStriker, self).__init__(data)

    def AddEffect(self, character):
        super(NightmareStriker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NightmareStriker, self).RemoveEffect(character)


class NightmareWeaver(Feat):

    def __init__(self, data=None):
        super(NightmareWeaver, self).__init__(data)

    def AddEffect(self, character):
        super(NightmareWeaver, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NightmareWeaver, self).RemoveEffect(character)


class NoName(Feat):

    def __init__(self, data=None):
        super(NoName, self).__init__(data)

    def AddEffect(self, character):
        super(NoName, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NoName, self).RemoveEffect(character)


class OpeningVolley(Feat):

    def __init__(self, data=None):
        super(OpeningVolley, self).__init__(data)

    def AddEffect(self, character):
        super(OpeningVolley, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OpeningVolley, self).RemoveEffect(character)


class PackAttack(Feat):

    def __init__(self, data=None):
        super(PackAttack, self).__init__(data)

    def AddEffect(self, character):
        super(PackAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PackAttack, self).RemoveEffect(character)


class PantherClaw(Feat):

    def __init__(self, data=None):
        super(PantherClaw, self).__init__(data)

    def AddEffect(self, character):
        super(PantherClaw, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PantherClaw, self).RemoveEffect(character)


class PantherParry(Feat):

    def __init__(self, data=None):
        super(PantherParry, self).__init__(data)

    def AddEffect(self, character):
        super(PantherParry, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PantherParry, self).RemoveEffect(character)


class PantherStyle(Feat):

    def __init__(self, data=None):
        super(PantherStyle, self).__init__(data)

    def AddEffect(self, character):
        super(PantherStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PantherStyle, self).RemoveEffect(character)


class PassingTrick(Feat):

    def __init__(self, data=None):
        super(PassingTrick, self).__init__(data)

    def AddEffect(self, character):
        super(PassingTrick, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PassingTrick, self).RemoveEffect(character)


class PerformanceWeaponMastery(Feat):

    def __init__(self, data=None):
        super(PerformanceWeaponMastery, self).__init__(data)

    def AddEffect(self, character):
        super(PerformanceWeaponMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PerformanceWeaponMastery, self).RemoveEffect(character)


class PerformingCombatant(Feat):

    def __init__(self, data=None):
        super(PerformingCombatant, self).__init__(data)

    def AddEffect(self, character):
        super(PerformingCombatant, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PerformingCombatant, self).RemoveEffect(character)


class PinDown(Feat):

    def __init__(self, data=None):
        super(PinDown, self).__init__(data)

    def AddEffect(self, character):
        super(PinDown, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PinDown, self).RemoveEffect(character)


class PinningKnockout(Feat):

    def __init__(self, data=None):
        super(PinningKnockout, self).__init__(data)

    def AddEffect(self, character):
        super(PinningKnockout, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PinningKnockout, self).RemoveEffect(character)


class PinningRend(Feat):

    def __init__(self, data=None):
        super(PinningRend, self).__init__(data)

    def AddEffect(self, character):
        super(PinningRend, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PinningRend, self).RemoveEffect(character)


class PinpointPoisoner(Feat):

    def __init__(self, data=None):
        super(PinpointPoisoner, self).__init__(data)

    def AddEffect(self, character):
        super(PinpointPoisoner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PinpointPoisoner, self).RemoveEffect(character)


class PlanarWildShape(Feat):

    def __init__(self, data=None):
        super(PlanarWildShape, self).__init__(data)

    def AddEffect(self, character):
        super(PlanarWildShape, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PlanarWildShape, self).RemoveEffect(character)


class ProneShooter(Feat):

    def __init__(self, data=None):
        super(ProneShooter, self).__init__(data)

    def AddEffect(self, character):
        super(ProneShooter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ProneShooter, self).RemoveEffect(character)


class ProneSlinger(Feat):

    def __init__(self, data=None):
        super(ProneSlinger, self).__init__(data)

    def AddEffect(self, character):
        super(ProneSlinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ProneSlinger, self).RemoveEffect(character)


class QuickBullRush(Feat):

    def __init__(self, data=None):
        super(QuickBullRush, self).__init__(data)

    def AddEffect(self, character):
        super(QuickBullRush, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickBullRush, self).RemoveEffect(character)


class QuickDirtyTrick(Feat):

    def __init__(self, data=None):
        super(QuickDirtyTrick, self).__init__(data)

    def AddEffect(self, character):
        super(QuickDirtyTrick, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickDirtyTrick, self).RemoveEffect(character)


class QuickDrag(Feat):

    def __init__(self, data=None):
        super(QuickDrag, self).__init__(data)

    def AddEffect(self, character):
        super(QuickDrag, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickDrag, self).RemoveEffect(character)


class QuickReposition(Feat):

    def __init__(self, data=None):
        super(QuickReposition, self).__init__(data)

    def AddEffect(self, character):
        super(QuickReposition, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickReposition, self).RemoveEffect(character)


class QuickSteal(Feat):

    def __init__(self, data=None):
        super(QuickSteal, self).__init__(data)

    def AddEffect(self, character):
        super(QuickSteal, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickSteal, self).RemoveEffect(character)


class RagingBrutality(Feat):

    def __init__(self, data=None):
        super(RagingBrutality, self).__init__(data)

    def AddEffect(self, character):
        super(RagingBrutality, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RagingBrutality, self).RemoveEffect(character)


class RagingDeathblow(Feat):

    def __init__(self, data=None):
        super(RagingDeathblow, self).__init__(data)

    def AddEffect(self, character):
        super(RagingDeathblow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RagingDeathblow, self).RemoveEffect(character)


class RagingHurler(Feat):

    def __init__(self, data=None):
        super(RagingHurler, self).__init__(data)

    def AddEffect(self, character):
        super(RagingHurler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RagingHurler, self).RemoveEffect(character)


class RagingThrow(Feat):

    def __init__(self, data=None):
        super(RagingThrow, self).__init__(data)

    def AddEffect(self, character):
        super(RagingThrow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RagingThrow, self).RemoveEffect(character)


class RapidGrappler(Feat):

    def __init__(self, data=None):
        super(RapidGrappler, self).__init__(data)

    def AddEffect(self, character):
        super(RapidGrappler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RapidGrappler, self).RemoveEffect(character)


class ReboundingLeap(Feat):

    def __init__(self, data=None):
        super(ReboundingLeap, self).__init__(data)

    def AddEffect(self, character):
        super(ReboundingLeap, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ReboundingLeap, self).RemoveEffect(character)


class RebuffingReduction(Feat):

    def __init__(self, data=None):
        super(RebuffingReduction, self).__init__(data)

    def AddEffect(self, character):
        super(RebuffingReduction, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RebuffingReduction, self).RemoveEffect(character)


class RendingFury(Feat):

    def __init__(self, data=None):
        super(RendingFury, self).__init__(data)

    def AddEffect(self, character):
        super(RendingFury, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RendingFury, self).RemoveEffect(character)


class RevelationStrike(Feat):

    def __init__(self, data=None):
        super(RevelationStrike, self).__init__(data)

    def AddEffect(self, character):
        super(RevelationStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RevelationStrike, self).RemoveEffect(character)


class RhetoricalFlourish(Feat):

    def __init__(self, data=None):
        super(RhetoricalFlourish, self).__init__(data)

    def AddEffect(self, character):
        super(RhetoricalFlourish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RhetoricalFlourish, self).RemoveEffect(character)


class RicochetShotDeed(Feat):

    def __init__(self, data=None):
        super(RicochetShotDeed, self).__init__(data)

    def AddEffect(self, character):
        super(RicochetShotDeed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RicochetShotDeed, self).RemoveEffect(character)


class RighteousHealing(Feat):

    def __init__(self, data=None):
        super(RighteousHealing, self).__init__(data)

    def AddEffect(self, character):
        super(RighteousHealing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RighteousHealing, self).RemoveEffect(character)


class SapAdept(Feat):

    def __init__(self, data=None):
        super(SapAdept, self).__init__(data)

    def AddEffect(self, character):
        super(SapAdept, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SapAdept, self).RemoveEffect(character)


class SapMaster(Feat):

    def __init__(self, data=None):
        super(SapMaster, self).__init__(data)

    def AddEffect(self, character):
        super(SapMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SapMaster, self).RemoveEffect(character)


class SavageDisplay(Feat):

    def __init__(self, data=None):
        super(SavageDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(SavageDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SavageDisplay, self).RemoveEffect(character)


class SchoolStrike(Feat):

    def __init__(self, data=None):
        super(SchoolStrike, self).__init__(data)

    def AddEffect(self, character):
        super(SchoolStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SchoolStrike, self).RemoveEffect(character)


class SeaLegs(Feat):

    def __init__(self, data=None):
        super(SeaLegs, self).__init__(data)

    def AddEffect(self, character):
        super(SeaLegs, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SeaLegs, self).RemoveEffect(character)


class SecretStashDeed(Feat):

    def __init__(self, data=None):
        super(SecretStashDeed, self).__init__(data)

    def AddEffect(self, character):
        super(SecretStashDeed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SecretStashDeed, self).RemoveEffect(character)


class SeizeTheMoment(Feat):

    def __init__(self, data=None):
        super(SeizeTheMoment, self).__init__(data)

    def AddEffect(self, character):
        super(SeizeTheMoment, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SeizeTheMoment, self).RemoveEffect(character)


class ShaitanEarthblast(Feat):

    def __init__(self, data=None):
        super(ShaitanEarthblast, self).__init__(data)

    def AddEffect(self, character):
        super(ShaitanEarthblast, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShaitanEarthblast, self).RemoveEffect(character)


class ShaitanSkin(Feat):

    def __init__(self, data=None):
        super(ShaitanSkin, self).__init__(data)

    def AddEffect(self, character):
        super(ShaitanSkin, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShaitanSkin, self).RemoveEffect(character)


class ShaitanStyle(Feat):

    def __init__(self, data=None):
        super(ShaitanStyle, self).__init__(data)

    def AddEffect(self, character):
        super(ShaitanStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShaitanStyle, self).RemoveEffect(character)


class ShakeItOff(Feat):

    def __init__(self, data=None):
        super(ShakeItOff, self).__init__(data)

    def AddEffect(self, character):
        super(ShakeItOff, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShakeItOff, self).RemoveEffect(character)


class ShapeshifterFoil(Feat):

    def __init__(self, data=None):
        super(ShapeshifterFoil, self).__init__(data)

    def AddEffect(self, character):
        super(ShapeshifterFoil, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShapeshifterFoil, self).RemoveEffect(character)


class ShapeshiftingHunter(Feat):

    def __init__(self, data=None):
        super(ShapeshiftingHunter, self).__init__(data)

    def AddEffect(self, character):
        super(ShapeshiftingHunter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShapeshiftingHunter, self).RemoveEffect(character)


class SharedJudgment(Feat):

    def __init__(self, data=None):
        super(SharedJudgment, self).__init__(data)

    def AddEffect(self, character):
        super(SharedJudgment, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SharedJudgment, self).RemoveEffect(character)


class SiegeCommander(Feat):

    def __init__(self, data=None):
        super(SiegeCommander, self).__init__(data)

    def AddEffect(self, character):
        super(SiegeCommander, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SiegeCommander, self).RemoveEffect(character)


class SiegeEngineer(Feat):

    def __init__(self, data=None):
        super(SiegeEngineer, self).__init__(data)

    def AddEffect(self, character):
        super(SiegeEngineer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SiegeEngineer, self).RemoveEffect(character)


class SiegeGunner(Feat):

    def __init__(self, data=None):
        super(SiegeGunner, self).__init__(data)

    def AddEffect(self, character):
        super(SiegeGunner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SiegeGunner, self).RemoveEffect(character)


class SignatureDeed(Feat):

    def __init__(self, data=None):
        super(SignatureDeed, self).__init__(data)

    def AddEffect(self, character):
        super(SignatureDeed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SignatureDeed, self).RemoveEffect(character)


class SkilledDriver(Feat):

    def __init__(self, data=None):
        super(SkilledDriver, self).__init__(data)

    def AddEffect(self, character):
        super(SkilledDriver, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SkilledDriver, self).RemoveEffect(character)


class SlayerSKnack(Feat):

    def __init__(self, data=None):
        super(SlayerSKnack, self).__init__(data)

    def AddEffect(self, character):
        super(SlayerSKnack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SlayerSKnack, self).RemoveEffect(character)


class SlingFlail(Feat):

    def __init__(self, data=None):
        super(SlingFlail, self).__init__(data)

    def AddEffect(self, character):
        super(SlingFlail, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SlingFlail, self).RemoveEffect(character)


class SnakeFang(Feat):

    def __init__(self, data=None):
        super(SnakeFang, self).__init__(data)

    def AddEffect(self, character):
        super(SnakeFang, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SnakeFang, self).RemoveEffect(character)


class SnakeStyle(Feat):

    def __init__(self, data=None):
        super(SnakeStyle, self).__init__(data)

    def AddEffect(self, character):
        super(SnakeStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SnakeStyle, self).RemoveEffect(character)


class SnapShot(Feat):

    def __init__(self, data=None):
        super(SnapShot, self).__init__(data)

    def AddEffect(self, character):
        super(SnapShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SnapShot, self).RemoveEffect(character)


class SnappingTurtleClutch(Feat):

    def __init__(self, data=None):
        super(SnappingTurtleClutch, self).__init__(data)

    def AddEffect(self, character):
        super(SnappingTurtleClutch, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SnappingTurtleClutch, self).RemoveEffect(character)


class SnappingTurtleShell(Feat):

    def __init__(self, data=None):
        super(SnappingTurtleShell, self).__init__(data)

    def AddEffect(self, character):
        super(SnappingTurtleShell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SnappingTurtleShell, self).RemoveEffect(character)


class SnappingTurtleStyle(Feat):

    def __init__(self, data=None):
        super(SnappingTurtleStyle, self).__init__(data)

    def AddEffect(self, character):
        super(SnappingTurtleStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SnappingTurtleStyle, self).RemoveEffect(character)


class SneakingPrecision(Feat):

    def __init__(self, data=None):
        super(SneakingPrecision, self).__init__(data)

    def AddEffect(self, character):
        super(SneakingPrecision, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SneakingPrecision, self).RemoveEffect(character)


class SorcerousStrike(Feat):

    def __init__(self, data=None):
        super(SorcerousStrike, self).__init__(data)

    def AddEffect(self, character):
        super(SorcerousStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SorcerousStrike, self).RemoveEffect(character)


class SpellBane(Feat):

    def __init__(self, data=None):
        super(SpellBane, self).__init__(data)

    def AddEffect(self, character):
        super(SpellBane, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellBane, self).RemoveEffect(character)


class SpinningThrow(Feat):

    def __init__(self, data=None):
        super(SpinningThrow, self).__init__(data)

    def AddEffect(self, character):
        super(SpinningThrow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpinningThrow, self).RemoveEffect(character)


class SplinteringWeapon(Feat):

    def __init__(self, data=None):
        super(SplinteringWeapon, self).__init__(data)

    def AddEffect(self, character):
        super(SplinteringWeapon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SplinteringWeapon, self).RemoveEffect(character)


class StageCombatant(Feat):

    def __init__(self, data=None):
        super(StageCombatant, self).__init__(data)

    def AddEffect(self, character):
        super(StageCombatant, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StageCombatant, self).RemoveEffect(character)


class Stalwart(Feat):

    def __init__(self, data=None):
        super(Stalwart, self).__init__(data)

    def AddEffect(self, character):
        super(Stalwart, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Stalwart, self).RemoveEffect(character)


class StealthSynergy(Feat):

    def __init__(self, data=None):
        super(StealthSynergy, self).__init__(data)

    def AddEffect(self, character):
        super(StealthSynergy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StealthSynergy, self).RemoveEffect(character)


class Strangler(Feat):

    def __init__(self, data=None):
        super(Strangler, self).__init__(data)

    def AddEffect(self, character):
        super(Strangler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Strangler, self).RemoveEffect(character)


class StrongComeback(Feat):

    def __init__(self, data=None):
        super(StrongComeback, self).__init__(data)

    def AddEffect(self, character):
        super(StrongComeback, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StrongComeback, self).RemoveEffect(character)


class StunningPin(Feat):

    def __init__(self, data=None):
        super(StunningPin, self).__init__(data)

    def AddEffect(self, character):
        super(StunningPin, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StunningPin, self).RemoveEffect(character)


class SureGrasp(Feat):

    def __init__(self, data=None):
        super(SureGrasp, self).__init__(data)

    def AddEffect(self, character):
        super(SureGrasp, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SureGrasp, self).RemoveEffect(character)


class SwordAndPistol(Feat):

    def __init__(self, data=None):
        super(SwordAndPistol, self).__init__(data)

    def AddEffect(self, character):
        super(SwordAndPistol, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SwordAndPistol, self).RemoveEffect(character)


class TandemTrip(Feat):

    def __init__(self, data=None):
        super(TandemTrip, self).__init__(data)

    def AddEffect(self, character):
        super(TandemTrip, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TandemTrip, self).RemoveEffect(character)


class TargetOfOpportunity(Feat):

    def __init__(self, data=None):
        super(TargetOfOpportunity, self).__init__(data)

    def AddEffect(self, character):
        super(TargetOfOpportunity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TargetOfOpportunity, self).RemoveEffect(character)


class TeamPickpocketing(Feat):

    def __init__(self, data=None):
        super(TeamPickpocketing, self).__init__(data)

    def AddEffect(self, character):
        super(TeamPickpocketing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TeamPickpocketing, self).RemoveEffect(character)


class TigerClaws(Feat):

    def __init__(self, data=None):
        super(TigerClaws, self).__init__(data)

    def AddEffect(self, character):
        super(TigerClaws, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TigerClaws, self).RemoveEffect(character)


class TigerPounce(Feat):

    def __init__(self, data=None):
        super(TigerPounce, self).__init__(data)

    def AddEffect(self, character):
        super(TigerPounce, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TigerPounce, self).RemoveEffect(character)


class TigerStyle(Feat):

    def __init__(self, data=None):
        super(TigerStyle, self).__init__(data)

    def AddEffect(self, character):
        super(TigerStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TigerStyle, self).RemoveEffect(character)


class TrapperSSetup(Feat):

    def __init__(self, data=None):
        super(TrapperSSetup, self).__init__(data)

    def AddEffect(self, character):
        super(TrapperSSetup, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TrapperSSetup, self).RemoveEffect(character)


class TwinThunders(Feat):

    def __init__(self, data=None):
        super(TwinThunders, self).__init__(data)

    def AddEffect(self, character):
        super(TwinThunders, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwinThunders, self).RemoveEffect(character)


class TwinThundersFlurry(Feat):

    def __init__(self, data=None):
        super(TwinThundersFlurry, self).__init__(data)

    def AddEffect(self, character):
        super(TwinThundersFlurry, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwinThundersFlurry, self).RemoveEffect(character)


class TwinThundersMaster(Feat):

    def __init__(self, data=None):
        super(TwinThundersMaster, self).__init__(data)

    def AddEffect(self, character):
        super(TwinThundersMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwinThundersMaster, self).RemoveEffect(character)


class TwoHandedThrower(Feat):

    def __init__(self, data=None):
        super(TwoHandedThrower, self).__init__(data)

    def AddEffect(self, character):
        super(TwoHandedThrower, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwoHandedThrower, self).RemoveEffect(character)


class TwoWeaponFeint(Feat):

    def __init__(self, data=None):
        super(TwoWeaponFeint, self).__init__(data)

    def AddEffect(self, character):
        super(TwoWeaponFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwoWeaponFeint, self).RemoveEffect(character)


class ViciousStomp(Feat):

    def __init__(self, data=None):
        super(ViciousStomp, self).__init__(data)

    def AddEffect(self, character):
        super(ViciousStomp, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ViciousStomp, self).RemoveEffect(character)


class WaveStrike(Feat):

    def __init__(self, data=None):
        super(WaveStrike, self).__init__(data)

    def AddEffect(self, character):
        super(WaveStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WaveStrike, self).RemoveEffect(character)


class WhipMastery(Feat):

    def __init__(self, data=None):
        super(WhipMastery, self).__init__(data)

    def AddEffect(self, character):
        super(WhipMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WhipMastery, self).RemoveEffect(character)


class AbundantRevelations(Feat):

    def __init__(self, data=None):
        super(AbundantRevelations, self).__init__(data)

    def AddEffect(self, character):
        super(AbundantRevelations, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AbundantRevelations, self).RemoveEffect(character)


class AccursedCritical(Feat):

    def __init__(self, data=None):
        super(AccursedCritical, self).__init__(data)

    def AddEffect(self, character):
        super(AccursedCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AccursedCritical, self).RemoveEffect(character)


class AccursedHex(Feat):

    def __init__(self, data=None):
        super(AccursedHex, self).__init__(data)

    def AddEffect(self, character):
        super(AccursedHex, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AccursedHex, self).RemoveEffect(character)


class AdvancedRangerTrap(Feat):

    def __init__(self, data=None):
        super(AdvancedRangerTrap, self).__init__(data)

    def AddEffect(self, character):
        super(AdvancedRangerTrap, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AdvancedRangerTrap, self).RemoveEffect(character)


class Antagonize(Feat):

    def __init__(self, data=None):
        super(Antagonize, self).__init__(data)

    def AddEffect(self, character):
        super(Antagonize, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Antagonize, self).RemoveEffect(character)


class BlightedCritical(Feat):

    def __init__(self, data=None):
        super(BlightedCritical, self).__init__(data)

    def AddEffect(self, character):
        super(BlightedCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlightedCritical, self).RemoveEffect(character)


class BlightedCriticalMastery(Feat):

    def __init__(self, data=None):
        super(BlightedCriticalMastery, self).__init__(data)

    def AddEffect(self, character):
        super(BlightedCriticalMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlightedCriticalMastery, self).RemoveEffect(character)


class BurningSpell(Feat):

    def __init__(self, data=None):
        super(BurningSpell, self).__init__(data)

    def AddEffect(self, character):
        super(BurningSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BurningSpell, self).RemoveEffect(character)


class ChanneledShieldWall(Feat):

    def __init__(self, data=None):
        super(ChanneledShieldWall, self).__init__(data)

    def AddEffect(self, character):
        super(ChanneledShieldWall, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ChanneledShieldWall, self).RemoveEffect(character)


class ConcussiveSpell(Feat):

    def __init__(self, data=None):
        super(ConcussiveSpell, self).__init__(data)

    def AddEffect(self, character):
        super(ConcussiveSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ConcussiveSpell, self).RemoveEffect(character)


class CreateReliquaryArmsAndShields(Feat):

    def __init__(self, data=None):
        super(CreateReliquaryArmsAndShields, self).__init__(data)

    def AddEffect(self, character):
        super(CreateReliquaryArmsAndShields, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CreateReliquaryArmsAndShields, self).RemoveEffect(character)


class CreateSanguineElixir(Feat):

    def __init__(self, data=None):
        super(CreateSanguineElixir, self).__init__(data)

    def AddEffect(self, character):
        super(CreateSanguineElixir, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CreateSanguineElixir, self).RemoveEffect(character)


class DefendingEidolon(Feat):

    def __init__(self, data=None):
        super(DefendingEidolon, self).__init__(data)

    def AddEffect(self, character):
        super(DefendingEidolon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DefendingEidolon, self).RemoveEffect(character)


class DenyDeath(Feat):

    def __init__(self, data=None):
        super(DenyDeath, self).__init__(data)

    def AddEffect(self, character):
        super(DenyDeath, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DenyDeath, self).RemoveEffect(character)


class DetectExpertise(Feat):

    def __init__(self, data=None):
        super(DetectExpertise, self).__init__(data)

    def AddEffect(self, character):
        super(DetectExpertise, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DetectExpertise, self).RemoveEffect(character)


class DieForYourMaster(Feat):

    def __init__(self, data=None):
        super(DieForYourMaster, self).__init__(data)

    def AddEffect(self, character):
        super(DieForYourMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DieForYourMaster, self).RemoveEffect(character)


class DivineInterference(Feat):

    def __init__(self, data=None):
        super(DivineInterference, self).__init__(data)

    def AddEffect(self, character):
        super(DivineInterference, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DivineInterference, self).RemoveEffect(character)


class DragonbaneAura(Feat):

    def __init__(self, data=None):
        super(DragonbaneAura, self).__init__(data)

    def AddEffect(self, character):
        super(DragonbaneAura, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DragonbaneAura, self).RemoveEffect(character)


class EchoingSpell(Feat):

    def __init__(self, data=None):
        super(EchoingSpell, self).__init__(data)

    def AddEffect(self, character):
        super(EchoingSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EchoingSpell, self).RemoveEffect(character)


class EldritchHeritage(Feat):

    def __init__(self, data=None):
        super(EldritchHeritage, self).__init__(data)

    def AddEffect(self, character):
        super(EldritchHeritage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EldritchHeritage, self).RemoveEffect(character)


class Ensemble(Feat):

    def __init__(self, data=None):
        super(Ensemble, self).__init__(data)

    def AddEffect(self, character):
        super(Ensemble, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Ensemble, self).RemoveEffect(character)


class EvolvedFamiliar(Feat):

    def __init__(self, data=None):
        super(EvolvedFamiliar, self).__init__(data)

    def AddEffect(self, character):
        super(EvolvedFamiliar, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EvolvedFamiliar, self).RemoveEffect(character)


class ExploitLore(Feat):

    def __init__(self, data=None):
        super(ExploitLore, self).__init__(data)

    def AddEffect(self, character):
        super(ExploitLore, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExploitLore, self).RemoveEffect(character)


class ExtraArcana(Feat):

    def __init__(self, data=None):
        super(ExtraArcana, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraArcana, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraArcana, self).RemoveEffect(character)


class ExtraArcanePool(Feat):

    def __init__(self, data=None):
        super(ExtraArcanePool, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraArcanePool, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraArcanePool, self).RemoveEffect(character)


class ExtendedBane(Feat):

    def __init__(self, data=None):
        super(ExtendedBane, self).__init__(data)

    def AddEffect(self, character):
        super(ExtendedBane, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtendedBane, self).RemoveEffect(character)


class ExtraCantripsOrOrisons(Feat):

    def __init__(self, data=None):
        super(ExtraCantripsOrOrisons, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraCantripsOrOrisons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraCantripsOrOrisons, self).RemoveEffect(character)


class ExtraEvolution(Feat):

    def __init__(self, data=None):
        super(ExtraEvolution, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraEvolution, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraEvolution, self).RemoveEffect(character)


class ExtraRangerTrap(Feat):

    def __init__(self, data=None):
        super(ExtraRangerTrap, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraRangerTrap, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraRangerTrap, self).RemoveEffect(character)


class ExtraSummons(Feat):

    def __init__(self, data=None):
        super(ExtraSummons, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraSummons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraSummons, self).RemoveEffect(character)


class EyesOfJudgment(Feat):

    def __init__(self, data=None):
        super(EyesOfJudgment, self).__init__(data)

    def AddEffect(self, character):
        super(EyesOfJudgment, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EyesOfJudgment, self).RemoveEffect(character)


class FastEmpathy(Feat):

    def __init__(self, data=None):
        super(FastEmpathy, self).__init__(data)

    def AddEffect(self, character):
        super(FastEmpathy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FastEmpathy, self).RemoveEffect(character)


class FavoredJudgment(Feat):

    def __init__(self, data=None):
        super(FavoredJudgment, self).__init__(data)

    def AddEffect(self, character):
        super(FavoredJudgment, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FavoredJudgment, self).RemoveEffect(character)


class FearlessAura(Feat):

    def __init__(self, data=None):
        super(FearlessAura, self).__init__(data)

    def AddEffect(self, character):
        super(FearlessAura, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FearlessAura, self).RemoveEffect(character)


class FireMusic(Feat):

    def __init__(self, data=None):
        super(FireMusic, self).__init__(data)

    def AddEffect(self, character):
        super(FireMusic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FireMusic, self).RemoveEffect(character)


class FlaringSpell(Feat):

    def __init__(self, data=None):
        super(FlaringSpell, self).__init__(data)

    def AddEffect(self, character):
        super(FlaringSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FlaringSpell, self).RemoveEffect(character)


class FocusedEidolon(Feat):

    def __init__(self, data=None):
        super(FocusedEidolon, self).__init__(data)

    def AddEffect(self, character):
        super(FocusedEidolon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FocusedEidolon, self).RemoveEffect(character)


class GlidingSteps(Feat):

    def __init__(self, data=None):
        super(GlidingSteps, self).__init__(data)

    def AddEffect(self, character):
        super(GlidingSteps, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GlidingSteps, self).RemoveEffect(character)


class GrantInitiative(Feat):

    def __init__(self, data=None):
        super(GrantInitiative, self).__init__(data)

    def AddEffect(self, character):
        super(GrantInitiative, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GrantInitiative, self).RemoveEffect(character)


class GreaterBlightedCritical(Feat):

    def __init__(self, data=None):
        super(GreaterBlightedCritical, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterBlightedCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterBlightedCritical, self).RemoveEffect(character)


class GreaterEldritchHeritage(Feat):

    def __init__(self, data=None):
        super(GreaterEldritchHeritage, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterEldritchHeritage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterEldritchHeritage, self).RemoveEffect(character)


class GreaterMercy(Feat):

    def __init__(self, data=None):
        super(GreaterMercy, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterMercy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterMercy, self).RemoveEffect(character)


class GreaterSpellSpecialization(Feat):

    def __init__(self, data=None):
        super(GreaterSpellSpecialization, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterSpellSpecialization, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterSpellSpecialization, self).RemoveEffect(character)


class GreaterWildEmpathy(Feat):

    def __init__(self, data=None):
        super(GreaterWildEmpathy, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterWildEmpathy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterWildEmpathy, self).RemoveEffect(character)


class ImplantBomb(Feat):

    def __init__(self, data=None):
        super(ImplantBomb, self).__init__(data)

    def AddEffect(self, character):
        super(ImplantBomb, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImplantBomb, self).RemoveEffect(character)


class ImprovedEldritchHeritage(Feat):

    def __init__(self, data=None):
        super(ImprovedEldritchHeritage, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedEldritchHeritage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedEldritchHeritage, self).RemoveEffect(character)


class ImprovedMonsterLore(Feat):

    def __init__(self, data=None):
        super(ImprovedMonsterLore, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedMonsterLore, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedMonsterLore, self).RemoveEffect(character)


class InsightfulGaze(Feat):

    def __init__(self, data=None):
        super(InsightfulGaze, self).__init__(data)

    def AddEffect(self, character):
        super(InsightfulGaze, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InsightfulGaze, self).RemoveEffect(character)


class IntimidatingGaze(Feat):

    def __init__(self, data=None):
        super(IntimidatingGaze, self).__init__(data)

    def AddEffect(self, character):
        super(IntimidatingGaze, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(IntimidatingGaze, self).RemoveEffect(character)


class JudgmentSurge(Feat):

    def __init__(self, data=None):
        super(JudgmentSurge, self).__init__(data)

    def AddEffect(self, character):
        super(JudgmentSurge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(JudgmentSurge, self).RemoveEffect(character)


class KiStand(Feat):

    def __init__(self, data=None):
        super(KiStand, self).__init__(data)

    def AddEffect(self, character):
        super(KiStand, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KiStand, self).RemoveEffect(character)


class LearnRangerTrap(Feat):

    def __init__(self, data=None):
        super(LearnRangerTrap, self).__init__(data)

    def AddEffect(self, character):
        super(LearnRangerTrap, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LearnRangerTrap, self).RemoveEffect(character)


class LifeLure(Feat):

    def __init__(self, data=None):
        super(LifeLure, self).__init__(data)

    def AddEffect(self, character):
        super(LifeLure, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LifeLure, self).RemoveEffect(character)


class MoonlightSummons(Feat):

    def __init__(self, data=None):
        super(MoonlightSummons, self).__init__(data)

    def AddEffect(self, character):
        super(MoonlightSummons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MoonlightSummons, self).RemoveEffect(character)


class MysticStride(Feat):

    def __init__(self, data=None):
        super(MysticStride, self).__init__(data)

    def AddEffect(self, character):
        super(MysticStride, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MysticStride, self).RemoveEffect(character)


class OracularIntuition(Feat):

    def __init__(self, data=None):
        super(OracularIntuition, self).__init__(data)

    def AddEffect(self, character):
        super(OracularIntuition, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OracularIntuition, self).RemoveEffect(character)


class PainfulAnchor(Feat):

    def __init__(self, data=None):
        super(PainfulAnchor, self).__init__(data)

    def AddEffect(self, character):
        super(PainfulAnchor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PainfulAnchor, self).RemoveEffect(character)


class PiercingSpell(Feat):

    def __init__(self, data=None):
        super(PiercingSpell, self).__init__(data)

    def AddEffect(self, character):
        super(PiercingSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PiercingSpell, self).RemoveEffect(character)


class PlanarPreservationist(Feat):

    def __init__(self, data=None):
        super(PlanarPreservationist, self).__init__(data)

    def AddEffect(self, character):
        super(PlanarPreservationist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PlanarPreservationist, self).RemoveEffect(character)


class PowerfulShape(Feat):

    def __init__(self, data=None):
        super(PowerfulShape, self).__init__(data)

    def AddEffect(self, character):
        super(PowerfulShape, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PowerfulShape, self).RemoveEffect(character)


class Prodigy(Feat):

    def __init__(self, data=None):
        super(Prodigy, self).__init__(data)

    def AddEffect(self, character):
        super(Prodigy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Prodigy, self).RemoveEffect(character)


class PropheticVisionary(Feat):

    def __init__(self, data=None):
        super(PropheticVisionary, self).__init__(data)

    def AddEffect(self, character):
        super(PropheticVisionary, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PropheticVisionary, self).RemoveEffect(character)


class PureFaith(Feat):

    def __init__(self, data=None):
        super(PureFaith, self).__init__(data)

    def AddEffect(self, character):
        super(PureFaith, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PureFaith, self).RemoveEffect(character)


class QuarterstaffMaster(Feat):

    def __init__(self, data=None):
        super(QuarterstaffMaster, self).__init__(data)

    def AddEffect(self, character):
        super(QuarterstaffMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuarterstaffMaster, self).RemoveEffect(character)


class QuickChannel(Feat):

    def __init__(self, data=None):
        super(QuickChannel, self).__init__(data)

    def AddEffect(self, character):
        super(QuickChannel, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickChannel, self).RemoveEffect(character)


class QuickWildShape(Feat):

    def __init__(self, data=None):
        super(QuickWildShape, self).__init__(data)

    def AddEffect(self, character):
        super(QuickWildShape, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickWildShape, self).RemoveEffect(character)


class RadiantCharge(Feat):

    def __init__(self, data=None):
        super(RadiantCharge, self).__init__(data)

    def AddEffect(self, character):
        super(RadiantCharge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RadiantCharge, self).RemoveEffect(character)


class RemoteBomb(Feat):

    def __init__(self, data=None):
        super(RemoteBomb, self).__init__(data)

    def AddEffect(self, character):
        super(RemoteBomb, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RemoteBomb, self).RemoveEffect(character)


class ResilientEidolon(Feat):

    def __init__(self, data=None):
        super(ResilientEidolon, self).__init__(data)

    def AddEffect(self, character):
        super(ResilientEidolon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ResilientEidolon, self).RemoveEffect(character)


class RewardOfGrace(Feat):

    def __init__(self, data=None):
        super(RewardOfGrace, self).__init__(data)

    def AddEffect(self, character):
        super(RewardOfGrace, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RewardOfGrace, self).RemoveEffect(character)


class RewardOfLife(Feat):

    def __init__(self, data=None):
        super(RewardOfLife, self).__init__(data)

    def AddEffect(self, character):
        super(RewardOfLife, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RewardOfLife, self).RemoveEffect(character)


class RicochetSplashWeapon(Feat):

    def __init__(self, data=None):
        super(RicochetSplashWeapon, self).__init__(data)

    def AddEffect(self, character):
        super(RicochetSplashWeapon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RicochetSplashWeapon, self).RemoveEffect(character)


class RimeSpell(Feat):

    def __init__(self, data=None):
        super(RimeSpell, self).__init__(data)

    def AddEffect(self, character):
        super(RimeSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RimeSpell, self).RemoveEffect(character)


class SacredSummons(Feat):

    def __init__(self, data=None):
        super(SacredSummons, self).__init__(data)

    def AddEffect(self, character):
        super(SacredSummons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SacredSummons, self).RemoveEffect(character)


class SenseLink(Feat):

    def __init__(self, data=None):
        super(SenseLink, self).__init__(data)

    def AddEffect(self, character):
        super(SenseLink, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SenseLink, self).RemoveEffect(character)


class ShapingFocus(Feat):

    def __init__(self, data=None):
        super(ShapingFocus, self).__init__(data)

    def AddEffect(self, character):
        super(ShapingFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShapingFocus, self).RemoveEffect(character)


class SinSeer(Feat):

    def __init__(self, data=None):
        super(SinSeer, self).__init__(data)

    def AddEffect(self, character):
        super(SinSeer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SinSeer, self).RemoveEffect(character)


class SkeletonSummoner(Feat):

    def __init__(self, data=None):
        super(SkeletonSummoner, self).__init__(data)

    def AddEffect(self, character):
        super(SkeletonSummoner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SkeletonSummoner, self).RemoveEffect(character)


class SorcerousBloodstrike(Feat):

    def __init__(self, data=None):
        super(SorcerousBloodstrike, self).__init__(data)

    def AddEffect(self, character):
        super(SorcerousBloodstrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SorcerousBloodstrike, self).RemoveEffect(character)


class SpellBluff(Feat):

    def __init__(self, data=None):
        super(SpellBluff, self).__init__(data)

    def AddEffect(self, character):
        super(SpellBluff, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellBluff, self).RemoveEffect(character)


class SpellHex(Feat):

    def __init__(self, data=None):
        super(SpellHex, self).__init__(data)

    def AddEffect(self, character):
        super(SpellHex, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellHex, self).RemoveEffect(character)


class SpellSpecialization(Feat):

    def __init__(self, data=None):
        super(SpellSpecialization, self).__init__(data)

    def AddEffect(self, character):
        super(SpellSpecialization, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellSpecialization, self).RemoveEffect(character)


class Spellsong(Feat):

    def __init__(self, data=None):
        super(Spellsong, self).__init__(data)

    def AddEffect(self, character):
        super(Spellsong, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Spellsong, self).RemoveEffect(character)


class SplitHex(Feat):

    def __init__(self, data=None):
        super(SplitHex, self).__init__(data)

    def AddEffect(self, character):
        super(SplitHex, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SplitHex, self).RemoveEffect(character)


class SplitMajorHex(Feat):

    def __init__(self, data=None):
        super(SplitMajorHex, self).__init__(data)

    def AddEffect(self, character):
        super(SplitMajorHex, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SplitMajorHex, self).RemoveEffect(character)


class SpontaneousMetafocus(Feat):

    def __init__(self, data=None):
        super(SpontaneousMetafocus, self).__init__(data)

    def AddEffect(self, character):
        super(SpontaneousMetafocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpontaneousMetafocus, self).RemoveEffect(character)


class StarlightSummons(Feat):

    def __init__(self, data=None):
        super(StarlightSummons, self).__init__(data)

    def AddEffect(self, character):
        super(StarlightSummons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StarlightSummons, self).RemoveEffect(character)


class SunlightSummons(Feat):

    def __init__(self, data=None):
        super(SunlightSummons, self).__init__(data)

    def AddEffect(self, character):
        super(SunlightSummons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SunlightSummons, self).RemoveEffect(character)


class SuperiorSummoning(Feat):

    def __init__(self, data=None):
        super(SuperiorSummoning, self).__init__(data)

    def AddEffect(self, character):
        super(SuperiorSummoning, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SuperiorSummoning, self).RemoveEffect(character)


class ThanatopicSpell(Feat):

    def __init__(self, data=None):
        super(ThanatopicSpell, self).__init__(data)

    def AddEffect(self, character):
        super(ThanatopicSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThanatopicSpell, self).RemoveEffect(character)


class Theurgy(Feat):

    def __init__(self, data=None):
        super(Theurgy, self).__init__(data)

    def AddEffect(self, character):
        super(Theurgy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Theurgy, self).RemoveEffect(character)


class ThoughtfulDiscernment(Feat):

    def __init__(self, data=None):
        super(ThoughtfulDiscernment, self).__init__(data)

    def AddEffect(self, character):
        super(ThoughtfulDiscernment, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThoughtfulDiscernment, self).RemoveEffect(character)


class ThrenodicSpell(Feat):

    def __init__(self, data=None):
        super(ThrenodicSpell, self).__init__(data)

    def AddEffect(self, character):
        super(ThrenodicSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThrenodicSpell, self).RemoveEffect(character)


class TopplingSpell(Feat):

    def __init__(self, data=None):
        super(TopplingSpell, self).__init__(data)

    def AddEffect(self, character):
        super(TopplingSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TopplingSpell, self).RemoveEffect(character)


class TrippingStaff(Feat):

    def __init__(self, data=None):
        super(TrippingStaff, self).__init__(data)

    def AddEffect(self, character):
        super(TrippingStaff, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TrippingStaff, self).RemoveEffect(character)


class TrippingTwirl(Feat):

    def __init__(self, data=None):
        super(TrippingTwirl, self).__init__(data)

    def AddEffect(self, character):
        super(TrippingTwirl, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TrippingTwirl, self).RemoveEffect(character)


class UltimateMercy(Feat):

    def __init__(self, data=None):
        super(UltimateMercy, self).__init__(data)

    def AddEffect(self, character):
        super(UltimateMercy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UltimateMercy, self).RemoveEffect(character)


class UltimateResolve(Feat):

    def __init__(self, data=None):
        super(UltimateResolve, self).__init__(data)

    def AddEffect(self, character):
        super(UltimateResolve, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UltimateResolve, self).RemoveEffect(character)


class UncannyAlertness(Feat):

    def __init__(self, data=None):
        super(UncannyAlertness, self).__init__(data)

    def AddEffect(self, character):
        super(UncannyAlertness, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UncannyAlertness, self).RemoveEffect(character)


class UncannyConcentration(Feat):

    def __init__(self, data=None):
        super(UncannyConcentration, self).__init__(data)

    def AddEffect(self, character):
        super(UncannyConcentration, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UncannyConcentration, self).RemoveEffect(character)


class UndeadMaster(Feat):

    def __init__(self, data=None):
        super(UndeadMaster, self).__init__(data)

    def AddEffect(self, character):
        super(UndeadMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UndeadMaster, self).RemoveEffect(character)


class UnsanctionedDetection(Feat):

    def __init__(self, data=None):
        super(UnsanctionedDetection, self).__init__(data)

    def AddEffect(self, character):
        super(UnsanctionedDetection, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UnsanctionedDetection, self).RemoveEffect(character)


class UnsanctionedKnowledge(Feat):

    def __init__(self, data=None):
        super(UnsanctionedKnowledge, self).__init__(data)

    def AddEffect(self, character):
        super(UnsanctionedKnowledge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UnsanctionedKnowledge, self).RemoveEffect(character)


class VersatileChanneler(Feat):

    def __init__(self, data=None):
        super(VersatileChanneler, self).__init__(data)

    def AddEffect(self, character):
        super(VersatileChanneler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VersatileChanneler, self).RemoveEffect(character)


class VigilantEidolon(Feat):

    def __init__(self, data=None):
        super(VigilantEidolon, self).__init__(data)

    def AddEffect(self, character):
        super(VigilantEidolon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VigilantEidolon, self).RemoveEffect(character)


class VoiceOfTheSibyl(Feat):

    def __init__(self, data=None):
        super(VoiceOfTheSibyl, self).__init__(data)

    def AddEffect(self, character):
        super(VoiceOfTheSibyl, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VoiceOfTheSibyl, self).RemoveEffect(character)


class WarriorPriest(Feat):

    def __init__(self, data=None):
        super(WarriorPriest, self).__init__(data)

    def AddEffect(self, character):
        super(WarriorPriest, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WarriorPriest, self).RemoveEffect(character)


class WildSpeech(Feat):

    def __init__(self, data=None):
        super(WildSpeech, self).__init__(data)

    def AddEffect(self, character):
        super(WildSpeech, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WildSpeech, self).RemoveEffect(character)


class WitchKnife(Feat):

    def __init__(self, data=None):
        super(WitchKnife, self).__init__(data)

    def AddEffect(self, character):
        super(WitchKnife, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WitchKnife, self).RemoveEffect(character)


class WordOfHealing(Feat):

    def __init__(self, data=None):
        super(WordOfHealing, self).__init__(data)

    def AddEffect(self, character):
        super(WordOfHealing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WordOfHealing, self).RemoveEffect(character)


class Brewmaster(Feat):

    def __init__(self, data=None):
        super(Brewmaster, self).__init__(data)

    def AddEffect(self, character):
        super(Brewmaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Brewmaster, self).RemoveEffect(character)


class CleaveThrough(Feat):

    def __init__(self, data=None):
        super(CleaveThrough, self).__init__(data)

    def AddEffect(self, character):
        super(CleaveThrough, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CleaveThrough, self).RemoveEffect(character)


class ClovenHelm(Feat):

    def __init__(self, data=None):
        super(ClovenHelm, self).__init__(data)

    def AddEffect(self, character):
        super(ClovenHelm, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ClovenHelm, self).RemoveEffect(character)


class DentedHelm(Feat):

    def __init__(self, data=None):
        super(DentedHelm, self).__init__(data)

    def AddEffect(self, character):
        super(DentedHelm, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DentedHelm, self).RemoveEffect(character)


class GiantKiller(Feat):

    def __init__(self, data=None):
        super(GiantKiller, self).__init__(data)

    def AddEffect(self, character):
        super(GiantKiller, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GiantKiller, self).RemoveEffect(character)


class GoblinCleaver(Feat):

    def __init__(self, data=None):
        super(GoblinCleaver, self).__init__(data)

    def AddEffect(self, character):
        super(GoblinCleaver, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GoblinCleaver, self).RemoveEffect(character)


class HardHeaded(Feat):

    def __init__(self, data=None):
        super(HardHeaded, self).__init__(data)

    def AddEffect(self, character):
        super(HardHeaded, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HardHeaded, self).RemoveEffect(character)


class LedgeWalker(Feat):

    def __init__(self, data=None):
        super(LedgeWalker, self).__init__(data)

    def AddEffect(self, character):
        super(LedgeWalker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LedgeWalker, self).RemoveEffect(character)


class OrcHewer(Feat):

    def __init__(self, data=None):
        super(OrcHewer, self).__init__(data)

    def AddEffect(self, character):
        super(OrcHewer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OrcHewer, self).RemoveEffect(character)


class Shatterspell(Feat):

    def __init__(self, data=None):
        super(Shatterspell, self).__init__(data)

    def AddEffect(self, character):
        super(Shatterspell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Shatterspell, self).RemoveEffect(character)


class ToxicRecovery(Feat):

    def __init__(self, data=None):
        super(ToxicRecovery, self).__init__(data)

    def AddEffect(self, character):
        super(ToxicRecovery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ToxicRecovery, self).RemoveEffect(character)


class AttunedToTheWild(Feat):

    def __init__(self, data=None):
        super(AttunedToTheWild, self).__init__(data)

    def AddEffect(self, character):
        super(AttunedToTheWild, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AttunedToTheWild, self).RemoveEffect(character)


class ElvenBattleTraining(Feat):

    def __init__(self, data=None):
        super(ElvenBattleTraining, self).__init__(data)

    def AddEffect(self, character):
        super(ElvenBattleTraining, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElvenBattleTraining, self).RemoveEffect(character)


class GuardianOfTheWild(Feat):

    def __init__(self, data=None):
        super(GuardianOfTheWild, self).__init__(data)

    def AddEffect(self, character):
        super(GuardianOfTheWild, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GuardianOfTheWild, self).RemoveEffect(character)


class MageOfTheWild(Feat):

    def __init__(self, data=None):
        super(MageOfTheWild, self).__init__(data)

    def AddEffect(self, character):
        super(MageOfTheWild, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MageOfTheWild, self).RemoveEffect(character)


class SpiritOfTheWild(Feat):

    def __init__(self, data=None):
        super(SpiritOfTheWild, self).__init__(data)

    def AddEffect(self, character):
        super(SpiritOfTheWild, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpiritOfTheWild, self).RemoveEffect(character)


class CasualIllusionist(Feat):

    def __init__(self, data=None):
        super(CasualIllusionist, self).__init__(data)

    def AddEffect(self, character):
        super(CasualIllusionist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CasualIllusionist, self).RemoveEffect(character)


class ExpandedResistance(Feat):

    def __init__(self, data=None):
        super(ExpandedResistance, self).__init__(data)

    def AddEffect(self, character):
        super(ExpandedResistance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExpandedResistance, self).RemoveEffect(character)


class GnomeWeaponFocus(Feat):

    def __init__(self, data=None):
        super(GnomeWeaponFocus, self).__init__(data)

    def AddEffect(self, character):
        super(GnomeWeaponFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GnomeWeaponFocus, self).RemoveEffect(character)


class GreatHatred(Feat):

    def __init__(self, data=None):
        super(GreatHatred, self).__init__(data)

    def AddEffect(self, character):
        super(GreatHatred, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreatHatred, self).RemoveEffect(character)


class VastHatred(Feat):

    def __init__(self, data=None):
        super(VastHatred, self).__init__(data)

    def AddEffect(self, character):
        super(VastHatred, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VastHatred, self).RemoveEffect(character)


class DiscerningEye(Feat):

    def __init__(self, data=None):
        super(DiscerningEye, self).__init__(data)

    def AddEffect(self, character):
        super(DiscerningEye, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DiscerningEye, self).RemoveEffect(character)


class ElvenSpirit(Feat):

    def __init__(self, data=None):
        super(ElvenSpirit, self).__init__(data)

    def AddEffect(self, character):
        super(ElvenSpirit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElvenSpirit, self).RemoveEffect(character)


class ExileSPath(Feat):

    def __init__(self, data=None):
        super(ExileSPath, self).__init__(data)

    def AddEffect(self, character):
        super(ExileSPath, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExileSPath, self).RemoveEffect(character)


class HalfDrowParagon(Feat):

    def __init__(self, data=None):
        super(HalfDrowParagon, self).__init__(data)

    def AddEffect(self, character):
        super(HalfDrowParagon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HalfDrowParagon, self).RemoveEffect(character)


class HumanSpirit(Feat):

    def __init__(self, data=None):
        super(HumanSpirit, self).__init__(data)

    def AddEffect(self, character):
        super(HumanSpirit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HumanSpirit, self).RemoveEffect(character)


class MultitalentedMastery(Feat):

    def __init__(self, data=None):
        super(MultitalentedMastery, self).__init__(data)

    def AddEffect(self, character):
        super(MultitalentedMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MultitalentedMastery, self).RemoveEffect(character)


class NeitherElfNorHuman(Feat):

    def __init__(self, data=None):
        super(NeitherElfNorHuman, self).__init__(data)

    def AddEffect(self, character):
        super(NeitherElfNorHuman, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NeitherElfNorHuman, self).RemoveEffect(character)


class SeenAndUnseen(Feat):

    def __init__(self, data=None):
        super(SeenAndUnseen, self).__init__(data)

    def AddEffect(self, character):
        super(SeenAndUnseen, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SeenAndUnseen, self).RemoveEffect(character)


class SharedManipulation(Feat):

    def __init__(self, data=None):
        super(SharedManipulation, self).__init__(data)

    def AddEffect(self, character):
        super(SharedManipulation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SharedManipulation, self).RemoveEffect(character)


class BeastRider(Feat):

    def __init__(self, data=None):
        super(BeastRider, self).__init__(data)

    def AddEffect(self, character):
        super(BeastRider, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BeastRider, self).RemoveEffect(character)


class BloodVengeance(Feat):

    def __init__(self, data=None):
        super(BloodVengeance, self).__init__(data)

    def AddEffect(self, character):
        super(BloodVengeance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodVengeance, self).RemoveEffect(character)


class DestroyerSBlessing(Feat):

    def __init__(self, data=None):
        super(DestroyerSBlessing, self).__init__(data)

    def AddEffect(self, character):
        super(DestroyerSBlessing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DestroyerSBlessing, self).RemoveEffect(character)


class FerociousResolve(Feat):

    def __init__(self, data=None):
        super(FerociousResolve, self).__init__(data)

    def AddEffect(self, character):
        super(FerociousResolve, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FerociousResolve, self).RemoveEffect(character)


class FerociousSummons(Feat):

    def __init__(self, data=None):
        super(FerociousSummons, self).__init__(data)

    def AddEffect(self, character):
        super(FerociousSummons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FerociousSummons, self).RemoveEffect(character)


class FerociousTenacity(Feat):

    def __init__(self, data=None):
        super(FerociousTenacity, self).__init__(data)

    def AddEffect(self, character):
        super(FerociousTenacity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FerociousTenacity, self).RemoveEffect(character)


class GoreFiend(Feat):

    def __init__(self, data=None):
        super(GoreFiend, self).__init__(data)

    def AddEffect(self, character):
        super(GoreFiend, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GoreFiend, self).RemoveEffect(character)


class HordeCharge(Feat):

    def __init__(self, data=None):
        super(HordeCharge, self).__init__(data)

    def AddEffect(self, character):
        super(HordeCharge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HordeCharge, self).RemoveEffect(character)


class ImprovedSurpriseFollowThrough(Feat):

    def __init__(self, data=None):
        super(ImprovedSurpriseFollowThrough, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedSurpriseFollowThrough, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedSurpriseFollowThrough, self).RemoveEffect(character)


class ResilientBrute(Feat):

    def __init__(self, data=None):
        super(ResilientBrute, self).__init__(data)

    def AddEffect(self, character):
        super(ResilientBrute, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ResilientBrute, self).RemoveEffect(character)


class SurpriseFollowThrough(Feat):

    def __init__(self, data=None):
        super(SurpriseFollowThrough, self).__init__(data)

    def AddEffect(self, character):
        super(SurpriseFollowThrough, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SurpriseFollowThrough, self).RemoveEffect(character)


class SympatheticRage(Feat):

    def __init__(self, data=None):
        super(SympatheticRage, self).__init__(data)

    def AddEffect(self, character):
        super(SympatheticRage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SympatheticRage, self).RemoveEffect(character)


class TenaciousSurvivor(Feat):

    def __init__(self, data=None):
        super(TenaciousSurvivor, self).__init__(data)

    def AddEffect(self, character):
        super(TenaciousSurvivor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TenaciousSurvivor, self).RemoveEffect(character)


class ThrillOfTheKill(Feat):

    def __init__(self, data=None):
        super(ThrillOfTheKill, self).__init__(data)

    def AddEffect(self, character):
        super(ThrillOfTheKill, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThrillOfTheKill, self).RemoveEffect(character)


class AdaptiveFortune(Feat):

    def __init__(self, data=None):
        super(AdaptiveFortune, self).__init__(data)

    def AddEffect(self, character):
        super(AdaptiveFortune, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AdaptiveFortune, self).RemoveEffect(character)


class BlunderingDefense(Feat):

    def __init__(self, data=None):
        super(BlunderingDefense, self).__init__(data)

    def AddEffect(self, character):
        super(BlunderingDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlunderingDefense, self).RemoveEffect(character)


class CautiousFighter(Feat):

    def __init__(self, data=None):
        super(CautiousFighter, self).__init__(data)

    def AddEffect(self, character):
        super(CautiousFighter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CautiousFighter, self).RemoveEffect(character)


class CourageousResolve(Feat):

    def __init__(self, data=None):
        super(CourageousResolve, self).__init__(data)

    def AddEffect(self, character):
        super(CourageousResolve, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CourageousResolve, self).RemoveEffect(character)


class DesperateSwing(Feat):

    def __init__(self, data=None):
        super(DesperateSwing, self).__init__(data)

    def AddEffect(self, character):
        super(DesperateSwing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DesperateSwing, self).RemoveEffect(character)


class FortunateOne(Feat):

    def __init__(self, data=None):
        super(FortunateOne, self).__init__(data)

    def AddEffect(self, character):
        super(FortunateOne, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FortunateOne, self).RemoveEffect(character)


class ImprovedLowBlow(Feat):

    def __init__(self, data=None):
        super(ImprovedLowBlow, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedLowBlow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedLowBlow, self).RemoveEffect(character)


class LuckyHealer(Feat):

    def __init__(self, data=None):
        super(LuckyHealer, self).__init__(data)

    def AddEffect(self, character):
        super(LuckyHealer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LuckyHealer, self).RemoveEffect(character)


class LuckyStrike(Feat):

    def __init__(self, data=None):
        super(LuckyStrike, self).__init__(data)

    def AddEffect(self, character):
        super(LuckyStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LuckyStrike, self).RemoveEffect(character)


class RiskyStriker(Feat):

    def __init__(self, data=None):
        super(RiskyStriker, self).__init__(data)

    def AddEffect(self, character):
        super(RiskyStriker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RiskyStriker, self).RemoveEffect(character)


class SureAndFleet(Feat):

    def __init__(self, data=None):
        super(SureAndFleet, self).__init__(data)

    def AddEffect(self, character):
        super(SureAndFleet, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SureAndFleet, self).RemoveEffect(character)


class SurpriseStrike(Feat):

    def __init__(self, data=None):
        super(SurpriseStrike, self).__init__(data)

    def AddEffect(self, character):
        super(SurpriseStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SurpriseStrike, self).RemoveEffect(character)


class UncannyDefense(Feat):

    def __init__(self, data=None):
        super(UncannyDefense, self).__init__(data)

    def AddEffect(self, character):
        super(UncannyDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UncannyDefense, self).RemoveEffect(character)


class BestowLuck(Feat):

    def __init__(self, data=None):
        super(BestowLuck, self).__init__(data)

    def AddEffect(self, character):
        super(BestowLuck, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BestowLuck, self).RemoveEffect(character)


class CriticalVersatility(Feat):

    def __init__(self, data=None):
        super(CriticalVersatility, self).__init__(data)

    def AddEffect(self, character):
        super(CriticalVersatility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CriticalVersatility, self).RemoveEffect(character)


class DauntlessDestiny(Feat):

    def __init__(self, data=None):
        super(DauntlessDestiny, self).__init__(data)

    def AddEffect(self, character):
        super(DauntlessDestiny, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DauntlessDestiny, self).RemoveEffect(character)


class DefiantLuck(Feat):

    def __init__(self, data=None):
        super(DefiantLuck, self).__init__(data)

    def AddEffect(self, character):
        super(DefiantLuck, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DefiantLuck, self).RemoveEffect(character)


class FastLearner(Feat):

    def __init__(self, data=None):
        super(FastLearner, self).__init__(data)

    def AddEffect(self, character):
        super(FastLearner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FastLearner, self).RemoveEffect(character)


class FearlessCuriosity(Feat):

    def __init__(self, data=None):
        super(FearlessCuriosity, self).__init__(data)

    def AddEffect(self, character):
        super(FearlessCuriosity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FearlessCuriosity, self).RemoveEffect(character)


class HeroicWill(Feat):

    def __init__(self, data=None):
        super(HeroicWill, self).__init__(data)

    def AddEffect(self, character):
        super(HeroicWill, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HeroicWill, self).RemoveEffect(character)


class Huntmaster(Feat):

    def __init__(self, data=None):
        super(Huntmaster, self).__init__(data)

    def AddEffect(self, character):
        super(Huntmaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Huntmaster, self).RemoveEffect(character)


class ImprovedImprovisation(Feat):

    def __init__(self, data=None):
        super(ImprovedImprovisation, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedImprovisation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedImprovisation, self).RemoveEffect(character)


class Improvisation(Feat):

    def __init__(self, data=None):
        super(Improvisation, self).__init__(data)

    def AddEffect(self, character):
        super(Improvisation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Improvisation, self).RemoveEffect(character)


class InexplicableLuck(Feat):

    def __init__(self, data=None):
        super(InexplicableLuck, self).__init__(data)

    def AddEffect(self, character):
        super(InexplicableLuck, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InexplicableLuck, self).RemoveEffect(character)


class IntimidatingConfidence(Feat):

    def __init__(self, data=None):
        super(IntimidatingConfidence, self).__init__(data)

    def AddEffect(self, character):
        super(IntimidatingConfidence, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(IntimidatingConfidence, self).RemoveEffect(character)


class MartialMastery(Feat):

    def __init__(self, data=None):
        super(MartialMastery, self).__init__(data)

    def AddEffect(self, character):
        super(MartialMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MartialMastery, self).RemoveEffect(character)


class MartialVersatility(Feat):

    def __init__(self, data=None):
        super(MartialVersatility, self).__init__(data)

    def AddEffect(self, character):
        super(MartialVersatility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MartialVersatility, self).RemoveEffect(character)


class SurgeOfSuccess(Feat):

    def __init__(self, data=None):
        super(SurgeOfSuccess, self).__init__(data)

    def AddEffect(self, character):
        super(SurgeOfSuccess, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SurgeOfSuccess, self).RemoveEffect(character)


class AngelWings(Feat):

    def __init__(self, data=None):
        super(AngelWings, self).__init__(data)

    def AddEffect(self, character):
        super(AngelWings, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AngelWings, self).RemoveEffect(character)


class AngelicBlood(Feat):

    def __init__(self, data=None):
        super(AngelicBlood, self).__init__(data)

    def AddEffect(self, character):
        super(AngelicBlood, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AngelicBlood, self).RemoveEffect(character)


class AngelicFlesh(Feat):

    def __init__(self, data=None):
        super(AngelicFlesh, self).__init__(data)

    def AddEffect(self, character):
        super(AngelicFlesh, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AngelicFlesh, self).RemoveEffect(character)


class CelestialServant(Feat):

    def __init__(self, data=None):
        super(CelestialServant, self).__init__(data)

    def AddEffect(self, character):
        super(CelestialServant, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CelestialServant, self).RemoveEffect(character)


class ChannelForce(Feat):

    def __init__(self, data=None):
        super(ChannelForce, self).__init__(data)

    def AddEffect(self, character):
        super(ChannelForce, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ChannelForce, self).RemoveEffect(character)


class GreaterChannelForce(Feat):

    def __init__(self, data=None):
        super(GreaterChannelForce, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterChannelForce, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterChannelForce, self).RemoveEffect(character)


class HeavenlyRadiance(Feat):

    def __init__(self, data=None):
        super(HeavenlyRadiance, self).__init__(data)

    def AddEffect(self, character):
        super(HeavenlyRadiance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HeavenlyRadiance, self).RemoveEffect(character)


class ImprovedChannelForce(Feat):

    def __init__(self, data=None):
        super(ImprovedChannelForce, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedChannelForce, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedChannelForce, self).RemoveEffect(character)


class MetallicWings(Feat):

    def __init__(self, data=None):
        super(MetallicWings, self).__init__(data)

    def AddEffect(self, character):
        super(MetallicWings, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MetallicWings, self).RemoveEffect(character)


class BlackCat(Feat):

    def __init__(self, data=None):
        super(BlackCat, self).__init__(data)

    def AddEffect(self, character):
        super(BlackCat, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlackCat, self).RemoveEffect(character)


class CatfolkExemplar(Feat):

    def __init__(self, data=None):
        super(CatfolkExemplar, self).__init__(data)

    def AddEffect(self, character):
        super(CatfolkExemplar, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CatfolkExemplar, self).RemoveEffect(character)


class ClawPounce(Feat):

    def __init__(self, data=None):
        super(ClawPounce, self).__init__(data)

    def AddEffect(self, character):
        super(ClawPounce, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ClawPounce, self).RemoveEffect(character)


class FelineGrace(Feat):

    def __init__(self, data=None):
        super(FelineGrace, self).__init__(data)

    def AddEffect(self, character):
        super(FelineGrace, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FelineGrace, self).RemoveEffect(character)


class NimbleStriker(Feat):

    def __init__(self, data=None):
        super(NimbleStriker, self).__init__(data)

    def AddEffect(self, character):
        super(NimbleStriker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NimbleStriker, self).RemoveEffect(character)


class BloodDrinker(Feat):

    def __init__(self, data=None):
        super(BloodDrinker, self).__init__(data)

    def AddEffect(self, character):
        super(BloodDrinker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodDrinker, self).RemoveEffect(character)


class BloodFeaster(Feat):

    def __init__(self, data=None):
        super(BloodFeaster, self).__init__(data)

    def AddEffect(self, character):
        super(BloodFeaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodFeaster, self).RemoveEffect(character)


class BloodSalvage(Feat):

    def __init__(self, data=None):
        super(BloodSalvage, self).__init__(data)

    def AddEffect(self, character):
        super(BloodSalvage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodSalvage, self).RemoveEffect(character)


class DiversePalate(Feat):

    def __init__(self, data=None):
        super(DiversePalate, self).__init__(data)

    def AddEffect(self, character):
        super(DiversePalate, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DiversePalate, self).RemoveEffect(character)


class NaturalCharmer(Feat):

    def __init__(self, data=None):
        super(NaturalCharmer, self).__init__(data)

    def AddEffect(self, character):
        super(NaturalCharmer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NaturalCharmer, self).RemoveEffect(character)


class DrowNobility(Feat):

    def __init__(self, data=None):
        super(DrowNobility, self).__init__(data)

    def AddEffect(self, character):
        super(DrowNobility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DrowNobility, self).RemoveEffect(character)


class GreaterDrowNobility(Feat):

    def __init__(self, data=None):
        super(GreaterDrowNobility, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterDrowNobility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterDrowNobility, self).RemoveEffect(character)


class ImprovedDrowNobility(Feat):

    def __init__(self, data=None):
        super(ImprovedDrowNobility, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedDrowNobility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedDrowNobility, self).RemoveEffect(character)


class ImprovedUmbralScion(Feat):

    def __init__(self, data=None):
        super(ImprovedUmbralScion, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedUmbralScion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedUmbralScion, self).RemoveEffect(character)


class NobleSpellResistance(Feat):

    def __init__(self, data=None):
        super(NobleSpellResistance, self).__init__(data)

    def AddEffect(self, character):
        super(NobleSpellResistance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NobleSpellResistance, self).RemoveEffect(character)


class ShadowCaster(Feat):

    def __init__(self, data=None):
        super(ShadowCaster, self).__init__(data)

    def AddEffect(self, character):
        super(ShadowCaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadowCaster, self).RemoveEffect(character)


class SpiderStep(Feat):

    def __init__(self, data=None):
        super(SpiderStep, self).__init__(data)

    def AddEffect(self, character):
        super(SpiderStep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpiderStep, self).RemoveEffect(character)


class SpiderSummoner(Feat):

    def __init__(self, data=None):
        super(SpiderSummoner, self).__init__(data)

    def AddEffect(self, character):
        super(SpiderSummoner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpiderSummoner, self).RemoveEffect(character)


class UmbralScion(Feat):

    def __init__(self, data=None):
        super(UmbralScion, self).__init__(data)

    def AddEffect(self, character):
        super(UmbralScion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UmbralScion, self).RemoveEffect(character)


class NaturalJouster(Feat):

    def __init__(self, data=None):
        super(NaturalJouster, self).__init__(data)

    def AddEffect(self, character):
        super(NaturalJouster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NaturalJouster, self).RemoveEffect(character)


class LastwallPhalanx(Feat):

    def __init__(self, data=None):
        super(LastwallPhalanx, self).__init__(data)

    def AddEffect(self, character):
        super(LastwallPhalanx, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LastwallPhalanx, self).RemoveEffect(character)


class LastwallPhalanx(Feat):

    def __init__(self, data=None):
        super(LastwallPhalanx, self).__init__(data)

    def AddEffect(self, character):
        super(LastwallPhalanx, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LastwallPhalanx, self).RemoveEffect(character)


class LegacyOfOzem(Feat):

    def __init__(self, data=None):
        super(LegacyOfOzem, self).__init__(data)

    def AddEffect(self, character):
        super(LegacyOfOzem, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LegacyOfOzem, self).RemoveEffect(character)


class Peacemaker(Feat):

    def __init__(self, data=None):
        super(Peacemaker, self).__init__(data)

    def AddEffect(self, character):
        super(Peacemaker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Peacemaker, self).RemoveEffect(character)


class SiphonPoison(Feat):

    def __init__(self, data=None):
        super(SiphonPoison, self).__init__(data)

    def AddEffect(self, character):
        super(SiphonPoison, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SiphonPoison, self).RemoveEffect(character)


class WorldwoundWalker(Feat):

    def __init__(self, data=None):
        super(WorldwoundWalker, self).__init__(data)

    def AddEffect(self, character):
        super(WorldwoundWalker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WorldwoundWalker, self).RemoveEffect(character)


class DarkSight(Feat):

    def __init__(self, data=None):
        super(DarkSight, self).__init__(data)

    def AddEffect(self, character):
        super(DarkSight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DarkSight, self).RemoveEffect(character)


class GloomSight(Feat):

    def __init__(self, data=None):
        super(GloomSight, self).__init__(data)

    def AddEffect(self, character):
        super(GloomSight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GloomSight, self).RemoveEffect(character)


class GloomStrike(Feat):

    def __init__(self, data=None):
        super(GloomStrike, self).__init__(data)

    def AddEffect(self, character):
        super(GloomStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GloomStrike, self).RemoveEffect(character)


class ImprovedDarkSight(Feat):

    def __init__(self, data=None):
        super(ImprovedDarkSight, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedDarkSight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedDarkSight, self).RemoveEffect(character)


class ShadowGhost(Feat):

    def __init__(self, data=None):
        super(ShadowGhost, self).__init__(data)

    def AddEffect(self, character):
        super(ShadowGhost, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadowGhost, self).RemoveEffect(character)


class ShadowWalker(Feat):

    def __init__(self, data=None):
        super(ShadowWalker, self).__init__(data)

    def AddEffect(self, character):
        super(ShadowWalker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadowWalker, self).RemoveEffect(character)


class BurnBurnBurn(Feat):

    def __init__(self, data=None):
        super(BurnBurnBurn, self).__init__(data)

    def AddEffect(self, character):
        super(BurnBurnBurn, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BurnBurnBurn, self).RemoveEffect(character)


class FireHand(Feat):

    def __init__(self, data=None):
        super(FireHand, self).__init__(data)

    def AddEffect(self, character):
        super(FireHand, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FireHand, self).RemoveEffect(character)


class FireTamer(Feat):

    def __init__(self, data=None):
        super(FireTamer, self).__init__(data)

    def AddEffect(self, character):
        super(FireTamer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FireTamer, self).RemoveEffect(character)


class FlameHeart(Feat):

    def __init__(self, data=None):
        super(FlameHeart, self).__init__(data)

    def AddEffect(self, character):
        super(FlameHeart, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FlameHeart, self).RemoveEffect(character)


class GoblinGunslinger(Feat):

    def __init__(self, data=None):
        super(GoblinGunslinger, self).__init__(data)

    def AddEffect(self, character):
        super(GoblinGunslinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GoblinGunslinger, self).RemoveEffect(character)


class TangleFeet(Feat):

    def __init__(self, data=None):
        super(TangleFeet, self).__init__(data)

    def AddEffect(self, character):
        super(TangleFeet, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TangleFeet, self).RemoveEffect(character)


class DeafeningExplosion(Feat):

    def __init__(self, data=None):
        super(DeafeningExplosion, self).__init__(data)

    def AddEffect(self, character):
        super(DeafeningExplosion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeafeningExplosion, self).RemoveEffect(character)


class DemoralizingLash(Feat):

    def __init__(self, data=None):
        super(DemoralizingLash, self).__init__(data)

    def AddEffect(self, character):
        super(DemoralizingLash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DemoralizingLash, self).RemoveEffect(character)


class FocusingBlow(Feat):

    def __init__(self, data=None):
        super(FocusingBlow, self).__init__(data)

    def AddEffect(self, character):
        super(FocusingBlow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FocusingBlow, self).RemoveEffect(character)


class HobgoblinDiscipline(Feat):

    def __init__(self, data=None):
        super(HobgoblinDiscipline, self).__init__(data)

    def AddEffect(self, character):
        super(HobgoblinDiscipline, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HobgoblinDiscipline, self).RemoveEffect(character)


class Taskmaster(Feat):

    def __init__(self, data=None):
        super(Taskmaster, self).__init__(data)

    def AddEffect(self, character):
        super(Taskmaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Taskmaster, self).RemoveEffect(character)


class TerrorizingDisplay(Feat):

    def __init__(self, data=None):
        super(TerrorizingDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(TerrorizingDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TerrorizingDisplay, self).RemoveEffect(character)


class BlazingAura(Feat):

    def __init__(self, data=None):
        super(BlazingAura, self).__init__(data)

    def AddEffect(self, character):
        super(BlazingAura, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlazingAura, self).RemoveEffect(character)


class BlisteringFeint(Feat):

    def __init__(self, data=None):
        super(BlisteringFeint, self).__init__(data)

    def AddEffect(self, character):
        super(BlisteringFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlisteringFeint, self).RemoveEffect(character)


class ElementalJaunt(Feat):

    def __init__(self, data=None):
        super(ElementalJaunt, self).__init__(data)

    def AddEffect(self, character):
        super(ElementalJaunt, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElementalJaunt, self).RemoveEffect(character)


class Firesight(Feat):

    def __init__(self, data=None):
        super(Firesight, self).__init__(data)

    def AddEffect(self, character):
        super(Firesight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Firesight, self).RemoveEffect(character)


class InnerFlame(Feat):

    def __init__(self, data=None):
        super(InnerFlame, self).__init__(data)

    def AddEffect(self, character):
        super(InnerFlame, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InnerFlame, self).RemoveEffect(character)


class ScorchingWeapons(Feat):

    def __init__(self, data=None):
        super(ScorchingWeapons, self).__init__(data)

    def AddEffect(self, character):
        super(ScorchingWeapons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ScorchingWeapons, self).RemoveEffect(character)


class DraconicAspect(Feat):

    def __init__(self, data=None):
        super(DraconicAspect, self).__init__(data)

    def AddEffect(self, character):
        super(DraconicAspect, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DraconicAspect, self).RemoveEffect(character)


class DraconicBreath(Feat):

    def __init__(self, data=None):
        super(DraconicBreath, self).__init__(data)

    def AddEffect(self, character):
        super(DraconicBreath, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DraconicBreath, self).RemoveEffect(character)


class DraconicGlide(Feat):

    def __init__(self, data=None):
        super(DraconicGlide, self).__init__(data)

    def AddEffect(self, character):
        super(DraconicGlide, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DraconicGlide, self).RemoveEffect(character)


class DraconicParagon(Feat):

    def __init__(self, data=None):
        super(DraconicParagon, self).__init__(data)

    def AddEffect(self, character):
        super(DraconicParagon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DraconicParagon, self).RemoveEffect(character)


class KoboldAmbusher(Feat):

    def __init__(self, data=None):
        super(KoboldAmbusher, self).__init__(data)

    def AddEffect(self, character):
        super(KoboldAmbusher, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KoboldAmbusher, self).RemoveEffect(character)


class KoboldSniper(Feat):

    def __init__(self, data=None):
        super(KoboldSniper, self).__init__(data)

    def AddEffect(self, character):
        super(KoboldSniper, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KoboldSniper, self).RemoveEffect(character)


class TailTerror(Feat):

    def __init__(self, data=None):
        super(TailTerror, self).__init__(data)

    def AddEffect(self, character):
        super(TailTerror, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TailTerror, self).RemoveEffect(character)


class BornAlone(Feat):

    def __init__(self, data=None):
        super(BornAlone, self).__init__(data)

    def AddEffect(self, character):
        super(BornAlone, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BornAlone, self).RemoveEffect(character)


class BullyingBlow(Feat):

    def __init__(self, data=None):
        super(BullyingBlow, self).__init__(data)

    def AddEffect(self, character):
        super(BullyingBlow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BullyingBlow, self).RemoveEffect(character)


class FerociousAction(Feat):

    def __init__(self, data=None):
        super(FerociousAction, self).__init__(data)

    def AddEffect(self, character):
        super(FerociousAction, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FerociousAction, self).RemoveEffect(character)


class FomentTheBlood(Feat):

    def __init__(self, data=None):
        super(FomentTheBlood, self).__init__(data)

    def AddEffect(self, character):
        super(FomentTheBlood, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FomentTheBlood, self).RemoveEffect(character)


class GrudgeFighter(Feat):

    def __init__(self, data=None):
        super(GrudgeFighter, self).__init__(data)

    def AddEffect(self, character):
        super(GrudgeFighter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GrudgeFighter, self).RemoveEffect(character)


class OrcWeaponExpertise(Feat):

    def __init__(self, data=None):
        super(OrcWeaponExpertise, self).__init__(data)

    def AddEffect(self, character):
        super(OrcWeaponExpertise, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OrcWeaponExpertise, self).RemoveEffect(character)


class ResoluteRager(Feat):

    def __init__(self, data=None):
        super(ResoluteRager, self).__init__(data)

    def AddEffect(self, character):
        super(ResoluteRager, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ResoluteRager, self).RemoveEffect(character)


class ReverseFeint(Feat):

    def __init__(self, data=None):
        super(ReverseFeint, self).__init__(data)

    def AddEffect(self, character):
        super(ReverseFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ReverseFeint, self).RemoveEffect(character)


class TrapWrecker(Feat):

    def __init__(self, data=None):
        super(TrapWrecker, self).__init__(data)

    def AddEffect(self, character):
        super(TrapWrecker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TrapWrecker, self).RemoveEffect(character)


class DwarfBlooded(Feat):

    def __init__(self, data=None):
        super(DwarfBlooded, self).__init__(data)

    def AddEffect(self, character):
        super(DwarfBlooded, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DwarfBlooded, self).RemoveEffect(character)


class EchoesOfStone(Feat):

    def __init__(self, data=None):
        super(EchoesOfStone, self).__init__(data)

    def AddEffect(self, character):
        super(EchoesOfStone, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EchoesOfStone, self).RemoveEffect(character)


class MurmursOfEarth(Feat):

    def __init__(self, data=None):
        super(MurmursOfEarth, self).__init__(data)

    def AddEffect(self, character):
        super(MurmursOfEarth, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MurmursOfEarth, self).RemoveEffect(character)


class OreadBurrower(Feat):

    def __init__(self, data=None):
        super(OreadBurrower, self).__init__(data)

    def AddEffect(self, character):
        super(OreadBurrower, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OreadBurrower, self).RemoveEffect(character)


class OreadEarthGlider(Feat):

    def __init__(self, data=None):
        super(OreadEarthGlider, self).__init__(data)

    def AddEffect(self, character):
        super(OreadEarthGlider, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OreadEarthGlider, self).RemoveEffect(character)


class StonyStep(Feat):

    def __init__(self, data=None):
        super(StonyStep, self).__init__(data)

    def AddEffect(self, character):
        super(StonyStep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StonyStep, self).RemoveEffect(character)


class BurrowingTeeth(Feat):

    def __init__(self, data=None):
        super(BurrowingTeeth, self).__init__(data)

    def AddEffect(self, character):
        super(BurrowingTeeth, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BurrowingTeeth, self).RemoveEffect(character)


class Sharpclaw(Feat):

    def __init__(self, data=None):
        super(Sharpclaw, self).__init__(data)

    def AddEffect(self, character):
        super(Sharpclaw, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Sharpclaw, self).RemoveEffect(character)


class TunnelRat(Feat):

    def __init__(self, data=None):
        super(TunnelRat, self).__init__(data)

    def AddEffect(self, character):
        super(TunnelRat, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TunnelRat, self).RemoveEffect(character)


class AiryStep(Feat):

    def __init__(self, data=None):
        super(AiryStep, self).__init__(data)

    def AddEffect(self, character):
        super(AiryStep, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AiryStep, self).RemoveEffect(character)


class CloudGazer(Feat):

    def __init__(self, data=None):
        super(CloudGazer, self).__init__(data)

    def AddEffect(self, character):
        super(CloudGazer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CloudGazer, self).RemoveEffect(character)


class InnerBreath(Feat):

    def __init__(self, data=None):
        super(InnerBreath, self).__init__(data)

    def AddEffect(self, character):
        super(InnerBreath, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InnerBreath, self).RemoveEffect(character)


class WingsOfAir(Feat):

    def __init__(self, data=None):
        super(WingsOfAir, self).__init__(data)

    def AddEffect(self, character):
        super(WingsOfAir, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WingsOfAir, self).RemoveEffect(character)


class BloodBeak(Feat):

    def __init__(self, data=None):
        super(BloodBeak, self).__init__(data)

    def AddEffect(self, character):
        super(BloodBeak, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodBeak, self).RemoveEffect(character)


class CarrionFeeder(Feat):

    def __init__(self, data=None):
        super(CarrionFeeder, self).__init__(data)

    def AddEffect(self, character):
        super(CarrionFeeder, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CarrionFeeder, self).RemoveEffect(character)


class LongNoseForm(Feat):

    def __init__(self, data=None):
        super(LongNoseForm, self).__init__(data)

    def AddEffect(self, character):
        super(LongNoseForm, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LongNoseForm, self).RemoveEffect(character)


class ScavengerSEye(Feat):

    def __init__(self, data=None):
        super(ScavengerSEye, self).__init__(data)

    def AddEffect(self, character):
        super(ScavengerSEye, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ScavengerSEye, self).RemoveEffect(character)


class TenguRavenForm(Feat):

    def __init__(self, data=None):
        super(TenguRavenForm, self).__init__(data)

    def AddEffect(self, character):
        super(TenguRavenForm, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TenguRavenForm, self).RemoveEffect(character)


class TenguWings(Feat):

    def __init__(self, data=None):
        super(TenguWings, self).__init__(data)

    def AddEffect(self, character):
        super(TenguWings, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TenguWings, self).RemoveEffect(character)


class ArmorOfThePit(Feat):

    def __init__(self, data=None):
        super(ArmorOfThePit, self).__init__(data)

    def AddEffect(self, character):
        super(ArmorOfThePit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArmorOfThePit, self).RemoveEffect(character)


class ExpandedFiendishResistance(Feat):

    def __init__(self, data=None):
        super(ExpandedFiendishResistance, self).__init__(data)

    def AddEffect(self, character):
        super(ExpandedFiendishResistance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExpandedFiendishResistance, self).RemoveEffect(character)


class FiendSight(Feat):

    def __init__(self, data=None):
        super(FiendSight, self).__init__(data)

    def AddEffect(self, character):
        super(FiendSight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FiendSight, self).RemoveEffect(character)


class GraspingTail(Feat):

    def __init__(self, data=None):
        super(GraspingTail, self).__init__(data)

    def AddEffect(self, character):
        super(GraspingTail, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GraspingTail, self).RemoveEffect(character)


class AquaticAncestry(Feat):

    def __init__(self, data=None):
        super(AquaticAncestry, self).__init__(data)

    def AddEffect(self, character):
        super(AquaticAncestry, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AquaticAncestry, self).RemoveEffect(character)


class HydraulicManeuver(Feat):

    def __init__(self, data=None):
        super(HydraulicManeuver, self).__init__(data)

    def AddEffect(self, character):
        super(HydraulicManeuver, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HydraulicManeuver, self).RemoveEffect(character)


class SteamCaster(Feat):

    def __init__(self, data=None):
        super(SteamCaster, self).__init__(data)

    def AddEffect(self, character):
        super(SteamCaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SteamCaster, self).RemoveEffect(character)


class TritonPortal(Feat):

    def __init__(self, data=None):
        super(TritonPortal, self).__init__(data)

    def AddEffect(self, character):
        super(TritonPortal, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TritonPortal, self).RemoveEffect(character)


class WaterSkinned(Feat):

    def __init__(self, data=None):
        super(WaterSkinned, self).__init__(data)

    def AddEffect(self, character):
        super(WaterSkinned, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WaterSkinned, self).RemoveEffect(character)


class MotherSGift(Feat):

    def __init__(self, data=None):
        super(MotherSGift, self).__init__(data)

    def AddEffect(self, character):
        super(MotherSGift, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MotherSGift, self).RemoveEffect(character)


class GiantSteps(Feat):

    def __init__(self, data=None):
        super(GiantSteps, self).__init__(data)

    def AddEffect(self, character):
        super(GiantSteps, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GiantSteps, self).RemoveEffect(character)


class LingeringInvisibility(Feat):

    def __init__(self, data=None):
        super(LingeringInvisibility, self).__init__(data)

    def AddEffect(self, character):
        super(LingeringInvisibility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LingeringInvisibility, self).RemoveEffect(character)


class AgileTongue(Feat):

    def __init__(self, data=None):
        super(AgileTongue, self).__init__(data)

    def AddEffect(self, character):
        super(AgileTongue, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AgileTongue, self).RemoveEffect(character)


class MagicalTail(Feat):

    def __init__(self, data=None):
        super(MagicalTail, self).__init__(data)

    def AddEffect(self, character):
        super(MagicalTail, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MagicalTail, self).RemoveEffect(character)


class RealisticLikeness(Feat):

    def __init__(self, data=None):
        super(RealisticLikeness, self).__init__(data)

    def AddEffect(self, character):
        super(RealisticLikeness, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RealisticLikeness, self).RemoveEffect(character)


class SeaHunter(Feat):

    def __init__(self, data=None):
        super(SeaHunter, self).__init__(data)

    def AddEffect(self, character):
        super(SeaHunter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SeaHunter, self).RemoveEffect(character)


class SpitVenom(Feat):

    def __init__(self, data=None):
        super(SpitVenom, self).__init__(data)

    def AddEffect(self, character):
        super(SpitVenom, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpitVenom, self).RemoveEffect(character)


class LifeSBlood(Feat):

    def __init__(self, data=None):
        super(LifeSBlood, self).__init__(data)

    def AddEffect(self, character):
        super(LifeSBlood, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LifeSBlood, self).RemoveEffect(character)


class StretchedWings(Feat):

    def __init__(self, data=None):
        super(StretchedWings, self).__init__(data)

    def AddEffect(self, character):
        super(StretchedWings, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StretchedWings, self).RemoveEffect(character)


class ExtraElementalAssault(Feat):

    def __init__(self, data=None):
        super(ExtraElementalAssault, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraElementalAssault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraElementalAssault, self).RemoveEffect(character)


class IncrementalElementalAssault(Feat):

    def __init__(self, data=None):
        super(IncrementalElementalAssault, self).__init__(data)

    def AddEffect(self, character):
        super(IncrementalElementalAssault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(IncrementalElementalAssault, self).RemoveEffect(character)


class StoicPose(Feat):

    def __init__(self, data=None):
        super(StoicPose, self).__init__(data)

    def AddEffect(self, character):
        super(StoicPose, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StoicPose, self).RemoveEffect(character)


class TreeHanger(Feat):

    def __init__(self, data=None):
        super(TreeHanger, self).__init__(data)

    def AddEffect(self, character):
        super(TreeHanger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TreeHanger, self).RemoveEffect(character)


class SleepVenom(Feat):

    def __init__(self, data=None):
        super(SleepVenom, self).__init__(data)

    def AddEffect(self, character):
        super(SleepVenom, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SleepVenom, self).RemoveEffect(character)


class ShadowyDash(Feat):

    def __init__(self, data=None):
        super(ShadowyDash, self).__init__(data)

    def AddEffect(self, character):
        super(ShadowyDash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadowyDash, self).RemoveEffect(character)


class BelierSBite(Feat):

    def __init__(self, data=None):
        super(BelierSBite, self).__init__(data)

    def AddEffect(self, character):
        super(BelierSBite, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BelierSBite, self).RemoveEffect(character)


class CornugonShield(Feat):

    def __init__(self, data=None):
        super(CornugonShield, self).__init__(data)

    def AddEffect(self, character):
        super(CornugonShield, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CornugonShield, self).RemoveEffect(character)


class CornugonSmash(Feat):

    def __init__(self, data=None):
        super(CornugonSmash, self).__init__(data)

    def AddEffect(self, character):
        super(CornugonSmash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CornugonSmash, self).RemoveEffect(character)


class CornugonStun(Feat):

    def __init__(self, data=None):
        super(CornugonStun, self).__init__(data)

    def AddEffect(self, character):
        super(CornugonStun, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CornugonStun, self).RemoveEffect(character)


class CornugonTrip(Feat):

    def __init__(self, data=None):
        super(CornugonTrip, self).__init__(data)

    def AddEffect(self, character):
        super(CornugonTrip, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CornugonTrip, self).RemoveEffect(character)


class FurySFall(Feat):

    def __init__(self, data=None):
        super(FurySFall, self).__init__(data)

    def AddEffect(self, character):
        super(FurySFall, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FurySFall, self).RemoveEffect(character)


class FurySSnare(Feat):

    def __init__(self, data=None):
        super(FurySSnare, self).__init__(data)

    def AddEffect(self, character):
        super(FurySSnare, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FurySSnare, self).RemoveEffect(character)


class HamatulaGrasp(Feat):

    def __init__(self, data=None):
        super(HamatulaGrasp, self).__init__(data)

    def AddEffect(self, character):
        super(HamatulaGrasp, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HamatulaGrasp, self).RemoveEffect(character)


class HamatulaStrike(Feat):

    def __init__(self, data=None):
        super(HamatulaStrike, self).__init__(data)

    def AddEffect(self, character):
        super(HamatulaStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HamatulaStrike, self).RemoveEffect(character)


class HellcatPounce(Feat):

    def __init__(self, data=None):
        super(HellcatPounce, self).__init__(data)

    def AddEffect(self, character):
        super(HellcatPounce, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HellcatPounce, self).RemoveEffect(character)


class HellcatStealth(Feat):

    def __init__(self, data=None):
        super(HellcatStealth, self).__init__(data)

    def AddEffect(self, character):
        super(HellcatStealth, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HellcatStealth, self).RemoveEffect(character)


class OsyluthGuile(Feat):

    def __init__(self, data=None):
        super(OsyluthGuile, self).__init__(data)

    def AddEffect(self, character):
        super(OsyluthGuile, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OsyluthGuile, self).RemoveEffect(character)


class BoundingHammer(Feat):

    def __init__(self, data=None):
        super(BoundingHammer, self).__init__(data)

    def AddEffect(self, character):
        super(BoundingHammer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BoundingHammer, self).RemoveEffect(character)


class DartingViper(Feat):

    def __init__(self, data=None):
        super(DartingViper, self).__init__(data)

    def AddEffect(self, character):
        super(DartingViper, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DartingViper, self).RemoveEffect(character)


class DornDergarMaster(Feat):

    def __init__(self, data=None):
        super(DornDergarMaster, self).__init__(data)

    def AddEffect(self, character):
        super(DornDergarMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DornDergarMaster, self).RemoveEffect(character)


class SlidingAxeThrow(Feat):

    def __init__(self, data=None):
        super(SlidingAxeThrow, self).__init__(data)

    def AddEffect(self, character):
        super(SlidingAxeThrow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SlidingAxeThrow, self).RemoveEffect(character)


class StanceOfTheXorn(Feat):

    def __init__(self, data=None):
        super(StanceOfTheXorn, self).__init__(data)

    def AddEffect(self, character):
        super(StanceOfTheXorn, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StanceOfTheXorn, self).RemoveEffect(character)


class ArcaneSchoolSpirit(Feat):

    def __init__(self, data=None):
        super(ArcaneSchoolSpirit, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneSchoolSpirit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneSchoolSpirit, self).RemoveEffect(character)


class BewilderingKoan(Feat):

    def __init__(self, data=None):
        super(BewilderingKoan, self).__init__(data)

    def AddEffect(self, character):
        super(BewilderingKoan, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BewilderingKoan, self).RemoveEffect(character)


class BloodTies(Feat):

    def __init__(self, data=None):
        super(BloodTies, self).__init__(data)

    def AddEffect(self, character):
        super(BloodTies, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodTies, self).RemoveEffect(character)


class BabblePeddler(Feat):

    def __init__(self, data=None):
        super(BabblePeddler, self).__init__(data)

    def AddEffect(self, character):
        super(BabblePeddler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BabblePeddler, self).RemoveEffect(character)


class CausticSlur(Feat):

    def __init__(self, data=None):
        super(CausticSlur, self).__init__(data)

    def AddEffect(self, character):
        super(CausticSlur, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CausticSlur, self).RemoveEffect(character)


class HelplessPrisoner(Feat):

    def __init__(self, data=None):
        super(HelplessPrisoner, self).__init__(data)

    def AddEffect(self, character):
        super(HelplessPrisoner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HelplessPrisoner, self).RemoveEffect(character)


class InvokePrimalInstinct(Feat):

    def __init__(self, data=None):
        super(InvokePrimalInstinct, self).__init__(data)

    def AddEffect(self, character):
        super(InvokePrimalInstinct, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InvokePrimalInstinct, self).RemoveEffect(character)


class Tantrum(Feat):

    def __init__(self, data=None):
        super(Tantrum, self).__init__(data)

    def AddEffect(self, character):
        super(Tantrum, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Tantrum, self).RemoveEffect(character)


class WittyFeint(Feat):

    def __init__(self, data=None):
        super(WittyFeint, self).__init__(data)

    def AddEffect(self, character):
        super(WittyFeint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WittyFeint, self).RemoveEffect(character)


class MountedBlade(Feat):

    def __init__(self, data=None):
        super(MountedBlade, self).__init__(data)

    def AddEffect(self, character):
        super(MountedBlade, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MountedBlade, self).RemoveEffect(character)


class ElephantStomp(Feat):

    def __init__(self, data=None):
        super(ElephantStomp, self).__init__(data)

    def AddEffect(self, character):
        super(ElephantStomp, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ElephantStomp, self).RemoveEffect(character)


class JaguarPounce(Feat):

    def __init__(self, data=None):
        super(JaguarPounce, self).__init__(data)

    def AddEffect(self, character):
        super(JaguarPounce, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(JaguarPounce, self).RemoveEffect(character)


class MonkeyLunge(Feat):

    def __init__(self, data=None):
        super(MonkeyLunge, self).__init__(data)

    def AddEffect(self, character):
        super(MonkeyLunge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MonkeyLunge, self).RemoveEffect(character)


class PiranhaStrike(Feat):

    def __init__(self, data=None):
        super(PiranhaStrike, self).__init__(data)

    def AddEffect(self, character):
        super(PiranhaStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PiranhaStrike, self).RemoveEffect(character)


class RhinoCharge(Feat):

    def __init__(self, data=None):
        super(RhinoCharge, self).__init__(data)

    def AddEffect(self, character):
        super(RhinoCharge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RhinoCharge, self).RemoveEffect(character)


class BoonCompanion(Feat):

    def __init__(self, data=None):
        super(BoonCompanion, self).__init__(data)

    def AddEffect(self, character):
        super(BoonCompanion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BoonCompanion, self).RemoveEffect(character)


class CriticalConduit(Feat):

    def __init__(self, data=None):
        super(CriticalConduit, self).__init__(data)

    def AddEffect(self, character):
        super(CriticalConduit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CriticalConduit, self).RemoveEffect(character)


class ExtraItemSlot(Feat):

    def __init__(self, data=None):
        super(ExtraItemSlot, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraItemSlot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraItemSlot, self).RemoveEffect(character)


class FamiliarFocus(Feat):

    def __init__(self, data=None):
        super(FamiliarFocus, self).__init__(data)

    def AddEffect(self, character):
        super(FamiliarFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FamiliarFocus, self).RemoveEffect(character)


class FamiliarSpell(Feat):

    def __init__(self, data=None):
        super(FamiliarSpell, self).__init__(data)

    def AddEffect(self, character):
        super(FamiliarSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FamiliarSpell, self).RemoveEffect(character)


class Jumper(Feat):

    def __init__(self, data=None):
        super(Jumper, self).__init__(data)

    def AddEffect(self, character):
        super(Jumper, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Jumper, self).RemoveEffect(character)


class LitheAttacker(Feat):

    def __init__(self, data=None):
        super(LitheAttacker, self).__init__(data)

    def AddEffect(self, character):
        super(LitheAttacker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LitheAttacker, self).RemoveEffect(character)


class MasterOfYourKind(Feat):

    def __init__(self, data=None):
        super(MasterOfYourKind, self).__init__(data)

    def AddEffect(self, character):
        super(MasterOfYourKind, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MasterOfYourKind, self).RemoveEffect(character)


class NarrowFrame(Feat):

    def __init__(self, data=None):
        super(NarrowFrame, self).__init__(data)

    def AddEffect(self, character):
        super(NarrowFrame, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NarrowFrame, self).RemoveEffect(character)


class SpellSponge(Feat):

    def __init__(self, data=None):
        super(SpellSponge, self).__init__(data)

    def AddEffect(self, character):
        super(SpellSponge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellSponge, self).RemoveEffect(character)


class StableGallop(Feat):

    def __init__(self, data=None):
        super(StableGallop, self).__init__(data)

    def AddEffect(self, character):
        super(StableGallop, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StableGallop, self).RemoveEffect(character)


class SureFooted(Feat):

    def __init__(self, data=None):
        super(SureFooted, self).__init__(data)

    def AddEffect(self, character):
        super(SureFooted, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SureFooted, self).RemoveEffect(character)


class ValiantSteed(Feat):

    def __init__(self, data=None):
        super(ValiantSteed, self).__init__(data)

    def AddEffect(self, character):
        super(ValiantSteed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ValiantSteed, self).RemoveEffect(character)


class ArchonDiversion(Feat):

    def __init__(self, data=None):
        super(ArchonDiversion, self).__init__(data)

    def AddEffect(self, character):
        super(ArchonDiversion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArchonDiversion, self).RemoveEffect(character)


class ArchonJustice(Feat):

    def __init__(self, data=None):
        super(ArchonJustice, self).__init__(data)

    def AddEffect(self, character):
        super(ArchonJustice, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArchonJustice, self).RemoveEffect(character)


class ArchonStyle(Feat):

    def __init__(self, data=None):
        super(ArchonStyle, self).__init__(data)

    def AddEffect(self, character):
        super(ArchonStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArchonStyle, self).RemoveEffect(character)


class BanishingCritical(Feat):

    def __init__(self, data=None):
        super(BanishingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(BanishingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BanishingCritical, self).RemoveEffect(character)


class BlindingLight(Feat):

    def __init__(self, data=None):
        super(BlindingLight, self).__init__(data)

    def AddEffect(self, character):
        super(BlindingLight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlindingLight, self).RemoveEffect(character)


class ConsecrateSpell(Feat):

    def __init__(self, data=None):
        super(ConsecrateSpell, self).__init__(data)

    def AddEffect(self, character):
        super(ConsecrateSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ConsecrateSpell, self).RemoveEffect(character)


class InnerLight(Feat):

    def __init__(self, data=None):
        super(InnerLight, self).__init__(data)

    def AddEffect(self, character):
        super(InnerLight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InnerLight, self).RemoveEffect(character)


class ReveredGuidance(Feat):

    def __init__(self, data=None):
        super(ReveredGuidance, self).__init__(data)

    def AddEffect(self, character):
        super(ReveredGuidance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ReveredGuidance, self).RemoveEffect(character)


class SunlitStrike(Feat):

    def __init__(self, data=None):
        super(SunlitStrike, self).__init__(data)

    def AddEffect(self, character):
        super(SunlitStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SunlitStrike, self).RemoveEffect(character)


class SupernalFeast(Feat):

    def __init__(self, data=None):
        super(SupernalFeast, self).__init__(data)

    def AddEffect(self, character):
        super(SupernalFeast, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SupernalFeast, self).RemoveEffect(character)


class AncestralScorn(Feat):

    def __init__(self, data=None):
        super(AncestralScorn, self).__init__(data)

    def AddEffect(self, character):
        super(AncestralScorn, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AncestralScorn, self).RemoveEffect(character)


class BannerOfDoom(Feat):

    def __init__(self, data=None):
        super(BannerOfDoom, self).__init__(data)

    def AddEffect(self, character):
        super(BannerOfDoom, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BannerOfDoom, self).RemoveEffect(character)


class BlindingSneakAttack(Feat):

    def __init__(self, data=None):
        super(BlindingSneakAttack, self).__init__(data)

    def AddEffect(self, character):
        super(BlindingSneakAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlindingSneakAttack, self).RemoveEffect(character)


class FiendishDarkness(Feat):

    def __init__(self, data=None):
        super(FiendishDarkness, self).__init__(data)

    def AddEffect(self, character):
        super(FiendishDarkness, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FiendishDarkness, self).RemoveEffect(character)


class FiendishFacade(Feat):

    def __init__(self, data=None):
        super(FiendishFacade, self).__init__(data)

    def AddEffect(self, character):
        super(FiendishFacade, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FiendishFacade, self).RemoveEffect(character)


class FiendishResilience(Feat):

    def __init__(self, data=None):
        super(FiendishResilience, self).__init__(data)

    def AddEffect(self, character):
        super(FiendishResilience, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FiendishResilience, self).RemoveEffect(character)


class FuryOfTheTainted(Feat):

    def __init__(self, data=None):
        super(FuryOfTheTainted, self).__init__(data)

    def AddEffect(self, character):
        super(FuryOfTheTainted, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FuryOfTheTainted, self).RemoveEffect(character)


class ImprovedFiendishDarkness(Feat):

    def __init__(self, data=None):
        super(ImprovedFiendishDarkness, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedFiendishDarkness, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedFiendishDarkness, self).RemoveEffect(character)


class ImprovedFiendishSorcery(Feat):

    def __init__(self, data=None):
        super(ImprovedFiendishSorcery, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedFiendishSorcery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedFiendishSorcery, self).RemoveEffect(character)


class ImprovedFuryOfTheTainted(Feat):

    def __init__(self, data=None):
        super(ImprovedFuryOfTheTainted, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedFuryOfTheTainted, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedFuryOfTheTainted, self).RemoveEffect(character)


class MonstrousMask(Feat):

    def __init__(self, data=None):
        super(MonstrousMask, self).__init__(data)

    def AddEffect(self, character):
        super(MonstrousMask, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MonstrousMask, self).RemoveEffect(character)


class TerrifyingMask(Feat):

    def __init__(self, data=None):
        super(TerrifyingMask, self).__init__(data)

    def AddEffect(self, character):
        super(TerrifyingMask, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TerrifyingMask, self).RemoveEffect(character)


class WickedValor(Feat):

    def __init__(self, data=None):
        super(WickedValor, self).__init__(data)

    def AddEffect(self, character):
        super(WickedValor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WickedValor, self).RemoveEffect(character)


class RecklessAim(Feat):

    def __init__(self, data=None):
        super(RecklessAim, self).__init__(data)

    def AddEffect(self, character):
        super(RecklessAim, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RecklessAim, self).RemoveEffect(character)


class Conviction(Feat):

    def __init__(self, data=None):
        super(Conviction, self).__init__(data)

    def AddEffect(self, character):
        super(Conviction, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Conviction, self).RemoveEffect(character)


class HymnSinger(Feat):

    def __init__(self, data=None):
        super(HymnSinger, self).__init__(data)

    def AddEffect(self, character):
        super(HymnSinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HymnSinger, self).RemoveEffect(character)


class LifeDominantSoul(Feat):

    def __init__(self, data=None):
        super(LifeDominantSoul, self).__init__(data)

    def AddEffect(self, character):
        super(LifeDominantSoul, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LifeDominantSoul, self).RemoveEffect(character)


class PotentHolySymbol(Feat):

    def __init__(self, data=None):
        super(PotentHolySymbol, self).__init__(data)

    def AddEffect(self, character):
        super(PotentHolySymbol, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PotentHolySymbol, self).RemoveEffect(character)


class SchooledResolve(Feat):

    def __init__(self, data=None):
        super(SchooledResolve, self).__init__(data)

    def AddEffect(self, character):
        super(SchooledResolve, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SchooledResolve, self).RemoveEffect(character)


class AversionTolerance(Feat):

    def __init__(self, data=None):
        super(AversionTolerance, self).__init__(data)

    def AddEffect(self, character):
        super(AversionTolerance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AversionTolerance, self).RemoveEffect(character)


class FamineTolerance(Feat):

    def __init__(self, data=None):
        super(FamineTolerance, self).__init__(data)

    def AddEffect(self, character):
        super(FamineTolerance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FamineTolerance, self).RemoveEffect(character)


class VampiricCompanion(Feat):

    def __init__(self, data=None):
        super(VampiricCompanion, self).__init__(data)

    def AddEffect(self, character):
        super(VampiricCompanion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VampiricCompanion, self).RemoveEffect(character)


class VariantPrayerScroll(Feat):

    def __init__(self, data=None):
        super(VariantPrayerScroll, self).__init__(data)

    def AddEffect(self, character):
        super(VariantPrayerScroll, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VariantPrayerScroll, self).RemoveEffect(character)


class BlindingFlash(Feat):

    def __init__(self, data=None):
        super(BlindingFlash, self).__init__(data)

    def AddEffect(self, character):
        super(BlindingFlash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlindingFlash, self).RemoveEffect(character)


class DisorientingBlow(Feat):

    def __init__(self, data=None):
        super(DisorientingBlow, self).__init__(data)

    def AddEffect(self, character):
        super(DisorientingBlow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisorientingBlow, self).RemoveEffect(character)


class EnhancedKiThrow(Feat):

    def __init__(self, data=None):
        super(EnhancedKiThrow, self).__init__(data)

    def AddEffect(self, character):
        super(EnhancedKiThrow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EnhancedKiThrow, self).RemoveEffect(character)


class FeintingFlurry(Feat):

    def __init__(self, data=None):
        super(FeintingFlurry, self).__init__(data)

    def AddEffect(self, character):
        super(FeintingFlurry, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FeintingFlurry, self).RemoveEffect(character)


class HoldTheBlade(Feat):

    def __init__(self, data=None):
        super(HoldTheBlade, self).__init__(data)

    def AddEffect(self, character):
        super(HoldTheBlade, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HoldTheBlade, self).RemoveEffect(character)


class ImprovedFeintingFlurry(Feat):

    def __init__(self, data=None):
        super(ImprovedFeintingFlurry, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedFeintingFlurry, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedFeintingFlurry, self).RemoveEffect(character)


class QuiveringPalmAdept(Feat):

    def __init__(self, data=None):
        super(QuiveringPalmAdept, self).__init__(data)

    def AddEffect(self, character):
        super(QuiveringPalmAdept, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuiveringPalmAdept, self).RemoveEffect(character)


class QuiveringPalmVersatility(Feat):

    def __init__(self, data=None):
        super(QuiveringPalmVersatility, self).__init__(data)

    def AddEffect(self, character):
        super(QuiveringPalmVersatility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuiveringPalmVersatility, self).RemoveEffect(character)


class SleeperHold(Feat):

    def __init__(self, data=None):
        super(SleeperHold, self).__init__(data)

    def AddEffect(self, character):
        super(SleeperHold, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SleeperHold, self).RemoveEffect(character)


class StunningFistAdept(Feat):

    def __init__(self, data=None):
        super(StunningFistAdept, self).__init__(data)

    def AddEffect(self, character):
        super(StunningFistAdept, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StunningFistAdept, self).RemoveEffect(character)


class ArcaneTrapSuppressor(Feat):

    def __init__(self, data=None):
        super(ArcaneTrapSuppressor, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneTrapSuppressor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneTrapSuppressor, self).RemoveEffect(character)


class CloseCall(Feat):

    def __init__(self, data=None):
        super(CloseCall, self).__init__(data)

    def AddEffect(self, character):
        super(CloseCall, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CloseCall, self).RemoveEffect(character)


class TacticalReposition(Feat):

    def __init__(self, data=None):
        super(TacticalReposition, self).__init__(data)

    def AddEffect(self, character):
        super(TacticalReposition, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TacticalReposition, self).RemoveEffect(character)


class CoaxingSpell(Feat):

    def __init__(self, data=None):
        super(CoaxingSpell, self).__init__(data)

    def AddEffect(self, character):
        super(CoaxingSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CoaxingSpell, self).RemoveEffect(character)


class DampenPresence(Feat):

    def __init__(self, data=None):
        super(DampenPresence, self).__init__(data)

    def AddEffect(self, character):
        super(DampenPresence, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DampenPresence, self).RemoveEffect(character)


class CursedItemDetection(Feat):

    def __init__(self, data=None):
        super(CursedItemDetection, self).__init__(data)

    def AddEffect(self, character):
        super(CursedItemDetection, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CursedItemDetection, self).RemoveEffect(character)


class OstentatiousDisplay(Feat):

    def __init__(self, data=None):
        super(OstentatiousDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(OstentatiousDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OstentatiousDisplay, self).RemoveEffect(character)


class TorchHandling(Feat):

    def __init__(self, data=None):
        super(TorchHandling, self).__init__(data)

    def AddEffect(self, character):
        super(TorchHandling, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TorchHandling, self).RemoveEffect(character)


class ArcaneInsight(Feat):

    def __init__(self, data=None):
        super(ArcaneInsight, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneInsight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneInsight, self).RemoveEffect(character)


class BloodyVengeance(Feat):

    def __init__(self, data=None):
        super(BloodyVengeance, self).__init__(data)

    def AddEffect(self, character):
        super(BloodyVengeance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodyVengeance, self).RemoveEffect(character)


class MeasuredResponse(Feat):

    def __init__(self, data=None):
        super(MeasuredResponse, self).__init__(data)

    def AddEffect(self, character):
        super(MeasuredResponse, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MeasuredResponse, self).RemoveEffect(character)


class RiptideAttack(Feat):

    def __init__(self, data=None):
        super(RiptideAttack, self).__init__(data)

    def AddEffect(self, character):
        super(RiptideAttack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RiptideAttack, self).RemoveEffect(character)


class SpikedDestroyer(Feat):

    def __init__(self, data=None):
        super(SpikedDestroyer, self).__init__(data)

    def AddEffect(self, character):
        super(SpikedDestroyer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpikedDestroyer, self).RemoveEffect(character)


class SteadyEngagement(Feat):

    def __init__(self, data=None):
        super(SteadyEngagement, self).__init__(data)

    def AddEffect(self, character):
        super(SteadyEngagement, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SteadyEngagement, self).RemoveEffect(character)


class Firebrand(Feat):

    def __init__(self, data=None):
        super(Firebrand, self).__init__(data)

    def AddEffect(self, character):
        super(Firebrand, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Firebrand, self).RemoveEffect(character)


class OrderedMind(Feat):

    def __init__(self, data=None):
        super(OrderedMind, self).__init__(data)

    def AddEffect(self, character):
        super(OrderedMind, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OrderedMind, self).RemoveEffect(character)


class DestroyIdentity(Feat):

    def __init__(self, data=None):
        super(DestroyIdentity, self).__init__(data)

    def AddEffect(self, character):
        super(DestroyIdentity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DestroyIdentity, self).RemoveEffect(character)


class FearsomeFinish(Feat):

    def __init__(self, data=None):
        super(FearsomeFinish, self).__init__(data)

    def AddEffect(self, character):
        super(FearsomeFinish, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FearsomeFinish, self).RemoveEffect(character)


class RejectPoison(Feat):

    def __init__(self, data=None):
        super(RejectPoison, self).__init__(data)

    def AddEffect(self, character):
        super(RejectPoison, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RejectPoison, self).RemoveEffect(character)


class ShadowDodge(Feat):

    def __init__(self, data=None):
        super(ShadowDodge, self).__init__(data)

    def AddEffect(self, character):
        super(ShadowDodge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadowDodge, self).RemoveEffect(character)


class MercilessRush(Feat):

    def __init__(self, data=None):
        super(MercilessRush, self).__init__(data)

    def AddEffect(self, character):
        super(MercilessRush, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MercilessRush, self).RemoveEffect(character)


class SquashFlat(Feat):

    def __init__(self, data=None):
        super(SquashFlat, self).__init__(data)

    def AddEffect(self, character):
        super(SquashFlat, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SquashFlat, self).RemoveEffect(character)


class ShatterResolve(Feat):

    def __init__(self, data=None):
        super(ShatterResolve, self).__init__(data)

    def AddEffect(self, character):
        super(ShatterResolve, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShatterResolve, self).RemoveEffect(character)


class Bloodletting(Feat):

    def __init__(self, data=None):
        super(Bloodletting, self).__init__(data)

    def AddEffect(self, character):
        super(Bloodletting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Bloodletting, self).RemoveEffect(character)


class AldoriDuelingMastery(Feat):

    def __init__(self, data=None):
        super(AldoriDuelingMastery, self).__init__(data)

    def AddEffect(self, character):
        super(AldoriDuelingMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AldoriDuelingMastery, self).RemoveEffect(character)


class AltitudeAffinity(Feat):

    def __init__(self, data=None):
        super(AltitudeAffinity, self).__init__(data)

    def AddEffect(self, character):
        super(AltitudeAffinity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AltitudeAffinity, self).RemoveEffect(character)


class AndorenFalconry(Feat):

    def __init__(self, data=None):
        super(AndorenFalconry, self).__init__(data)

    def AddEffect(self, character):
        super(AndorenFalconry, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AndorenFalconry, self).RemoveEffect(character)


class ArcaneVendetta(Feat):

    def __init__(self, data=None):
        super(ArcaneVendetta, self).__init__(data)

    def AddEffect(self, character):
        super(ArcaneVendetta, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArcaneVendetta, self).RemoveEffect(character)


class CarefulSpeaker(Feat):

    def __init__(self, data=None):
        super(CarefulSpeaker, self).__init__(data)

    def AddEffect(self, character):
        super(CarefulSpeaker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CarefulSpeaker, self).RemoveEffect(character)


class CypherMagic(Feat):

    def __init__(self, data=None):
        super(CypherMagic, self).__init__(data)

    def AddEffect(self, character):
        super(CypherMagic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CypherMagic, self).RemoveEffect(character)


class CypherScript(Feat):

    def __init__(self, data=None):
        super(CypherScript, self).__init__(data)

    def AddEffect(self, character):
        super(CypherScript, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CypherScript, self).RemoveEffect(character)


class DemonHunter(Feat):

    def __init__(self, data=None):
        super(DemonHunter, self).__init__(data)

    def AddEffect(self, character):
        super(DemonHunter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DemonHunter, self).RemoveEffect(character)


class DervishDance(Feat):

    def __init__(self, data=None):
        super(DervishDance, self).__init__(data)

    def AddEffect(self, character):
        super(DervishDance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DervishDance, self).RemoveEffect(character)


class DesertDweller(Feat):

    def __init__(self, data=None):
        super(DesertDweller, self).__init__(data)

    def AddEffect(self, character):
        super(DesertDweller, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DesertDweller, self).RemoveEffect(character)


class DesperateBattler(Feat):

    def __init__(self, data=None):
        super(DesperateBattler, self).__init__(data)

    def AddEffect(self, character):
        super(DesperateBattler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DesperateBattler, self).RemoveEffect(character)


class EyeOfTheArclord(Feat):

    def __init__(self, data=None):
        super(EyeOfTheArclord, self).__init__(data)

    def AddEffect(self, character):
        super(EyeOfTheArclord, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EyeOfTheArclord, self).RemoveEffect(character)


class FeyFoundling(Feat):

    def __init__(self, data=None):
        super(FeyFoundling, self).__init__(data)

    def AddEffect(self, character):
        super(FeyFoundling, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FeyFoundling, self).RemoveEffect(character)


class Flagbearer(Feat):

    def __init__(self, data=None):
        super(Flagbearer, self).__init__(data)

    def AddEffect(self, character):
        super(Flagbearer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Flagbearer, self).RemoveEffect(character)


class FocusedDiscipline(Feat):

    def __init__(self, data=None):
        super(FocusedDiscipline, self).__init__(data)

    def AddEffect(self, character):
        super(FocusedDiscipline, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FocusedDiscipline, self).RemoveEffect(character)


class FortuneTeller(Feat):

    def __init__(self, data=None):
        super(FortuneTeller, self).__init__(data)

    def AddEffect(self, character):
        super(FortuneTeller, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FortuneTeller, self).RemoveEffect(character)


class FreeSpirit(Feat):

    def __init__(self, data=None):
        super(FreeSpirit, self).__init__(data)

    def AddEffect(self, character):
        super(FreeSpirit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FreeSpirit, self).RemoveEffect(character)


class GodlessHealing(Feat):

    def __init__(self, data=None):
        super(GodlessHealing, self).__init__(data)

    def AddEffect(self, character):
        super(GodlessHealing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GodlessHealing, self).RemoveEffect(character)


class GreenFaithAcolyte(Feat):

    def __init__(self, data=None):
        super(GreenFaithAcolyte, self).__init__(data)

    def AddEffect(self, character):
        super(GreenFaithAcolyte, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreenFaithAcolyte, self).RemoveEffect(character)


class Hamatulatsu(Feat):

    def __init__(self, data=None):
        super(Hamatulatsu, self).__init__(data)

    def AddEffect(self, character):
        super(Hamatulatsu, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Hamatulatsu, self).RemoveEffect(character)


class HarmonicSpell(Feat):

    def __init__(self, data=None):
        super(HarmonicSpell, self).__init__(data)

    def AddEffect(self, character):
        super(HarmonicSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HarmonicSpell, self).RemoveEffect(character)


class Harrowed(Feat):

    def __init__(self, data=None):
        super(Harrowed, self).__init__(data)

    def AddEffect(self, character):
        super(Harrowed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Harrowed, self).RemoveEffect(character)


class HermeanBlood(Feat):

    def __init__(self, data=None):
        super(HermeanBlood, self).__init__(data)

    def AddEffect(self, character):
        super(HermeanBlood, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HermeanBlood, self).RemoveEffect(character)


class NecromanticAffinity(Feat):

    def __init__(self, data=None):
        super(NecromanticAffinity, self).__init__(data)

    def AddEffect(self, character):
        super(NecromanticAffinity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NecromanticAffinity, self).RemoveEffect(character)


class NobleScion(Feat):

    def __init__(self, data=None):
        super(NobleScion, self).__init__(data)

    def AddEffect(self, character):
        super(NobleScion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NobleScion, self).RemoveEffect(character)


class RapidReload(Feat):

    def __init__(self, data=None):
        super(RapidReload, self).__init__(data)

    def AddEffect(self, character):
        super(RapidReload, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RapidReload, self).RemoveEffect(character)


class RuggedNortherner(Feat):

    def __init__(self, data=None):
        super(RuggedNortherner, self).__init__(data)

    def AddEffect(self, character):
        super(RuggedNortherner, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RuggedNortherner, self).RemoveEffect(character)


class Scholar(Feat):

    def __init__(self, data=None):
        super(Scholar, self).__init__(data)

    def AddEffect(self, character):
        super(Scholar, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Scholar, self).RemoveEffect(character)


class SecretSigns(Feat):

    def __init__(self, data=None):
        super(SecretSigns, self).__init__(data)

    def AddEffect(self, character):
        super(SecretSigns, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SecretSigns, self).RemoveEffect(character)


class ShadeOfTheUskwood(Feat):

    def __init__(self, data=None):
        super(ShadeOfTheUskwood, self).__init__(data)

    def AddEffect(self, character):
        super(ShadeOfTheUskwood, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadeOfTheUskwood, self).RemoveEffect(character)


class ShrewdTactician(Feat):

    def __init__(self, data=None):
        super(ShrewdTactician, self).__init__(data)

    def AddEffect(self, character):
        super(ShrewdTactician, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShrewdTactician, self).RemoveEffect(character)


class Stoic(Feat):

    def __init__(self, data=None):
        super(Stoic, self).__init__(data)

    def AddEffect(self, character):
        super(Stoic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Stoic, self).RemoveEffect(character)


class StormLashed(Feat):

    def __init__(self, data=None):
        super(StormLashed, self).__init__(data)

    def AddEffect(self, character):
        super(StormLashed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StormLashed, self).RemoveEffect(character)


class Survivor(Feat):

    def __init__(self, data=None):
        super(Survivor, self).__init__(data)

    def AddEffect(self, character):
        super(Survivor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Survivor, self).RemoveEffect(character)


class TaldanDuelist(Feat):

    def __init__(self, data=None):
        super(TaldanDuelist, self).__init__(data)

    def AddEffect(self, character):
        super(TaldanDuelist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TaldanDuelist, self).RemoveEffect(character)


class TotemSpirit(Feat):

    def __init__(self, data=None):
        super(TotemSpirit, self).__init__(data)

    def AddEffect(self, character):
        super(TotemSpirit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TotemSpirit, self).RemoveEffect(character)


class VarisianTattoo(Feat):

    def __init__(self, data=None):
        super(VarisianTattoo, self).__init__(data)

    def AddEffect(self, character):
        super(VarisianTattoo, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VarisianTattoo, self).RemoveEffect(character)


class WandDancer(Feat):

    def __init__(self, data=None):
        super(WandDancer, self).__init__(data)

    def AddEffect(self, character):
        super(WandDancer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WandDancer, self).RemoveEffect(character)


class SlayingSprint(Feat):

    def __init__(self, data=None):
        super(SlayingSprint, self).__init__(data)

    def AddEffect(self, character):
        super(SlayingSprint, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SlayingSprint, self).RemoveEffect(character)


class GreaterSerpentLash(Feat):

    def __init__(self, data=None):
        super(GreaterSerpentLash, self).__init__(data)

    def AddEffect(self, character):
        super(GreaterSerpentLash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GreaterSerpentLash, self).RemoveEffect(character)


class SerpentLash(Feat):

    def __init__(self, data=None):
        super(SerpentLash, self).__init__(data)

    def AddEffect(self, character):
        super(SerpentLash, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SerpentLash, self).RemoveEffect(character)


class CirclingOffense(Feat):

    def __init__(self, data=None):
        super(CirclingOffense, self).__init__(data)

    def AddEffect(self, character):
        super(CirclingOffense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CirclingOffense, self).RemoveEffect(character)


class Footslasher(Feat):

    def __init__(self, data=None):
        super(Footslasher, self).__init__(data)

    def AddEffect(self, character):
        super(Footslasher, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Footslasher, self).RemoveEffect(character)


class ToppleFoe(Feat):

    def __init__(self, data=None):
        super(ToppleFoe, self).__init__(data)

    def AddEffect(self, character):
        super(ToppleFoe, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ToppleFoe, self).RemoveEffect(character)


class JackalHeritage(Feat):

    def __init__(self, data=None):
        super(JackalHeritage, self).__init__(data)

    def AddEffect(self, character):
        super(JackalHeritage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(JackalHeritage, self).RemoveEffect(character)


class DrunkenBrawler(Feat):

    def __init__(self, data=None):
        super(DrunkenBrawler, self).__init__(data)

    def AddEffect(self, character):
        super(DrunkenBrawler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DrunkenBrawler, self).RemoveEffect(character)


class ButterflySSting(Feat):

    def __init__(self, data=None):
        super(ButterflySSting, self).__init__(data)

    def AddEffect(self, character):
        super(ButterflySSting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ButterflySSting, self).RemoveEffect(character)


class DivinationGuide(Feat):

    def __init__(self, data=None):
        super(DivinationGuide, self).__init__(data)

    def AddEffect(self, character):
        super(DivinationGuide, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DivinationGuide, self).RemoveEffect(character)


class BullseyeShot(Feat):

    def __init__(self, data=None):
        super(BullseyeShot, self).__init__(data)

    def AddEffect(self, character):
        super(BullseyeShot, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BullseyeShot, self).RemoveEffect(character)


class NimbleNaturalSummons(Feat):

    def __init__(self, data=None):
        super(NimbleNaturalSummons, self).__init__(data)

    def AddEffect(self, character):
        super(NimbleNaturalSummons, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NimbleNaturalSummons, self).RemoveEffect(character)


class ChargeOfTheRighteous(Feat):

    def __init__(self, data=None):
        super(ChargeOfTheRighteous, self).__init__(data)

    def AddEffect(self, character):
        super(ChargeOfTheRighteous, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ChargeOfTheRighteous, self).RemoveEffect(character)


class ProtectorSStrike(Feat):

    def __init__(self, data=None):
        super(ProtectorSStrike, self).__init__(data)

    def AddEffect(self, character):
        super(ProtectorSStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ProtectorSStrike, self).RemoveEffect(character)


class BestowHope(Feat):

    def __init__(self, data=None):
        super(BestowHope, self).__init__(data)

    def AddEffect(self, character):
        super(BestowHope, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BestowHope, self).RemoveEffect(character)


class GloriousHeat(Feat):

    def __init__(self, data=None):
        super(GloriousHeat, self).__init__(data)

    def AddEffect(self, character):
        super(GloriousHeat, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GloriousHeat, self).RemoveEffect(character)


class SpearDancer(Feat):

    def __init__(self, data=None):
        super(SpearDancer, self).__init__(data)

    def AddEffect(self, character):
        super(SpearDancer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpearDancer, self).RemoveEffect(character)


class StoneRead(Feat):

    def __init__(self, data=None):
        super(StoneRead, self).__init__(data)

    def AddEffect(self, character):
        super(StoneRead, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StoneRead, self).RemoveEffect(character)


class UnderminingExploit(Feat):

    def __init__(self, data=None):
        super(UnderminingExploit, self).__init__(data)

    def AddEffect(self, character):
        super(UnderminingExploit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UnderminingExploit, self).RemoveEffect(character)


class AnkleBiter(Feat):

    def __init__(self, data=None):
        super(AnkleBiter, self).__init__(data)

    def AddEffect(self, character):
        super(AnkleBiter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AnkleBiter, self).RemoveEffect(character)


class BattleSinger(Feat):

    def __init__(self, data=None):
        super(BattleSinger, self).__init__(data)

    def AddEffect(self, character):
        super(BattleSinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BattleSinger, self).RemoveEffect(character)


class DogKillerHorseHunter(Feat):

    def __init__(self, data=None):
        super(DogKillerHorseHunter, self).__init__(data)

    def AddEffect(self, character):
        super(DogKillerHorseHunter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DogKillerHorseHunter, self).RemoveEffect(character)


class LeadFromTheBack(Feat):

    def __init__(self, data=None):
        super(LeadFromTheBack, self).__init__(data)

    def AddEffect(self, character):
        super(LeadFromTheBack, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LeadFromTheBack, self).RemoveEffect(character)


class LetterFury(Feat):

    def __init__(self, data=None):
        super(LetterFury, self).__init__(data)

    def AddEffect(self, character):
        super(LetterFury, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LetterFury, self).RemoveEffect(character)


class RollWithIt(Feat):

    def __init__(self, data=None):
        super(RollWithIt, self).__init__(data)

    def AddEffect(self, character):
        super(RollWithIt, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RollWithIt, self).RemoveEffect(character)


class SaddleShrieker(Feat):

    def __init__(self, data=None):
        super(SaddleShrieker, self).__init__(data)

    def AddEffect(self, character):
        super(SaddleShrieker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SaddleShrieker, self).RemoveEffect(character)


class CombatDistraction(Feat):

    def __init__(self, data=None):
        super(CombatDistraction, self).__init__(data)

    def AddEffect(self, character):
        super(CombatDistraction, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CombatDistraction, self).RemoveEffect(character)


class Vandal(Feat):

    def __init__(self, data=None):
        super(Vandal, self).__init__(data)

    def AddEffect(self, character):
        super(Vandal, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Vandal, self).RemoveEffect(character)


class AmmoDrop(Feat):

    def __init__(self, data=None):
        super(AmmoDrop, self).__init__(data)

    def AddEffect(self, character):
        super(AmmoDrop, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AmmoDrop, self).RemoveEffect(character)


class HalflingSlinger(Feat):

    def __init__(self, data=None):
        super(HalflingSlinger, self).__init__(data)

    def AddEffect(self, character):
        super(HalflingSlinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HalflingSlinger, self).RemoveEffect(character)


class JuggleLoad(Feat):

    def __init__(self, data=None):
        super(JuggleLoad, self).__init__(data)

    def AddEffect(self, character):
        super(JuggleLoad, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(JuggleLoad, self).RemoveEffect(character)


class LargeTarget(Feat):

    def __init__(self, data=None):
        super(LargeTarget, self).__init__(data)

    def AddEffect(self, character):
        super(LargeTarget, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LargeTarget, self).RemoveEffect(character)


class WhipSlinger(Feat):

    def __init__(self, data=None):
        super(WhipSlinger, self).__init__(data)

    def AddEffect(self, character):
        super(WhipSlinger, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WhipSlinger, self).RemoveEffect(character)


class AmplifiedRage(Feat):

    def __init__(self, data=None):
        super(AmplifiedRage, self).__init__(data)

    def AddEffect(self, character):
        super(AmplifiedRage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AmplifiedRage, self).RemoveEffect(character)


class BloodVengeance(Feat):

    def __init__(self, data=None):
        super(BloodVengeance, self).__init__(data)

    def AddEffect(self, character):
        super(BloodVengeance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodVengeance, self).RemoveEffect(character)


class BrutalGrappler(Feat):

    def __init__(self, data=None):
        super(BrutalGrappler, self).__init__(data)

    def AddEffect(self, character):
        super(BrutalGrappler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BrutalGrappler, self).RemoveEffect(character)


class DestroyerSBlessing(Feat):

    def __init__(self, data=None):
        super(DestroyerSBlessing, self).__init__(data)

    def AddEffect(self, character):
        super(DestroyerSBlessing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DestroyerSBlessing, self).RemoveEffect(character)


class FerociousTenacity(Feat):

    def __init__(self, data=None):
        super(FerociousTenacity, self).__init__(data)

    def AddEffect(self, character):
        super(FerociousTenacity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FerociousTenacity, self).RemoveEffect(character)


class FerociousTenacity(Feat):

    def __init__(self, data=None):
        super(FerociousTenacity, self).__init__(data)

    def AddEffect(self, character):
        super(FerociousTenacity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FerociousTenacity, self).RemoveEffect(character)


class FireGodSBlessing(Feat):

    def __init__(self, data=None):
        super(FireGodSBlessing, self).__init__(data)

    def AddEffect(self, character):
        super(FireGodSBlessing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FireGodSBlessing, self).RemoveEffect(character)


class GoreFiend(Feat):

    def __init__(self, data=None):
        super(GoreFiend, self).__init__(data)

    def AddEffect(self, character):
        super(GoreFiend, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GoreFiend, self).RemoveEffect(character)


class SympatheticRage(Feat):

    def __init__(self, data=None):
        super(SympatheticRage, self).__init__(data)

    def AddEffect(self, character):
        super(SympatheticRage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SympatheticRage, self).RemoveEffect(character)


class ThrillOfTheKill(Feat):

    def __init__(self, data=None):
        super(ThrillOfTheKill, self).__init__(data)

    def AddEffect(self, character):
        super(ThrillOfTheKill, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThrillOfTheKill, self).RemoveEffect(character)


class WarleaderSRage(Feat):

    def __init__(self, data=None):
        super(WarleaderSRage, self).__init__(data)

    def AddEffect(self, character):
        super(WarleaderSRage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WarleaderSRage, self).RemoveEffect(character)


class AdeptChannel(Feat):

    def __init__(self, data=None):
        super(AdeptChannel, self).__init__(data)

    def AddEffect(self, character):
        super(AdeptChannel, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AdeptChannel, self).RemoveEffect(character)


class ColdCelerity(Feat):

    def __init__(self, data=None):
        super(ColdCelerity, self).__init__(data)

    def AddEffect(self, character):
        super(ColdCelerity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ColdCelerity, self).RemoveEffect(character)


class TribalScars(Feat):

    def __init__(self, data=None):
        super(TribalScars, self).__init__(data)

    def AddEffect(self, character):
        super(TribalScars, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TribalScars, self).RemoveEffect(character)


class Witchbreaker(Feat):

    def __init__(self, data=None):
        super(Witchbreaker, self).__init__(data)

    def AddEffect(self, character):
        super(Witchbreaker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Witchbreaker, self).RemoveEffect(character)


class DeadlyDealer(Feat):

    def __init__(self, data=None):
        super(DeadlyDealer, self).__init__(data)

    def AddEffect(self, character):
        super(DeadlyDealer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeadlyDealer, self).RemoveEffect(character)


class ThunderAndFang(Feat):

    def __init__(self, data=None):
        super(ThunderAndFang, self).__init__(data)

    def AddEffect(self, character):
        super(ThunderAndFang, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThunderAndFang, self).RemoveEffect(character)


class Chainbreaker(Feat):

    def __init__(self, data=None):
        super(Chainbreaker, self).__init__(data)

    def AddEffect(self, character):
        super(Chainbreaker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Chainbreaker, self).RemoveEffect(character)


class DevilSFoe(Feat):

    def __init__(self, data=None):
        super(DevilSFoe, self).__init__(data)

    def AddEffect(self, character):
        super(DevilSFoe, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DevilSFoe, self).RemoveEffect(character)


class EagleKnightCandidate(Feat):

    def __init__(self, data=None):
        super(EagleKnightCandidate, self).__init__(data)

    def AddEffect(self, character):
        super(EagleKnightCandidate, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EagleKnightCandidate, self).RemoveEffect(character)


class TalmandorSLifting(Feat):

    def __init__(self, data=None):
        super(TalmandorSLifting, self).__init__(data)

    def AddEffect(self, character):
        super(TalmandorSLifting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TalmandorSLifting, self).RemoveEffect(character)


class AdvancedDefensiveCombatTraining(Feat):

    def __init__(self, data=None):
        super(AdvancedDefensiveCombatTraining, self).__init__(data)

    def AddEffect(self, character):
        super(AdvancedDefensiveCombatTraining, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AdvancedDefensiveCombatTraining, self).RemoveEffect(character)


class BloodstoneManhunter(Feat):

    def __init__(self, data=None):
        super(BloodstoneManhunter, self).__init__(data)

    def AddEffect(self, character):
        super(BloodstoneManhunter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodstoneManhunter, self).RemoveEffect(character)


class CalmDisposition(Feat):

    def __init__(self, data=None):
        super(CalmDisposition, self).__init__(data)

    def AddEffect(self, character):
        super(CalmDisposition, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CalmDisposition, self).RemoveEffect(character)


class DeathSSuitor(Feat):

    def __init__(self, data=None):
        super(DeathSSuitor, self).__init__(data)

    def AddEffect(self, character):
        super(DeathSSuitor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeathSSuitor, self).RemoveEffect(character)


class DisassembleMagicItem(Feat):

    def __init__(self, data=None):
        super(DisassembleMagicItem, self).__init__(data)

    def AddEffect(self, character):
        super(DisassembleMagicItem, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DisassembleMagicItem, self).RemoveEffect(character)


class DivineDeception(Feat):

    def __init__(self, data=None):
        super(DivineDeception, self).__init__(data)

    def AddEffect(self, character):
        super(DivineDeception, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DivineDeception, self).RemoveEffect(character)


class FastCrawl(Feat):

    def __init__(self, data=None):
        super(FastCrawl, self).__init__(data)

    def AddEffect(self, character):
        super(FastCrawl, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FastCrawl, self).RemoveEffect(character)


class FearsomeBarricade(Feat):

    def __init__(self, data=None):
        super(FearsomeBarricade, self).__init__(data)

    def AddEffect(self, character):
        super(FearsomeBarricade, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FearsomeBarricade, self).RemoveEffect(character)


class GrandMasterPerformer(Feat):

    def __init__(self, data=None):
        super(GrandMasterPerformer, self).__init__(data)

    def AddEffect(self, character):
        super(GrandMasterPerformer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GrandMasterPerformer, self).RemoveEffect(character)


class KiDiversity(Feat):

    def __init__(self, data=None):
        super(KiDiversity, self).__init__(data)

    def AddEffect(self, character):
        super(KiDiversity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KiDiversity, self).RemoveEffect(character)


class LetThemCome(Feat):

    def __init__(self, data=None):
        super(LetThemCome, self).__init__(data)

    def AddEffect(self, character):
        super(LetThemCome, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LetThemCome, self).RemoveEffect(character)


class MasterPerformer(Feat):

    def __init__(self, data=None):
        super(MasterPerformer, self).__init__(data)

    def AddEffect(self, character):
        super(MasterPerformer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MasterPerformer, self).RemoveEffect(character)


class NamelessServitor(Feat):

    def __init__(self, data=None):
        super(NamelessServitor, self).__init__(data)

    def AddEffect(self, character):
        super(NamelessServitor, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NamelessServitor, self).RemoveEffect(character)


class OldCultsAwakener(Feat):

    def __init__(self, data=None):
        super(OldCultsAwakener, self).__init__(data)

    def AddEffect(self, character):
        super(OldCultsAwakener, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OldCultsAwakener, self).RemoveEffect(character)


class OminousMien(Feat):

    def __init__(self, data=None):
        super(OminousMien, self).__init__(data)

    def AddEffect(self, character):
        super(OminousMien, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OminousMien, self).RemoveEffect(character)


class SilentPerformer(Feat):

    def __init__(self, data=None):
        super(SilentPerformer, self).__init__(data)

    def AddEffect(self, character):
        super(SilentPerformer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SilentPerformer, self).RemoveEffect(character)


class TouchedBySacredFire(Feat):

    def __init__(self, data=None):
        super(TouchedBySacredFire, self).__init__(data)

    def AddEffect(self, character):
        super(TouchedBySacredFire, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TouchedBySacredFire, self).RemoveEffect(character)


class VerbosePerformer(Feat):

    def __init__(self, data=None):
        super(VerbosePerformer, self).__init__(data)

    def AddEffect(self, character):
        super(VerbosePerformer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VerbosePerformer, self).RemoveEffect(character)


class WhisperedKnowledge(Feat):

    def __init__(self, data=None):
        super(WhisperedKnowledge, self).__init__(data)

    def AddEffect(self, character):
        super(WhisperedKnowledge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WhisperedKnowledge, self).RemoveEffect(character)


class BloodOfHeroes(Feat):

    def __init__(self, data=None):
        super(BloodOfHeroes, self).__init__(data)

    def AddEffect(self, character):
        super(BloodOfHeroes, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodOfHeroes, self).RemoveEffect(character)


class HeroSFortune(Feat):

    def __init__(self, data=None):
        super(HeroSFortune, self).__init__(data)

    def AddEffect(self, character):
        super(HeroSFortune, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HeroSFortune, self).RemoveEffect(character)


class LuckOfHeroes(Feat):

    def __init__(self, data=None):
        super(LuckOfHeroes, self).__init__(data)

    def AddEffect(self, character):
        super(LuckOfHeroes, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LuckOfHeroes, self).RemoveEffect(character)


class CelestialObedience(Feat):

    def __init__(self, data=None):
        super(CelestialObedience, self).__init__(data)

    def AddEffect(self, character):
        super(CelestialObedience, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CelestialObedience, self).RemoveEffect(character)


class Accursed(Feat):

    def __init__(self, data=None):
        super(Accursed, self).__init__(data)

    def AddEffect(self, character):
        super(Accursed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Accursed, self).RemoveEffect(character)


class Arisen(Feat):

    def __init__(self, data=None):
        super(Arisen, self).__init__(data)

    def AddEffect(self, character):
        super(Arisen, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Arisen, self).RemoveEffect(character)


class BattlefieldHealer(Feat):

    def __init__(self, data=None):
        super(BattlefieldHealer, self).__init__(data)

    def AddEffect(self, character):
        super(BattlefieldHealer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BattlefieldHealer, self).RemoveEffect(character)


class Champion(Feat):

    def __init__(self, data=None):
        super(Champion, self).__init__(data)

    def AddEffect(self, character):
        super(Champion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Champion, self).RemoveEffect(character)


class Damned(Feat):

    def __init__(self, data=None):
        super(Damned, self).__init__(data)

    def AddEffect(self, character):
        super(Damned, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Damned, self).RemoveEffect(character)


class DenyTheReaper(Feat):

    def __init__(self, data=None):
        super(DenyTheReaper, self).__init__(data)

    def AddEffect(self, character):
        super(DenyTheReaper, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DenyTheReaper, self).RemoveEffect(character)


class EldritchResearcher(Feat):

    def __init__(self, data=None):
        super(EldritchResearcher, self).__init__(data)

    def AddEffect(self, character):
        super(EldritchResearcher, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EldritchResearcher, self).RemoveEffect(character)


class FearlessZeal(Feat):

    def __init__(self, data=None):
        super(FearlessZeal, self).__init__(data)

    def AddEffect(self, character):
        super(FearlessZeal, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FearlessZeal, self).RemoveEffect(character)


class FeralHeart(Feat):

    def __init__(self, data=None):
        super(FeralHeart, self).__init__(data)

    def AddEffect(self, character):
        super(FeralHeart, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FeralHeart, self).RemoveEffect(character)


class Foeslayer(Feat):

    def __init__(self, data=None):
        super(Foeslayer, self).__init__(data)

    def AddEffect(self, character):
        super(Foeslayer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Foeslayer, self).RemoveEffect(character)


class ForgottenPast(Feat):

    def __init__(self, data=None):
        super(ForgottenPast, self).__init__(data)

    def AddEffect(self, character):
        super(ForgottenPast, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ForgottenPast, self).RemoveEffect(character)


class GlimpseBeyond(Feat):

    def __init__(self, data=None):
        super(GlimpseBeyond, self).__init__(data)

    def AddEffect(self, character):
        super(GlimpseBeyond, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GlimpseBeyond, self).RemoveEffect(character)


class InnocentBlood(Feat):

    def __init__(self, data=None):
        super(InnocentBlood, self).__init__(data)

    def AddEffect(self, character):
        super(InnocentBlood, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InnocentBlood, self).RemoveEffect(character)


class Liberator(Feat):

    def __init__(self, data=None):
        super(Liberator, self).__init__(data)

    def AddEffect(self, character):
        super(Liberator, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Liberator, self).RemoveEffect(character)


class LostLegacy(Feat):

    def __init__(self, data=None):
        super(LostLegacy, self).__init__(data)

    def AddEffect(self, character):
        super(LostLegacy, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LostLegacy, self).RemoveEffect(character)


class MagnumOpus(Feat):

    def __init__(self, data=None):
        super(MagnumOpus, self).__init__(data)

    def AddEffect(self, character):
        super(MagnumOpus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MagnumOpus, self).RemoveEffect(character)


class MonumentBuilder(Feat):

    def __init__(self, data=None):
        super(MonumentBuilder, self).__init__(data)

    def AddEffect(self, character):
        super(MonumentBuilder, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MonumentBuilder, self).RemoveEffect(character)


class NationBuilder(Feat):

    def __init__(self, data=None):
        super(NationBuilder, self).__init__(data)

    def AddEffect(self, character):
        super(NationBuilder, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NationBuilder, self).RemoveEffect(character)


class Nemesis(Feat):

    def __init__(self, data=None):
        super(Nemesis, self).__init__(data)

    def AddEffect(self, character):
        super(Nemesis, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Nemesis, self).RemoveEffect(character)


class Prophet(Feat):

    def __init__(self, data=None):
        super(Prophet, self).__init__(data)

    def AddEffect(self, character):
        super(Prophet, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Prophet, self).RemoveEffect(character)


class Redemption(Feat):

    def __init__(self, data=None):
        super(Redemption, self).__init__(data)

    def AddEffect(self, character):
        super(Redemption, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Redemption, self).RemoveEffect(character)


class Shamed(Feat):

    def __init__(self, data=None):
        super(Shamed, self).__init__(data)

    def AddEffect(self, character):
        super(Shamed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Shamed, self).RemoveEffect(character)


class Stronghold(Feat):

    def __init__(self, data=None):
        super(Stronghold, self).__init__(data)

    def AddEffect(self, character):
        super(Stronghold, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Stronghold, self).RemoveEffect(character)


class ThiefOfLegend(Feat):

    def __init__(self, data=None):
        super(ThiefOfLegend, self).__init__(data)

    def AddEffect(self, character):
        super(ThiefOfLegend, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThiefOfLegend, self).RemoveEffect(character)


class TownTamer(Feat):

    def __init__(self, data=None):
        super(TownTamer, self).__init__(data)

    def AddEffect(self, character):
        super(TownTamer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TownTamer, self).RemoveEffect(character)


class TrueLove(Feat):

    def __init__(self, data=None):
        super(TrueLove, self).__init__(data)

    def AddEffect(self, character):
        super(TrueLove, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TrueLove, self).RemoveEffect(character)


class Unforgotten(Feat):

    def __init__(self, data=None):
        super(Unforgotten, self).__init__(data)

    def AddEffect(self, character):
        super(Unforgotten, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Unforgotten, self).RemoveEffect(character)


class Vengeance(Feat):

    def __init__(self, data=None):
        super(Vengeance, self).__init__(data)

    def AddEffect(self, character):
        super(Vengeance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Vengeance, self).RemoveEffect(character)


class AncientDraconic(Feat):

    def __init__(self, data=None):
        super(AncientDraconic, self).__init__(data)

    def AddEffect(self, character):
        super(AncientDraconic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AncientDraconic, self).RemoveEffect(character)


class ImprovedLearnRangerTrap(Feat):

    def __init__(self, data=None):
        super(ImprovedLearnRangerTrap, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedLearnRangerTrap, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedLearnRangerTrap, self).RemoveEffect(character)


class KoboldConfidence(Feat):

    def __init__(self, data=None):
        super(KoboldConfidence, self).__init__(data)

    def AddEffect(self, character):
        super(KoboldConfidence, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KoboldConfidence, self).RemoveEffect(character)


class LearnRangerTrap(Feat):

    def __init__(self, data=None):
        super(LearnRangerTrap, self).__init__(data)

    def AddEffect(self, character):
        super(LearnRangerTrap, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LearnRangerTrap, self).RemoveEffect(character)


class MercilessMagic(Feat):

    def __init__(self, data=None):
        super(MercilessMagic, self).__init__(data)

    def AddEffect(self, character):
        super(MercilessMagic, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MercilessMagic, self).RemoveEffect(character)


class MercilessPrecision(Feat):

    def __init__(self, data=None):
        super(MercilessPrecision, self).__init__(data)

    def AddEffect(self, character):
        super(MercilessPrecision, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MercilessPrecision, self).RemoveEffect(character)


class MixedScales(Feat):

    def __init__(self, data=None):
        super(MixedScales, self).__init__(data)

    def AddEffect(self, character):
        super(MixedScales, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MixedScales, self).RemoveEffect(character)


class RedeemedKobold(Feat):

    def __init__(self, data=None):
        super(RedeemedKobold, self).__init__(data)

    def AddEffect(self, character):
        super(RedeemedKobold, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(RedeemedKobold, self).RemoveEffect(character)


class ScaledDisciple(Feat):

    def __init__(self, data=None):
        super(ScaledDisciple, self).__init__(data)

    def AddEffect(self, character):
        super(ScaledDisciple, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ScaledDisciple, self).RemoveEffect(character)


class SmallButDeadly(Feat):

    def __init__(self, data=None):
        super(SmallButDeadly, self).__init__(data)

    def AddEffect(self, character):
        super(SmallButDeadly, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SmallButDeadly, self).RemoveEffect(character)


class KoboldFlood(Feat):

    def __init__(self, data=None):
        super(KoboldFlood, self).__init__(data)

    def AddEffect(self, character):
        super(KoboldFlood, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KoboldFlood, self).RemoveEffect(character)


class KoboldGroundling(Feat):

    def __init__(self, data=None):
        super(KoboldGroundling, self).__init__(data)

    def AddEffect(self, character):
        super(KoboldGroundling, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KoboldGroundling, self).RemoveEffect(character)


class KoboldStyle(Feat):

    def __init__(self, data=None):
        super(KoboldStyle, self).__init__(data)

    def AddEffect(self, character):
        super(KoboldStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(KoboldStyle, self).RemoveEffect(character)


class TribeMentality(Feat):

    def __init__(self, data=None):
        super(TribeMentality, self).__init__(data)

    def AddEffect(self, character):
        super(TribeMentality, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TribeMentality, self).RemoveEffect(character)


class WallOfflesh(Feat):

    def __init__(self, data=None):
        super(WallOfflesh, self).__init__(data)

    def AddEffect(self, character):
        super(WallOfflesh, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WallOfflesh, self).RemoveEffect(character)


class Apotheosis(Feat):

    def __init__(self, data=None):
        super(Apotheosis, self).__init__(data)

    def AddEffect(self, character):
        super(Apotheosis, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Apotheosis, self).RemoveEffect(character)


class ArtifactHunter(Feat):

    def __init__(self, data=None):
        super(ArtifactHunter, self).__init__(data)

    def AddEffect(self, character):
        super(ArtifactHunter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ArtifactHunter, self).RemoveEffect(character)


class Blessed(Feat):

    def __init__(self, data=None):
        super(Blessed, self).__init__(data)

    def AddEffect(self, character):
        super(Blessed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Blessed, self).RemoveEffect(character)


class Damned(Feat):

    def __init__(self, data=None):
        super(Damned, self).__init__(data)

    def AddEffect(self, character):
        super(Damned, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Damned, self).RemoveEffect(character)


class DynastyFounder(Feat):

    def __init__(self, data=None):
        super(DynastyFounder, self).__init__(data)

    def AddEffect(self, character):
        super(DynastyFounder, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DynastyFounder, self).RemoveEffect(character)


class Explorer(Feat):

    def __init__(self, data=None):
        super(Explorer, self).__init__(data)

    def AddEffect(self, character):
        super(Explorer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Explorer, self).RemoveEffect(character)


class Foeslayer(Feat):

    def __init__(self, data=None):
        super(Foeslayer, self).__init__(data)

    def AddEffect(self, character):
        super(Foeslayer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Foeslayer, self).RemoveEffect(character)


class Liberator(Feat):

    def __init__(self, data=None):
        super(Liberator, self).__init__(data)

    def AddEffect(self, character):
        super(Liberator, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Liberator, self).RemoveEffect(character)


class PlanarTraveler(Feat):

    def __init__(self, data=None):
        super(PlanarTraveler, self).__init__(data)

    def AddEffect(self, character):
        super(PlanarTraveler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PlanarTraveler, self).RemoveEffect(character)


class Prophet(Feat):

    def __init__(self, data=None):
        super(Prophet, self).__init__(data)

    def AddEffect(self, character):
        super(Prophet, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Prophet, self).RemoveEffect(character)


class TruthSeeker(Feat):

    def __init__(self, data=None):
        super(TruthSeeker, self).__init__(data)

    def AddEffect(self, character):
        super(TruthSeeker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TruthSeeker, self).RemoveEffect(character)


class ObjectOfLegend(Feat):

    def __init__(self, data=None):
        super(ObjectOfLegend, self).__init__(data)

    def AddEffect(self, character):
        super(ObjectOfLegend, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ObjectOfLegend, self).RemoveEffect(character)


class CenterOfPower(Feat):

    def __init__(self, data=None):
        super(CenterOfPower, self).__init__(data)

    def AddEffect(self, character):
        super(CenterOfPower, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CenterOfPower, self).RemoveEffect(character)


class ExpertTrainer(Feat):

    def __init__(self, data=None):
        super(ExpertTrainer, self).__init__(data)

    def AddEffect(self, character):
        super(ExpertTrainer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExpertTrainer, self).RemoveEffect(character)


class FocusedOverseer(Feat):

    def __init__(self, data=None):
        super(FocusedOverseer, self).__init__(data)

    def AddEffect(self, character):
        super(FocusedOverseer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FocusedOverseer, self).RemoveEffect(character)


class FocusedWorker(Feat):

    def __init__(self, data=None):
        super(FocusedWorker, self).__init__(data)

    def AddEffect(self, character):
        super(FocusedWorker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FocusedWorker, self).RemoveEffect(character)


class FortunateRuler(Feat):

    def __init__(self, data=None):
        super(FortunateRuler, self).__init__(data)

    def AddEffect(self, character):
        super(FortunateRuler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FortunateRuler, self).RemoveEffect(character)


class FortunateManager(Feat):

    def __init__(self, data=None):
        super(FortunateManager, self).__init__(data)

    def AddEffect(self, character):
        super(FortunateManager, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FortunateManager, self).RemoveEffect(character)


class InspirationalCommander(Feat):

    def __init__(self, data=None):
        super(InspirationalCommander, self).__init__(data)

    def AddEffect(self, character):
        super(InspirationalCommander, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InspirationalCommander, self).RemoveEffect(character)


class NaturalRuler(Feat):

    def __init__(self, data=None):
        super(NaturalRuler, self).__init__(data)

    def AddEffect(self, character):
        super(NaturalRuler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NaturalRuler, self).RemoveEffect(character)


class PrecociousYouth(Feat):

    def __init__(self, data=None):
        super(PrecociousYouth, self).__init__(data)

    def AddEffect(self, character):
        super(PrecociousYouth, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PrecociousYouth, self).RemoveEffect(character)


class DogSniffHate(Feat):

    def __init__(self, data=None):
        super(DogSniffHate, self).__init__(data)

    def AddEffect(self, character):
        super(DogSniffHate, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DogSniffHate, self).RemoveEffect(character)


class Dragoncrafting(Feat):

    def __init__(self, data=None):
        super(Dragoncrafting, self).__init__(data)

    def AddEffect(self, character):
        super(Dragoncrafting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Dragoncrafting, self).RemoveEffect(character)


class CourageInNumbers(Feat):

    def __init__(self, data=None):
        super(CourageInNumbers, self).__init__(data)

    def AddEffect(self, character):
        super(CourageInNumbers, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CourageInNumbers, self).RemoveEffect(character)


class Overwhelm(Feat):

    def __init__(self, data=None):
        super(Overwhelm, self).__init__(data)

    def AddEffect(self, character):
        super(Overwhelm, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Overwhelm, self).RemoveEffect(character)


class Tandemevasion(Feat):

    def __init__(self, data=None):
        super(Tandemevasion, self).__init__(data)

    def AddEffect(self, character):
        super(Tandemevasion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Tandemevasion, self).RemoveEffect(character)


class CoveringShield(Feat):

    def __init__(self, data=None):
        super(CoveringShield, self).__init__(data)

    def AddEffect(self, character):
        super(CoveringShield, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CoveringShield, self).RemoveEffect(character)


class DeathFrombelow(Feat):

    def __init__(self, data=None):
        super(DeathFrombelow, self).__init__(data)

    def AddEffect(self, character):
        super(DeathFrombelow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DeathFrombelow, self).RemoveEffect(character)


class Dragonheart(Feat):

    def __init__(self, data=None):
        super(Dragonheart, self).__init__(data)

    def AddEffect(self, character):
        super(Dragonheart, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Dragonheart, self).RemoveEffect(character)


class Dragonslayer(Feat):

    def __init__(self, data=None):
        super(Dragonslayer, self).__init__(data)

    def AddEffect(self, character):
        super(Dragonslayer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Dragonslayer, self).RemoveEffect(character)


class FlayingCritical(Feat):

    def __init__(self, data=None):
        super(FlayingCritical, self).__init__(data)

    def AddEffect(self, character):
        super(FlayingCritical, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FlayingCritical, self).RemoveEffect(character)


class PorcupineDefense(Feat):

    def __init__(self, data=None):
        super(PorcupineDefense, self).__init__(data)

    def AddEffect(self, character):
        super(PorcupineDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PorcupineDefense, self).RemoveEffect(character)


class ReachDefense(Feat):

    def __init__(self, data=None):
        super(ReachDefense, self).__init__(data)

    def AddEffect(self, character):
        super(ReachDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ReachDefense, self).RemoveEffect(character)


class Snoutgrip(Feat):

    def __init__(self, data=None):
        super(Snoutgrip, self).__init__(data)

    def AddEffect(self, character):
        super(Snoutgrip, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Snoutgrip, self).RemoveEffect(character)


class Wingclipper(Feat):

    def __init__(self, data=None):
        super(Wingclipper, self).__init__(data)

    def AddEffect(self, character):
        super(Wingclipper, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Wingclipper, self).RemoveEffect(character)


class ImprovedDayJob(Feat):

    def __init__(self, data=None):
        super(ImprovedDayJob, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedDayJob, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedDayJob, self).RemoveEffect(character)


class PatientStrike(Feat):

    def __init__(self, data=None):
        super(PatientStrike, self).__init__(data)

    def AddEffect(self, character):
        super(PatientStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PatientStrike, self).RemoveEffect(character)


class SteadfastMind(Feat):

    def __init__(self, data=None):
        super(SteadfastMind, self).__init__(data)

    def AddEffect(self, character):
        super(SteadfastMind, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SteadfastMind, self).RemoveEffect(character)


class QuickPreparation(Feat):

    def __init__(self, data=None):
        super(QuickPreparation, self).__init__(data)

    def AddEffect(self, character):
        super(QuickPreparation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuickPreparation, self).RemoveEffect(character)


class Renown(Feat):

    def __init__(self, data=None):
        super(Renown, self).__init__(data)

    def AddEffect(self, character):
        super(Renown, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Renown, self).RemoveEffect(character)


class VersatileSpontaneity(Feat):

    def __init__(self, data=None):
        super(VersatileSpontaneity, self).__init__(data)

    def AddEffect(self, character):
        super(VersatileSpontaneity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VersatileSpontaneity, self).RemoveEffect(character)


class CollectiveRecollection(Feat):

    def __init__(self, data=None):
        super(CollectiveRecollection, self).__init__(data)

    def AddEffect(self, character):
        super(CollectiveRecollection, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CollectiveRecollection, self).RemoveEffect(character)


class EsotericAdvantage(Feat):

    def __init__(self, data=None):
        super(EsotericAdvantage, self).__init__(data)

    def AddEffect(self, character):
        super(EsotericAdvantage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EsotericAdvantage, self).RemoveEffect(character)


class UncannyActivation(Feat):

    def __init__(self, data=None):
        super(UncannyActivation, self).__init__(data)

    def AddEffect(self, character):
        super(UncannyActivation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UncannyActivation, self).RemoveEffect(character)


class EmergencyAttunement(Feat):

    def __init__(self, data=None):
        super(EmergencyAttunement, self).__init__(data)

    def AddEffect(self, character):
        super(EmergencyAttunement, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EmergencyAttunement, self).RemoveEffect(character)


class PlannedSpontaneity(Feat):

    def __init__(self, data=None):
        super(PlannedSpontaneity, self).__init__(data)

    def AddEffect(self, character):
        super(PlannedSpontaneity, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PlannedSpontaneity, self).RemoveEffect(character)


class TapestryTraveler(Feat):

    def __init__(self, data=None):
        super(TapestryTraveler, self).__init__(data)

    def AddEffect(self, character):
        super(TapestryTraveler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TapestryTraveler, self).RemoveEffect(character)


class CutYourLosses(Feat):

    def __init__(self, data=None):
        super(CutYourLosses, self).__init__(data)

    def AddEffect(self, character):
        super(CutYourLosses, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CutYourLosses, self).RemoveEffect(character)


class ImprovedUnderhandedTeamwork(Feat):

    def __init__(self, data=None):
        super(ImprovedUnderhandedTeamwork, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedUnderhandedTeamwork, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedUnderhandedTeamwork, self).RemoveEffect(character)


class UnderhandedTeamwork(Feat):

    def __init__(self, data=None):
        super(UnderhandedTeamwork, self).__init__(data)

    def AddEffect(self, character):
        super(UnderhandedTeamwork, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UnderhandedTeamwork, self).RemoveEffect(character)


class AtheistAbjurations(Feat):

    def __init__(self, data=None):
        super(AtheistAbjurations, self).__init__(data)

    def AddEffect(self, character):
        super(AtheistAbjurations, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AtheistAbjurations, self).RemoveEffect(character)


class DivineDefiance(Feat):

    def __init__(self, data=None):
        super(DivineDefiance, self).__init__(data)

    def AddEffect(self, character):
        super(DivineDefiance, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DivineDefiance, self).RemoveEffect(character)


class DivineDenouncer(Feat):

    def __init__(self, data=None):
        super(DivineDenouncer, self).__init__(data)

    def AddEffect(self, character):
        super(DivineDenouncer, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DivineDenouncer, self).RemoveEffect(character)


class FocusedDisbelief(Feat):

    def __init__(self, data=None):
        super(FocusedDisbelief, self).__init__(data)

    def AddEffect(self, character):
        super(FocusedDisbelief, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FocusedDisbelief, self).RemoveEffect(character)


class Iconoclast(Feat):

    def __init__(self, data=None):
        super(Iconoclast, self).__init__(data)

    def AddEffect(self, character):
        super(Iconoclast, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Iconoclast, self).RemoveEffect(character)


class SeedsOfdoubt(Feat):

    def __init__(self, data=None):
        super(SeedsOfdoubt, self).__init__(data)

    def AddEffect(self, character):
        super(SeedsOfdoubt, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SeedsOfdoubt, self).RemoveEffect(character)


class AnimalAlly(Feat):

    def __init__(self, data=None):
        super(AnimalAlly, self).__init__(data)

    def AddEffect(self, character):
        super(AnimalAlly, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AnimalAlly, self).RemoveEffect(character)


class DruidicDecoder(Feat):

    def __init__(self, data=None):
        super(DruidicDecoder, self).__init__(data)

    def AddEffect(self, character):
        super(DruidicDecoder, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DruidicDecoder, self).RemoveEffect(character)


class FriendToAnimals(Feat):

    def __init__(self, data=None):
        super(FriendToAnimals, self).__init__(data)

    def AddEffect(self, character):
        super(FriendToAnimals, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FriendToAnimals, self).RemoveEffect(character)


class NatureSoul(Feat):

    def __init__(self, data=None):
        super(NatureSoul, self).__init__(data)

    def AddEffect(self, character):
        super(NatureSoul, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NatureSoul, self).RemoveEffect(character)


class WeatherEye(Feat):

    def __init__(self, data=None):
        super(WeatherEye, self).__init__(data)

    def AddEffect(self, character):
        super(WeatherEye, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WeatherEye, self).RemoveEffect(character)


class BendWithTheWind(Feat):

    def __init__(self, data=None):
        super(BendWithTheWind, self).__init__(data)

    def AddEffect(self, character):
        super(BendWithTheWind, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BendWithTheWind, self).RemoveEffect(character)


class BodyControl(Feat):

    def __init__(self, data=None):
        super(BodyControl, self).__init__(data)

    def AddEffect(self, character):
        super(BodyControl, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BodyControl, self).RemoveEffect(character)


class BodyMastery(Feat):

    def __init__(self, data=None):
        super(BodyMastery, self).__init__(data)

    def AddEffect(self, character):
        super(BodyMastery, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BodyMastery, self).RemoveEffect(character)


class CombatMeditation(Feat):

    def __init__(self, data=None):
        super(CombatMeditation, self).__init__(data)

    def AddEffect(self, character):
        super(CombatMeditation, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CombatMeditation, self).RemoveEffect(character)


class MeditationMaster(Feat):

    def __init__(self, data=None):
        super(MeditationMaster, self).__init__(data)

    def AddEffect(self, character):
        super(MeditationMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MeditationMaster, self).RemoveEffect(character)


class MeditativeConcentration(Feat):

    def __init__(self, data=None):
        super(MeditativeConcentration, self).__init__(data)

    def AddEffect(self, character):
        super(MeditativeConcentration, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MeditativeConcentration, self).RemoveEffect(character)


class PerfectAwareness(Feat):

    def __init__(self, data=None):
        super(PerfectAwareness, self).__init__(data)

    def AddEffect(self, character):
        super(PerfectAwareness, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PerfectAwareness, self).RemoveEffect(character)


class PerfectCenter(Feat):

    def __init__(self, data=None):
        super(PerfectCenter, self).__init__(data)

    def AddEffect(self, character):
        super(PerfectCenter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PerfectCenter, self).RemoveEffect(character)


class SlowTime(Feat):

    def __init__(self, data=None):
        super(SlowTime, self).__init__(data)

    def AddEffect(self, character):
        super(SlowTime, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SlowTime, self).RemoveEffect(character)


class DemonicNemesis(Feat):

    def __init__(self, data=None):
        super(DemonicNemesis, self).__init__(data)

    def AddEffect(self, character):
        super(DemonicNemesis, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DemonicNemesis, self).RemoveEffect(character)


class ExorcistSRebuttal(Feat):

    def __init__(self, data=None):
        super(ExorcistSRebuttal, self).__init__(data)

    def AddEffect(self, character):
        super(ExorcistSRebuttal, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExorcistSRebuttal, self).RemoveEffect(character)


class OuterPlanesTraveler(Feat):

    def __init__(self, data=None):
        super(OuterPlanesTraveler, self).__init__(data)

    def AddEffect(self, character):
        super(OuterPlanesTraveler, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OuterPlanesTraveler, self).RemoveEffect(character)


class VengefulBanisher(Feat):

    def __init__(self, data=None):
        super(VengefulBanisher, self).__init__(data)

    def AddEffect(self, character):
        super(VengefulBanisher, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(VengefulBanisher, self).RemoveEffect(character)


class CoordinatedDistraction(Feat):

    def __init__(self, data=None):
        super(CoordinatedDistraction, self).__init__(data)

    def AddEffect(self, character):
        super(CoordinatedDistraction, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CoordinatedDistraction, self).RemoveEffect(character)


class PunchThrough(Feat):

    def __init__(self, data=None):
        super(PunchThrough, self).__init__(data)

    def AddEffect(self, character):
        super(PunchThrough, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PunchThrough, self).RemoveEffect(character)


class SpellChain(Feat):

    def __init__(self, data=None):
        super(SpellChain, self).__init__(data)

    def AddEffect(self, character):
        super(SpellChain, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpellChain, self).RemoveEffect(character)


class BabauRogueTalent(Feat):

    def __init__(self, data=None):
        super(BabauRogueTalent, self).__init__(data)

    def AddEffect(self, character):
        super(BabauRogueTalent, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BabauRogueTalent, self).RemoveEffect(character)


class FlensingStrike(Feat):

    def __init__(self, data=None):
        super(FlensingStrike, self).__init__(data)

    def AddEffect(self, character):
        super(FlensingStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FlensingStrike, self).RemoveEffect(character)


class ImprovedStench(Feat):

    def __init__(self, data=None):
        super(ImprovedStench, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedStench, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedStench, self).RemoveEffect(character)


class PungentStench(Feat):

    def __init__(self, data=None):
        super(PungentStench, self).__init__(data)

    def AddEffect(self, character):
        super(PungentStench, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PungentStench, self).RemoveEffect(character)


class ToxicStench(Feat):

    def __init__(self, data=None):
        super(ToxicStench, self).__init__(data)

    def AddEffect(self, character):
        super(ToxicStench, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ToxicStench, self).RemoveEffect(character)


class DemonicPossession(Feat):

    def __init__(self, data=None):
        super(DemonicPossession, self).__init__(data)

    def AddEffect(self, character):
        super(DemonicPossession, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DemonicPossession, self).RemoveEffect(character)


class ImprovedPossession(Feat):

    def __init__(self, data=None):
        super(ImprovedPossession, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedPossession, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedPossession, self).RemoveEffect(character)


class PenetratingPossession(Feat):

    def __init__(self, data=None):
        super(PenetratingPossession, self).__init__(data)

    def AddEffect(self, character):
        super(PenetratingPossession, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PenetratingPossession, self).RemoveEffect(character)


class SpiritVision(Feat):

    def __init__(self, data=None):
        super(SpiritVision, self).__init__(data)

    def AddEffect(self, character):
        super(SpiritVision, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SpiritVision, self).RemoveEffect(character)


class ImprovedInfuseWeapon(Feat):

    def __init__(self, data=None):
        super(ImprovedInfuseWeapon, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedInfuseWeapon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedInfuseWeapon, self).RemoveEffect(character)


class MultiweaponDefense(Feat):

    def __init__(self, data=None):
        super(MultiweaponDefense, self).__init__(data)

    def AddEffect(self, character):
        super(MultiweaponDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MultiweaponDefense, self).RemoveEffect(character)


class MultiweaponSpecialist(Feat):

    def __init__(self, data=None):
        super(MultiweaponSpecialist, self).__init__(data)

    def AddEffect(self, character):
        super(MultiweaponSpecialist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MultiweaponSpecialist, self).RemoveEffect(character)


class ConsumeUndeath(Feat):

    def __init__(self, data=None):
        super(ConsumeUndeath, self).__init__(data)

    def AddEffect(self, character):
        super(ConsumeUndeath, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ConsumeUndeath, self).RemoveEffect(character)


class ImprovedDeathStealing(Feat):

    def __init__(self, data=None):
        super(ImprovedDeathStealing, self).__init__(data)

    def AddEffect(self, character):
        super(ImprovedDeathStealing, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ImprovedDeathStealing, self).RemoveEffect(character)


class AscendantSpell(Feat):

    def __init__(self, data=None):
        super(AscendantSpell, self).__init__(data)

    def AddEffect(self, character):
        super(AscendantSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(AscendantSpell, self).RemoveEffect(character)


class DrinkIsLife(Feat):

    def __init__(self, data=None):
        super(DrinkIsLife, self).__init__(data)

    def AddEffect(self, character):
        super(DrinkIsLife, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DrinkIsLife, self).RemoveEffect(character)


class DualPath(Feat):

    def __init__(self, data=None):
        super(DualPath, self).__init__(data)

    def AddEffect(self, character):
        super(DualPath, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DualPath, self).RemoveEffect(character)


class ExtraMythicPower(Feat):

    def __init__(self, data=None):
        super(ExtraMythicPower, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraMythicPower, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraMythicPower, self).RemoveEffect(character)


class ExtraPathAbility(Feat):

    def __init__(self, data=None):
        super(ExtraPathAbility, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraPathAbility, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraPathAbility, self).RemoveEffect(character)


class FabulousFigments(Feat):

    def __init__(self, data=None):
        super(FabulousFigments, self).__init__(data)

    def AddEffect(self, character):
        super(FabulousFigments, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FabulousFigments, self).RemoveEffect(character)


class LegendaryTeamwork(Feat):

    def __init__(self, data=None):
        super(LegendaryTeamwork, self).__init__(data)

    def AddEffect(self, character):
        super(LegendaryTeamwork, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LegendaryTeamwork, self).RemoveEffect(character)


class LuckySurge(Feat):

    def __init__(self, data=None):
        super(LuckySurge, self).__init__(data)

    def AddEffect(self, character):
        super(LuckySurge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(LuckySurge, self).RemoveEffect(character)


class MarkedForGlory(Feat):

    def __init__(self, data=None):
        super(MarkedForGlory, self).__init__(data)

    def AddEffect(self, character):
        super(MarkedForGlory, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MarkedForGlory, self).RemoveEffect(character)


class MaximizeSurge(Feat):

    def __init__(self, data=None):
        super(MaximizeSurge, self).__init__(data)

    def AddEffect(self, character):
        super(MaximizeSurge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MaximizeSurge, self).RemoveEffect(character)


class MythicCompanion(Feat):

    def __init__(self, data=None):
        super(MythicCompanion, self).__init__(data)

    def AddEffect(self, character):
        super(MythicCompanion, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MythicCompanion, self).RemoveEffect(character)


class MythicCrafter(Feat):

    def __init__(self, data=None):
        super(MythicCrafter, self).__init__(data)

    def AddEffect(self, character):
        super(MythicCrafter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MythicCrafter, self).RemoveEffect(character)


class MythicParagon(Feat):

    def __init__(self, data=None):
        super(MythicParagon, self).__init__(data)

    def AddEffect(self, character):
        super(MythicParagon, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MythicParagon, self).RemoveEffect(character)


class MythicSpellLore(Feat):

    def __init__(self, data=None):
        super(MythicSpellLore, self).__init__(data)

    def AddEffect(self, character):
        super(MythicSpellLore, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MythicSpellLore, self).RemoveEffect(character)


class PotentSurge(Feat):

    def __init__(self, data=None):
        super(PotentSurge, self).__init__(data)

    def AddEffect(self, character):
        super(PotentSurge, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PotentSurge, self).RemoveEffect(character)


class TitanStrike(Feat):

    def __init__(self, data=None):
        super(TitanStrike, self).__init__(data)

    def AddEffect(self, character):
        super(TitanStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TitanStrike, self).RemoveEffect(character)


class TwoFistedDrinker(Feat):

    def __init__(self, data=None):
        super(TwoFistedDrinker, self).__init__(data)

    def AddEffect(self, character):
        super(TwoFistedDrinker, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TwoFistedDrinker, self).RemoveEffect(character)


class ValiantVault(Feat):

    def __init__(self, data=None):
        super(ValiantVault, self).__init__(data)

    def AddEffect(self, character):
        super(ValiantVault, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ValiantVault, self).RemoveEffect(character)


class Demonologist(Feat):

    def __init__(self, data=None):
        super(Demonologist, self).__init__(data)

    def AddEffect(self, character):
        super(Demonologist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Demonologist, self).RemoveEffect(character)


class DemonGrafter(Feat):

    def __init__(self, data=None):
        super(DemonGrafter, self).__init__(data)

    def AddEffect(self, character):
        super(DemonGrafter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DemonGrafter, self).RemoveEffect(character)


class DemonicObedience(Feat):

    def __init__(self, data=None):
        super(DemonicObedience, self).__init__(data)

    def AddEffect(self, character):
        super(DemonicObedience, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DemonicObedience, self).RemoveEffect(character)


class ExtraFeature(Feat):

    def __init__(self, data=None):
        super(ExtraFeature, self).__init__(data)

    def AddEffect(self, character):
        super(ExtraFeature, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtraFeature, self).RemoveEffect(character)


class FastChange(Feat):

    def __init__(self, data=None):
        super(FastChange, self).__init__(data)

    def AddEffect(self, character):
        super(FastChange, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FastChange, self).RemoveEffect(character)


class BatShape(Feat):

    def __init__(self, data=None):
        super(BatShape, self).__init__(data)

    def AddEffect(self, character):
        super(BatShape, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BatShape, self).RemoveEffect(character)


class BloodmarkedFlight(Feat):

    def __init__(self, data=None):
        super(BloodmarkedFlight, self).__init__(data)

    def AddEffect(self, character):
        super(BloodmarkedFlight, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloodmarkedFlight, self).RemoveEffect(character)


class DireBatShape(Feat):

    def __init__(self, data=None):
        super(DireBatShape, self).__init__(data)

    def AddEffect(self, character):
        super(DireBatShape, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DireBatShape, self).RemoveEffect(character)


class BearHug(Feat):

    def __init__(self, data=None):
        super(BearHug, self).__init__(data)

    def AddEffect(self, character):
        super(BearHug, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BearHug, self).RemoveEffect(character)


class BeartrapBite(Feat):

    def __init__(self, data=None):
        super(BeartrapBite, self).__init__(data)

    def AddEffect(self, character):
        super(BeartrapBite, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BeartrapBite, self).RemoveEffect(character)


class FerociousLoyalty(Feat):

    def __init__(self, data=None):
        super(FerociousLoyalty, self).__init__(data)

    def AddEffect(self, character):
        super(FerociousLoyalty, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FerociousLoyalty, self).RemoveEffect(character)


class SwarmScatter(Feat):

    def __init__(self, data=None):
        super(SwarmScatter, self).__init__(data)

    def AddEffect(self, character):
        super(SwarmScatter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SwarmScatter, self).RemoveEffect(character)


class SwarmStrike(Feat):

    def __init__(self, data=None):
        super(SwarmStrike, self).__init__(data)

    def AddEffect(self, character):
        super(SwarmStrike, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SwarmStrike, self).RemoveEffect(character)


class MotivatingDisplay(Feat):

    def __init__(self, data=None):
        super(MotivatingDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(MotivatingDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MotivatingDisplay, self).RemoveEffect(character)


class SurprisingCombatant(Feat):

    def __init__(self, data=None):
        super(SurprisingCombatant, self).__init__(data)

    def AddEffect(self, character):
        super(SurprisingCombatant, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SurprisingCombatant, self).RemoveEffect(character)


class ViolentDisplay(Feat):

    def __init__(self, data=None):
        super(ViolentDisplay, self).__init__(data)

    def AddEffect(self, character):
        super(ViolentDisplay, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ViolentDisplay, self).RemoveEffect(character)


class WolfSavage(Feat):

    def __init__(self, data=None):
        super(WolfSavage, self).__init__(data)

    def AddEffect(self, character):
        super(WolfSavage, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WolfSavage, self).RemoveEffect(character)


class WolfStyle(Feat):

    def __init__(self, data=None):
        super(WolfStyle, self).__init__(data)

    def AddEffect(self, character):
        super(WolfStyle, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WolfStyle, self).RemoveEffect(character)


class WolfTrip(Feat):

    def __init__(self, data=None):
        super(WolfTrip, self).__init__(data)

    def AddEffect(self, character):
        super(WolfTrip, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WolfTrip, self).RemoveEffect(character)


class BloatmageInitiate(Feat):

    def __init__(self, data=None):
        super(BloatmageInitiate, self).__init__(data)

    def AddEffect(self, character):
        super(BloatmageInitiate, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BloatmageInitiate, self).RemoveEffect(character)


class MultiweaponFighting(Feat):

    def __init__(self, data=None):
        super(MultiweaponFighting, self).__init__(data)

    def AddEffect(self, character):
        super(MultiweaponFighting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(MultiweaponFighting, self).RemoveEffect(character)


class StableSpell(Feat):

    def __init__(self, data=None):
        super(StableSpell, self).__init__(data)

    def AddEffect(self, character):
        super(StableSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(StableSpell, self).RemoveEffect(character)


class ShadowGambit(Feat):

    def __init__(self, data=None):
        super(ShadowGambit, self).__init__(data)

    def AddEffect(self, character):
        super(ShadowGambit, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadowGambit, self).RemoveEffect(character)


class ShadowGrasp(Feat):

    def __init__(self, data=None):
        super(ShadowGrasp, self).__init__(data)

    def AddEffect(self, character):
        super(ShadowGrasp, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShadowGrasp, self).RemoveEffect(character)


class TenebrousSpell(Feat):

    def __init__(self, data=None):
        super(TenebrousSpell, self).__init__(data)

    def AddEffect(self, character):
        super(TenebrousSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(TenebrousSpell, self).RemoveEffect(character)


class UmbralSpell(Feat):

    def __init__(self, data=None):
        super(UmbralSpell, self).__init__(data)

    def AddEffect(self, character):
        super(UmbralSpell, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(UmbralSpell, self).RemoveEffect(character)


class InscribeMagicalTattoo(Feat):

    def __init__(self, data=None):
        super(InscribeMagicalTattoo, self).__init__(data)

    def AddEffect(self, character):
        super(InscribeMagicalTattoo, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(InscribeMagicalTattoo, self).RemoveEffect(character)


class ExtendTheBulwark(Feat):

    def __init__(self, data=None):
        super(ExtendTheBulwark, self).__init__(data)

    def AddEffect(self, character):
        super(ExtendTheBulwark, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ExtendTheBulwark, self).RemoveEffect(character)


class QuillbreakerDefense(Feat):

    def __init__(self, data=None):
        super(QuillbreakerDefense, self).__init__(data)

    def AddEffect(self, character):
        super(QuillbreakerDefense, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(QuillbreakerDefense, self).RemoveEffect(character)


class ShieldSnag(Feat):

    def __init__(self, data=None):
        super(ShieldSnag, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldSnag, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldSnag, self).RemoveEffect(character)


class EquipmentTrick(Feat):

    def __init__(self, data=None):
        super(EquipmentTrick, self).__init__(data)

    def AddEffect(self, character):
        super(EquipmentTrick, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(EquipmentTrick, self).RemoveEffect(character)


class BlowoutShotDeed(Feat):

    def __init__(self, data=None):
        super(BlowoutShotDeed, self).__init__(data)

    def AddEffect(self, character):
        super(BlowoutShotDeed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BlowoutShotDeed, self).RemoveEffect(character)


class WhipShotDeed(Feat):

    def __init__(self, data=None):
        super(WhipShotDeed, self).__init__(data)

    def AddEffect(self, character):
        super(WhipShotDeed, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WhipShotDeed, self).RemoveEffect(character)


class FalseCasting(Feat):

    def __init__(self, data=None):
        super(FalseCasting, self).__init__(data)

    def AddEffect(self, character):
        super(FalseCasting, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FalseCasting, self).RemoveEffect(character)


class FalseFocus(Feat):

    def __init__(self, data=None):
        super(FalseFocus, self).__init__(data)

    def AddEffect(self, character):
        super(FalseFocus, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(FalseFocus, self).RemoveEffect(character)


class Osirionology(Feat):

    def __init__(self, data=None):
        super(Osirionology, self).__init__(data)

    def AddEffect(self, character):
        super(Osirionology, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Osirionology, self).RemoveEffect(character)


class OutOfTheSun(Feat):

    def __init__(self, data=None):
        super(OutOfTheSun, self).__init__(data)

    def AddEffect(self, character):
        super(OutOfTheSun, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(OutOfTheSun, self).RemoveEffect(character)


class ThuvianGrenadier(Feat):

    def __init__(self, data=None):
        super(ThuvianGrenadier, self).__init__(data)

    def AddEffect(self, character):
        super(ThuvianGrenadier, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ThuvianGrenadier, self).RemoveEffect(character)


class Undermine(Feat):

    def __init__(self, data=None):
        super(Undermine, self).__init__(data)

    def AddEffect(self, character):
        super(Undermine, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Undermine, self).RemoveEffect(character)


class HornOfTheCriosphinx(Feat):

    def __init__(self, data=None):
        super(HornOfTheCriosphinx, self).__init__(data)

    def AddEffect(self, character):
        super(HornOfTheCriosphinx, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(HornOfTheCriosphinx, self).RemoveEffect(character)


class WingsOfTheAndrosphinx(Feat):

    def __init__(self, data=None):
        super(WingsOfTheAndrosphinx, self).__init__(data)

    def AddEffect(self, character):
        super(WingsOfTheAndrosphinx, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(WingsOfTheAndrosphinx, self).RemoveEffect(character)


class ShieldMaster(Feat):

    def __init__(self, data=None):
        super(ShieldMaster, self).__init__(data)

    def AddEffect(self, character):
        super(ShieldMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(ShieldMaster, self).RemoveEffect(character)


class BetrayingBlow(Feat):

    def __init__(self, data=None):
        super(BetrayingBlow, self).__init__(data)

    def AddEffect(self, character):
        super(BetrayingBlow, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(BetrayingBlow, self).RemoveEffect(character)


class SoloManeuvers(Feat):

    def __init__(self, data=None):
        super(SoloManeuvers, self).__init__(data)

    def AddEffect(self, character):
        super(SoloManeuvers, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(SoloManeuvers, self).RemoveEffect(character)


class DirtyTrickMaster(Feat):

    def __init__(self, data=None):
        super(DirtyTrickMaster, self).__init__(data)

    def AddEffect(self, character):
        super(DirtyTrickMaster, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DirtyTrickMaster, self).RemoveEffect(character)


class DivertHarm(Feat):

    def __init__(self, data=None):
        super(DivertHarm, self).__init__(data)

    def AddEffect(self, character):
        super(DivertHarm, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(DivertHarm, self).RemoveEffect(character)


class CrisisOfConscience(Feat):

    def __init__(self, data=None):
        super(CrisisOfConscience, self).__init__(data)

    def AddEffect(self, character):
        super(CrisisOfConscience, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(CrisisOfConscience, self).RemoveEffect(character)


class PlanarHunter(Feat):

    def __init__(self, data=None):
        super(PlanarHunter, self).__init__(data)

    def AddEffect(self, character):
        super(PlanarHunter, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PlanarHunter, self).RemoveEffect(character)


class PracticedLeadership(Feat):

    def __init__(self, data=None):
        super(PracticedLeadership, self).__init__(data)

    def AddEffect(self, character):
        super(PracticedLeadership, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(PracticedLeadership, self).RemoveEffect(character)


class Fabulist(Feat):

    def __init__(self, data=None):
        super(Fabulist, self).__init__(data)

    def AddEffect(self, character):
        super(Fabulist, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(Fabulist, self).RemoveEffect(character)


class GunTwirling(Feat):

    def __init__(self, data=None):
        super(GunTwirling, self).__init__(data)

    def AddEffect(self, character):
        super(GunTwirling, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(GunTwirling, self).RemoveEffect(character)


class NamedBullet(Feat):

    def __init__(self, data=None):
        super(NamedBullet, self).__init__(data)

    def AddEffect(self, character):
        super(NamedBullet, self).AddEffect(character)

    def RemoveEffect(self, character):
        super(NamedBullet, self).RemoveEffect(character)


FeatClasses = {
    config.FEAT_ACROBATIC: Acrobatic,
    config.FEAT_ACROBATIC_STEPS: AcrobaticSteps,
    config.FEAT_AGILE_MANEUVERS: AgileManeuvers,
    config.FEAT_ALERTNESS: Alertness,
    config.FEAT_ALIGNMENT_CHANNEL: AlignmentChannel,
    config.FEAT_ANIMAL_AFFINITY: AnimalAffinity,
    config.FEAT_ARCANE_ARMOR_MASTERY: ArcaneArmorMastery,
    config.FEAT_ARCANE_ARMOR_TRAINING: ArcaneArmorTraining,
    config.FEAT_ARCANE_STRIKE: ArcaneStrike,
    config.FEAT_HEAVY_ARMOR_PROFICIENCY: HeavyArmorProficiency,
    config.FEAT_LIGHT_ARMOR_PROFICIENCY: LightArmorProficiency,
    config.FEAT_MEDIUM_ARMOR_PROFICIENCY: MediumArmorProficiency,
    config.FEAT_ATHLETIC: Athletic,
    config.FEAT_AUGMENT_SUMMONING: AugmentSummoning,
    config.FEAT_BLEEDING_CRITICAL: BleedingCritical,
    config.FEAT_BLIND_FIGHT: BlindFight,
    config.FEAT_BLINDING_CRITICAL: BlindingCritical,
    config.FEAT_BREW_POTION: BrewPotion,
    config.FEAT_CATCH_OFF_GUARD: CatchOffGuard,
    config.FEAT_CHANNEL_SMITE: ChannelSmite,
    config.FEAT_CLEAVE: Cleave,
    config.FEAT_COMBAT_CASTING: CombatCasting,
    config.FEAT_COMBAT_EXPERTISE: CombatExpertise,
    config.FEAT_COMBAT_REFLEXES: CombatReflexes,
    config.FEAT_COMMAND_UNDEAD: CommandUndead,
    config.FEAT_CRAFT_MAGIC_ARMS_AND_ARMOR: CraftMagicArmsAndArmor,
    config.FEAT_CRAFT_ROD: CraftRod,
    config.FEAT_CRAFT_WAND: CraftWand,
    config.FEAT_CRAFT_STAFF: CraftStaff,
    config.FEAT_CRAFT_WONDROUS_ITEM: CraftWondrousItem,
    config.FEAT_CRITICAL_FOCUS: CriticalFocus,
    config.FEAT_CRITICAL_MASTERY: CriticalMastery,
    config.FEAT_DAZZLING_DISPLAY: DazzlingDisplay,
    config.FEAT_DEADLY_AIM: DeadlyAim,
    config.FEAT_DEADLY_STROKE: DeadlyStroke,
    config.FEAT_DEAFENING_CRITICAL: DeafeningCritical,
    config.FEAT_DECEITFUL: Deceitful,
    config.FEAT_DEFENSIVE_COMBAT_TRAINING: DefensiveCombatTraining,
    config.FEAT_DEFLECT_ARROWS: DeflectArrows,
    config.FEAT_DEFT_HANDS: DeftHands,
    config.FEAT_DIEHARD: Diehard,
    config.FEAT_DISRUPTIVE: Disruptive,
    config.FEAT_DODGE: Dodge,
    config.FEAT_DOUBLE_SLICE: DoubleSlice,
    config.FEAT_ELEMENTAL_CHANNEL: ElementalChannel,
    config.FEAT_EMPOWER_SPELL: EmpowerSpell,
    config.FEAT_ENDURANCE: Endurance,
    config.FEAT_ENLARGE_SPELL: EnlargeSpell,
    config.FEAT_ESCHEW_MATERIALS: EschewMaterials,
    config.FEAT_EXHAUSTING_CRITICAL: ExhaustingCritical,
    config.FEAT_EXOTIC_WEAPON_PROFICIENCY: ExoticWeaponProficiency,
    config.FEAT_EXTEND_SPELL: ExtendSpell,
    config.FEAT_EXTRA_CHANNEL: ExtraChannel,
    config.FEAT_EXTRA_KI: ExtraKi,
    config.FEAT_EXTRA_LAY_ON_HANDS: ExtraLayOnHands,
    config.FEAT_EXTRA_MERCY: ExtraMercy,
    config.FEAT_EXTRA_PERFORMANCE: ExtraPerformance,
    config.FEAT_EXTRA_RAGE: ExtraRage,
    config.FEAT_FAR_SHOT: FarShot,
    config.FEAT_FLEET: Fleet,
    config.FEAT_FORGE_RING: ForgeRing,
    config.FEAT_GORGON_S_FIST: GorgonSFist,
    config.FEAT_GREAT_CLEAVE: GreatCleave,
    config.FEAT_GREAT_FORTITUDE: GreatFortitude,
    config.FEAT_GREATER_BULL_RUSH: GreaterBullRush,
    config.FEAT_GREATER_DISARM: GreaterDisarm,
    config.FEAT_GREATER_FEINT: GreaterFeint,
    config.FEAT_GREATER_GRAPPLE: GreaterGrapple,
    config.FEAT_GREATER_OVERRUN: GreaterOverrun,
    config.FEAT_GREATER_PENETRATING_STRIKE: GreaterPenetratingStrike,
    config.FEAT_GREATER_SHIELD_FOCUS: GreaterShieldFocus,
    config.FEAT_GREATER_SPELL_FOCUS: GreaterSpellFocus,
    config.FEAT_GREATER_SPELL_PENETRATION: GreaterSpellPenetration,
    config.FEAT_GREATER_SUNDER: GreaterSunder,
    config.FEAT_GREATER_TRIP: GreaterTrip,
    config.FEAT_GREATER_TWO_WEAPON_FIGHTING: GreaterTwoWeaponFighting,
    config.FEAT_GREATER_VITAL_STRIKE: GreaterVitalStrike,
    config.FEAT_GREATER_WEAPON_FOCUS: GreaterWeaponFocus,
    config.FEAT_GREATER_WEAPON_SPECIALIZATION: GreaterWeaponSpecialization,
    config.FEAT_HEIGHTEN_SPELL: HeightenSpell,
    config.FEAT_IMPROVED_BULL_RUSH: ImprovedBullRush,
    config.FEAT_IMPROVED_CHANNEL: ImprovedChannel,
    config.FEAT_IMPROVED_COUNTERSPELL: ImprovedCounterspell,
    config.FEAT_IMPROVED_CRITICAL: ImprovedCritical,
    config.FEAT_IMPROVED_DISARM: ImprovedDisarm,
    config.FEAT_IMPROVED_FAMILIAR: ImprovedFamiliar,
    config.FEAT_IMPROVED_FEINT: ImprovedFeint,
    config.FEAT_IMPROVED_GRAPPLE: ImprovedGrapple,
    config.FEAT_IMPROVED_GREAT_FORTITUDE: ImprovedGreatFortitude,
    config.FEAT_IMPROVED_INITIATIVE: ImprovedInitiative,
    config.FEAT_IMPROVED_IRON_WILL: ImprovedIronWill,
    config.FEAT_IMPROVED_LIGHTNING_REFLEXES: ImprovedLightningReflexes,
    config.FEAT_IMPROVED_OVERRUN: ImprovedOverrun,
    config.FEAT_IMPROVED_PRECISE_SHOT: ImprovedPreciseShot,
    config.FEAT_IMPROVED_SHIELD_BASH: ImprovedShieldBash,
    config.FEAT_IMPROVED_SUNDER: ImprovedSunder,
    config.FEAT_IMPROVED_TRIP: ImprovedTrip,
    config.FEAT_IMPROVED_TWO_WEAPON_FIGHTING: ImprovedTwoWeaponFighting,
    config.FEAT_IMPROVED_UNARMED_STRIKE: ImprovedUnarmedStrike,
    config.FEAT_IMPROVED_VITAL_STRIKE: ImprovedVitalStrike,
    config.FEAT_IMPROVISED_WEAPON_MASTERY: ImprovisedWeaponMastery,
    config.FEAT_INTIMIDATING_PROWESS: IntimidatingProwess,
    config.FEAT_IRON_WILL: IronWill,
    config.FEAT_LEADERSHIP: Leadership,
    config.FEAT_LIGHTNING_REFLEXES: LightningReflexes,
    config.FEAT_LIGHTNING_STANCE: LightningStance,
    config.FEAT_LUNGE: Lunge,
    config.FEAT_MAGICAL_APTITUDE: MagicalAptitude,
    config.FEAT_MANYSHOT: Manyshot,
    config.FEAT_MARTIAL_WEAPON_PROFICIENCY: MartialWeaponProficiency,
    config.FEAT_MASTER_CRAFTSMAN: MasterCraftsman,
    config.FEAT_MAXIMIZE_SPELL: MaximizeSpell,
    config.FEAT_MEDUSA_S_WRATH: MedusaSWrath,
    config.FEAT_MOBILITY: Mobility,
    config.FEAT_MOUNTED_ARCHERY: MountedArchery,
    config.FEAT_MOUNTED_COMBAT: MountedCombat,
    config.FEAT_NATURAL_SPELL: NaturalSpell,
    config.FEAT_NIMBLE_MOVES: NimbleMoves,
    config.FEAT_PENETRATING_STRIKE: PenetratingStrike,
    config.FEAT_PERSUASIVE: Persuasive,
    config.FEAT_PINPOINT_TARGETING: PinpointTargeting,
    config.FEAT_POINT_BLANK_SHOT: PointBlankShot,
    config.FEAT_POWER_ATTACK: PowerAttack,
    config.FEAT_PRECISE_SHOT: PreciseShot,
    config.FEAT_QUICK_DRAW: QuickDraw,
    config.FEAT_QUICKEN_SPELL: QuickenSpell,
    config.FEAT_RAPID_SHOT: RapidShot,
    config.FEAT_RIDE_BY_ATTACK: RideByAttack,
    config.FEAT_RUN: Run,
    config.FEAT_SCORPION_STYLE: ScorpionStyle,
    config.FEAT_SCRIBE_SCROLL: ScribeScroll,
    config.FEAT_SELECTIVE_CHANNELING: SelectiveChanneling,
    config.FEAT_SELF_SUFFICIENT: SelfSufficient,
    config.FEAT_SHATTER_DEFENSES: ShatterDefenses,
    config.FEAT_SHIELD_FOCUS: ShieldFocus,
    config.FEAT_SHIELD_PROFICIENCY: ShieldProficiency,
    config.FEAT_SHIELD_SLAM: ShieldSlam,
    config.FEAT_SHOT_ON_THE_RUN: ShotOnTheRun,
    config.FEAT_SICKENING_CRITICAL: SickeningCritical,
    config.FEAT_SILENT_SPELL: SilentSpell,
    config.FEAT_SIMPLE_WEAPON_PROFICIENCY: SimpleWeaponProficiency,
    config.FEAT_SKILL_FOCUS: SkillFocus,
    config.FEAT_SNATCH_ARROWS: SnatchArrows,
    config.FEAT_SPELL_FOCUS: SpellFocus,
    config.FEAT_SPELL_MASTERY: SpellMastery,
    config.FEAT_SPELL_PENETRATION: SpellPenetration,
    config.FEAT_SPELLBREAKER: Spellbreaker,
    config.FEAT_SPIRITED_CHARGE: SpiritedCharge,
    config.FEAT_SPRING_ATTACK: SpringAttack,
    config.FEAT_STAGGERING_CRITICAL: StaggeringCritical,
    config.FEAT_STAND_STILL: StandStill,
    config.FEAT_STEALTHY: Stealthy,
    config.FEAT_STEP_UP: StepUp,
    config.FEAT_STILL_SPELL: StillSpell,
    config.FEAT_STRIKE_BACK: StrikeBack,
    config.FEAT_STUNNING_CRITICAL: StunningCritical,
    config.FEAT_STUNNING_FIST: StunningFist,
    config.FEAT_THROW_ANYTHING: ThrowAnything,
    config.FEAT_TIRING_CRITICAL: TiringCritical,
    config.FEAT_TOUGHNESS: Toughness,
    config.FEAT_TOWER_SHIELD_PROFICIENCY: TowerShieldProficiency,
    config.FEAT_TRAMPLE: Trample,
    config.FEAT_TURN_UNDEAD: TurnUndead,
    config.FEAT_TWO_WEAPON_DEFENSE: TwoWeaponDefense,
    config.FEAT_TWO_WEAPON_FIGHTING: TwoWeaponFighting,
    config.FEAT_TWO_WEAPON_REND: TwoWeaponRend,
    config.FEAT_UNSEAT: Unseat,
    config.FEAT_VITAL_STRIKE: VitalStrike,
    config.FEAT_WEAPON_FINESSE: WeaponFinesse,
    config.FEAT_WEAPON_FOCUS: WeaponFocus,
    config.FEAT_WEAPON_SPECIALIZATION: WeaponSpecialization,
    config.FEAT_WHIRLWIND_ATTACK: WhirlwindAttack,
    config.FEAT_WIDEN_SPELL: WidenSpell,
    config.FEAT_WIND_STANCE: WindStance,
    config.FEAT_ADDITIONAL_TRAITS: AdditionalTraits,
    config.FEAT_ABILITY_FOCUS: AbilityFocus,
    config.FEAT_AWESOME_BLOW: AwesomeBlow,
    config.FEAT_CRAFT_CONSTRUCT: CraftConstruct,
    config.FEAT_EMPOWER_SPELL_LIKE_ABILITY: EmpowerSpellLikeAbility,
    config.FEAT_FLYBY_ATTACK: FlybyAttack,
    config.FEAT_HOVER: Hover,
    config.FEAT_IMPROVED_NATURAL_ARMOR: ImprovedNaturalArmor,
    config.FEAT_IMPROVED_NATURAL_ATTACK: ImprovedNaturalAttack,
    config.FEAT_MULTIATTACK: Multiattack,
    config.FEAT_QUICKEN_SPELL_LIKE_ABILITY: QuickenSpellLikeAbility,
    config.FEAT_SNATCH: Snatch,
    config.FEAT_WINGOVER: Wingover,
    config.FEAT_ALLIED_SPELLCASTER: AlliedSpellcaster,
    config.FEAT_ARCANE_BLAST: ArcaneBlast,
    config.FEAT_ARCANE_SHIELD: ArcaneShield,
    config.FEAT_ARCANE_TALENT: ArcaneTalent,
    config.FEAT_ASPECT_OF_THE_BEAST: AspectOfTheBeast,
    config.FEAT_BASHING_FINISH: BashingFinish,
    config.FEAT_BLOODY_ASSAULT: BloodyAssault,
    config.FEAT_BODYGUARD: Bodyguard,
    config.FEAT_BOUNCING_SPELL: BouncingSpell,
    config.FEAT_BREADTH_OF_EXPERIENCE: BreadthOfExperience,
    config.FEAT_BULL_RUSH_STRIKE: BullRushStrike,
    config.FEAT_CHARGE_THROUGH: ChargeThrough,
    config.FEAT_CHILDLIKE: Childlike,
    config.FEAT_CLOUD_STEP: CloudStep,
    config.FEAT_COCKATRICE_STRIKE: CockatriceStrike,
    config.FEAT_COMBAT_PATROL: CombatPatrol,
    config.FEAT_COOPERATIVE_CRAFTING: CooperativeCrafting,
    config.FEAT_COORDINATED_DEFENSE: CoordinatedDefense,
    config.FEAT_COORDINATED_MANEUVERS: CoordinatedManeuvers,
    config.FEAT_COSMOPOLITAN: Cosmopolitan,
    config.FEAT_COVERING_DEFENSE: CoveringDefense,
    config.FEAT_CRIPPLING_CRITICAL: CripplingCritical,
    config.FEAT_CROSSBOW_MASTERY: CrossbowMastery,
    config.FEAT_DASTARDLY_FINISH: DastardlyFinish,
    config.FEAT_DAZING_ASSAULT: DazingAssault,
    config.FEAT_DAZING_SPELL: DazingSpell,
    config.FEAT_DEEP_DRINKER: DeepDrinker,
    config.FEAT_DEEPSIGHT: Deepsight,
    config.FEAT_DISARMING_STRIKE: DisarmingStrike,
    config.FEAT_DISRUPTING_SHOT: DisruptingShot,
    config.FEAT_DISRUPTIVE_SPELL: DisruptiveSpell,
    config.FEAT_DIVINER_S_DELVING: DivinerSDelving,
    config.FEAT_DREADFUL_CARNAGE: DreadfulCarnage,
    config.FEAT_DUCK_AND_COVER: DuckAndCover,
    config.FEAT_EAGLE_EYES: EagleEyes,
    config.FEAT_ECLECTIC: Eclectic,
    config.FEAT_ECTOPLASMIC_SPELL: EctoplasmicSpell,
    config.FEAT_ELDRITCH_CLAWS: EldritchClaws,
    config.FEAT_ELEMENTAL_FIST: ElementalFist,
    config.FEAT_ELEMENTAL_FOCUS: ElementalFocus,
    config.FEAT_ELEMENTAL_SPELL: ElementalSpell,
    config.FEAT_ELVEN_ACCURACY: ElvenAccuracy,
    config.FEAT_ENFORCER: Enforcer,
    config.FEAT_EXPANDED_ARCANA: ExpandedArcana,
    config.FEAT_EXTRA_BOMBS: ExtraBombs,
    config.FEAT_EXTRA_DISCOVERY: ExtraDiscovery,
    config.FEAT_EXTRA_HEX: ExtraHex,
    config.FEAT_EXTRA_RAGE_POWER: ExtraRagePower,
    config.FEAT_EXTRA_REVELATION: ExtraRevelation,
    config.FEAT_EXTRA_ROGUE_TALENT: ExtraRogueTalent,
    config.FEAT_FAST_DRINKER: FastDrinker,
    config.FEAT_FAST_HEALER: FastHealer,
    config.FEAT_FAVORED_DEFENSE: FavoredDefense,
    config.FEAT_FIGHT_ON: FightOn,
    config.FEAT_FOCUSED_SHOT: FocusedShot,
    config.FEAT_FOCUSED_SPELL: FocusedSpell,
    config.FEAT_FOLLOWING_STEP: FollowingStep,
    config.FEAT_FURIOUS_FOCUS: FuriousFocus,
    config.FEAT_GANG_UP: GangUp,
    config.FEAT_GNOME_TRICKSTER: GnomeTrickster,
    config.FEAT_GO_UNNOTICED: GoUnnoticed,
    config.FEAT_GREATER_BLIND_FIGHT: GreaterBlindFight,
    config.FEAT_GREATER_DIRTY_TRICK: GreaterDirtyTrick,
    config.FEAT_GREATER_DRAG: GreaterDrag,
    config.FEAT_GREATER_ELEMENTAL_FOCUS: GreaterElementalFocus,
    config.FEAT_GREATER_REPOSITION: GreaterReposition,
    config.FEAT_GREATER_SHIELD_SPECIALIZATION: GreaterShieldSpecialization,
    config.FEAT_GREATER_STEAL: GreaterSteal,
    config.FEAT_GROUNDLING: Groundling,
    config.FEAT_HEROIC_DEFIANCE: HeroicDefiance,
    config.FEAT_HEROIC_RECOVERY: HeroicRecovery,
    config.FEAT_IMPROVED_BLIND_FIGHT: ImprovedBlindFight,
    config.FEAT_IMPROVED_DIRTY_TRICK: ImprovedDirtyTrick,
    config.FEAT_IMPROVED_DRAG: ImprovedDrag,
    config.FEAT_IMPROVED_KI_THROW: ImprovedKiThrow,
    config.FEAT_IMPROVED_REPOSITION: ImprovedReposition,
    config.FEAT_IMPROVED_SECOND_CHANCE: ImprovedSecondChance,
    config.FEAT_IMPROVED_SHARE_SPELLS: ImprovedShareSpells,
    config.FEAT_IMPROVED_SIDESTEP: ImprovedSidestep,
    config.FEAT_IMPROVED_STEAL: ImprovedSteal,
    config.FEAT_IMPROVED_STONECUNNING: ImprovedStonecunning,
    config.FEAT_INTENSIFIED_SPELL: IntensifiedSpell,
    config.FEAT_IN_HARM_S_WAY: InHarmSWay,
    config.FEAT_IRONGUTS: Ironguts,
    config.FEAT_IRONHIDE: Ironhide,
    config.FEAT_KEEN_SCENT: KeenScent,
    config.FEAT_KI_THROW: KiThrow,
    config.FEAT_LEAF_SINGER: LeafSinger,
    config.FEAT_LIGHT_STEP: LightStep,
    config.FEAT_LINGERING_PERFORMANCE: LingeringPerformance,
    config.FEAT_LINGERING_SPELL: LingeringSpell,
    config.FEAT_LOOKOUT: Lookout,
    config.FEAT_LOW_PROFILE: LowProfile,
    config.FEAT_LUCKY_HALFLING: LuckyHalfling,
    config.FEAT_MAJOR_SPELL_EXPERTISE: MajorSpellExpertise,
    config.FEAT_MASTER_ALCHEMIST: MasterAlchemist,
    config.FEAT_MERCIFUL_SPELL: MercifulSpell,
    config.FEAT_MINOR_SPELL_EXPERTISE: MinorSpellExpertise,
    config.FEAT_MISSILE_SHIELD: MissileShield,
    config.FEAT_MOUNTED_SHIELD: MountedShield,
    config.FEAT_MOUNTED_SKIRMISHER: MountedSkirmisher,
    config.FEAT_OUTFLANK: Outflank,
    config.FEAT_PAIRED_OPPORTUNISTS: PairedOpportunists,
    config.FEAT_PARRY_SPELL: ParrySpell,
    config.FEAT_PARTING_SHOT: PartingShot,
    config.FEAT_PASS_FOR_HUMAN: PassForHuman,
    config.FEAT_PERFECT_STRIKE: PerfectStrike,
    config.FEAT_PERSISTENT_SPELL: PersistentSpell,
    config.FEAT_POINT_BLANK_MASTER: PointBlankMaster,
    config.FEAT_PRACTICED_TACTICIAN: PracticedTactician,
    config.FEAT_PRECISE_STRIKE: PreciseStrike,
    config.FEAT_PREFERRED_SPELL: PreferredSpell,
    config.FEAT_PUNISHING_KICK: PunishingKick,
    config.FEAT_PUSHING_ASSAULT: PushingAssault,
    config.FEAT_RACIAL_HERITAGE: RacialHeritage,
    config.FEAT_RAGING_VITALITY: RagingVitality,
    config.FEAT_RAY_SHIELD: RayShield,
    config.FEAT_RAZORTUSK: Razortusk,
    config.FEAT_REACH_SPELL: ReachSpell,
    config.FEAT_RENDING_CLAWS: RendingClaws,
    config.FEAT_REPOSITIONING_STRIKE: RepositioningStrike,
    config.FEAT_SAVING_SHIELD: SavingShield,
    config.FEAT_SECOND_CHANCE: SecondChance,
    config.FEAT_SELECTIVE_SPELL: SelectiveSpell,
    config.FEAT_SHADOW_STRIKE: ShadowStrike,
    config.FEAT_SHARED_INSIGHT: SharedInsight,
    config.FEAT_SHARP_SENSES: SharpSenses,
    config.FEAT_SHIELD_OF_SWINGS: ShieldOfSwings,
    config.FEAT_SHIELD_SPECIALIZATION: ShieldSpecialization,
    config.FEAT_SHIELD_WALL: ShieldWall,
    config.FEAT_SHIELDED_CASTER: ShieldedCaster,
    config.FEAT_SICKENING_SPELL: SickeningSpell,
    config.FEAT_SIDESTEP: Sidestep,
    config.FEAT_SMASH: Smash,
    config.FEAT_SMELL_FEAR: SmellFear,
    config.FEAT_SOCIABLE: Sociable,
    config.FEAT_SPELL_PERFECTION: SpellPerfection,
    config.FEAT_SPIDER_STEP: SpiderStep,
    config.FEAT_STABBING_SHOT: StabbingShot,
    config.FEAT_STEEL_SOUL: SteelSoul,
    config.FEAT_STEP_UP_AND_STRIKE: StepUpAndStrike,
    config.FEAT_STONE_FACED: StoneFaced,
    config.FEAT_STONE_SENSE: StoneSense,
    config.FEAT_STONE_SINGER: StoneSinger,
    config.FEAT_STUNNING_ASSAULT: StunningAssault,
    config.FEAT_SUMMONER_S_CALL: SummonerSCall,
    config.FEAT_SUNDERING_STRIKE: SunderingStrike,
    config.FEAT_SWAP_PLACES: SwapPlaces,
    config.FEAT_SWIFT_AID: SwiftAid,
    config.FEAT_TAUNT: Taunt,
    config.FEAT_TEAM_UP: TeamUp,
    config.FEAT_TELEPORT_TACTICIAN: TeleportTactician,
    config.FEAT_TENACIOUS_TRANSMUTATION: TenaciousTransmutation,
    config.FEAT_THUNDERING_SPELL: ThunderingSpell,
    config.FEAT_TOUCH_OF_SERENITY: TouchOfSerenity,
    config.FEAT_TRICK_RIDING: TrickRiding,
    config.FEAT_TRIPPING_STRIKE: TrippingStrike,
    config.FEAT_UNDER_AND_OVER: UnderAndOver,
    config.FEAT_UNDERFOOT: Underfoot,
    config.FEAT_VERMIN_HEART: VerminHeart,
    config.FEAT_WAR_SINGER: WarSinger,
    config.FEAT_WELL_PREPARED: WellPrepared,
    config.FEAT_ADDER_STRIKE: AdderStrike,
    config.FEAT_ADEPT_CHAMPION: AdeptChampion,
    config.FEAT_AMATEUR_GUNSLINGER: AmateurGunslinger,
    config.FEAT_ARC_SLINGER: ArcSlinger,
    config.FEAT_BACK_TO_BACK: BackToBack,
    config.FEAT_BETRAYER: Betrayer,
    config.FEAT_BINDING_THROW: BindingThrow,
    config.FEAT_BLUDGEONER: Bludgeoner,
    config.FEAT_BOAR_FEROCITY: BoarFerocity,
    config.FEAT_BOAR_SHRED: BoarShred,
    config.FEAT_BOAR_STYLE: BoarStyle,
    config.FEAT_BODY_SHIELD: BodyShield,
    config.FEAT_BOLSTERED_RESILIENCE: BolsteredResilience,
    config.FEAT_BONEBREAKER: Bonebreaker,
    config.FEAT_BRANDED_FOR_RETRIBUTION: BrandedForRetribution,
    config.FEAT_BREAK_GUARD: BreakGuard,
    config.FEAT_BROKEN_WING_GAMBIT: BrokenWingGambit,
    config.FEAT_CARTWHEEL_DODGE: CartwheelDodge,
    config.FEAT_CAVALRY_FORMATION: CavalryFormation,
    config.FEAT_CHANNELED_REVIVAL: ChanneledRevival,
    config.FEAT_CHANNELING_SCOURGE: ChannelingScourge,
    config.FEAT_CHARGING_HURLER: ChargingHurler,
    config.FEAT_CHOKEHOLD: Chokehold,
    config.FEAT_CLEAVING_FINISH: CleavingFinish,
    config.FEAT_CLOSE_QUARTERS_THROWER: CloseQuartersThrower,
    config.FEAT_CLUSTERED_SHOTS: ClusteredShots,
    config.FEAT_COMBAT_MEDIC: CombatMedic,
    config.FEAT_COMBAT_STYLE_MASTER: CombatStyleMaster,
    config.FEAT_CONTINGENT_CHANNELING: ContingentChanneling,
    config.FEAT_COORDINATED_CHARGE: CoordinatedCharge,
    config.FEAT_CRANE_RIPOSTE: CraneRiposte,
    config.FEAT_CRANE_STYLE: CraneStyle,
    config.FEAT_CRANE_WING: CraneWing,
    config.FEAT_CRUSADER_S_FIST: CrusaderSFist,
    config.FEAT_CRUSADER_S_FLURRY: CrusaderSFlurry,
    config.FEAT_CRUSHING_BLOW: CrushingBlow,
    config.FEAT_DEADLY_FINISH: DeadlyFinish,
    config.FEAT_DEATH_FROM_ABOVE: DeathFromAbove,
    config.FEAT_DEATH_OR_GLORY: DeathOrGlory,
    config.FEAT_DEATHLESS_INITIATE: DeathlessInitiate,
    config.FEAT_DEATHLESS_MASTER: DeathlessMaster,
    config.FEAT_DEATHLESS_ZEALOT: DeathlessZealot,
    config.FEAT_DECEPTIVE_EXCHANGE: DeceptiveExchange,
    config.FEAT_DEFENSIVE_WEAPON_TRAINING: DefensiveWeaponTraining,
    config.FEAT_DEFT_SHOOTIST_DEED: DeftShootistDeed,
    config.FEAT_DESTRUCTIVE_DISPEL: DestructiveDispel,
    config.FEAT_DEVASTATING_STRIKE: DevastatingStrike,
    config.FEAT_DIMENSIONAL_AGILITY: DimensionalAgility,
    config.FEAT_DIMENSIONAL_ASSAULT: DimensionalAssault,
    config.FEAT_DIMENSIONAL_DERVISH: DimensionalDervish,
    config.FEAT_DIMENSIONAL_MANEUVERS: DimensionalManeuvers,
    config.FEAT_DIMENSIONAL_SAVANT: DimensionalSavant,
    config.FEAT_DISCORDANT_VOICE: DiscordantVoice,
    config.FEAT_DISENGAGING_FEINT: DisengagingFeint,
    config.FEAT_DISENGAGING_FLOURISH: DisengagingFlourish,
    config.FEAT_DISENGAGING_SHOT: DisengagingShot,
    config.FEAT_DISORIENTING_MANEUVER: DisorientingManeuver,
    config.FEAT_DISPEL_SYNERGY: DispelSynergy,
    config.FEAT_DISPELLING_CRITICAL: DispellingCritical,
    config.FEAT_DISPELLING_FIST: DispellingFist,
    config.FEAT_DISPOSABLE_WEAPON: DisposableWeapon,
    config.FEAT_DISRUPTIVE_RECALL: DisruptiveRecall,
    config.FEAT_DISTANCE_THROWER: DistanceThrower,
    config.FEAT_DJINNI_SPIN: DjinniSpin,
    config.FEAT_DJINNI_SPIRIT: DjinniSpirit,
    config.FEAT_DJINNI_STYLE: DjinniStyle,
    config.FEAT_DOMAIN_STRIKE: DomainStrike,
    config.FEAT_DOUBLE_BANE: DoubleBane,
    config.FEAT_DRAG_DOWN: DragDown,
    config.FEAT_DRAGON_FEROCITY: DragonFerocity,
    config.FEAT_DRAGON_ROAR: DragonRoar,
    config.FEAT_DRAGON_STYLE: DragonStyle,
    config.FEAT_DRAMATIC_DISPLAY: DramaticDisplay,
    config.FEAT_EARTH_CHILD_BINDER: EarthChildBinder,
    config.FEAT_EARTH_CHILD_STYLE: EarthChildStyle,
    config.FEAT_EARTH_CHILD_TOPPLE: EarthChildTopple,
    config.FEAT_EFREETI_STANCE: EfreetiStance,
    config.FEAT_EFREETI_STYLE: EfreetiStyle,
    config.FEAT_EFREETI_TOUCH: EfreetiTouch,
    config.FEAT_ELUSIVE_REDIRECTION: ElusiveRedirection,
    config.FEAT_ENFILADING_FIRE: EnfiladingFire,
    config.FEAT_ESCAPE_ROUTE: EscapeRoute,
    config.FEAT_EXPERT_DRIVER: ExpertDriver,
    config.FEAT_EXTRA_BANE: ExtraBane,
    config.FEAT_EXTRA_GRIT: ExtraGrit,
    config.FEAT_FALSE_OPENING: FalseOpening,
    config.FEAT_FEINT_PARTNER: FeintPartner,
    config.FEAT_FELLING_ESCAPE: FellingEscape,
    config.FEAT_FELLING_SMASH: FellingSmash,
    config.FEAT_FERAL_COMBAT_TRAINING: FeralCombatTraining,
    config.FEAT_FIELD_REPAIR: FieldRepair,
    config.FEAT_FINAL_EMBRACE: FinalEmbrace,
    config.FEAT_FINAL_EMBRACE_HORROR: FinalEmbraceHorror,
    config.FEAT_FINAL_EMBRACE_MASTER: FinalEmbraceMaster,
    config.FEAT_FLANKING_FOIL: FlankingFoil,
    config.FEAT_FORTIFIED_ARMOR_TRAINING: FortifiedArmorTraining,
    config.FEAT_FURIOUS_FINISH: FuriousFinish,
    config.FEAT_GORY_FINISH: GoryFinish,
    config.FEAT_GREATER_CHANNEL_SMITE: GreaterChannelSmite,
    config.FEAT_GREATER_RENDING_FURY: GreaterRendingFury,
    config.FEAT_GREATER_SNAP_SHOT: GreaterSnapShot,
    config.FEAT_GREATER_WHIP_MASTERY: GreaterWhipMastery,
    config.FEAT_GUIDED_HAND: GuidedHand,
    config.FEAT_GUNSMITHING: Gunsmithing,
    config.FEAT_HAMMER_THE_GAP: HammerTheGap,
    config.FEAT_HARMONIC_SAGE: HarmonicSage,
    config.FEAT_HAUNTED_GNOME: HauntedGnome,
    config.FEAT_HAUNTED_GNOME_ASSAULT: HauntedGnomeAssault,
    config.FEAT_HAUNTED_GNOME_SHROUD: HauntedGnomeShroud,
    config.FEAT_HERO_S_DISPLAY: HeroSDisplay,
    config.FEAT_HEX_STRIKE: HexStrike,
    config.FEAT_HORSE_MASTER: HorseMaster,
    config.FEAT_IMPACT_CRITICAL_SHOT: ImpactCriticalShot,
    config.FEAT_IMPALING_CRITICAL: ImpalingCritical,
    config.FEAT_IMPROVED_BACK_TO_BACK: ImprovedBackToBack,
    config.FEAT_IMPROVED_CHARGING_HURLER: ImprovedChargingHurler,
    config.FEAT_IMPROVED_CLEAVING_FINISH: ImprovedCleavingFinish,
    config.FEAT_IMPROVED_DEVASTATING_STRIKE: ImprovedDevastatingStrike,
    config.FEAT_IMPROVED_FEINT_PARTNER: ImprovedFeintPartner,
    config.FEAT_IMPROVED_IMPALING_CRITICAL: ImprovedImpalingCritical,
    config.FEAT_IMPROVED_RENDING_FURY: ImprovedRendingFury,
    config.FEAT_IMPROVED_SNAP_SHOT: ImprovedSnapShot,
    config.FEAT_IMPROVED_STALWART: ImprovedStalwart,
    config.FEAT_IMPROVED_TWO_WEAPON_FEINT: ImprovedTwoWeaponFeint,
    config.FEAT_IMPROVED_WHIP_MASTERY: ImprovedWhipMastery,
    config.FEAT_INSTANT_JUDGMENT: InstantJudgment,
    config.FEAT_INTIMIDATING_BANE: IntimidatingBane,
    config.FEAT_JANNI_RUSH: JanniRush,
    config.FEAT_JANNI_STYLE: JanniStyle,
    config.FEAT_JANNI_TEMPEST: JanniTempest,
    config.FEAT_JAWBREAKER: Jawbreaker,
    config.FEAT_KIRIN_PATH: KirinPath,
    config.FEAT_KIRIN_STRIKE: KirinStrike,
    config.FEAT_KIRIN_STYLE: KirinStyle,
    config.FEAT_KNOCKOUT_ARTIST: KnockoutArtist,
    config.FEAT_LANDING_ROLL: LandingRoll,
    config.FEAT_LEAPING_SHOT_DEED: LeapingShotDeed,
    config.FEAT_MANTIS_STYLE: MantisStyle,
    config.FEAT_MANTIS_TORMENT: MantisTorment,
    config.FEAT_MANTIS_WISDOM: MantisWisdom,
    config.FEAT_MARID_COLDSNAP: MaridColdsnap,
    config.FEAT_MARID_SPIRIT: MaridSpirit,
    config.FEAT_MARID_STYLE: MaridStyle,
    config.FEAT_MASTER_COMBAT_PERFORMER: MasterCombatPerformer,
    config.FEAT_MASTER_SIEGE_ENGINEER: MasterSiegeEngineer,
    config.FEAT_MASTERFUL_DISPLAY: MasterfulDisplay,
    config.FEAT_MAXIMIZED_SPELLSTRIKE: MaximizedSpellstrike,
    config.FEAT_MENACING_BANE: MenacingBane,
    config.FEAT_MERCIFUL_BANE: MercifulBane,
    config.FEAT_MOCKING_DANCE: MockingDance,
    config.FEAT_MONASTIC_LEGACY: MonasticLegacy,
    config.FEAT_MONKEY_MOVES: MonkeyMoves,
    config.FEAT_MONKEY_SHINE: MonkeyShine,
    config.FEAT_MONKEY_STYLE: MonkeyStyle,
    config.FEAT_MOONLIGHT_STALKER: MoonlightStalker,
    config.FEAT_MOONLIGHT_STALKER_FEINT: MoonlightStalkerFeint,
    config.FEAT_MOONLIGHT_STALKER_MASTER: MoonlightStalkerMaster,
    config.FEAT_MURDERER_S_CIRCLE: MurdererSCircle,
    config.FEAT_NECKBREAKER: Neckbreaker,
    config.FEAT_NET_ADEPT: NetAdept,
    config.FEAT_NET_AND_TRIDENT: NetAndTrident,
    config.FEAT_NET_MANEUVERING: NetManeuvering,
    config.FEAT_NET_TRICKERY: NetTrickery,
    config.FEAT_NIGHTMARE_FIST: NightmareFist,
    config.FEAT_NIGHTMARE_STRIKER: NightmareStriker,
    config.FEAT_NIGHTMARE_WEAVER: NightmareWeaver,
    config.FEAT_NO_NAME: NoName,
    config.FEAT_OPENING_VOLLEY: OpeningVolley,
    config.FEAT_PACK_ATTACK: PackAttack,
    config.FEAT_PANTHER_CLAW: PantherClaw,
    config.FEAT_PANTHER_PARRY: PantherParry,
    config.FEAT_PANTHER_STYLE: PantherStyle,
    config.FEAT_PASSING_TRICK: PassingTrick,
    config.FEAT_PERFORMANCE_WEAPON_MASTERY: PerformanceWeaponMastery,
    config.FEAT_PERFORMING_COMBATANT: PerformingCombatant,
    config.FEAT_PIN_DOWN: PinDown,
    config.FEAT_PINNING_KNOCKOUT: PinningKnockout,
    config.FEAT_PINNING_REND: PinningRend,
    config.FEAT_PINPOINT_POISONER: PinpointPoisoner,
    config.FEAT_PLANAR_WILD_SHAPE: PlanarWildShape,
    config.FEAT_PRONE_SHOOTER: ProneShooter,
    config.FEAT_PRONE_SLINGER: ProneSlinger,
    config.FEAT_QUICK_BULL_RUSH: QuickBullRush,
    config.FEAT_QUICK_DIRTY_TRICK: QuickDirtyTrick,
    config.FEAT_QUICK_DRAG: QuickDrag,
    config.FEAT_QUICK_REPOSITION: QuickReposition,
    config.FEAT_QUICK_STEAL: QuickSteal,
    config.FEAT_RAGING_BRUTALITY: RagingBrutality,
    config.FEAT_RAGING_DEATHBLOW: RagingDeathblow,
    config.FEAT_RAGING_HURLER: RagingHurler,
    config.FEAT_RAGING_THROW: RagingThrow,
    config.FEAT_RAPID_GRAPPLER: RapidGrappler,
    config.FEAT_REBOUNDING_LEAP: ReboundingLeap,
    config.FEAT_REBUFFING_REDUCTION: RebuffingReduction,
    config.FEAT_RENDING_FURY: RendingFury,
    config.FEAT_REVELATION_STRIKE: RevelationStrike,
    config.FEAT_RHETORICAL_FLOURISH: RhetoricalFlourish,
    config.FEAT_RICOCHET_SHOT_DEED: RicochetShotDeed,
    config.FEAT_RIGHTEOUS_HEALING: RighteousHealing,
    config.FEAT_SAP_ADEPT: SapAdept,
    config.FEAT_SAP_MASTER: SapMaster,
    config.FEAT_SAVAGE_DISPLAY: SavageDisplay,
    config.FEAT_SCHOOL_STRIKE: SchoolStrike,
    config.FEAT_SEA_LEGS: SeaLegs,
    config.FEAT_SECRET_STASH_DEED: SecretStashDeed,
    config.FEAT_SEIZE_THE_MOMENT: SeizeTheMoment,
    config.FEAT_SHAITAN_EARTHBLAST: ShaitanEarthblast,
    config.FEAT_SHAITAN_SKIN: ShaitanSkin,
    config.FEAT_SHAITAN_STYLE: ShaitanStyle,
    config.FEAT_SHAKE_IT_OFF: ShakeItOff,
    config.FEAT_SHAPESHIFTER_FOIL: ShapeshifterFoil,
    config.FEAT_SHAPESHIFTING_HUNTER: ShapeshiftingHunter,
    config.FEAT_SHARED_JUDGMENT: SharedJudgment,
    config.FEAT_SIEGE_COMMANDER: SiegeCommander,
    config.FEAT_SIEGE_ENGINEER: SiegeEngineer,
    config.FEAT_SIEGE_GUNNER: SiegeGunner,
    config.FEAT_SIGNATURE_DEED: SignatureDeed,
    config.FEAT_SKILLED_DRIVER: SkilledDriver,
    config.FEAT_SLAYER_S_KNACK: SlayerSKnack,
    config.FEAT_SLING_FLAIL: SlingFlail,
    config.FEAT_SNAKE_FANG: SnakeFang,
    config.FEAT_SNAKE_STYLE: SnakeStyle,
    config.FEAT_SNAP_SHOT: SnapShot,
    config.FEAT_SNAPPING_TURTLE_CLUTCH: SnappingTurtleClutch,
    config.FEAT_SNAPPING_TURTLE_SHELL: SnappingTurtleShell,
    config.FEAT_SNAPPING_TURTLE_STYLE: SnappingTurtleStyle,
    config.FEAT_SNEAKING_PRECISION: SneakingPrecision,
    config.FEAT_SORCEROUS_STRIKE: SorcerousStrike,
    config.FEAT_SPELL_BANE: SpellBane,
    config.FEAT_SPINNING_THROW: SpinningThrow,
    config.FEAT_SPLINTERING_WEAPON: SplinteringWeapon,
    config.FEAT_STAGE_COMBATANT: StageCombatant,
    config.FEAT_STALWART: Stalwart,
    config.FEAT_STEALTH_SYNERGY: StealthSynergy,
    config.FEAT_STRANGLER: Strangler,
    config.FEAT_STRONG_COMEBACK: StrongComeback,
    config.FEAT_STUNNING_PIN: StunningPin,
    config.FEAT_SURE_GRASP: SureGrasp,
    config.FEAT_SWORD_AND_PISTOL: SwordAndPistol,
    config.FEAT_TANDEM_TRIP: TandemTrip,
    config.FEAT_TARGET_OF_OPPORTUNITY: TargetOfOpportunity,
    config.FEAT_TEAM_PICKPOCKETING: TeamPickpocketing,
    config.FEAT_TIGER_CLAWS: TigerClaws,
    config.FEAT_TIGER_POUNCE: TigerPounce,
    config.FEAT_TIGER_STYLE: TigerStyle,
    config.FEAT_TRAPPER_S_SETUP: TrapperSSetup,
    config.FEAT_TWIN_THUNDERS: TwinThunders,
    config.FEAT_TWIN_THUNDERS_FLURRY: TwinThundersFlurry,
    config.FEAT_TWIN_THUNDERS_MASTER: TwinThundersMaster,
    config.FEAT_TWO_HANDED_THROWER: TwoHandedThrower,
    config.FEAT_TWO_WEAPON_FEINT: TwoWeaponFeint,
    config.FEAT_VICIOUS_STOMP: ViciousStomp,
    config.FEAT_WAVE_STRIKE: WaveStrike,
    config.FEAT_WHIP_MASTERY: WhipMastery,
    config.FEAT_ABUNDANT_REVELATIONS: AbundantRevelations,
    config.FEAT_ACCURSED_CRITICAL: AccursedCritical,
    config.FEAT_ACCURSED_HEX: AccursedHex,
    config.FEAT_ADVANCED_RANGER_TRAP: AdvancedRangerTrap,
    config.FEAT_ANTAGONIZE: Antagonize,
    config.FEAT_BLIGHTED_CRITICAL: BlightedCritical,
    config.FEAT_BLIGHTED_CRITICAL_MASTERY: BlightedCriticalMastery,
    config.FEAT_BURNING_SPELL: BurningSpell,
    config.FEAT_CHANNELED_SHIELD_WALL: ChanneledShieldWall,
    config.FEAT_CONCUSSIVE_SPELL: ConcussiveSpell,
    config.FEAT_CREATE_RELIQUARY_ARMS_AND_SHIELDS: CreateReliquaryArmsAndShields,
    config.FEAT_CREATE_SANGUINE_ELIXIR: CreateSanguineElixir,
    config.FEAT_DEFENDING_EIDOLON: DefendingEidolon,
    config.FEAT_DENY_DEATH: DenyDeath,
    config.FEAT_DETECT_EXPERTISE: DetectExpertise,
    config.FEAT_DIE_FOR_YOUR_MASTER: DieForYourMaster,
    config.FEAT_DIVINE_INTERFERENCE: DivineInterference,
    config.FEAT_DRAGONBANE_AURA: DragonbaneAura,
    config.FEAT_ECHOING_SPELL: EchoingSpell,
    config.FEAT_ELDRITCH_HERITAGE: EldritchHeritage,
    config.FEAT_ENSEMBLE: Ensemble,
    config.FEAT_EVOLVED_FAMILIAR: EvolvedFamiliar,
    config.FEAT_EXPLOIT_LORE: ExploitLore,
    config.FEAT_EXTRA_ARCANA: ExtraArcana,
    config.FEAT_EXTRA_ARCANE_POOL: ExtraArcanePool,
    config.FEAT_EXTENDED_BANE: ExtendedBane,
    config.FEAT_EXTRA_CANTRIPS_OR_ORISONS: ExtraCantripsOrOrisons,
    config.FEAT_EXTRA_EVOLUTION: ExtraEvolution,
    config.FEAT_EXTRA_RANGER_TRAP: ExtraRangerTrap,
    config.FEAT_EXTRA_SUMMONS: ExtraSummons,
    config.FEAT_EYES_OF_JUDGMENT: EyesOfJudgment,
    config.FEAT_FAST_EMPATHY: FastEmpathy,
    config.FEAT_FAVORED_JUDGMENT: FavoredJudgment,
    config.FEAT_FEARLESS_AURA: FearlessAura,
    config.FEAT_FIRE_MUSIC: FireMusic,
    config.FEAT_FLARING_SPELL: FlaringSpell,
    config.FEAT_FOCUSED_EIDOLON: FocusedEidolon,
    config.FEAT_GLIDING_STEPS: GlidingSteps,
    config.FEAT_GRANT_INITIATIVE: GrantInitiative,
    config.FEAT_GREATER_BLIGHTED_CRITICAL: GreaterBlightedCritical,
    config.FEAT_GREATER_ELDRITCH_HERITAGE: GreaterEldritchHeritage,
    config.FEAT_GREATER_MERCY: GreaterMercy,
    config.FEAT_GREATER_SPELL_SPECIALIZATION: GreaterSpellSpecialization,
    config.FEAT_GREATER_WILD_EMPATHY: GreaterWildEmpathy,
    config.FEAT_IMPLANT_BOMB: ImplantBomb,
    config.FEAT_IMPROVED_ELDRITCH_HERITAGE: ImprovedEldritchHeritage,
    config.FEAT_IMPROVED_MONSTER_LORE: ImprovedMonsterLore,
    config.FEAT_INSIGHTFUL_GAZE: InsightfulGaze,
    config.FEAT_INTIMIDATING_GAZE: IntimidatingGaze,
    config.FEAT_JUDGMENT_SURGE: JudgmentSurge,
    config.FEAT_KI_STAND: KiStand,
    config.FEAT_LEARN_RANGER_TRAP: LearnRangerTrap,
    config.FEAT_LIFE_LURE: LifeLure,
    config.FEAT_MOONLIGHT_SUMMONS: MoonlightSummons,
    config.FEAT_MYSTIC_STRIDE: MysticStride,
    config.FEAT_ORACULAR_INTUITION: OracularIntuition,
    config.FEAT_PAINFUL_ANCHOR: PainfulAnchor,
    config.FEAT_PIERCING_SPELL: PiercingSpell,
    config.FEAT_PLANAR_PRESERVATIONIST: PlanarPreservationist,
    config.FEAT_POWERFUL_SHAPE: PowerfulShape,
    config.FEAT_PRODIGY: Prodigy,
    config.FEAT_PROPHETIC_VISIONARY: PropheticVisionary,
    config.FEAT_PURE_FAITH: PureFaith,
    config.FEAT_QUARTERSTAFF_MASTER: QuarterstaffMaster,
    config.FEAT_QUICK_CHANNEL: QuickChannel,
    config.FEAT_QUICK_WILD_SHAPE: QuickWildShape,
    config.FEAT_RADIANT_CHARGE: RadiantCharge,
    config.FEAT_REMOTE_BOMB: RemoteBomb,
    config.FEAT_RESILIENT_EIDOLON: ResilientEidolon,
    config.FEAT_REWARD_OF_GRACE: RewardOfGrace,
    config.FEAT_REWARD_OF_LIFE: RewardOfLife,
    config.FEAT_RICOCHET_SPLASH_WEAPON: RicochetSplashWeapon,
    config.FEAT_RIME_SPELL: RimeSpell,
    config.FEAT_SACRED_SUMMONS: SacredSummons,
    config.FEAT_SENSE_LINK: SenseLink,
    config.FEAT_SHAPING_FOCUS: ShapingFocus,
    config.FEAT_SIN_SEER: SinSeer,
    config.FEAT_SKELETON_SUMMONER: SkeletonSummoner,
    config.FEAT_SORCEROUS_BLOODSTRIKE: SorcerousBloodstrike,
    config.FEAT_SPELL_BLUFF: SpellBluff,
    config.FEAT_SPELL_HEX: SpellHex,
    config.FEAT_SPELL_SPECIALIZATION: SpellSpecialization,
    config.FEAT_SPELLSONG: Spellsong,
    config.FEAT_SPLIT_HEX: SplitHex,
    config.FEAT_SPLIT_MAJOR_HEX: SplitMajorHex,
    config.FEAT_SPONTANEOUS_METAFOCUS: SpontaneousMetafocus,
    config.FEAT_STARLIGHT_SUMMONS: StarlightSummons,
    config.FEAT_SUNLIGHT_SUMMONS: SunlightSummons,
    config.FEAT_SUPERIOR_SUMMONING: SuperiorSummoning,
    config.FEAT_THANATOPIC_SPELL: ThanatopicSpell,
    config.FEAT_THEURGY: Theurgy,
    config.FEAT_THOUGHTFUL_DISCERNMENT: ThoughtfulDiscernment,
    config.FEAT_THRENODIC_SPELL: ThrenodicSpell,
    config.FEAT_TOPPLING_SPELL: TopplingSpell,
    config.FEAT_TRIPPING_STAFF: TrippingStaff,
    config.FEAT_TRIPPING_TWIRL: TrippingTwirl,
    config.FEAT_ULTIMATE_MERCY: UltimateMercy,
    config.FEAT_ULTIMATE_RESOLVE: UltimateResolve,
    config.FEAT_UNCANNY_ALERTNESS: UncannyAlertness,
    config.FEAT_UNCANNY_CONCENTRATION: UncannyConcentration,
    config.FEAT_UNDEAD_MASTER: UndeadMaster,
    config.FEAT_UNSANCTIONED_DETECTION: UnsanctionedDetection,
    config.FEAT_UNSANCTIONED_KNOWLEDGE: UnsanctionedKnowledge,
    config.FEAT_VERSATILE_CHANNELER: VersatileChanneler,
    config.FEAT_VIGILANT_EIDOLON: VigilantEidolon,
    config.FEAT_VOICE_OF_THE_SIBYL: VoiceOfTheSibyl,
    config.FEAT_WARRIOR_PRIEST: WarriorPriest,
    config.FEAT_WILD_SPEECH: WildSpeech,
    config.FEAT_WITCH_KNIFE: WitchKnife,
    config.FEAT_WORD_OF_HEALING: WordOfHealing,
    config.FEAT_BREWMASTER: Brewmaster,
    config.FEAT_CLEAVE_THROUGH: CleaveThrough,
    config.FEAT_CLOVEN_HELM: ClovenHelm,
    config.FEAT_DENTED_HELM: DentedHelm,
    config.FEAT_GIANT_KILLER: GiantKiller,
    config.FEAT_GOBLIN_CLEAVER: GoblinCleaver,
    config.FEAT_HARD_HEADED: HardHeaded,
    config.FEAT_LEDGE_WALKER: LedgeWalker,
    config.FEAT_ORC_HEWER: OrcHewer,
    config.FEAT_SHATTERSPELL: Shatterspell,
    config.FEAT_TOXIC_RECOVERY: ToxicRecovery,
    config.FEAT_ATTUNED_TO_THE_WILD: AttunedToTheWild,
    config.FEAT_ELVEN_BATTLE_TRAINING: ElvenBattleTraining,
    config.FEAT_GUARDIAN_OF_THE_WILD: GuardianOfTheWild,
    config.FEAT_MAGE_OF_THE_WILD: MageOfTheWild,
    config.FEAT_SPIRIT_OF_THE_WILD: SpiritOfTheWild,
    config.FEAT_CASUAL_ILLUSIONIST: CasualIllusionist,
    config.FEAT_EXPANDED_RESISTANCE: ExpandedResistance,
    config.FEAT_GNOME_WEAPON_FOCUS: GnomeWeaponFocus,
    config.FEAT_GREAT_HATRED: GreatHatred,
    config.FEAT_VAST_HATRED: VastHatred,
    config.FEAT_DISCERNING_EYE: DiscerningEye,
    config.FEAT_ELVEN_SPIRIT: ElvenSpirit,
    config.FEAT_EXILE_S_PATH: ExileSPath,
    config.FEAT_HALF_DROW_PARAGON: HalfDrowParagon,
    config.FEAT_HUMAN_SPIRIT: HumanSpirit,
    config.FEAT_MULTITALENTED_MASTERY: MultitalentedMastery,
    config.FEAT_NEITHER_ELF_NOR_HUMAN: NeitherElfNorHuman,
    config.FEAT_SEEN_AND_UNSEEN: SeenAndUnseen,
    config.FEAT_SHARED_MANIPULATION: SharedManipulation,
    config.FEAT_BEAST_RIDER: BeastRider,
    config.FEAT_BLOOD_VENGEANCE: BloodVengeance,
    config.FEAT_DESTROYER_S_BLESSING: DestroyerSBlessing,
    config.FEAT_FEROCIOUS_RESOLVE: FerociousResolve,
    config.FEAT_FEROCIOUS_SUMMONS: FerociousSummons,
    config.FEAT_FEROCIOUS_TENACITY: FerociousTenacity,
    config.FEAT_GORE_FIEND: GoreFiend,
    config.FEAT_HORDE_CHARGE: HordeCharge,
    config.FEAT_IMPROVED_SURPRISE_FOLLOW_THROUGH: ImprovedSurpriseFollowThrough,
    config.FEAT_RESILIENT_BRUTE: ResilientBrute,
    config.FEAT_SURPRISE_FOLLOW_THROUGH: SurpriseFollowThrough,
    config.FEAT_SYMPATHETIC_RAGE: SympatheticRage,
    config.FEAT_TENACIOUS_SURVIVOR: TenaciousSurvivor,
    config.FEAT_THRILL_OF_THE_KILL: ThrillOfTheKill,
    config.FEAT_ADAPTIVE_FORTUNE: AdaptiveFortune,
    config.FEAT_BLUNDERING_DEFENSE: BlunderingDefense,
    config.FEAT_CAUTIOUS_FIGHTER: CautiousFighter,
    config.FEAT_COURAGEOUS_RESOLVE: CourageousResolve,
    config.FEAT_DESPERATE_SWING: DesperateSwing,
    config.FEAT_FORTUNATE_ONE: FortunateOne,
    config.FEAT_IMPROVED_LOW_BLOW: ImprovedLowBlow,
    config.FEAT_LUCKY_HEALER: LuckyHealer,
    config.FEAT_LUCKY_STRIKE: LuckyStrike,
    config.FEAT_RISKY_STRIKER: RiskyStriker,
    config.FEAT_SURE_AND_FLEET: SureAndFleet,
    config.FEAT_SURPRISE_STRIKE: SurpriseStrike,
    config.FEAT_UNCANNY_DEFENSE: UncannyDefense,
    config.FEAT_BESTOW_LUCK: BestowLuck,
    config.FEAT_CRITICAL_VERSATILITY: CriticalVersatility,
    config.FEAT_DAUNTLESS_DESTINY: DauntlessDestiny,
    config.FEAT_DEFIANT_LUCK: DefiantLuck,
    config.FEAT_FAST_LEARNER: FastLearner,
    config.FEAT_FEARLESS_CURIOSITY: FearlessCuriosity,
    config.FEAT_HEROIC_WILL: HeroicWill,
    config.FEAT_HUNTMASTER: Huntmaster,
    config.FEAT_IMPROVED_IMPROVISATION: ImprovedImprovisation,
    config.FEAT_IMPROVISATION: Improvisation,
    config.FEAT_INEXPLICABLE_LUCK: InexplicableLuck,
    config.FEAT_INTIMIDATING_CONFIDENCE: IntimidatingConfidence,
    config.FEAT_MARTIAL_MASTERY: MartialMastery,
    config.FEAT_MARTIAL_VERSATILITY: MartialVersatility,
    config.FEAT_SURGE_OF_SUCCESS: SurgeOfSuccess,
    config.FEAT_ANGEL_WINGS: AngelWings,
    config.FEAT_ANGELIC_BLOOD: AngelicBlood,
    config.FEAT_ANGELIC_FLESH: AngelicFlesh,
    config.FEAT_CELESTIAL_SERVANT: CelestialServant,
    config.FEAT_CHANNEL_FORCE: ChannelForce,
    config.FEAT_GREATER_CHANNEL_FORCE: GreaterChannelForce,
    config.FEAT_HEAVENLY_RADIANCE: HeavenlyRadiance,
    config.FEAT_IMPROVED_CHANNEL_FORCE: ImprovedChannelForce,
    config.FEAT_METALLIC_WINGS: MetallicWings,
    config.FEAT_BLACK_CAT: BlackCat,
    config.FEAT_CATFOLK_EXEMPLAR: CatfolkExemplar,
    config.FEAT_CLAW_POUNCE: ClawPounce,
    config.FEAT_FELINE_GRACE: FelineGrace,
    config.FEAT_NIMBLE_STRIKER: NimbleStriker,
    config.FEAT_BLOOD_DRINKER: BloodDrinker,
    config.FEAT_BLOOD_FEASTER: BloodFeaster,
    config.FEAT_BLOOD_SALVAGE: BloodSalvage,
    config.FEAT_DIVERSE_PALATE: DiversePalate,
    config.FEAT_NATURAL_CHARMER: NaturalCharmer,
    config.FEAT_DROW_NOBILITY: DrowNobility,
    config.FEAT_GREATER_DROW_NOBILITY: GreaterDrowNobility,
    config.FEAT_IMPROVED_DROW_NOBILITY: ImprovedDrowNobility,
    config.FEAT_IMPROVED_UMBRAL_SCION: ImprovedUmbralScion,
    config.FEAT_NOBLE_SPELL_RESISTANCE: NobleSpellResistance,
    config.FEAT_SHADOW_CASTER: ShadowCaster,
    config.FEAT_SPIDER_STEP: SpiderStep,
    config.FEAT_SPIDER_SUMMONER: SpiderSummoner,
    config.FEAT_UMBRAL_SCION: UmbralScion,
    config.FEAT_NATURAL_JOUSTER: NaturalJouster,
    config.FEAT_LASTWALL_PHALANX: LastwallPhalanx,
    config.FEAT_LASTWALL_PHALANX: LastwallPhalanx,
    config.FEAT_LEGACY_OF_OZEM: LegacyOfOzem,
    config.FEAT_PEACEMAKER: Peacemaker,
    config.FEAT_SIPHON_POISON: SiphonPoison,
    config.FEAT_WORLDWOUND_WALKER: WorldwoundWalker,
    config.FEAT_DARK_SIGHT: DarkSight,
    config.FEAT_GLOOM_SIGHT: GloomSight,
    config.FEAT_GLOOM_STRIKE: GloomStrike,
    config.FEAT_IMPROVED_DARK_SIGHT: ImprovedDarkSight,
    config.FEAT_SHADOW_GHOST: ShadowGhost,
    config.FEAT_SHADOW_WALKER: ShadowWalker,
    config.FEAT_BURN_BURN_BURN: BurnBurnBurn,
    config.FEAT_FIRE_HAND: FireHand,
    config.FEAT_FIRE_TAMER: FireTamer,
    config.FEAT_FLAME_HEART: FlameHeart,
    config.FEAT_GOBLIN_GUNSLINGER: GoblinGunslinger,
    config.FEAT_TANGLE_FEET: TangleFeet,
    config.FEAT_DEAFENING_EXPLOSION: DeafeningExplosion,
    config.FEAT_DEMORALIZING_LASH: DemoralizingLash,
    config.FEAT_FOCUSING_BLOW: FocusingBlow,
    config.FEAT_HOBGOBLIN_DISCIPLINE: HobgoblinDiscipline,
    config.FEAT_TASKMASTER: Taskmaster,
    config.FEAT_TERRORIZING_DISPLAY: TerrorizingDisplay,
    config.FEAT_BLAZING_AURA: BlazingAura,
    config.FEAT_BLISTERING_FEINT: BlisteringFeint,
    config.FEAT_ELEMENTAL_JAUNT: ElementalJaunt,
    config.FEAT_FIRESIGHT: Firesight,
    config.FEAT_INNER_FLAME: InnerFlame,
    config.FEAT_SCORCHING_WEAPONS: ScorchingWeapons,
    config.FEAT_DRACONIC_ASPECT: DraconicAspect,
    config.FEAT_DRACONIC_BREATH: DraconicBreath,
    config.FEAT_DRACONIC_GLIDE: DraconicGlide,
    config.FEAT_DRACONIC_PARAGON: DraconicParagon,
    config.FEAT_KOBOLD_AMBUSHER: KoboldAmbusher,
    config.FEAT_KOBOLD_SNIPER: KoboldSniper,
    config.FEAT_TAIL_TERROR: TailTerror,
    config.FEAT_BORN_ALONE: BornAlone,
    config.FEAT_BULLYING_BLOW: BullyingBlow,
    config.FEAT_FEROCIOUS_ACTION: FerociousAction,
    config.FEAT_FOMENT_THE_BLOOD: FomentTheBlood,
    config.FEAT_GRUDGE_FIGHTER: GrudgeFighter,
    config.FEAT_ORC_WEAPON_EXPERTISE: OrcWeaponExpertise,
    config.FEAT_RESOLUTE_RAGER: ResoluteRager,
    config.FEAT_REVERSE_FEINT: ReverseFeint,
    config.FEAT_TRAP_WRECKER: TrapWrecker,
    config.FEAT_DWARF_BLOODED: DwarfBlooded,
    config.FEAT_ECHOES_OF_STONE: EchoesOfStone,
    config.FEAT_MURMURS_OF_EARTH: MurmursOfEarth,
    config.FEAT_OREAD_BURROWER: OreadBurrower,
    config.FEAT_OREAD_EARTH_GLIDER: OreadEarthGlider,
    config.FEAT_STONY_STEP: StonyStep,
    config.FEAT_BURROWING_TEETH: BurrowingTeeth,
    config.FEAT_SHARPCLAW: Sharpclaw,
    config.FEAT_TUNNEL_RAT: TunnelRat,
    config.FEAT_AIRY_STEP: AiryStep,
    config.FEAT_CLOUD_GAZER: CloudGazer,
    config.FEAT_INNER_BREATH: InnerBreath,
    config.FEAT_WINGS_OF_AIR: WingsOfAir,
    config.FEAT_BLOOD_BEAK: BloodBeak,
    config.FEAT_CARRION_FEEDER: CarrionFeeder,
    config.FEAT_LONG_NOSE_FORM: LongNoseForm,
    config.FEAT_SCAVENGER_S_EYE: ScavengerSEye,
    config.FEAT_TENGU_RAVEN_FORM: TenguRavenForm,
    config.FEAT_TENGU_WINGS: TenguWings,
    config.FEAT_ARMOR_OF_THE_PIT: ArmorOfThePit,
    config.FEAT_EXPANDED_FIENDISH_RESISTANCE: ExpandedFiendishResistance,
    config.FEAT_FIEND_SIGHT: FiendSight,
    config.FEAT_GRASPING_TAIL: GraspingTail,
    config.FEAT_AQUATIC_ANCESTRY: AquaticAncestry,
    config.FEAT_HYDRAULIC_MANEUVER: HydraulicManeuver,
    config.FEAT_STEAM_CASTER: SteamCaster,
    config.FEAT_TRITON_PORTAL: TritonPortal,
    config.FEAT_WATER_SKINNED: WaterSkinned,
    config.FEAT_MOTHER_S_GIFT: MotherSGift,
    config.FEAT_GIANT_STEPS: GiantSteps,
    config.FEAT_LINGERING_INVISIBILITY: LingeringInvisibility,
    config.FEAT_AGILE_TONGUE: AgileTongue,
    config.FEAT_MAGICAL_TAIL: MagicalTail,
    config.FEAT_REALISTIC_LIKENESS: RealisticLikeness,
    config.FEAT_SEA_HUNTER: SeaHunter,
    config.FEAT_SPIT_VENOM: SpitVenom,
    config.FEAT_LIFE_S_BLOOD: LifeSBlood,
    config.FEAT_STRETCHED_WINGS: StretchedWings,
    config.FEAT_EXTRA_ELEMENTAL_ASSAULT: ExtraElementalAssault,
    config.FEAT_INCREMENTAL_ELEMENTAL_ASSAULT: IncrementalElementalAssault,
    config.FEAT_STOIC_POSE: StoicPose,
    config.FEAT_TREE_HANGER: TreeHanger,
    config.FEAT_SLEEP_VENOM: SleepVenom,
    config.FEAT_SHADOWY_DASH: ShadowyDash,
    config.FEAT_BELIER_S_BITE: BelierSBite,
    config.FEAT_CORNUGON_SHIELD: CornugonShield,
    config.FEAT_CORNUGON_SMASH: CornugonSmash,
    config.FEAT_CORNUGON_STUN: CornugonStun,
    config.FEAT_CORNUGON_TRIP: CornugonTrip,
    config.FEAT_FURY_S_FALL: FurySFall,
    config.FEAT_FURY_S_SNARE: FurySSnare,
    config.FEAT_HAMATULA_GRASP: HamatulaGrasp,
    config.FEAT_HAMATULA_STRIKE: HamatulaStrike,
    config.FEAT_HELLCAT_POUNCE: HellcatPounce,
    config.FEAT_HELLCAT_STEALTH: HellcatStealth,
    config.FEAT_OSYLUTH_GUILE: OsyluthGuile,
    config.FEAT_BOUNDING_HAMMER: BoundingHammer,
    config.FEAT_DARTING_VIPER: DartingViper,
    config.FEAT_DORN_DERGAR_MASTER: DornDergarMaster,
    config.FEAT_SLIDING_AXE_THROW: SlidingAxeThrow,
    config.FEAT_STANCE_OF_THE_XORN: StanceOfTheXorn,
    config.FEAT_ARCANE_SCHOOL_SPIRIT: ArcaneSchoolSpirit,
    config.FEAT_BEWILDERING_KOAN: BewilderingKoan,
    config.FEAT_BLOOD_TIES: BloodTies,
    config.FEAT_BABBLE_PEDDLER: BabblePeddler,
    config.FEAT_CAUSTIC_SLUR: CausticSlur,
    config.FEAT_HELPLESS_PRISONER: HelplessPrisoner,
    config.FEAT_INVOKE_PRIMAL_INSTINCT: InvokePrimalInstinct,
    config.FEAT_TANTRUM: Tantrum,
    config.FEAT_WITTY_FEINT: WittyFeint,
    config.FEAT_MOUNTED_BLADE: MountedBlade,
    config.FEAT_ELEPHANT_STOMP: ElephantStomp,
    config.FEAT_JAGUAR_POUNCE: JaguarPounce,
    config.FEAT_MONKEY_LUNGE: MonkeyLunge,
    config.FEAT_PIRANHA_STRIKE: PiranhaStrike,
    config.FEAT_RHINO_CHARGE: RhinoCharge,
    config.FEAT_BOON_COMPANION: BoonCompanion,
    config.FEAT_CRITICAL_CONDUIT: CriticalConduit,
    config.FEAT_EXTRA_ITEM_SLOT: ExtraItemSlot,
    config.FEAT_FAMILIAR_FOCUS: FamiliarFocus,
    config.FEAT_FAMILIAR_SPELL: FamiliarSpell,
    config.FEAT_JUMPER: Jumper,
    config.FEAT_LITHE_ATTACKER: LitheAttacker,
    config.FEAT_MASTER_OF_YOUR_KIND: MasterOfYourKind,
    config.FEAT_NARROW_FRAME: NarrowFrame,
    config.FEAT_SPELL_SPONGE: SpellSponge,
    config.FEAT_STABLE_GALLOP: StableGallop,
    config.FEAT_SURE_FOOTED: SureFooted,
    config.FEAT_VALIANT_STEED: ValiantSteed,
    config.FEAT_ARCHON_DIVERSION: ArchonDiversion,
    config.FEAT_ARCHON_JUSTICE: ArchonJustice,
    config.FEAT_ARCHON_STYLE: ArchonStyle,
    config.FEAT_BANISHING_CRITICAL: BanishingCritical,
    config.FEAT_BLINDING_LIGHT: BlindingLight,
    config.FEAT_CONSECRATE_SPELL: ConsecrateSpell,
    config.FEAT_INNER_LIGHT: InnerLight,
    config.FEAT_REVERED_GUIDANCE: ReveredGuidance,
    config.FEAT_SUNLIT_STRIKE: SunlitStrike,
    config.FEAT_SUPERNAL_FEAST: SupernalFeast,
    config.FEAT_ANCESTRAL_SCORN: AncestralScorn,
    config.FEAT_BANNER_OF_DOOM: BannerOfDoom,
    config.FEAT_BLINDING_SNEAK_ATTACK: BlindingSneakAttack,
    config.FEAT_FIENDISH_DARKNESS: FiendishDarkness,
    config.FEAT_FIENDISH_FACADE: FiendishFacade,
    config.FEAT_FIENDISH_RESILIENCE: FiendishResilience,
    config.FEAT_FURY_OF_THE_TAINTED: FuryOfTheTainted,
    config.FEAT_IMPROVED_FIENDISH_DARKNESS: ImprovedFiendishDarkness,
    config.FEAT_IMPROVED_FIENDISH_SORCERY: ImprovedFiendishSorcery,
    config.FEAT_IMPROVED_FURY_OF_THE_TAINTED: ImprovedFuryOfTheTainted,
    config.FEAT_MONSTROUS_MASK: MonstrousMask,
    config.FEAT_TERRIFYING_MASK: TerrifyingMask,
    config.FEAT_WICKED_VALOR: WickedValor,
    config.FEAT_RECKLESS_AIM: RecklessAim,
    config.FEAT_CONVICTION: Conviction,
    config.FEAT_HYMN_SINGER: HymnSinger,
    config.FEAT_LIFE_DOMINANT_SOUL: LifeDominantSoul,
    config.FEAT_POTENT_HOLY_SYMBOL: PotentHolySymbol,
    config.FEAT_SCHOOLED_RESOLVE: SchooledResolve,
    config.FEAT_AVERSION_TOLERANCE: AversionTolerance,
    config.FEAT_FAMINE_TOLERANCE: FamineTolerance,
    config.FEAT_VAMPIRIC_COMPANION: VampiricCompanion,
    config.FEAT_VARIANT_PRAYER_SCROLL: VariantPrayerScroll,
    config.FEAT_BLINDING_FLASH: BlindingFlash,
    config.FEAT_DISORIENTING_BLOW: DisorientingBlow,
    config.FEAT_ENHANCED_KI_THROW: EnhancedKiThrow,
    config.FEAT_FEINTING_FLURRY: FeintingFlurry,
    config.FEAT_HOLD_THE_BLADE: HoldTheBlade,
    config.FEAT_IMPROVED_FEINTING_FLURRY: ImprovedFeintingFlurry,
    config.FEAT_QUIVERING_PALM_ADEPT: QuiveringPalmAdept,
    config.FEAT_QUIVERING_PALM_VERSATILITY: QuiveringPalmVersatility,
    config.FEAT_SLEEPER_HOLD: SleeperHold,
    config.FEAT_STUNNING_FIST_ADEPT: StunningFistAdept,
    config.FEAT_ARCANE_TRAP_SUPPRESSOR: ArcaneTrapSuppressor,
    config.FEAT_CLOSE_CALL: CloseCall,
    config.FEAT_TACTICAL_REPOSITION: TacticalReposition,
    config.FEAT_COAXING_SPELL: CoaxingSpell,
    config.FEAT_DAMPEN_PRESENCE: DampenPresence,
    config.FEAT_CURSED_ITEM_DETECTION: CursedItemDetection,
    config.FEAT_OSTENTATIOUS_DISPLAY: OstentatiousDisplay,
    config.FEAT_TORCH_HANDLING: TorchHandling,
    config.FEAT_ARCANE_INSIGHT: ArcaneInsight,
    config.FEAT_BLOODY_VENGEANCE: BloodyVengeance,
    config.FEAT_MEASURED_RESPONSE: MeasuredResponse,
    config.FEAT_RIPTIDE_ATTACK: RiptideAttack,
    config.FEAT_SPIKED_DESTROYER: SpikedDestroyer,
    config.FEAT_STEADY_ENGAGEMENT: SteadyEngagement,
    config.FEAT_FIREBRAND: Firebrand,
    config.FEAT_ORDERED_MIND: OrderedMind,
    config.FEAT_DESTROY_IDENTITY: DestroyIdentity,
    config.FEAT_FEARSOME_FINISH: FearsomeFinish,
    config.FEAT_REJECT_POISON: RejectPoison,
    config.FEAT_SHADOW_DODGE: ShadowDodge,
    config.FEAT_MERCILESS_RUSH: MercilessRush,
    config.FEAT_SQUASH_FLAT: SquashFlat,
    config.FEAT_SHATTER_RESOLVE: ShatterResolve,
    config.FEAT_BLOODLETTING: Bloodletting,
    config.FEAT_ALDORI_DUELING_MASTERY: AldoriDuelingMastery,
    config.FEAT_ALTITUDE_AFFINITY: AltitudeAffinity,
    config.FEAT_ANDOREN_FALCONRY: AndorenFalconry,
    config.FEAT_ARCANE_VENDETTA: ArcaneVendetta,
    config.FEAT_CAREFUL_SPEAKER: CarefulSpeaker,
    config.FEAT_CYPHER_MAGIC: CypherMagic,
    config.FEAT_CYPHER_SCRIPT: CypherScript,
    config.FEAT_DEMON_HUNTER: DemonHunter,
    config.FEAT_DERVISH_DANCE: DervishDance,
    config.FEAT_DESERT_DWELLER: DesertDweller,
    config.FEAT_DESPERATE_BATTLER: DesperateBattler,
    config.FEAT_EYE_OF_THE_ARCLORD: EyeOfTheArclord,
    config.FEAT_FEY_FOUNDLING: FeyFoundling,
    config.FEAT_FLAGBEARER: Flagbearer,
    config.FEAT_FOCUSED_DISCIPLINE: FocusedDiscipline,
    config.FEAT_FORTUNE_TELLER: FortuneTeller,
    config.FEAT_FREE_SPIRIT: FreeSpirit,
    config.FEAT_GODLESS_HEALING: GodlessHealing,
    config.FEAT_GREEN_FAITH_ACOLYTE: GreenFaithAcolyte,
    config.FEAT_HAMATULATSU: Hamatulatsu,
    config.FEAT_HARMONIC_SPELL: HarmonicSpell,
    config.FEAT_HARROWED: Harrowed,
    config.FEAT_HERMEAN_BLOOD: HermeanBlood,
    config.FEAT_NECROMANTIC_AFFINITY: NecromanticAffinity,
    config.FEAT_NOBLE_SCION: NobleScion,
    config.FEAT_RAPID_RELOAD: RapidReload,
    config.FEAT_RUGGED_NORTHERNER: RuggedNortherner,
    config.FEAT_SCHOLAR: Scholar,
    config.FEAT_SECRET_SIGNS: SecretSigns,
    config.FEAT_SHADE_OF_THE_USKWOOD: ShadeOfTheUskwood,
    config.FEAT_SHREWD_TACTICIAN: ShrewdTactician,
    config.FEAT_STOIC: Stoic,
    config.FEAT_STORM_LASHED: StormLashed,
    config.FEAT_SURVIVOR: Survivor,
    config.FEAT_TALDAN_DUELIST: TaldanDuelist,
    config.FEAT_TOTEM_SPIRIT: TotemSpirit,
    config.FEAT_VARISIAN_TATTOO: VarisianTattoo,
    config.FEAT_WAND_DANCER: WandDancer,
    config.FEAT_SLAYING_SPRINT: SlayingSprint,
    config.FEAT_GREATER_SERPENT_LASH: GreaterSerpentLash,
    config.FEAT_SERPENT_LASH: SerpentLash,
    config.FEAT_CIRCLING_OFFENSE: CirclingOffense,
    config.FEAT_FOOTSLASHER: Footslasher,
    config.FEAT_TOPPLE_FOE: ToppleFoe,
    config.FEAT_JACKAL_HERITAGE: JackalHeritage,
    config.FEAT_DRUNKEN_BRAWLER: DrunkenBrawler,
    config.FEAT_BUTTERFLY_S_STING: ButterflySSting,
    config.FEAT_DIVINATION_GUIDE: DivinationGuide,
    config.FEAT_BULLSEYE_SHOT: BullseyeShot,
    config.FEAT_NIMBLE_NATURAL_SUMMONS: NimbleNaturalSummons,
    config.FEAT_CHARGE_OF_THE_RIGHTEOUS: ChargeOfTheRighteous,
    config.FEAT_PROTECTOR_S_STRIKE: ProtectorSStrike,
    config.FEAT_BESTOW_HOPE: BestowHope,
    config.FEAT_GLORIOUS_HEAT: GloriousHeat,
    config.FEAT_SPEAR_DANCER: SpearDancer,
    config.FEAT_STONE_READ: StoneRead,
    config.FEAT_UNDERMINING_EXPLOIT: UnderminingExploit,
    config.FEAT_ANKLE_BITER: AnkleBiter,
    config.FEAT_BATTLE_SINGER: BattleSinger,
    config.FEAT_DOG_KILLER_HORSE_HUNTER: DogKillerHorseHunter,
    config.FEAT_LEAD_FROM_THE_BACK: LeadFromTheBack,
    config.FEAT_LETTER_FURY: LetterFury,
    config.FEAT_ROLL_WITH_IT: RollWithIt,
    config.FEAT_SADDLE_SHRIEKER: SaddleShrieker,
    config.FEAT_COMBAT_DISTRACTION: CombatDistraction,
    config.FEAT_VANDAL: Vandal,
    config.FEAT_AMMO_DROP: AmmoDrop,
    config.FEAT_HALFLING_SLINGER: HalflingSlinger,
    config.FEAT_JUGGLE_LOAD: JuggleLoad,
    config.FEAT_LARGE_TARGET: LargeTarget,
    config.FEAT_WHIP_SLINGER: WhipSlinger,
    config.FEAT_AMPLIFIED_RAGE: AmplifiedRage,
    config.FEAT_BLOOD_VENGEANCE: BloodVengeance,
    config.FEAT_BRUTAL_GRAPPLER: BrutalGrappler,
    config.FEAT_DESTROYER_S_BLESSING: DestroyerSBlessing,
    config.FEAT_FEROCIOUS_TENACITY: FerociousTenacity,
    config.FEAT_FEROCIOUS_TENACITY: FerociousTenacity,
    config.FEAT_FIRE_GOD_S_BLESSING: FireGodSBlessing,
    config.FEAT_GORE_FIEND: GoreFiend,
    config.FEAT_SYMPATHETIC_RAGE: SympatheticRage,
    config.FEAT_THRILL_OF_THE_KILL: ThrillOfTheKill,
    config.FEAT_WARLEADER_S_RAGE: WarleaderSRage,
    config.FEAT_ADEPT_CHANNEL: AdeptChannel,
    config.FEAT_COLD_CELERITY: ColdCelerity,
    config.FEAT_TRIBAL_SCARS: TribalScars,
    config.FEAT_WITCHBREAKER: Witchbreaker,
    config.FEAT_DEADLY_DEALER: DeadlyDealer,
    config.FEAT_THUNDER_AND_FANG: ThunderAndFang,
    config.FEAT_CHAINBREAKER: Chainbreaker,
    config.FEAT_DEVIL_S_FOE: DevilSFoe,
    config.FEAT_EAGLE_KNIGHT_CANDIDATE: EagleKnightCandidate,
    config.FEAT_TALMANDOR_S_LIFTING: TalmandorSLifting,
    config.FEAT_ADVANCED_DEFENSIVE_COMBAT_TRAINING: AdvancedDefensiveCombatTraining,
    config.FEAT_BLOODSTONE_MANHUNTER: BloodstoneManhunter,
    config.FEAT_CALM_DISPOSITION: CalmDisposition,
    config.FEAT_DEATH_S_SUITOR: DeathSSuitor,
    config.FEAT_DISASSEMBLE_MAGIC_ITEM: DisassembleMagicItem,
    config.FEAT_DIVINE_DECEPTION: DivineDeception,
    config.FEAT_FAST_CRAWL: FastCrawl,
    config.FEAT_FEARSOME_BARRICADE: FearsomeBarricade,
    config.FEAT_GRAND_MASTER_PERFORMER: GrandMasterPerformer,
    config.FEAT_KI_DIVERSITY: KiDiversity,
    config.FEAT_LET_THEM_COME: LetThemCome,
    config.FEAT_MASTER_PERFORMER: MasterPerformer,
    config.FEAT_NAMELESS_SERVITOR: NamelessServitor,
    config.FEAT_OLD_CULTS_AWAKENER: OldCultsAwakener,
    config.FEAT_OMINOUS_MIEN: OminousMien,
    config.FEAT_SILENT_PERFORMER: SilentPerformer,
    config.FEAT_TOUCHED_BY_SACRED_FIRE: TouchedBySacredFire,
    config.FEAT_VERBOSE_PERFORMER: VerbosePerformer,
    config.FEAT_WHISPERED_KNOWLEDGE: WhisperedKnowledge,
    config.FEAT_BLOOD_OF_HEROES: BloodOfHeroes,
    config.FEAT_HERO_S_FORTUNE: HeroSFortune,
    config.FEAT_LUCK_OF_HEROES: LuckOfHeroes,
    config.FEAT_CELESTIAL_OBEDIENCE: CelestialObedience,
    config.FEAT_ACCURSED: Accursed,
    config.FEAT_ARISEN: Arisen,
    config.FEAT_BATTLEFIELD_HEALER: BattlefieldHealer,
    config.FEAT_CHAMPION: Champion,
    config.FEAT_DAMNED: Damned,
    config.FEAT_DENY_THE_REAPER: DenyTheReaper,
    config.FEAT_ELDRITCH_RESEARCHER: EldritchResearcher,
    config.FEAT_FEARLESS_ZEAL: FearlessZeal,
    config.FEAT_FERAL_HEART: FeralHeart,
    config.FEAT_FOESLAYER: Foeslayer,
    config.FEAT_FORGOTTEN_PAST: ForgottenPast,
    config.FEAT_GLIMPSE_BEYOND: GlimpseBeyond,
    config.FEAT_INNOCENT_BLOOD: InnocentBlood,
    config.FEAT_LIBERATOR: Liberator,
    config.FEAT_LOST_LEGACY: LostLegacy,
    config.FEAT_MAGNUM_OPUS: MagnumOpus,
    config.FEAT_MONUMENT_BUILDER: MonumentBuilder,
    config.FEAT_NATION_BUILDER: NationBuilder,
    config.FEAT_NEMESIS: Nemesis,
    config.FEAT_PROPHET: Prophet,
    config.FEAT_REDEMPTION: Redemption,
    config.FEAT_SHAMED: Shamed,
    config.FEAT_STRONGHOLD: Stronghold,
    config.FEAT_THIEF_OF_LEGEND: ThiefOfLegend,
    config.FEAT_TOWN_TAMER: TownTamer,
    config.FEAT_TRUE_LOVE: TrueLove,
    config.FEAT_UNFORGOTTEN: Unforgotten,
    config.FEAT_VENGEANCE: Vengeance,
    config.FEAT_ANCIENT_DRACONIC: AncientDraconic,
    config.FEAT_IMPROVED_LEARN_RANGER_TRAP: ImprovedLearnRangerTrap,
    config.FEAT_KOBOLD_CONFIDENCE: KoboldConfidence,
    config.FEAT_LEARN_RANGER_TRAP: LearnRangerTrap,
    config.FEAT_MERCILESS_MAGIC: MercilessMagic,
    config.FEAT_MERCILESS_PRECISION: MercilessPrecision,
    config.FEAT_MIXED_SCALES: MixedScales,
    config.FEAT_REDEEMED_KOBOLD: RedeemedKobold,
    config.FEAT_SCALED_DISCIPLE: ScaledDisciple,
    config.FEAT_SMALL_BUT_DEADLY: SmallButDeadly,
    config.FEAT_KOBOLD_FLOOD: KoboldFlood,
    config.FEAT_KOBOLD_GROUNDLING: KoboldGroundling,
    config.FEAT_KOBOLD_STYLE: KoboldStyle,
    config.FEAT_TRIBE_MENTALITY: TribeMentality,
    config.FEAT_WALL_OFFLESH: WallOfflesh,
    config.FEAT_APOTHEOSIS: Apotheosis,
    config.FEAT_ARTIFACT_HUNTER: ArtifactHunter,
    config.FEAT_BLESSED: Blessed,
    config.FEAT_DAMNED: Damned,
    config.FEAT_DYNASTY_FOUNDER: DynastyFounder,
    config.FEAT_EXPLORER: Explorer,
    config.FEAT_FOESLAYER: Foeslayer,
    config.FEAT_LIBERATOR: Liberator,
    config.FEAT_PLANAR_TRAVELER: PlanarTraveler,
    config.FEAT_PROPHET: Prophet,
    config.FEAT_TRUTH_SEEKER: TruthSeeker,
    config.FEAT_OBJECT_OF_LEGEND: ObjectOfLegend,
    config.FEAT_CENTER_OF_POWER: CenterOfPower,
    config.FEAT_EXPERT_TRAINER: ExpertTrainer,
    config.FEAT_FOCUSED_OVERSEER: FocusedOverseer,
    config.FEAT_FOCUSED_WORKER: FocusedWorker,
    config.FEAT_FORTUNATE_RULER: FortunateRuler,
    config.FEAT_FORTUNATE_MANAGER: FortunateManager,
    config.FEAT_INSPIRATIONAL_COMMANDER: InspirationalCommander,
    config.FEAT_NATURAL_RULER: NaturalRuler,
    config.FEAT_PRECOCIOUS_YOUTH: PrecociousYouth,
    config.FEAT_DOG_SNIFF_HATE: DogSniffHate,
    config.FEAT_DRAGONCRAFTING: Dragoncrafting,
    config.FEAT_COURAGE_IN_NUMBERS: CourageInNumbers,
    config.FEAT_OVERWHELM: Overwhelm,
    config.FEAT_TANDEMEVASION: Tandemevasion,
    config.FEAT_COVERING_SHIELD: CoveringShield,
    config.FEAT_DEATH_FROMBELOW: DeathFrombelow,
    config.FEAT_DRAGONHEART: Dragonheart,
    config.FEAT_DRAGONSLAYER: Dragonslayer,
    config.FEAT_FLAYING_CRITICAL: FlayingCritical,
    config.FEAT_PORCUPINE_DEFENSE: PorcupineDefense,
    config.FEAT_REACH_DEFENSE: ReachDefense,
    config.FEAT_SNOUTGRIP: Snoutgrip,
    config.FEAT_WINGCLIPPER: Wingclipper,
    config.FEAT_IMPROVED_DAY_JOB: ImprovedDayJob,
    config.FEAT_PATIENT_STRIKE: PatientStrike,
    config.FEAT_STEADFAST_MIND: SteadfastMind,
    config.FEAT_QUICK_PREPARATION: QuickPreparation,
    config.FEAT_RENOWN: Renown,
    config.FEAT_VERSATILE_SPONTANEITY: VersatileSpontaneity,
    config.FEAT_COLLECTIVE_RECOLLECTION: CollectiveRecollection,
    config.FEAT_ESOTERIC_ADVANTAGE: EsotericAdvantage,
    config.FEAT_UNCANNY_ACTIVATION: UncannyActivation,
    config.FEAT_EMERGENCY_ATTUNEMENT: EmergencyAttunement,
    config.FEAT_PLANNED_SPONTANEITY: PlannedSpontaneity,
    config.FEAT_TAPESTRY_TRAVELER: TapestryTraveler,
    config.FEAT_CUT_YOUR_LOSSES: CutYourLosses,
    config.FEAT_IMPROVED_UNDERHANDED_TEAMWORK: ImprovedUnderhandedTeamwork,
    config.FEAT_UNDERHANDED_TEAMWORK: UnderhandedTeamwork,
    config.FEAT_ATHEIST_ABJURATIONS: AtheistAbjurations,
    config.FEAT_DIVINE_DEFIANCE: DivineDefiance,
    config.FEAT_DIVINE_DENOUNCER: DivineDenouncer,
    config.FEAT_FOCUSED_DISBELIEF: FocusedDisbelief,
    config.FEAT_ICONOCLAST: Iconoclast,
    config.FEAT_SEEDS_OFDOUBT: SeedsOfdoubt,
    config.FEAT_ANIMAL_ALLY: AnimalAlly,
    config.FEAT_DRUIDIC_DECODER: DruidicDecoder,
    config.FEAT_FRIEND_TO_ANIMALS: FriendToAnimals,
    config.FEAT_NATURE_SOUL: NatureSoul,
    config.FEAT_WEATHER_EYE: WeatherEye,
    config.FEAT_BEND_WITH_THE_WIND: BendWithTheWind,
    config.FEAT_BODY_CONTROL: BodyControl,
    config.FEAT_BODY_MASTERY: BodyMastery,
    config.FEAT_COMBAT_MEDITATION: CombatMeditation,
    config.FEAT_MEDITATION_MASTER: MeditationMaster,
    config.FEAT_MEDITATIVE_CONCENTRATION: MeditativeConcentration,
    config.FEAT_PERFECT_AWARENESS: PerfectAwareness,
    config.FEAT_PERFECT_CENTER: PerfectCenter,
    config.FEAT_SLOW_TIME: SlowTime,
    config.FEAT_DEMONIC_NEMESIS: DemonicNemesis,
    config.FEAT_EXORCIST_S_REBUTTAL: ExorcistSRebuttal,
    config.FEAT_OUTER_PLANES_TRAVELER: OuterPlanesTraveler,
    config.FEAT_VENGEFUL_BANISHER: VengefulBanisher,
    config.FEAT_COORDINATED_DISTRACTION: CoordinatedDistraction,
    config.FEAT_PUNCH_THROUGH: PunchThrough,
    config.FEAT_SPELL_CHAIN: SpellChain,
    config.FEAT_BABAU_ROGUE_TALENT: BabauRogueTalent,
    config.FEAT_FLENSING_STRIKE: FlensingStrike,
    config.FEAT_IMPROVED_STENCH: ImprovedStench,
    config.FEAT_PUNGENT_STENCH: PungentStench,
    config.FEAT_TOXIC_STENCH: ToxicStench,
    config.FEAT_DEMONIC_POSSESSION: DemonicPossession,
    config.FEAT_IMPROVED_POSSESSION: ImprovedPossession,
    config.FEAT_PENETRATING_POSSESSION: PenetratingPossession,
    config.FEAT_SPIRIT_VISION: SpiritVision,
    config.FEAT_IMPROVED_INFUSE_WEAPON: ImprovedInfuseWeapon,
    config.FEAT_MULTIWEAPON_DEFENSE: MultiweaponDefense,
    config.FEAT_MULTIWEAPON_SPECIALIST: MultiweaponSpecialist,
    config.FEAT_CONSUME_UNDEATH: ConsumeUndeath,
    config.FEAT_IMPROVED_DEATH_STEALING: ImprovedDeathStealing,
    config.FEAT_ACCURSED_HEX: AccursedHex,
    config.FEAT_ACROBATIC: Acrobatic,
    config.FEAT_ALERTNESS: Alertness,
    config.FEAT_ALIGNMENT_CHANNEL: AlignmentChannel,
    config.FEAT_ANIMAL_AFFINITY: AnimalAffinity,
    config.FEAT_ARCANE_ARMOR_TRAINING: ArcaneArmorTraining,
    config.FEAT_ARCANE_BLAST: ArcaneBlast,
    config.FEAT_ARCANE_SHIELD: ArcaneShield,
    config.FEAT_ARCANE_STRIKE: ArcaneStrike,
    config.FEAT_ASCENDANT_SPELL: AscendantSpell,
    config.FEAT_ASPECT_OF_THE_BEAST: AspectOfTheBeast,
    config.FEAT_ATHLETIC: Athletic,
    config.FEAT_AUGMENT_SUMMONING: AugmentSummoning,
    config.FEAT_BLEEDING_CRITICAL: BleedingCritical,
    config.FEAT_BLIND_FIGHT: BlindFight,
    config.FEAT_CATCH_OFF_GUARD: CatchOffGuard,
    config.FEAT_CHANNEL_SMITE: ChannelSmite,
    config.FEAT_CHARGE_THROUGH: ChargeThrough,
    config.FEAT_CLEAVE: Cleave,
    config.FEAT_COMBAT_EXPERTISE: CombatExpertise,
    config.FEAT_COMBAT_REFLEXES: CombatReflexes,
    config.FEAT_COMMAND_UNDEAD: CommandUndead,
    config.FEAT_CRITICAL_FOCUS: CriticalFocus,
    config.FEAT_CRITICAL_MASTERY: CriticalMastery,
    config.FEAT_DASTARDLY_FINISH: DastardlyFinish,
    config.FEAT_DAZZLING_DISPLAY: DazzlingDisplay,
    config.FEAT_DEADLY_AIM: DeadlyAim,
    config.FEAT_DEADLY_STROKE: DeadlyStroke,
    config.FEAT_DEATH_FROM_ABOVE: DeathFromAbove,
    config.FEAT_DECEITFUL: Deceitful,
    config.FEAT_DEEPSIGHT: Deepsight,
    config.FEAT_DEFENSIVE_COMBAT_TRAINING: DefensiveCombatTraining,
    config.FEAT_DEFLECT_ARROWS: DeflectArrows,
    config.FEAT_DEFT_HANDS: DeftHands,
    config.FEAT_DETECT_EXPERTISE: DetectExpertise,
    config.FEAT_DISRUPTIVE: Disruptive,
    config.FEAT_DISTANCE_THROWER: DistanceThrower,
    config.FEAT_DIVINE_INTERFERENCE: DivineInterference,
    config.FEAT_DODGE: Dodge,
    config.FEAT_DREADFUL_CARNAGE: DreadfulCarnage,
    config.FEAT_DRINK_IS_LIFE: DrinkIsLife,
    config.FEAT_DUAL_PATH: DualPath,
    config.FEAT_EAGLE_EYES: EagleEyes,
    config.FEAT_ELDRITCH_HERITAGE: EldritchHeritage,
    config.FEAT_ELEMENTAL_CHANNEL: ElementalChannel,
    config.FEAT_ELEMENTAL_FIST: ElementalFist,
    config.FEAT_ELEMENTAL_FOCUS: ElementalFocus,
    config.FEAT_ELVEN_ACCURACY: ElvenAccuracy,
    config.FEAT_ENDURANCE: Endurance,
    config.FEAT_ESCHEW_MATERIALS: EschewMaterials,
    config.FEAT_EXTRA_MYTHIC_POWER: ExtraMythicPower,
    config.FEAT_EXTRA_PATH_ABILITY: ExtraPathAbility,
    config.FEAT_FABULOUS_FIGMENTS: FabulousFigments,
    config.FEAT_FAR_SHOT: FarShot,
    config.FEAT_FAST_EMPATHY: FastEmpathy,
    config.FEAT_FIRE_MUSIC: FireMusic,
    config.FEAT_FLEET: Fleet,
    config.FEAT_FURIOUS_FOCUS: FuriousFocus,
    config.FEAT_GNOME_TRICKSTER: GnomeTrickster,
    config.FEAT_GORGON_S_FIST: GorgonSFist,
    config.FEAT_GREAT_FORTITUDE: GreatFortitude,
    config.FEAT_GUIDED_HAND: GuidedHand,
    config.FEAT_HEROIC_DEFIANCE: HeroicDefiance,
    config.FEAT_HEROIC_RECOVERY: HeroicRecovery,
    config.FEAT_IMPROVED_BULL_RUSH: ImprovedBullRush,
    config.FEAT_IMPROVED_CHANNEL: ImprovedChannel,
    config.FEAT_IMPROVED_COUNTERSPELL: ImprovedCounterspell,
    config.FEAT_IMPROVED_CRITICAL: ImprovedCritical,
    config.FEAT_IMPROVED_DIRTY_TRICK: ImprovedDirtyTrick,
    config.FEAT_IMPROVED_DISARM: ImprovedDisarm,
    config.FEAT_IMPROVED_DRAG: ImprovedDrag,
    config.FEAT_IMPROVED_FAMILIAR: ImprovedFamiliar,
    config.FEAT_IMPROVED_GRAPPLE: ImprovedGrapple,
    config.FEAT_IMPROVED_INITIATIVE: ImprovedInitiative,
    config.FEAT_IMPROVED_OVERRUN: ImprovedOverrun,
    config.FEAT_IMPROVED_REPOSITION: ImprovedReposition,
    config.FEAT_IMPROVED_STEAL: ImprovedSteal,
    config.FEAT_IMPROVED_STONECUNNING: ImprovedStonecunning,
    config.FEAT_IMPROVED_SUNDER: ImprovedSunder,
    config.FEAT_IMPROVED_TRIP: ImprovedTrip,
    config.FEAT_IMPROVED_UNARMED_STRIKE: ImprovedUnarmedStrike,
    config.FEAT_INTIMIDATING_PROWESS: IntimidatingProwess,
    config.FEAT_IRON_WILL: IronWill,
    config.FEAT_KNOCKOUT_ARTIST: KnockoutArtist,
    config.FEAT_LEGENDARY_TEAMWORK: LegendaryTeamwork,
    config.FEAT_LIGHTNING_REFLEXES: LightningReflexes,
    config.FEAT_LUCKY_HALFLING: LuckyHalfling,
    config.FEAT_LUCKY_SURGE: LuckySurge,
    config.FEAT_LUNGE: Lunge,
    config.FEAT_MAGICAL_APTITUDE: MagicalAptitude,
    config.FEAT_MANYSHOT: Manyshot,
    config.FEAT_MARKED_FOR_GLORY: MarkedForGlory,
    config.FEAT_MAXIMIZE_SURGE: MaximizeSurge,
    config.FEAT_MEDUSA_S_WRATH: MedusaSWrath,
    config.FEAT_MISSILE_SHIELD: MissileShield,
    config.FEAT_MOBILITY: Mobility,
    config.FEAT_MONASTIC_LEGACY: MonasticLegacy,
    config.FEAT_MOUNTED_ARCHERY: MountedArchery,
    config.FEAT_MOUNTED_COMBAT: MountedCombat,
    config.FEAT_MYTHIC_COMPANION: MythicCompanion,
    config.FEAT_MYTHIC_CRAFTER: MythicCrafter,
    config.FEAT_MYTHIC_PARAGON: MythicParagon,
    config.FEAT_MYTHIC_SPELL_LORE: MythicSpellLore,
    config.FEAT_NATURAL_SPELL: NaturalSpell,
    config.FEAT_NIMBLE_MOVES: NimbleMoves,
    config.FEAT_PENETRATING_STRIKE: PenetratingStrike,
    config.FEAT_PERSUASIVE: Persuasive,
    config.FEAT_PINPOINT_TARGETING: PinpointTargeting,
    config.FEAT_POINT_BLANK_SHOT: PointBlankShot,
    config.FEAT_POTENT_SURGE: PotentSurge,
    config.FEAT_POWER_ATTACK: PowerAttack,
    config.FEAT_POWERFUL_SHAPE: PowerfulShape,
    config.FEAT_PROPHETIC_VISIONARY: PropheticVisionary,
    config.FEAT_QUICK_DRAW: QuickDraw,
    config.FEAT_RACIAL_HERITAGE: RacialHeritage,
    config.FEAT_RAPID_RELOAD: RapidReload,
    config.FEAT_RAPID_SHOT: RapidShot,
    config.FEAT_RHETORICAL_FLOURISH: RhetoricalFlourish,
    config.FEAT_RIDE_BY_ATTACK: RideByAttack,
    config.FEAT_RUN: Run,
    config.FEAT_SAVING_SHIELD: SavingShield,
    config.FEAT_SCORPION_STYLE: ScorpionStyle,
    config.FEAT_SELECTIVE_CHANNELING: SelectiveChanneling,
    config.FEAT_SELF_SUFFICIENT: SelfSufficient,
    config.FEAT_SHATTER_DEFENSES: ShatterDefenses,
    config.FEAT_SHIELD_FOCUS: ShieldFocus,
    config.FEAT_SHIELD_SLAM: ShieldSlam,
    config.FEAT_SHOT_ON_THE_RUN: ShotOnTheRun,
    config.FEAT_SKILL_FOCUS: SkillFocus,
    config.FEAT_SNATCH_ARROWS: SnatchArrows,
    config.FEAT_SOCIABLE: Sociable,
    config.FEAT_SPELL_FOCUS: SpellFocus,
    config.FEAT_SPELL_MASTERY: SpellMastery,
    config.FEAT_SPELL_PENETRATION: SpellPenetration,
    config.FEAT_SPELLBREAKER: Spellbreaker,
    config.FEAT_SPIRITED_CHARGE: SpiritedCharge,
    config.FEAT_SPONTANEOUS_METAFOCUS: SpontaneousMetafocus,
    config.FEAT_SPRING_ATTACK: SpringAttack,
    config.FEAT_STEALTHY: Stealthy,
    config.FEAT_STRIKE_BACK: StrikeBack,
    config.FEAT_STRONG_COMEBACK: StrongComeback,
    config.FEAT_STUNNING_FIST: StunningFist,
    config.FEAT_THROW_ANYTHING: ThrowAnything,
    config.FEAT_TITAN_STRIKE: TitanStrike,
    config.FEAT_TOUGHNESS: Toughness,
    config.FEAT_TRAMPLE: Trample,
    config.FEAT_TRIPPING_STAFF: TrippingStaff,
    config.FEAT_TWO_FISTED_DRINKER: TwoFistedDrinker,
    config.FEAT_TWO_WEAPON_DEFENSE: TwoWeaponDefense,
    config.FEAT_TWO_WEAPON_FIGHTING: TwoWeaponFighting,
    config.FEAT_TWO_WEAPON_REND: TwoWeaponRend,
    config.FEAT_UNDEAD_MASTER: UndeadMaster,
    config.FEAT_UNSEAT: Unseat,
    config.FEAT_VALIANT_VAULT: ValiantVault,
    config.FEAT_VITAL_STRIKE: VitalStrike,
    config.FEAT_VOICE_OF_THE_SIBYL: VoiceOfTheSibyl,
    config.FEAT_WARRIOR_PRIEST: WarriorPriest,
    config.FEAT_WEAPON_FINESSE: WeaponFinesse,
    config.FEAT_WEAPON_FOCUS: WeaponFocus,
    config.FEAT_WEAPON_SPECIALIZATION: WeaponSpecialization,
    config.FEAT_WITCH_KNIFE: WitchKnife,
    config.FEAT_DEMONOLOGIST: Demonologist,
    config.FEAT_DEMON_GRAFTER: DemonGrafter,
    config.FEAT_DEMONIC_OBEDIENCE: DemonicObedience,
    config.FEAT_EXTRA_FEATURE: ExtraFeature,
    config.FEAT_FAST_CHANGE: FastChange,
    config.FEAT_BAT_SHAPE: BatShape,
    config.FEAT_BLOODMARKED_FLIGHT: BloodmarkedFlight,
    config.FEAT_DIRE_BAT_SHAPE: DireBatShape,
    config.FEAT_BEAR_HUG: BearHug,
    config.FEAT_BEARTRAP_BITE: BeartrapBite,
    config.FEAT_FEROCIOUS_LOYALTY: FerociousLoyalty,
    config.FEAT_SWARM_SCATTER: SwarmScatter,
    config.FEAT_SWARM_STRIKE: SwarmStrike,
    config.FEAT_MOTIVATING_DISPLAY: MotivatingDisplay,
    config.FEAT_SURPRISING_COMBATANT: SurprisingCombatant,
    config.FEAT_VIOLENT_DISPLAY: ViolentDisplay,
    config.FEAT_WOLF_SAVAGE: WolfSavage,
    config.FEAT_WOLF_STYLE: WolfStyle,
    config.FEAT_WOLF_TRIP: WolfTrip,
    config.FEAT_BLOATMAGE_INITIATE: BloatmageInitiate,
    config.FEAT_MULTIWEAPON_FIGHTING: MultiweaponFighting,
    config.FEAT_STABLE_SPELL: StableSpell,
    config.FEAT_SHADOW_GAMBIT: ShadowGambit,
    config.FEAT_SHADOW_GRASP: ShadowGrasp,
    config.FEAT_TENEBROUS_SPELL: TenebrousSpell,
    config.FEAT_UMBRAL_SPELL: UmbralSpell,
    config.FEAT_INSCRIBE_MAGICAL_TATTOO: InscribeMagicalTattoo,
    config.FEAT_EXTEND_THE_BULWARK: ExtendTheBulwark,
    config.FEAT_QUILLBREAKER_DEFENSE: QuillbreakerDefense,
    config.FEAT_SHIELD_SNAG: ShieldSnag,
    config.FEAT_EQUIPMENT_TRICK: EquipmentTrick,
    config.FEAT_BLOWOUT_SHOT_DEED: BlowoutShotDeed,
    config.FEAT_WHIP_SHOT_DEED: WhipShotDeed,
    config.FEAT_FALSE_CASTING: FalseCasting,
    config.FEAT_FALSE_FOCUS: FalseFocus,
    config.FEAT_OSIRIONOLOGY: Osirionology,
    config.FEAT_OUT_OF_THE_SUN: OutOfTheSun,
    config.FEAT_THUVIAN_GRENADIER: ThuvianGrenadier,
    config.FEAT_UNDERMINE: Undermine,
    config.FEAT_HORN_OF_THE_CRIOSPHINX: HornOfTheCriosphinx,
    config.FEAT_WINGS_OF_THE_ANDROSPHINX: WingsOfTheAndrosphinx,
    config.FEAT_SHIELD_MASTER: ShieldMaster,
    config.FEAT_BETRAYING_BLOW: BetrayingBlow,
    config.FEAT_SOLO_MANEUVERS: SoloManeuvers,
    config.FEAT_DIRTY_TRICK_MASTER: DirtyTrickMaster,
    config.FEAT_DIVERT_HARM: DivertHarm,
    config.FEAT_CRISIS_OF_CONSCIENCE: CrisisOfConscience,
    config.FEAT_PLANAR_HUNTER: PlanarHunter,
    config.FEAT_PRACTICED_LEADERSHIP: PracticedLeadership,
    config.FEAT_FABULIST: Fabulist,
    config.FEAT_GUN_TWIRLING: GunTwirling,
    config.FEAT_NAMED_BULLET: NamedBullet
}