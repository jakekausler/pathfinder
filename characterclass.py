# -*- coding: utf-8 -*-

import config
import ability
import roll
import skill
import spell


def GetClassNames():
    return [
        "Cleric",
        "Bard",
        "Barbarian",
        "Druid",
        "Rogue",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Sorcerer",
        "Wizard",
        "Alchemist",
        "Summoner",
        "Witch",
        "Inquisitor",
        "Oracle",
        "Antipaladin",
        "Magus",
        "Adept"
    ]


def GetClassName(n):
    if n == config.CLASS_CLERIC:
        return 'Cleric'
    if n == config.CLASS_BARD:
        return 'Bard'
    if n == config.CLASS_BARBARIAN:
        return 'Barbarian'
    if n == config.CLASS_DRUID:
        return 'Druid'
    if n == config.CLASS_ROGUE:
        return 'Rogue'
    if n == config.CLASS_FIGHTER:
        return 'Fighter'
    if n == config.CLASS_MONK:
        return 'Monk'
    if n == config.CLASS_PALADIN:
        return 'Paladin'
    if n == config.CLASS_RANGER:
        return 'Ranger'
    if n == config.CLASS_SORCERER:
        return 'Sorcerer'
    if n == config.CLASS_WIZARD:
        return 'Wizard'
    if n == config.CLASS_ALCHEMIST:
        return 'Alchemist'
    if n == config.CLASS_SUMMONER:
        return 'Summoner'
    if n == config.CLASS_WITCH:
        return 'Witch'
    if n == config.CLASS_INQUISITOR:
        return 'Inquisitor'
    if n == config.CLASS_ORACLE:
        return 'Oracle'
    if n == config.CLASS_ANTIPALADIN:
        return 'Antipaladin'
    if n == config.CLASS_MAGUS:
        return 'Magus'
    if n == config.CLASS_ADEPT:
        return 'Adept'
    return ''


def GetDomainNames():
    return [
        "Air",
        "Air (Cloud)",
        "Air (Wind)",
        "Animal",
        "Animal (Feather)",
        "Animal (Fur)",
        "Artifice",
        "Artifice (Construct)",
        "Artifice (Toil)",
        "Artifice (Trap)",
        "Chaos",
        "Chaos (Azata)",
        "Chaos (Demodand)",
        "Chaos (Demon)",
        "Chaos (Entropy)",
        "Chaos (Protean)",
        "Chaos (Revelry)",
        "Chaos (Whimsy)",
        "Charm",
        "Charm (Love)",
        "Charm (Lust)",
        "Community",
        "Community (Cooperation)",
        "Community (Family)",
        "Community (Home)",
        "Darkness",
        "Darkness (Loss)",
        "Darkness (Moon)",
        "Darkness (Night)",
        "Death",
        "Death (Murder)",
        "Death (Psychopomp)",
        "Death (Undead)",
        "Destruction",
        "Destruction (Catastrophe)",
        "Destruction (Hatred)",
        "Destruction (Rage)",
        "Destruction (Torture)",
        "Earth",
        "Earth (Caves)",
        "Earth (Metal)",
        "Earth (Radiation)",
        "Evil",
        "Evil (Cannibalism)",
        "Evil (Corruption)",
        "Evil (Daemon)",
        "Evil (Demodand)",
        "Evil (Demon)",
        "Evil (Devil)",
        "Evil (Fear)",
        "Evil (Kyton)",
        "Fire",
        "Fire (Arson)",
        "Fire (Ash)",
        "Fire (Smoke)",
        "Glory",
        "Glory (Heroism)",
        "Glory (Honor)",
        "Good",
        "Good (Agathion)",
        "Good (Archon)",
        "Good (Azata)",
        "Good (Friendship)",
        "Good (Redemption)",
        "Healing",
        "Healing (Restoration)",
        "Healing (Resurrection)",
        "Knowledge",
        "Knowledge (Aeon)",
        "Knowledge (Memory)",
        "Knowledge (Thought)",
        "Law",
        "Law (Archon)",
        "Law (Devil)",
        "Law (Inevitable)",
        "Law (Judgment)",
        "Law (Kyton)",
        "Law (Loyalty)",
        "Law (Slavery)",
        "Law (Tyranny)",
        "Liberation",
        "Liberation (Freedom)",
        "Liberation (Revolution)",
        "Luck",
        "Luck (Curse)",
        "Luck (Fate)",
        "Luck (Imagination)",
        "Madness",
        "Madness (Insanity)",
        "Madness (Nightmare)",
        "Magic",
        "Magic (Arcane)",
        "Magic (Divine)",
        "Nobility",
        "Nobility (Aristocracy)",
        "Nobility (Leadership)",
        "Nobility (Martyr)",
        "Plant",
        "Plant (Decay)",
        "Plant (Growth)",
        "Protection",
        "Protection (Defense)",
        "Protection (Purity)",
        "Protection (Solitude)",
        "Repose",
        "Repose (Ancestors)",
        "Repose (Psychopomp)",
        "Repose (Souls)",
        "Ruins",
        "Rune",
        "Rune (Language)",
        "Rune (Wards)",
        "Scalykind",
        "Scalykind (Dragon)",
        "Scalykind (Saurian)",
        "Scalykind (Venom)",
        "Strength",
        "Strength (Ferocity)",
        "Strength (Fist)",
        "Strength (Resolve)",
        "Sun",
        "Sun (Day)",
        "Sun (Light)",
        "Sun (Revelation)",
        "Travel",
        "Travel (Exploration)",
        "Travel (Trade)",
        "Trickery",
        "Trickery (Ambush)",
        "Trickery (Deception)",
        "Trickery (Greed)",
        "Trickery (Innuendo)",
        "Trickery (Thievery)",
        "Vermin",
        "Void",
        "Void (Dark Tapestry)",
        "Void (Isolation)",
        "Void (Stars)",
        "War",
        "War (Blood)",
        "War (Tactics)",
        "Water",
        "Water (Flotsam)",
        "Water (Flowing)",
        "Water (Ice)",
        "Water (Oceans)",
        "Water (Rivers)",
        "Weather",
        "Weather (Seasons)",
        "Weather (Storms)"
    ]


class CharacterClass(object):
    Name = ""
    Type = config.NONE
    HitDie = roll.Dice(1)
    BAB = 1.0
    Fortitude = config.SAVE_SCORE_GOOD
    Reflex = config.SAVE_SCORE_GOOD
    Will = config.SAVE_SCORE_GOOD
    Skills = 0

    def __init__(self, character, characterClassIdx=0):
        self.Character = character
        self.CharacterClassIdx = characterClassIdx

    def ClassSkill(self, s):
        return False

    def ClassLevel(self):
        return self.Character.Classes[self.CharacterClassIdx][1]

    def ToJson(self):
        j = {}
        j['Type'] = self.Name
        j['Spellcaster'] = False
        return j


class SpellcastingClass(CharacterClass):
    Spellcasting = config.NONE
    SpellsPerDay = config.NONE_SPD
    SpellsKnown = config.NONE_SK
    MustPrepare = False
    UseDivineComponent = False
    UseDomain = False

    def __init__(self, character, characterClassIdx=0):
        super(SpellcastingClass, self).__init__(character, characterClassIdx)
        self.KnownSpells = [[] for i in range(10)]  # Per level, list of spells known. Empty if knows all
        self.PreparedSpells = [[] for i in range(10)]  # Per level, list of [spell, uses]
        self.UsedSpells = [0 for i in range(10)]

    def GetNumSpellsKnown(self, level):
        return self.SpellsKnown[self.ClassLevel()-1][level]

    def GetNumSpellsToLearn(self, level):
        return self.GetNumSpellsKnown(level) - len(self.KnownSpells[level])

    def GetKnownSpells(self, level=-1):
        if level >= 0:
            return self.KnownSpells[level]
        return self.KnownSpells

    def GetNumSpellsToPrepare(self, level):
        return self.NumSpellsPerDay(level) - sum(i[1] for i in self.GetPreparedSpells(level))

    def GetPreparedSpells(self, level=-1):
        if level >= 0:
            return self.PreparedSpells[level]
        return self.PreparedSpells

    def LearnSpell(self, sp):
        if self.CanLearnSpell(sp):
            self.KnownSpells[sp.GetSpellLevel(self)].append(sp)

    def ReplaceLearnedSpell(self, oldSpellIdx, newSpell, oldSpellLevel=-1):
        if oldSpellLevel == -1:
            oldSpellLevel = newSpell.GetSpellLevel(self)
        self.ForgetSpell(oldSpellIdx, oldSpellLevel)
        self.LearnSpell(newSpell)

    def ForgetSpell(self, spLevel, spIdx):
        del self.KnownSpells[spLevel][spIdx]

    def RemoveSpell(self, spLevel, spIdx):
        if self.MustPrepare:
            del self.PreparedSpells[spLevel][spIdx]
        else:
            del self.KnownSpells[spLevel][spIdx]

    def PrepareSpell(self, sp, uses):
        if self.CanPrepareSpell(sp, uses):
            self.PreparedSpells[sp.GetSpellLevel(self)].append([sp, uses])

    def PrepareExistingSpell(self, level, spellIdx, uses):
        if uses <= self.GetNumSpellsToPrepare(level):
            self.PreparedSpells[level][spellIdx][1] += uses

    def UseSpell(self, spLevel, spIdx, uses):
        if self.CanUseSpell(spLevel, spIdx, uses):
            if self.MustPrepare:
                self.PreparedSpells[spLevel][spIdx][1] -= uses
            self.UsedSpells[spLevel] += uses

    def CanPrepareSpell(self, sp, uses):
        return sp.GetSpellLevel(self) >= 0 and self.GetNumSpellsToPrepare(sp.GetSpellLevel(self)) >= uses and not self.IsPrepared(sp)

    def UnPrepareSpell(self, spLevel, spIdx, uses=-1):
        if uses >= 0:
            self.PreparedSpells[spLevel][spIdx][1] = max(0, self.PreparedSpells[spLevel][spIdx][1] - uses)
        else:
            self.PreparedSpells[spLevel][spIdx][1] = 0

    def UnPrepareSpells(self, level=-1):
        if level == -1:
            for l in range(0, 10):
                self.UnPrepareSpells(l)
        else:
            for i in range(len(self.PreparedSpells[level])):
                self.UnPrepareSpell(level, i, -1)

    def ShouldStringLevel(self, level):
        return True

    def ResetDay(self, level=-1):
        if level == -1:
            for i in range(10):
                self.ResetDay(i)
        else:
            if self.MustPrepare:
                self.UnPrepareSpells(level)
            self.UsedSpells[level] = 0

    def GetDailyUsagesLeft(self, level):
        if self.NumSpellsPerDay(level) < 0:
            return self.NumSpellsPerDay(level)
        return self.NumSpellsPerDay(level) - self.UsedSpells[level]

    def CanLearnSpell(self, sp):
        return sp.GetSpellLevel(self) >= 0 and self.GetNumSpellsToLearn(sp.GetSpellLevel(self)) > 0 and not self.IsKnown(sp)

    def CanUseSpell(self, sp, uses):
        lev = sp.GetSpellLevel(self)
        if lev < 0:
            return False
        return (self.GetDailyUsagesLeft(lev) >= uses or self.GetDailyUsagesLeft(lev) == config.INFINITY) and (not self.MustPrepare or self.IsPrepared(sp))

    def IsPrepared(self, sp):
        return any(sp == i[0] for i in self.PreparedSpells[sp.GetSpellLevel(self)])

    def IsKnown(self, sp):
        return any(sp == i for i in self.KnownSpells[sp.GetSpellLevel(self)])

    def NumSpellsPerDay(self, level):
        spd = self.SpellsPerDay[self.ClassLevel()-1][level]
        mod = config.SpellModifiers[self.Character.AbilityModifiers()[self.Spellcasting]][level] if self.Spellcasting != config.NONE else 0
        if mod < 0:
            spd = 0
        elif spd >= 0:
            spd += mod
        return spd

    def StringSpellsPerDay(self, level):
        spd = self.NumSpellsPerDay(level)
        if spd == config.INFINITY:
            spd = "∞"
        return str(spd) + " Left"

    def StringSpells(self):
        ret = ""
        for i in range(10):
            if (self.ShouldStringLevel(i)):
                ret += "Level {0:>2} ({1})\n".format(i, self.StringSpellsPerDay(i))
                for s in self.GetKnownSpells(i):
                    ret += "\t{0}\n".format(s.ToString(self.ClassLevel()))
        return ret[:-1]

    def GetValidSpells(self, level):
        ret = []
        for s in spell.GetValidSpells(self.Character, self.CharacterClassIdx, level):
            if self.CanLearnSpell(s):
                ret.append(s)
        return ret

    def GetValidSpellsJson(self, level):
        return [s.ToJson(self.ClassLevel(), self.Character.AbilityModifiers()[self.Spellcasting], s.GetSpellLevel(self), self.Type) for s in self.GetValidSpells(level)]

    def ToJson(self):
        j = super(SpellcastingClass, self).ToJson()
        j['LeftToLearn'] = [0 for i in range(10)]
        j['LeftToPrepare'] = [0 for i in range(10)]
        for i in range(10):
            j['LeftToLearn'][i] = self.GetNumSpellsToLearn(i)
            j['LeftToPrepare'][i] = self.GetNumSpellsToPrepare(i)
        j['Spellcaster'] = True
        j['UseDomain'] = self.UseDomain
        j['MustPrepare'] = self.MustPrepare
        j['SpellsPerDay'] = [self.GetDailyUsagesLeft(i) for i in range(10)]
        j['PreparedSpells'] = [[{'Spell': s[0].ToJson(self.ClassLevel(), self.Character.AbilityModifiers()[self.Spellcasting], s[0].GetSpellLevel(self), self.Type), 'Uses': s[1]} for s in self.GetPreparedSpells(i)] for i in range(10)]
        j['KnownSpells'] = [[s.ToJson(self.ClassLevel(), self.Character.AbilityModifiers()[self.Spellcasting], s.GetSpellLevel(self), self.Type) for s in self.GetKnownSpells(i)] for i in range(10)]
        j['UseDivineComponent'] = self.UseDivineComponent
        return j


class Cleric(SpellcastingClass):
    Name = "Cleric"
    Type = config.CLASS_CLERIC
    HitDie = roll.Dice(8)
    BAB = 0.75
    Fortitude = config.SAVE_SCORE_GOOD
    Reflex = config.SAVE_SCORE_POOR
    Will = config.SAVE_SCORE_GOOD
    Skills = 2
    Spellcasting = config.ABILITY_WISDOM
    SpellsPerDay = config.PREPARED_PRIMARY_SPD
    SpellsKnown = config.DIVINE_SK
    DomainSpellsPerDay = config.CLERIC_DOMAIN_SPD
    MustPrepare = True
    UseDivineComponent = True
    UseDomain = True

    def __init__(self, character, characterClassIdx=0):
        super(Cleric, self).__init__(character, characterClassIdx)
        self.DomainSpells = [[] for i in range(10)]
        self.Domains = []

    def ClassSkill(self, s):
        skills = [
                    config.SKILL_APPRAISE,
                    config.SKILL_CRAFT1,
                    config.SKILL_CRAFT2,
                    config.SKILL_DIPLOMACY,
                    config.SKILL_HEAL,
                    config.SKILL_KNOWLEDGE_ARCANA,
                    config.SKILL_KNOWLEDGE_HISTORY,
                    config.SKILL_KNOWLEDGE_NOBILITY,
                    config.SKILL_KNOWLEDGE_PLANES,
                    config.SKILL_KNOWLEDGE_RELIGION,
                    config.SKILL_LINGUISTICS,
                    config.SKILL_PROF1,
                    config.SKILL_PROF2,
                    config.SKILL_SENSE_MOTIVE,
                    config.SKILL_SPELLCRAFT
                    ]
        if config.DOMAIN_KNOWLEDGE in self.Domains:
            skills += [
                        config.SKILL_KNOWLEDGE_DUNGEONEERING,
                        config.SKILL_KNOWLEDGE_ENGINEERING,
                        config.SKILL_KNOWLEDGE_GEOGRAPHY,
                        config.SKILL_KNOWLEDGE_LOCAL,
                        config.SKILL_KNOWLEDGE_NATURE
            ]

    def AddDomain(self, domain):
        self.Domains.append(domain)

    def RemoveDomain(self, domain):
        for i in range(len(self.Domains)):
            if self.Domains[i] == domain:
                del self.Domains[i]
                break

    def GetValidSpells(self, level):
        ret = []
        for s in spell.GetValidSpells(self.Character, self.CharacterClassIdx, level, self.Domains):
            if self.CanPrepareSpell(s, 1, s.IsDomainSpell) or self.CanPrepareSpell(s, 1):
                ret.append(s)
        return ret

    def ShouldStringLevel(self, level):
        return len(self.GetPreparedSpells(level)) > 0 or self.GetNumSpellsToPrepare(level) > 0 or self.NumDomainSpellsPerDay(level) > 0

    def NumDomainSpellsPerDay(self, level):
        return self.DomainSpellsPerDay[self.ClassLevel()-1][level]

    def NumDomainSpellsPerDayLeft(self, level):
        return self.DomainSpellsPerDay(self.ClassLevel()-1) - self.NumDomainSpellsUsed(level)

    def NumDomainSpellsUsed(self, level):
        return sum(i[1] for i in self.GetDomainSpells(level))

    def GetNumSpellsToPrepareDomain(self, level):
        return self.NumDomainSpellsPerDay(level) - self.NumDomainSpellsUsed(level)

    def GetDomainSpells(self, level):
        return self.DomainSpells[level]

    def GetDailyUsagesLeft(self, level):
        if self.NumSpellsPerDay(level) < 0:
            return self.NumSpellsPerDay(level)
        if level == 0:
            return config.INFINITY
        return super(Cleric, self).GetDailyUsagesLeft(level) + self.GetNumSpellsToPrepareDomain(level)

    def RemoveSpell(self, spLevel, spIdx, domain=False):
        if domain:
            del self.DomainSpells[spLevel][spIdx]
        else:
            if self.MustPrepare:
                del self.PreparedSpells[spLevel][spIdx]
            else:
                del self.KnownSpells[spLevel][spIdx]

    def PrepareSpell(self, sp, uses, domain=False):
        if self.CanPrepareSpell(sp, uses, domain):
            if domain:
                self.DomainSpells[sp.GetSpellLevel(self)].append([sp, uses])
            else:
                self.PreparedSpells[sp.GetSpellLevel(self)].append([sp, uses])

    def PrepareExistingSpell(self, level, spellIdx, uses, domain=False):
        if domain:
            if uses <= self.GetNumSpellsToPrepareDomain(level):
                print level, spellIdx, uses
                self.DomainSpells[level][spellIdx][1] += uses
        else:
            super(Cleric, self).PrepareExistingSpell(level, spellIdx, uses)

    def CanPrepareSpell(self, sp, uses, domain=False):
        if domain:
            return sp.GetSpellLevel(self, domains=self.Domains) >= 0 and self.GetNumSpellsToPrepare(sp.GetSpellLevel(self, self.Domains)) >= uses and not self.IsPrepared(sp)
        else:
            return super(Cleric, self).CanPrepareSpell(sp, uses)

    def UseSpell(self, spLevel, spIdx, uses, domain=False):
        if spLevel == 0:
            return
        if self.CanUseSpell(spLevel, spIdx, uses, domain):
            if domain:
                self.DomainSpells[spLevel][spIdx][1] -= uses
            else:
                self.PreparedSpells[spLevel][spIdx][1] -= uses
            self.UsedSpells[spLevel] += uses

    def CanUseSpell(self, spLevel, spIdx, uses, domain=False):
        if domain:
            if not self.DomainSpells[spLevel] or not self.DomainSpells[spLevel][spIdx]:
                return False
            lev = self.DomainSpells[spLevel][spIdx].GetSpellLevel(self, domains=self.Domains)
            if lev < 0:
                return False
            return (self.GetDailyUsagesLeft(lev) >= uses or self.GetDailyUsagesLeft(lev) == config.INFINITY) and (not self.MustPrepare or self.IsPrepared(sp))
        else:
            return super(Cleric, self).CanUseSpell(self.PreparedSpells[spLevel][spIdx][0], uses)

    def IsPrepared(self, sp, domain=False):
        return any(sp == i[0] for i in self.PreparedSpells[sp.GetSpellLevel(self)]) or any(sp == i[0] for i in self.DomainSpells[sp.GetSpellLevel(self)])

    def UnPrepareSpell(self, spLevel, spIdx, uses=-1, domain=False):
        if domain:
            if uses >= 0:
                self.DomainSpells[spLevel][spIdx][1] = max(0, self.DomainSpells[spLevel][spIdx][0] - uses)
            else:
                self.DomainSpells[spLevel][spIdx][1] = 0
        else:
            super(Cleric, self).UnPrepareSpell(spLevel, spIdx, uses)

    def UnPrepareSpells(self, level):
        if level == -1:
            for i in range(0, 10):
                self.UnPrepareSpells(i)
        else:
            for i in range(len(self.DomainSpells[level])):
                self.UnPrepareSpell(level, i, -1, True)
            super(Cleric, self).UnPrepareSpells(level)

    def ResetDay(self, level=-1):
        self.UnPrepareSpells(level)
        super(Cleric, self).ResetDay(level)

    def StringSpellsPerDay(self, level):
        ret = super(Cleric, self).StringSpellsPerDay(level)
        domainSpd = str(self.NumDomainSpellsPerDayLeft(level))
        return ret[:ret.find(" ")] + " Non-Domain Uses Left" + ", " + domainSpd + " Domain Uses Left"

    def StringSpells(self):
        ret = ""
        for i in range(10):
            if (self.ShouldStringLevel(i)):
                ret += "Level {0:>2} ({1})\n".format(i, self.StringSpellsPerDay(i))
                for sp in self.GetPreparedSpells(i):
                    ret += "\t ({0:>2} Uses Left) {1}\n".format(sp[1], sp[0].ToString(self.ClassLevel()))
                for sp in self.GetDomainSpells(i):
                    ret += "\t*({0:>2} Uses Left) {1}\n".format(sp[1], sp[0].ToString(self.ClassLevel()))
        return ret[:-1]

    def ToJson(self):
        j = super(Cleric, self).ToJson()
        j['LeftToPrepareDomain'] = [0 for i in range(10)]
        for i in range(10):
            j['LeftToPrepareDomain'][i] = self.GetNumSpellsToPrepareDomain(i)
        j['DomainSpells'] = [[{'Spell': s[0].ToJson(self.ClassLevel(), self.Character.AbilityModifiers()[self.Spellcasting], s[0].GetSpellLevel(self), self.Type, self.Domains), 'Uses': s[1]} for s in self.GetDomainSpells(i)] for i in range(10)]
        return j


class Sorcerer(SpellcastingClass):
    Name = "Sorcerer"
    Type = config.CLASS_SORCERER
    HitDie = roll.Dice(6)
    BAB = 0.5
    Fortitude = config.SAVE_SCORE_POOR
    Reflex = config.SAVE_SCORE_POOR
    Will = config.SAVE_SCORE_GOOD
    Skills = 2
    Spellcasting = config.ABILITY_CHARISMA
    SpellsPerDay = config.SPONTANEOUS_PRIMARY_SPD
    SpellsKnown = config.SPONTANEOUS_PRIMARY_SK
    BloodlineSpells = config.BLOODLINE_SPELLS

    def __init__(self, character, characterClassIdx=0):
        super(Sorcerer, self).__init__(character, characterClassIdx)
        self.ReplacedSpells = 0

    def ClassSkill(self, s):
        return s in [
                    config.SKILL_APPRAISE,
                    config.SKILL_BLUFF,
                    config.SKILL_CRAFT1,
                    config.SKILL_CRAFT2,
                    config.SKILL_FLY,
                    config.SKILL_INTIMIDATE,
                    config.SKILL_KNOWLEDGE_ARCANA,
                    config.SKILL_PROF1,
                    config.SKILL_PROF2,
                    config.SKILL_SPELLCRAFT,
                    config.SKILL_USE_MAGIC_DEVICE
                    ]

    def StringSpellsPerDay(self, level):
        ret = super(Sorcerer, self).StringSpellsPerDay(level)
        numToLearn = str(self.GetNumSpellsToLearn(level))
        return ret + ", Can Learn " + numToLearn + " More)"

    def ShouldStringLevel(self, level):
        return len(self.GetKnownSpells(level)) > 0 or self.GetNumSpellsToLearn(level) > 0

    def GetNumSpellsKnown(self, level):
        return super(Sorcerer, self).GetNumSpellsKnown(level) - self.ReplacedSpells + config.BLOODLINE_SPELLS[self.ClassLevel()-1]

    def CanUseSpell(self, spLevel, spIdx, uses):
        return super(Sorcerer, self).CanUseSpell(self.KnownSpells[spLevel][spIdx], uses)
