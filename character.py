
import alignment
import race
import gender
import color
import ability
import growth
import magicalprotection
import encumberance
import skill
import item
import characterclass
import feat
import config

import random
import math
import string
import uuid

# TODO: Apply certain things, like BAB and class skills, from a character's race if it has no classes


class Character:

    def __init__(self):
        self.uuid = 'uuid'
        self.companions = []
        self.Name = ""
        self.Alignment = alignment.Alignment()
        self.Race = race.Race()
        self.Languages = self.Race.StartingLanguages
        self.Diety = ""
        self.PlayerName = ""
        self.Gender = config.GENDER_MALE
        self.Age = 0
        self.Height = 0  # In inches
        self.Weight = 0  # In pounds
        self.HairColor = color.Random()
        self.EyeColor = color.Random()
        self.Homeland = ""

        self.BaseAbilities = {}  # Dict of Ability: Base Score
        self.EnhancementAbilities = {}  # Dict of Ability: Enhancement Score
        self.InherentAbilities = {}  # Dict of Ability: Inherent Score
        self.TempAbilities = {}  # Dict of Ability: Temp Score
        self.MiscAbilities = {}  # Dict of Ability: Misc Score
        self.PenaltyAbilities = {}  # Dict of Ability: Penalty Score
        self.LeveledAbilities = {}  # Dict of Ability: Penalty Score
        self.FeatAbilities = {}  # Dict of Ability: Penalty Score
        for key in ability.GetAbilityNames():
            self.BaseAbilities[key] = 0
            self.EnhancementAbilities[key] = 0
            self.InherentAbilities[key] = 0
            self.TempAbilities[key] = 0
            self.MiscAbilities[key] = 0
            self.PenaltyAbilities[key] = 0
            self.LeveledAbilities[key] = 0
            self.FeatAbilities[key] = 0
        self.StartingIntelligence = self.BaseAbilities[config.ABILITY_INTELLIGENCE]

        self.BaseMaxHealth = 0
        self.TempBonusHealth = 0
        self.FCHealthUsed = 0
        self.CurrentDamage = 0
        self.NonLethalDamage = 0

        self.Classes = []  # List (Class, level). The first is the favored class

        self.Experience = 0
        self.GrowthRate = config.GROWTH_MEDIUM

        self.Effects = {}  # List of Effect name: effect

        # Effect changes. (List of (shouldBeActive function, amount, type))
        self.EffectNaturalArmorClass = []
        self.EffectArmorClass = []
        self.EffectFortitude = []
        self.EffectReflex = []
        self.EffectWill = []
        self.EffectAbilities = {}
        for key in ability.GetAbilityNames():
            self.EffectAbilities[key] = []
        self.EffectMeleeAttack = []
        self.EffectMeleeDamage = []
        self.EffectOffHandDamage = []
        self.EffectTwoHandDamage = []
        self.EffectRangedAttack = []
        self.EffectRangedDamage = []
        self.EffectTwoWeaponFightingExtraAttack = []
        self.EffectMeleeExtraAttack = []
        self.EffectRangedExtraAttack = []
        self.EffectSkillCheckAll = []
        self.EffectSkillCheck = {}
        for key in skill.GetSkillNames():
            self.EffectSkillCheck[key] = []
        self.EffectSizeChange = []
        self.EffectLandSpeed = []
        self.EffectFlySpeed = []
        self.EffectSwimSpeed = []
        self.EffectBurrowSpeed = []
        self.EffectClimbSpeed = []
        self.EffectSpeedMultiplierLand = []
        self.EffectSpeedMultiplierFly = []
        self.EffectSpeedMultiplierSwim = []
        self.EffectSpeedMultiplierBurrow = []
        self.EffectSpeedMultiplierClimb = []

        self.MiscArmorClass = 0
        self.MiscFlatFooted = 0
        self.MiscTouch = 0
        self.MiscCMD = 0
        self.MiscInitiative = 0
        self.MiscFortitude = 0
        self.MiscReflex = 0
        self.MiscWill = 0
        self.MiscMeleeAttack = 0
        self.MiscRangedAttack = 0
        self.MiscCMB = 0
        self.MiscSkills = {}
        for key in skill.GetSkillNames():
            self.MiscSkills[key] = 0
        self.TempArmorClass = 0
        self.TempFlatFooted = 0
        self.TempTouch = 0
        self.TempCMD = 0
        self.TempFortitude = 0
        self.TempReflex = 0
        self.TempWill = 0
        self.TempMeleeAttack = 0
        self.TempRangedAttack = 0
        self.TempCMB = 0
        self.TempSkills = {}
        for key in skill.GetSkillNames():
            self.TempSkills[key] = 0
        self.LearnedFeats = []  # List of feats. Adding one hear should also add the appropriate effect

        self.Skills = {}  # Dict of SkillName: (rank, skill class)
        self.FeatSkills = {}  # Dict of SkillName: Ranks
        for key in skill.GetSkillNames():
            self.Skills[key] = [0, skill.SkillClasses[key](key)]
            self.FeatSkills[key] = 0

        self.FCSkillPointsUsed = 0
        self.FCSkills = {}
        for key in skill.GetSkillNames():
            self.FCSkills[key] = 0

        self.RacialSkills = {}
        for key in skill.GetSkillNames():
            self.RacialSkills[key] = 0

        self.HeroPoints = 0
        self.MaxHeroPoints = 0

        self.Weapons = []  # List of (Weapon, active)

        self.Armor = (None, False)  # Armor, active
        self.Shield = (None, False)  # Shield, active

        self.MagicalProtection = []  # List of (MagicalProtection, active)

        self.FlightManeuverability = config.MOVETYPE_AVERAGE
        self.MovementIgnoreArmor = config.MOVETYPE_NO_EFFECT
        self.RunMultiplier = 1
        self.BaseChargeRunBoost = 0

        self.DamageResistance = 0
        self.SpellResistance = 0
        self.FireResistance = 0
        self.ColdResistance = 0
        self.AcidResistance = 0
        self.ElectricityResistance = 0
        self.SonicResistance = 0

        self.Inventory = item.Inventory(self, config.BODY_TYPE_BIPEDHANDS)  # Items and Equipment

        self.ChooseInitialLanguagesBasedOnIntelligence()

        self.CanFly = False
        self.CanSwim = False
        self.CanBurrow = False
        self.CanClimb = False

        # self.OpponentRace = race.NONE
        # self.OpponentType = race.NONE
        # self.OpponentSubTypes = race.NONE  # or these together as needed
        # self.OpponentClass = spell.NONE
        # self.OpponentSpell = spell.NONE
        # self.OpponentSpellClass = spell.NONE
        # self.OpponentSpAbility = spell.NONE
        # self.OpponentSuAbility = spell.NONE
        # self.OpponentItemType = item.NONE  # or together as needed e.g. poison, sword. Use tags
        # self.OpponentAttackType = NONE  # or together as needed e.g. bull rush, trip, etc

        # self.AppraisingItemType = item.NONE
        # self.PerceptionEnvironmentType = NONE  # e.g. stone, etc

    def CalculateEffects(self, effArray):
        seenTypes = set()
        total = 0
        for eff in effArray:
            if eff[2] in seenTypes:
                continue
            if eff[0](self):
                if not eff[2] in config.StackableTypes:
                    seenTypes.Add(eff[2])
                total += eff[1]
        return total

    def IsEffectActive(self, eff):
        return eff in self.Effects and self.Effects[eff] == True

    # Radius of what can be seen. Also applies vision effects
    def Vision(self, lightLevel=config.LIGHT_LEVEL_NORMAL):
        # TODO: Factor in effects and items, race vision, etc
        return 0

    def Smell(self):
        # TODO: Factor in effects and items, race smell, etc
        return 0

    def Hearing(self):
        # TODO: Factor in effects and items, race hearing, etc
        return 0

    def ChooseInitialLanguagesBasedOnIntelligence(self, rand=True):
        if rand:
            possibilities = self.Race.PossibleLanguages
            if not possibilities:
                return
            i = self.AbilityModifiers()[config.ABILITY_INTELLIGENCE]
            while i > 0 and not all(p in self.Languages for p in possibilities):
                r = random.choice(possibilities)
                if r not in self.Languages:
                    self.Languages.append(r)
                    i -= 1
        else:
            # TODO: Allow manually choosing additional languages from race
            return

    def Size(self):
        return self.Race.Size

    def AgeType(self):
        return self.Race.AgeType(self.Age)

    def MaxHealth(self):
        return self.BaseMaxHealth + self.FCHealthUsed + self.TempBonusHealth

    def CurrentHealth(self):
        return self.MaxHealth() - self.Damage()

    def Damage(self):
        return self.CurrentDamage

    def CheckNonLethalDamage(self):
        #TODO
        return

    def CheckDamage(self):
        # TODO
        return

    def Harm(self, amount):
        self.CurrentDamage += amount
        self.CheckDamage()

    def HarmNonLethal(self, amount):
        self.NonLethalDamage += amount
        self.CheckDamage()

    def Heal(self, amount):
        self.CurrentDamage -= amount
        self.CheckDamage()

    def HealNonLethal(self, amount):
        self.NonLethalDamage -= amount
        self.CheckDamage()

    def Kill(self):
        # TODO
        return

    def Resurrect(self):
        # TODO
        return

    # Add feats, effects, statuses, etc
    def AddEffect(self, effect, effectType):
        if effectType == config.EFFECT_LEARNED_FEAT:
            self.LearnedFeats.append(effect)
            self.LearnedFeats[len(self.LearnedFeats) - 1].AddEffect(self)

    # Remove feats, effects, statuses, etc
    def RemoveEffect(self, effectIdx, effectType):
        if effectType == config.EFFECT_LEARNED_FEAT:
            self.LearnedFeats[effectIdx].RemoveEffect(self)
            del self.LearnedFeats[effectIdx]

    def Abilities(self):
        ageAbilityModifiers = self.Race.GetAgeAbilityModifiers(self.Age)
        abil = {}
        for key in ability.GetAbilityNames():
            abil[key] = max(0, self.BaseAbilities[key] +
                            self.EnhancementAbilities[key] +
                            self.InherentAbilities[key] +
                            self.MiscAbilities[key] +
                            self.TempAbilities[key] -
                            self.PenaltyAbilities[key] +
                            self.LeveledAbilities[key] +
                            self.Race.AbilityScoreModifiers[key] +
                            ageAbilityModifiers[key])
        return abil

    def AbilityModifiers(self):
        abil = {}
        scores = self.Abilities()
        for key in ability.GetAbilityNames():
            abil[key] = max(-5, (scores[key] - 10) / 2)
        return abil

    def Level(self):
        return growth.GetLevel(self.GrowthRate, self.Experience)

    def ClassBAB(self):
        return sum(int(i[0].BAB * i[1]) for i in self.Classes)

    def ClassFortitude(self):
        return sum(int(2+i[1]/2 if i[0].Fortitude == config.SAVE_SCORE_GOOD else i[1]/3) for i in self.Classes)

    def ClassReflex(self):
        return sum(int(2+i[1]/2 if i[0].Reflex == config.SAVE_SCORE_GOOD else i[1]/3) for i in self.Classes)

    def ClassWill(self):
        return sum(int(2+i[1]/2 if i[0].Will == config.SAVE_SCORE_GOOD else i[1]/3) for i in self.Classes)

    def ClassSkillPoints(self):
        return sum(i[0].Skills*i[1] for i in self.Classes)

    def GetEffectScoreByType(self, eff=None, effectType=None):
        if eff and effectType:
            if effectType in config.StackableTypes:
                total = 0
                for i in eff:
                    if i[2] == effectType and i[0](self):
                        total += i[1]
                return total
            else:
                m = -9999999
                for i in eff:
                    if i[2] == effectType and i[0](self):
                        v = i[1]
                        if v > m:
                            m = v
                return m if m != -9999999 else 0
        return 0

    def AddLeveledAbility(self, type, amount):
        self.LeveledAbilities[type] += amount

    def AddMiscAbility(self, type, amount):
        self.MiscAbilities[type] += amount

    def AddPenaltyAbility(self, type, amount):
        self.PenaltyAbilities[type] += amount

    def IncreaseTempAbility(self, type, amount):
        self.TempAbilities[type] += amount

    def DecreaseTempAbility(self, type, amount):
        self.TempAbilities[type] -= amount

    def ArmorClass(self):
        return (10 +
                (self.Armor[0].ArmorClass() if self.Armor[1] else 0) +
                (self.Shield[0].ArmorClass() if self.Shield[1] else 0) +
                min(self.AbilityModifiers()[config.ABILITY_DEXTERITY], self.MaxDexBonus()) +
                self.Size().ArmorClass +
                self.CalculateEffects(self.EffectNaturalArmorClass) +
                self.GetEffectScoreByType(self.EffectArmorClass, config.EFFECT_DEFLECTION) +
                self.GetEffectScoreByType(self.EffectArmorClass, config.EFFECT_DODGE) +
                self.MiscArmorClass + self.TempArmorClass)

    def FlatFooted(self):
        return (10 +
                (self.Armor[0].ArmorClass() if self.Armor[1] else 0) +
                (self.Shield[0].ArmorClass() if self.Shield[1] else 0) +
                (-1 if min(self.AbilityModifiers()[config.ABILITY_DEXTERITY], self.MaxDexBonus()) < 0 else 0) +
                self.Size().ArmorClass +
                self.CalculateEffects(self.EffectNaturalArmorClass) +
                self.GetEffectScoreByType(self.EffectArmorClass, config.EFFECT_DEFLECTION) +
                self.MiscFlatFooted + self.TempFlatFooted)

    def Touch(self):
        return (10 +
                min(self.AbilityModifiers()[config.ABILITY_DEXTERITY], self.MaxDexBonus()) +
                self.Size().ArmorClass +
                self.GetEffectScoreByType(self.EffectArmorClass, config.EFFECT_DEFLECTION) +
                self.GetEffectScoreByType(self.EffectArmorClass, config.EFFECT_DODGE) +
                self.MiscArmorClass + self.TempArmorClass)

    def CMD(self):
        return (10 +
                self.ClassBAB() +
                self.AbilityModifiers()[config.ABILITY_STRENGTH] +
                min(self.AbilityModifiers()[config.ABILITY_DEXTERITY], self.MaxDexBonus()) +
                self.Size().CMB +
                self.GetEffectScoreByType(self.EffectArmorClass, config.EFFECT_DEFLECTION) +
                self.GetEffectScoreByType(self.EffectArmorClass, config.EFFECT_DODGE) +
                self.MiscArmorClass + self.TempArmorClass)

    def MaxDexBonus(self):
        enc = encumberance.GetEncumberance(self)
        return min((self.Armor[0].MaxDexBonus if self.Armor[1] else 99999),
                   (self.Shield[0].MaxDexBonus if self.Shield[1] else 99999),
                   (99999 if enc == config.ENCUMBERANCE_LIGHT else
                    (3 if enc == config.ENCUMBERANCE_MEDIUM else
                        (1 if enc == config.ENCUMBERANCE_HEAVY else
                            (0 if enc == config.ENCUMBERANCE_OVER else 99999)))))

    def ArcaneSpellFailure(self):
        return ((self.Armor[0].SpellFailure if self.Armor[1] else 0) +
                (self.Shield[0].SpellFailure if self.Shield[1] else 0))

    def Initiative(self):
        return min(self.AbilityModifiers()[config.ABILITY_DEXTERITY], self.MaxDexBonus()) + self.MiscInitiative;

    def FavoredClassPointsLeft(self):
        if not self.Classes:
            return 0
        return self.Classes[0][1] - self.FCHealthUsed - self.FCSkillPointsUsed

    def TotalSkillPoints(self):
        return self.ClassSkillPoints() + self.Level()*self.AbilityModifiers()[config.ABILITY_INTELLIGENCE] + self.FCSkillPointsUsed

    def SkillPointsLeft(self):
        return self.TotalSkillPoints() - sum(self.Skills[key][0] for key in self.Skills) - self.FCSkillPointsUsed

    def SkillScores(self):
        skills = {}
        for key in skill.GetSkillNames():
            skills[key] = self.Skills[key][1].GetTotal(self)
        return skills

    def SkillIsAvailable(self):
        skills = {}
        for key in skill.GetSkillNames():
            skills[key] = self.Skills[key][1].IsAvailable(self)
        return skills

    def ArmorCheckPenalty(self):
        enc = encumberance.GetEncumberance(self)
        return ((self.Armor[0].ArmorCheckPenalty if self.Armor[1] else 0) +
                (self.Shield[0].ArmorCheckPenalty if self.Shield[1] else 0) +
                (0 if enc == config.ENCUMBERANCE_LIGHT else
                    (-3 if enc == config.ENCUMBERANCE_MEDIUM else
                        (-6 if enc == config.ENCUMBERANCE_HEAVY else
                            (0 if enc == config.ENCUMBERANCE_OVER else -99999)))))

    def Fortitude(self):
        return (self.ClassFortitude() +
                self.AbilityModifiers()[config.ABILITY_CONSTITUTION] +
                self.GetEffectScoreByType(self.EffectFortitude, config.EFFECT_RESISTANCE) +
                self.MiscFortitude + self.TempFortitude)

    def Reflex(self):
        return (self.ClassReflex() +
                self.AbilityModifiers()[config.ABILITY_DEXTERITY] +
                self.GetEffectScoreByType(self.EffectReflex, config.EFFECT_RESISTANCE) +
                self.MiscReflex + self.TempReflex)

    def Will(self):
        return (self.ClassWill() +
                self.AbilityModifiers()[config.ABILITY_WISDOM] +
                self.GetEffectScoreByType(self.EffectWill, config.EFFECT_RESISTANCE) +
                self.MiscWill + self.TempWill)

    def MeleeAttack(self):
        return (self.ClassBAB() +
                self.AbilityModifiers()[config.ABILITY_STRENGTH] +
                self.Size().ArmorClass +
                self.MiscMeleeAttack + self.TempMeleeAttack)

    def RangedAttack(self):
        return (self.ClassBAB() +
                self.AbilityModifiers()[config.ABILITY_DEXTERITY] +
                self.Size().ArmorClass +
                self.MiscRangedAttack + self.TempRangedAttack)

    def CMB(self):
        return (self.ClassBAB() +
                self.AbilityModifiers()[config.ABILITY_STRENGTH] +
                self.Size().CMB +
                self.MiscCMB + self.TempCMB)

    # A dict of speed type: [single, charge, run]
    def Speeds(self):
        speeds = {}
        baseSpeedLand = 0
        baseSpeedFly = 0
        baseSpeedSwim = 0
        baseSpeedBurrow = 0
        baseSpeedClimb = 0
        enc = encumberance.GetEncumberance(self)
        if enc == config.ENCUMBERANCE_OVER:
            baseSpeedLand = 5
            baseSpeedFly = 5
            baseSpeedSwim = 5
            baseSpeedBurrow = 5
            baseSpeedClimb = 5
        else:
            if self.MovementIgnoreArmor == config.MOVETYPE_SLOW_AND_STEADY:
                baseSpeedLand = self.Race.Speed * (1 if self.CalculateEffects(self.EffectSpeedMultiplierLand)==0 else self.CalculateEffects(self.EffectSpeedMultiplierLand))
                baseSpeedFly = self.Race.Speed * (1 if self.CalculateEffects(self.EffectSpeedMultiplierFly)==0 else self.CalculateEffects(self.EffectSpeedMultiplierFly))
                baseSpeedSwim = self.Race.Speed * (1 if self.CalculateEffects(self.EffectSpeedMultiplierSwim)==0 else self.CalculateEffects(self.EffectSpeedMultiplierSwim))
                baseSpeedBurrow = self.Race.Speed * (1 if self.CalculateEffects(self.EffectSpeedMultiplierBurrow)==0 else self.CalculateEffects(self.EffectSpeedMultiplierBurrow))
                baseSpeedClimb = self.Race.Speed * (1 if self.CalculateEffects(self.EffectSpeedMultiplierClimb)==0 else self.CalculateEffects(self.EffectSpeedMultiplierClimb))
            else:
                if ((self.MovementIgnoreArmor == config.MOVETYPE_ARMOR_TRAINING_I) and
                    ((self.Armor[1] and self.Armor[0].Weight == config.ARMOR_HEAVY) or
                     enc == config.ENCUMBERANCE_MEDIUM or enc == config.ENCUMBERANCE_HEAVY)):
                        baseSpeedLand = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierLand)==0 else self.CalculateEffects(self.EffectSpeedMultiplierLand))
                        baseSpeedFly = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierFly)==0 else self.CalculateEffects(self.EffectSpeedMultiplierFly))
                        baseSpeedSwim = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierSwim)==0 else self.CalculateEffects(self.EffectSpeedMultiplierSwim))
                        baseSpeedBurrow = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierBurrow)==0 else self.CalculateEffects(self.EffectSpeedMultiplierBurrow))
                        baseSpeedClimb = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierClimb)==0 else self.CalculateEffects(self.EffectSpeedMultiplierClimb))
                else:
                    if (self.MovementIgnoreArmor == config.MOVETYPE_ARMOR_TRAINING_II and
                        (enc == config.ENCUMBERANCE_MEDIUM or enc == config.ENCUMBERANCE_HEAVY)):
                            baseSpeedLand = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierLand)==0 else self.CalculateEffects(self.EffectSpeedMultiplierLand))
                            baseSpeedFly = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierFly)==0 else self.CalculateEffects(self.EffectSpeedMultiplierFly))
                            baseSpeedSwim = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierSwim)==0 else self.CalculateEffects(self.EffectSpeedMultiplierSwim))
                            baseSpeedBurrow = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierBurrow)==0 else self.CalculateEffects(self.EffectSpeedMultiplierBurrow))
                            baseSpeedClimb = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierClimb)==0 else self.CalculateEffects(self.EffectSpeedMultiplierClimb))
                    else:
                        if (self.MovementIgnoreArmor == config.MOVETYPE_NO_EFFECT and
                            ((self.Armor[1] and self.Armor[0].Weight == config.ARMOR_HEAVY) or
                             (self.Armor[1] and self.Armor[0].Weight == config.ARMOR_MEDIUM) or
                             enc == config.ENCUMBERANCE_MEDIUM or enc == config.ENCUMBERANCE_HEAVY)):
                                baseSpeedLand = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierLand)==0 else self.CalculateEffects(self.EffectSpeedMultiplierLand))
                                baseSpeedFly = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierFly)==0 else self.CalculateEffects(self.EffectSpeedMultiplierFly))
                                baseSpeedSwim = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierSwim)==0 else self.CalculateEffects(self.EffectSpeedMultiplierSwim))
                                baseSpeedBurrow = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierBurrow)==0 else self.CalculateEffects(self.EffectSpeedMultiplierBurrow))
                                baseSpeedClimb = math.ceil(self.Race.Speed*float(2)/3/5)*5*(1 if self.CalculateEffects(self.EffectSpeedMultiplierClimb)==0 else self.CalculateEffects(self.EffectSpeedMultiplierClimb))
                        else:
                            baseSpeedLand = self.Race.Speed
                            baseSpeedFly = self.Race.Speed
                            baseSpeedSwim = self.Race.Speed
                            baseSpeedBurrow = self.Race.Speed
                            baseSpeedClimb = self.Race.Speed
        speeds[config.MOVETYPE_LAND - 1] = [(int)(baseSpeedLand),
                                 (int)((baseSpeedLand + self.BaseChargeRunBoost) * 2),
                                 (int)((baseSpeedLand + self.BaseChargeRunBoost) * (self.RunMultiplier if self.RunMultiplier != 1 else (3 if enc >= config.ENCUMBERANCE_HEAVY else 4)))]
        speeds[config.MOVETYPE_FLY - 1] = [(int)(baseSpeedFly),
                                 (int)((baseSpeedFly + self.BaseChargeRunBoost) * 2),
                                 (int)((baseSpeedFly + self.BaseChargeRunBoost) * (self.RunMultiplier if self.RunMultiplier != 1 else (3 if enc >= config.ENCUMBERANCE_HEAVY else 4)))]
        speeds[config.MOVETYPE_SWIM - 1] = [(int)(baseSpeedSwim),
                                 (int)((baseSpeedSwim + self.BaseChargeRunBoost) * 2),
                                 (int)((baseSpeedSwim + self.BaseChargeRunBoost) * (self.RunMultiplier if self.RunMultiplier != 1 else (3 if enc >= config.ENCUMBERANCE_HEAVY else 4)))]
        speeds[config.MOVETYPE_BURROW - 1] = [(int)(baseSpeedBurrow),
                                 (int)((baseSpeedBurrow + self.BaseChargeRunBoost) * 2),
                                 (int)((baseSpeedBurrow + self.BaseChargeRunBoost) * (self.RunMultiplier if self.RunMultiplier != 1 else (3 if enc >= config.ENCUMBERANCE_HEAVY else 4)))]
        speeds[config.MOVETYPE_CLIMB - 1] = [(int)(baseSpeedClimb),
                                 (int)((baseSpeedClimb + self.BaseChargeRunBoost) * 2),
                                 (int)((baseSpeedClimb + self.BaseChargeRunBoost) * (self.RunMultiplier if self.RunMultiplier != 1 else (3 if enc >= config.ENCUMBERANCE_HEAVY else 4)))]
        return speeds

    def GetWeaponDamage(self, index):
        if ():
            return self.Weapons[index].GetDamage(self)

    def GetWeaponAttack(self, index):
        if ():
            return self.Weapons[index].GetDamage(self)

    def IsClassSkill(self, key):
        return any(c[0].ClassSkill(key) for c in self.Classes)

    def CalculateMaxHP(self, hitDieMethod):
        for c in range(len(self.Classes)):
            if c == 0:
                self.BaseMaxHealth += self.Classes[c][0].HitDie.sides
            hd = self.Classes[c][0].HitDie
            hd.numRolls = self.Classes[c][1]
            if c == 0:
                hd.numRolls -= 1
            if hitDieMethod == config.HIT_DIE_RANDOM:
                self.BaseMaxHealth += hd.Roll()
            elif hitDieMethod == config.HIT_DIE_AVERAGE:
                self.BaseMaxHealth += hd.RollAverage()
            elif hitDieMethod == config.HIT_DIE_MINIMUM:
                self.BaseMaxHealth += hd.RollMinimum()
            elif hitDieMethod == config.HIT_DIE_MAXIMUM:
                self.BaseMaxHealth += hd.RollMaximum()

    def AddFavoredClassSkill(self, skill, amount):
        if amount > self.FavoredClassPointsLeft():
            amount = max(0, amount - self.FavoredClassPointsLeft())
        self.FCSkillPointsUsed += amount
        self.FCSkills[skill] += amount
        return

    def AddFavoredClassHP(self, amount):
        if amount > self.FavoredClassPointsLeft():
            amount = max(0, amount - self.FavoredClassPointsLeft())
        self.FCHealthUsed += amount

    def AddItem(self, item, qty=1):
        self.Inventory.AddItem(item, qty)

    def SpendGold(self, amount):
        self.Inventory.Gold -= amount

    def AddGold(self, amount):
        self.Inventory.Gold += amount

    def DecreaseExperience(self, amount):
        self.Experience -= amount

    def IncreaseExperience(self, amount):
        self.Experience += amount

    def LearnSpell(self, classIdx, sp):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            self.Classes[classIdx][0].LearnSpell(sp)

    def ReplaceLearnedSpell(self, classIdx, oldSpellIdx, newSpell, oldSpellLevel=-1):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            self.Classes[classIdx][0].ReplaceLearnedSpell(oldSpellIdx, newSpell, oldSpellLevel)

    def ForgetSpell(self, classIdx, spLevel, spIdx):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            self.Classes[classIdx][0].ForgetSpell(spLevel, spIdx)

    def RemoveSpell(self, classIdx, spLevel, spIdx, domain=False):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            if isinstance(self.Classes[classIdx][0], characterclass.Cleric):
                self.Classes[classIdx][0].RemoveSpell(spLevel, spIdx, domain)
            else:
                self.Classes[classIdx][0].RemoveSpell(spLevel, spIdx)

    def PrepareSpell(self, classIdx, sp, uses, domain=False):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            if isinstance(self.Classes[classIdx][0], characterclass.Cleric):
                self.Classes[classIdx][0].PrepareSpell(sp, uses, domain)
            else:
                self.Classes[classIdx][0].PrepareSpell(sp, uses)

    def PrepareExistingSpell(self, classIdx, level, spellIdx, uses, domain=False):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            if isinstance(self.Classes[classIdx][0], characterclass.Cleric):
                self.Classes[classIdx][0].PrepareExistingSpell(level, spellIdx, uses, domain)
            else:
                self.Classes[classIdx][0].PrepareExistingSpell(level, spellIdx, uses)

    def UseSpell(self, classIdx, spLevel, spIdx, uses, domain=False):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            if isinstance(self.Classes[classIdx][0], characterclass.Cleric):
                self.Classes[classIdx][0].UseSpell(spLevel, spIdx, uses, domain)
            else:
                self.Classes[classIdx][0].UseSpell(spLevel, spIdx, uses)

    def UnPrepareSpell(self, classIdx, spLevel, spIdx, uses, domain=False):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            if isinstance(self.Classes[classIdx][0], characterclass.Cleric):
                self.Classes[classIdx][0].UnPrepareSpell(spLevel, spIdx, uses, domain)
            else:
                self.Classes[classIdx][0].UnPrepareSpell(spLevel, spIdx, uses)

    def UnPrepareSpells(self, classIdx, level=-1):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            self.Classes[classIdx][0].UnPrepareSpells(level)

    def ResetClassSpellLevel(self, classIdx, level):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            self.Classes[classIdx][0].ResetDay(level)

    def ResetClassSpellLevels(self, classIdx):
        if isinstance(self.Classes[classIdx][0], characterclass.SpellcastingClass):
            self.Classes[classIdx][0].ResetDay()

    def ResetSpells(self):
        for i in range(len(self.Classes)):
            self.ResetClassSpellLevels(i)

    def AddDomain(self, classIdx, domain):
        self.Classes[classIdx][0].AddDomain(domain)

    def RemoveDomain(self, classIdx, domain):
        self.Classes[classIdx][0].RemoveDomain(domain)

    def GetFeatsLeftToLearn(self):
        return (self.Level() + 1) / 2 - len(self.LearnedFeats)

    def GetLanguagesLeftToLearn(self):
        return len(self.Languages) - len(self.Race.StartingLanguages) - self.Skills[config.SKILL_LINGUISTICS][0] - ((self.StartingIntelligence - 10) / 2 if (self.StartingIntelligence - 10) / 2 > 0 else 0)

    def ClassLevelsLeft(self):
        return self.Level() - sum(i[1] for i in self.Classes)

    def AbilityPointsLeft(self):
        return sum(self.LeveledAbilities[key] for key in self.LeveledAbilities) - self.Level() / 4

    def SetSkillRanks(self, skillid, value):
        self.Skills[skillid] = [value, self.Skills[skillid][1]]

    def LearnLanguage(self, l):
        if l not in self.Languages:
            self.Languages.append(l)

    def ForgetLanguage(self, l):
        for i in range(len(self.Languages)):
            if self.Languages[i] == l:
                del self.Languages[i]
                break

    def LearnFeat(self, l):
        if not any(f.ID == l for f in self.LearnedFeats):
            f = feat.LoadFeatById(l)
            self.LearnedFeats.append(f)

    def ForgetFeat(self, l):
        if l >= 0 or l < len(self.LearnedFeats):
            del self.LearnedFeats[l]

    def CreateRandom(self):
        self.companions = []
        self.Name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
        self.Alignment = alignment.Random()
        self.Race = race.RandomRace()()
        self.Languages = self.Race.StartingLanguages
        self.Diety = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
        self.PlayerName = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
        self.Gender = gender.Random()
        self.Height = self.Race.RandomHeight(self.Gender)  # In inches
        self.Weight = self.Race.RandomWeight(self.Gender)  # In pounds
        self.HairColor = color.Random()
        self.EyeColor = color.Random()
        self.Homeland = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(8, 17)))

        self.BaseAbilities = {}  # Dict of Ability: Base Score
        self.EnhancementAbilities = {}  # Dict of Ability: Enhancement Score
        self.InherentAbilities = {}  # Dict of Ability: Inherent Score
        self.TempAbilities = {}  # Dict of Ability: Temp Score
        self.MiscAbilities = {}  # Dict of Ability: Misc Score
        self.PenaltyAbilities = {}  # Dict of Ability: Penalty Score
        for key in ability.GetAbilityNames():
            self.BaseAbilities[key] = 0
            self.EnhancementAbilities[key] = 0
            self.InherentAbilities[key] = 0
            self.TempAbilities[key] = 0
            self.MiscAbilities[key] = 0
            self.PenaltyAbilities[key] = 0
        ability.GenerateRandomBase(self.BaseAbilities, method=ability.RandomMethod())

        self.BaseMaxHealth = 0
        self.TempBonusHealth = 0
        self.FCHealthUsed = 0
        self.CurrentDamage = 0
        self.NonLethalDamage = 0

        self.Classes = []  # List (Class, level). The first is the favored class

        ageMethod = self.Classes[0].AgeMethod if self.Classes else race.RandomAgeMethod()
        self.Age = self.Race.RandomAge(ageMethod)

        self.Experience = 0
        self.GrowthRate = growth.RandomRate()

        self.Effects = {}  # List of Effect name: effect

        # Effect changes. (Total Amount, Effect Types Dictionary (for stacking))
        # The effect type dictionary is as follows:
        #   Effect Type: List of (Effect Name, Amount)
        self.EffectNaturalArmorClass = []
        self.EffectArmorClass = []
        self.EffectFortitude = []
        self.EffectReflex = []
        self.EffectWill = []
        self.EffectAbilities = {}  # Dict of Ability Name: (Total Amount, Effect Type List)
        for key in ability.GetAbilityNames():
            self.EffectAbilities[key] = []
        self.EffectMeleeAttack = []
        self.EffectMeleeDamage = []
        self.EffectOffHandDamage = []
        self.EffectTwoHandDamage = []
        self.EffectRangedAttack = []
        self.EffectRangedDamage = []
        self.EffectTwoWeaponFightingExtraAttack = []
        self.EffectMeleeExtraAttack = []
        self.EffectRangedExtraAttack = []
        self.EffectSkillCheckAll = []
        self.EffectSkillCheck = {}  # Dict of Skill Name: (Total Amount, Effect Type List)
        for key in skill.GetSkillNames():
            self.EffectSkillCheck[key] = []
        self.EffectSizeChange = []
        self.EffectLandSpeed = []
        self.EffectFlySpeed = []
        self.EffectSwimSpeed = []
        self.EffectBurrowSpeed = []
        self.EffectClimbSpeed = []
        self.EffectSpeedMultiplierLand = []
        self.EffectSpeedMultiplierFly = []
        self.EffectSpeedMultiplierSwim = []
        self.EffectSpeedMultiplierBurrow = []
        self.EffectSpeedMultiplierClimb = []

        self.MiscArmorClass = 0
        self.MiscFlatFooted = 0
        self.MiscTouch = 0
        self.MiscCMD = 0
        self.MiscInititive = 0
        self.MiscFortitude = 0
        self.MiscReflex = 0
        self.MiscWill = 0
        self.MiscMeleeAttack = 0
        self.MiscRangedAttack = 0
        self.MiscCMB = 0
        self.MiscSkills = {}
        for key in skill.GetSkillNames():
            self.MiscSkills[key] = 0
        self.TempArmorClass = 0
        self.TempFlatFooted = 0
        self.TempTouch = 0
        self.TempCMD = 0
        self.TempInititive = 0
        self.TempFortitude = 0
        self.TempReflex = 0
        self.TempWill = 0
        self.TempMeleeAttack = 0
        self.TempRangedAttack = 0
        self.TempCMB = 0
        self.TempSkills = {}
        for key in skill.GetSkillNames():
            self.TempSkills[key] = 0
        self.LearnedFeats = []  # List of feats. Adding one hear should also add the appropriate effect

        self.Skills = {}  # Dict of SkillName: Ranks
        self.FeatSkills = {}  # Dict of SkillName: Ranks
        for key in skill.GetSkillNames():
            self.Skills[key] = [0, skill.SkillClasses[key](key)]
            self.FeatSkills[key] = 0

        self.FCSkillPointsUsed = 0

        self.HeroPoints = 0
        self.MaxHeroPoints = 0

        self.Weapons = []  # List of (Weapon, active)

        self.Armor = (None, False)  # Armor, active
        self.Shield = (None, False)  # Shield, active

        self.MagicalProtection = []  # List of (MagicalProtection, active)

        self.FlightManeuverability = config.MOVETYPE_AVERAGE
        self.MovementIgnoreArmor = config.MOVETYPE_NO_EFFECT
        self.RunMultiplier = 1
        self.BaseChargeRunBoost = 0

        self.DamageResistance = 0
        self.SpellResistance = 0
        self.FireResistance = 0
        self.ColdResistance = 0
        self.AcidResistance = 0
        self.ElectricityResistance = 0
        self.SonicResistance = 0

        self.Inventory = item.Inventory(self, item.RandomType())  # Items and Equipment

        self.ChooseInitialLanguagesBasedOnIntelligence()

    def CreateCustom(self, name, player, homeland=None, growth=None, armor=None, shield=None, magicalProtection=None, languages=None, skills=None, inventory=None, weapons=None, height=None, weight=None, hairColor=None, eyeColor=None, alignment=None, gender=None, age=None, diety=None, experience=0, abilities=None, race=None, classes=None, hitDieMethod=config.HIT_DIE_RANDOM):
        # self.CreateRandom()
        self.Name = name
        self.PlayerName = player
        if homeland:
            self.Homeland = homeland
        if armor:
            self.Armor = armor
        if shield:
            self.Sheild = shield
        if magicalProtection:
            self.MagicalProtection = magicalprotection
        if languages:
            self.Languages = languages
        if skills:
            self.Skills = skills
        if inventory:
            self.Inventory = inventory
        if weapons:
            self.Weapons = weapons
        if height:
            self.Height = height
        if weight:
            self.Weight = weight
        if hairColor:
            self.HairColor = hairColor
        if eyeColor:
            self.EyeColor = eyeColor
        if alignment:
            self.Alignment = alignment
        if gender:
            self.Gender = gender
        if age:
            self.Age = age
        if diety:
            self.Diety = diety
        if growth:
            self.Growth = growth
        if experience:
            self.Experience = experience
        if abilities:
            self.BaseAbilities = abilities
            self.StartingIntelligence = self.BaseAbilities[config.ABILITY_INTELLIGENCE]
        if race:
            self.Race = race
        if classes:
            self.Classes = classes
        if hitDieMethod is not None:
            self.CalculateMaxHP(hitDieMethod)

    def ToString(self):
        ret = ""
        ret += "Name:      {0:>18}\n".format(self.Name.title())
        ret += "Alignment: {0:>18}\n".format(str(self.Alignment))
        ret += "Race:      {0:>18}\n".format(self.Race.Name)
        ret += "Diety:     {0:>18}\n".format(self.Diety.title())
        ret += "Player:    {0:>18}\n".format(self.PlayerName.title())
        ret += "\n"
        ret += "Size:      {0:>18}\n".format(self.Size().Name)
        ret += "Gender:    {0:>18}\n".format(gender.String(self.Gender).title())
        ret += "Age:       {0:>18}\n".format(self.Age)
        ret += "Height:    {0:>15}{1:>3}\n".format(str(self.Height/12) + "'", str(self.Height % 12) + '"')
        ret += "Weight:    {0:>18}\n".format(str(self.Weight) + " lbs")
        ret += "Hair Color:{0:>18}\n".format(self.HairColor.name)
        ret += "Eye Color: {0:>18}\n".format(self.EyeColor.name)
        ret += "Homeland:  {0:>18}\n".format(self.Homeland.title())
        ret += "\n"
        ret += "Abilities\n"
        for key in ability.GetAbilityNames():
            name = ""
            if key == config.ABILITY_STRENGTH:
                name = "Strength"
            if key == config.ABILITY_DEXTERITY:
                name = "Dexterity"
            if key == config.ABILITY_CONSTITUTION:
                name = "Constitution"
            if key == config.ABILITY_INTELLIGENCE:
                name = "Intelligence"
            if key == config.ABILITY_WISDOM:
                name = "Wisdom"
            if key == config.ABILITY_CHARISMA:
                name = "Charisma"
            ret += "\t" + "{0:<13}".format(name+":") + "{0:>3} ({1:^3})\n".format(self.Abilities()[key], self.AbilityModifiers()[key])
        ret += "\n"
        ret += "HP:                {0:>4} /{1:>4}\n".format(self.CurrentHealth(), self.MaxHealth())
        ret += "Non Lethal Damage: {0:>10}\n".format(self.NonLethalDamage)
        ret += "\n"
        ret += "Classes\n"
        for c in self.Classes:
            ret += "\t{0:<18}{1:>3}\n".format(c[0].Name, c[1])
        ret += "Total Level: {0:<4}".format(self.Level())
        ret += "\n"
        ret += "Defense\n"
        ret += "\tArmor Class: {0:>4}\n".format(self.ArmorClass())
        ret += "\tFlat-Footed: {0:>4}\n".format(self.FlatFooted())
        ret += "\tTouch      : {0:>4}\n".format(self.Touch())
        ret += "\tCMD        : {0:>4}\n".format(self.CMD())
        ret += "\tSpell Fail : {0:>3}%\n".format(self.ArcaneSpellFailure())
        ret += "\tInitiative : {0:>4}\n".format(self.Initiative())
        ret += "\n"
        ret += "Saving Throws\n"
        ret += "\tFortitude: {0:>4}\n".format(self.Fortitude())
        ret += "\tReflex:    {0:>4}\n".format(self.Reflex())
        ret += "\tWill:      {0:>4}\n".format(self.Will())
        ret += "\n"
        ret += "Attacks\n"
        ret += "\tMelee:  {0:>4}\n".format(self.MeleeAttack())
        ret += "\tRanged: {0:>4}\n".format(self.RangedAttack())
        ret += "\tCMB:    {0:>4}\n".format(self.CMB())
        ret += "\n"
        ret += "Weapons\n"
        ret += "\t{0:^20}{1:^10}{2:^10}{3:^6}{4:^6}{5:^6}\n".format("Name", "Attacks", "Damage", "Crit", "Range", "Type")
        for w in range(len(self.Weapons)):
            weap, active = self.Weapons[w]
            if active:
                ret += "\t{0:<20}{1:>10}{2:>10}{3:>6}{4:>6}{5:>6}\n".format(weap.name + ":", self.GetWeaponAttack(w), self.GetWeaponDamage(w), weap.Crit, weap.Range, weap.Type)
        ret += "\n"
        ret += "Armor and Shield\n"
        if self.Armor[1]:
            ret += "\t{}".format(self.Armor[0].Name)
        if self.Shield[1]:
            ret += "\t{}".format(self.Shield[0].Name)
        ret += "\n"
        ret += "Magical Protection\n"
        for p in self.MagicalProtection:
            if p[1]:
                ret += "\t{}".format(p[0].name)
        ret += "\n"
        ret += "Skills\n"
        for key in skill.GetSkillNames():
            ret += "\t{0:<24}{1:>4}\n".format(self.Skills[key][1].Name + ":", self.Skills[key][1].GetTotal(self))
        ret += "Points: {0:>4} /{1:>4}".format(self.SkillPointsLeft(), self.TotalSkillPoints())

        ret += "\n"
        ret += "Languages"
        ret += "\t{}".format(", ".join(self.Languages))
        ret += "\n"
        ret += "Speeds\n"
        speeds = self.Speeds()
        ret += "\t        {0:^7}{1:^7}{2:^7}\n".format("Single", "Charge", "Run")
        ret += "\tLand:   {0:^7}{1:^7}{2:^7}\n".format(speeds[0][0], speeds[0][1], speeds[0][2])
        ret += "\tFly:    {0:^7}{1:^7}{2:^7}\n".format(speeds[1][0] if self.CanFly else 0, speeds[1][1] if self.CanFly else 0, speeds[1][2] if self.CanFly else 0)
        ret += "\tSwim:   {0:^7}{1:^7}{2:^7}\n".format(speeds[2][0] if self.CanSwim else 0, speeds[2][1] if self.CanSwim else 0, speeds[2][2] if self.CanSwim else 0)
        ret += "\tBurrow: {0:^7}{1:^7}{2:^7}\n".format(speeds[3][0] if self.CanBurrow else 0, speeds[3][1] if self.CanBurrow else 0, speeds[3][2] if self.CanBurrow else 0)
        ret += "\tClimb:  {0:^7}{1:^7}{2:^7}\n".format(speeds[4][0] if self.CanClimb else 0, speeds[4][1] if self.CanClimb else 0, speeds[4][2] if self.CanClimb else 0)
        ret += "\n"
        ret += "Resistances\n"
        ret += "\tDamage:  {0:>4}\n".format(self.DamageResistance)
        ret += "\tSpell:   {0:>4}\n".format(self.SpellResistance)
        ret += "\tFire:    {0:>4}\n".format(self.FireResistance)
        ret += "\tCold:    {0:>4}\n".format(self.ColdResistance)
        ret += "\tAcid:    {0:>4}\n".format(self.AcidResistance)
        ret += "\tElectric:{0:>4}\n".format(self.ElectricityResistance)
        ret += "\tSonic:   {0:>4}\n".format(self.SonicResistance)
        ret += "\n"
        ret += "Inventory:\n"
        inv = str(self.Inventory)
        for line in inv.split('\n'):
            ret += "\t" + line + '\n'
        ret += "\n"
        ret += "Spells\n"
        for c in self.Classes:
            ret += "\t{}\n".format(c[0].Name)
            if isinstance(c[0], characterclass.SpellcastingClass):
                sp = c[0].StringSpells()
                for line in sp.split("\n"):
                    ret += "\t\t" + line + "\n"
        return ret

    def ToJson(self):
        j = {}
        j['Id'] = self.uuid
        j['Name'] = self.Name
        j['Alignment'] = self.Alignment.ToJson()
        j['Race'] = self.Race.Name
        j['Languages'] = self.Languages
        j['LearnedFeats'] = [f.ToJson() for f in self.LearnedFeats]
        j['FeatsLeft'] = self.GetFeatsLeftToLearn()
        j['Diety'] = self.Diety
        j['PlayerName'] = self.PlayerName
        j['Gender'] = gender.String(self.Gender)
        j['Age'] = self.Age
        j['Size'] = self.Size().Name
        j['Height'] = self.Height
        j['Weight'] = self.Weight
        j['HairColor'] = self.HairColor.ToJson()
        j['EyeColor'] = self.EyeColor.ToJson()
        j['Homeland'] = self.Homeland
        j['Abilities'] = {}
        j['AbilityModifiers'] = {}
        for key in ability.GetAbilityNames():
            j['Abilities'][ability.GetAbilityName(key)] = self.Abilities()[key]
            j['AbilityModifiers'][ability.GetAbilityName(key)] = self.AbilityModifiers()[key]
        j['AbilityPointsLeft'] = self.AbilityPointsLeft()
        j['HP'] = self.CurrentHealth(), self.MaxHealth()
        j['NonLethalDamage'] = self.NonLethalDamage
        j['Classes'] = [{'Class': c[0].ToJson(), 'Level': c[1]} for c in self.Classes]
        j['ClassLevelsLeft'] = self.ClassLevelsLeft()
        j['Level'] = self.Level()
        j['ArmorClass'] = self.ArmorClass()
        j['ArmorClass'] = self.ArmorClass()
        j['FlatFooted'] = self.FlatFooted()
        j['Touch'] = self.Touch()
        j['CMD'] = self.CMD()
        j['ArcaneSpellFailure'] = self.ArcaneSpellFailure()
        j['Initiative'] = self.Initiative()
        j['Fortitude'] = self.Fortitude()
        j['Reflex'] = self.Reflex()
        j['Will'] = self.Will()
        j['MeleeAttack'] = self.MeleeAttack()
        j['RangedAttack'] = self.RangedAttack()
        j['CMB'] = self.CMB()
        j['Weapons'] = [{'Weapon': w[0].ToJson(), 'Active': w[1]} for w in self.Weapons]
        j['Armor'] = {'Armor': self.Armor[0], 'Active': self.Armor[1]}
        j['Shield'] = {'Shield': self.Shield[0], 'Active': self.Shield[1]}
        j['MagicalProtection'] = [{'MagicalProtection': p[0], 'Active': p[1]} for p in self.MagicalProtection]
        j['Skills'] = [{'SkillId': key, 'Skill': skill.GetSkillName(key), 'Description': skill.SkillClasses[key](key).GetWebInfo(), 'Ranks': self.Skills[key][0], 'Score': self.SkillScores()[key], 'Available': self.SkillIsAvailable()[key]} for key in skill.GetSkillNames()]
        j['SkillPointsLeft'] = self.SkillPointsLeft()
        j['TotalSkillPoints'] = self.TotalSkillPoints()
        j['Languages'] = self.Languages
        j['LanguagesLeft'] = self.GetLanguagesLeftToLearn()
        s = self.Speeds()
        j['Speeds'] = {
            'Land': {
                'Single': s[0][0],
                'Charge': s[0][1],
                'Run': s[0][2]
            },
            'Fly': {
                'Single': s[1][0],
                'Charge': s[1][1],
                'Run': s[1][2]
            },
            'Swim': {
                'Single': s[2][0],
                'Charge': s[2][1],
                'Run': s[2][2]
            },
            'Burrow': {
                'Single': s[3][0],
                'Charge': s[3][1],
                'Run': s[3][2]
            },
            'Climb': {
                'Single': s[4][0],
                'Charge': s[4][1],
                'Run': s[4][2]
            }
        }
        j['Resistances'] = {
            'Damage': self.DamageResistance,
            'Spell': self.SpellResistance,
            'Fire': self.FireResistance,
            'Cold': self.ColdResistance,
            'Acid': self.AcidResistance,
            'Electricity': self.ElectricityResistance,
            'Sonic': self.SonicResistance
        }
        j['Effects'] = []
        j['Encumberance'] = encumberance.GetEncumberanceString(encumberance.GetEncumberance(self))
        j['Growth'] = growth.GetGrowthString(self.GrowthRate)
        j['Experience'] = self.Experience
        j['NextLevelExperience'] = growth.GetStartingExperienceForLevel(self.GrowthRate, self.Level()+1)
        j['Encumberance'] = encumberance.GetEncumberanceString(encumberance.GetEncumberance(self))
        j['Inventory'] = self.Inventory.ToJson()
        j['Companions'] = [c.ToJson() for c in self.companions]
        return j
