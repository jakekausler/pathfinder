
import unittest

import random

import character
import alignment
import color
import race
import growth
import gender
import ability
import skill
import characterclass
import item
import spell

import format_spells


class HaltingTestCase(unittest.TestCase):

    def run(self, result=None):
        if not result.errors:
            super(HaltingTestCase, self).run(result)


class TestCharacter(HaltingTestCase):

    def test_01_create(self):
        character.Character()

    def test_02_Size(self):
        char = character.Character()
        char.Size()

    def test_03_AgeType(self):
        char = character.Character()
        char.AgeType()

    def test_04_MaxHealth(self):
        char = character.Character()
        char.MaxHealth()

    def test_05_CurrentHealth(self):
        char = character.Character()
        char.CurrentHealth()

    def test_06_Damage(self):
        char = character.Character()
        char.Damage()

    def test_07_CheckNonLethalDamage(self):
        char = character.Character()
        char.CheckNonLethalDamage()

    def test_08_CheckDamage(self):
        char = character.Character()
        char.CheckDamage()

    def test_09_Harm(self):
        char = character.Character()
        char.Harm(10)

    def test_10_Kill(self):
        char = character.Character()
        char.Kill()

    def test_11_Resurrect(self):
        char = character.Character()
        char.Resurrect()

    def test_12_AddEffect(self):
        char = character.Character()
        char.AddEffect()

    def test_13_RemoveEffect(self):
        char = character.Character()
        char.RemoveEffect()

    def test_14_Abilities(self):
        char = character.Character()
        char.Abilities()

    def test_15_AbilityModifiers(self):
        char = character.Character()
        char.AbilityModifiers()

    def test_16_Level(self):
        char = character.Character()
        char.Level()

    def test_17_ClassBAB(self):
        char = character.Character()
        char.ClassBAB()

    def test_18_ClassFortitude(self):
        char = character.Character()
        char.ClassFortitude()

    def test_19_ClassReflex(self):
        char = character.Character()
        char.ClassReflex()

    def test_20_ClassWill(self):
        char = character.Character()
        char.ClassWill()

    def test_21_ClassSkillPoints(self):
        char = character.Character()
        char.ClassSkillPoints()

    def test_22_GetEffectScoreByType(self):
        char = character.Character()
        char.GetEffectScoreByType()

    def test_23_ArmorClass(self):
        char = character.Character()
        char.ArmorClass()

    def test_24_FlatFooted(self):
        char = character.Character()
        char.FlatFooted()

    def test_25_Touch(self):
        char = character.Character()
        char.Touch()

    def test_26_CMD(self):
        char = character.Character()
        char.CMD()

    def test_27_MaxDexBonus(self):
        char = character.Character()
        char.MaxDexBonus()

    def test_28_ArcaneSpellFailure(self):
        char = character.Character()
        char.ArcaneSpellFailure()

    def test_29_Initiative(self):
        char = character.Character()
        char.Initiative()

    def test_30_FavoredClassPointsLeft(self):
        char = character.Character()
        char.FavoredClassPointsLeft()

    def test_31_TotalSkillPoints(self):
        char = character.Character()
        char.TotalSkillPoints()

    def test_32_SkillPointsLeft(self):
        char = character.Character()
        char.SkillPointsLeft()

    def test_33_SkillScores(self):
        char = character.Character()
        char.SkillScores()

    def test_34_ArmorCheckPenalty(self):
        char = character.Character()
        char.ArmorCheckPenalty()

    def test_35_Fortitude(self):
        char = character.Character()
        char.Fortitude()

    def test_36_Reflex(self):
        char = character.Character()
        char.Reflex()

    def test_37_Will(self):
        char = character.Character()
        char.Will()

    def test_38_MeleeAttack(self):
        char = character.Character()
        char.MeleeAttack()

    def test_39_RangedAttack(self):
        char = character.Character()
        char.RangedAttack()

    def test_40_CMB(self):
        char = character.Character()
        char.CMB()

    def test_41_Speeds(self):
        char = character.Character()
        char.Speeds()

    def test_42_GetWeaponDamage(self):
        char = character.Character()
        char.GetWeaponDamage(-1)

    def test_43_GetWeaponAttack(self):
        char = character.Character()
        char.GetWeaponAttack(-1)

    def test_44_IsClassSkill(self):
        char = character.Character()
        char.IsClassSkill(0)

    def test_45_Reset(self):
        char = character.Character()
        char.Reset()

    def test_46_CreateRandom(self):
        char = character.Character()
        char.CreateRandom()

    def test_47_CreateCustom(self):
        char = character.Character()
        char.CreateCustom("Bilborn Tantix",
                          "Jake Kausler",
                          homeland='Sas Arkan',
                          growth=growth.MEDIUM,
                          armor=None,
                          shield=None,
                          magicalProtection=None,
                          languages=['Common', 'Sylvan', 'Gnome', 'Orc', 'Goblin', 'Giant', 'Celestial'],
                          skills={
                              skill.ACROBATICS: [0, skill.SkillClasses[skill.ACROBATICS](skill.ACROBATICS)],
                              skill.APPRAISE: [0, skill.SkillClasses[skill.APPRAISE](skill.APPRAISE)],
                              skill.BLUFF: [0, skill.SkillClasses[skill.BLUFF](skill.BLUFF)],
                              skill.CLIMB: [0, skill.SkillClasses[skill.CLIMB](skill.CLIMB)],
                              skill.CRAFT1: [1, skill.SkillClasses[skill.CRAFT1](skill.CRAFT1)],
                              skill.CRAFT2: [0, skill.SkillClasses[skill.CRAFT2](skill.CRAFT2)],
                              skill.DIPLOMACY: [3, skill.SkillClasses[skill.DIPLOMACY](skill.DIPLOMACY)],
                              skill.DISABLE_DEVICE: [0, skill.SkillClasses[skill.DISABLE_DEVICE](skill.DISABLE_DEVICE)],
                              skill.DISGUISE: [0, skill.SkillClasses[skill.DISGUISE](skill.DISGUISE)],
                              skill.ESCAPE_ARTIST: [0, skill.SkillClasses[skill.ESCAPE_ARTIST](skill.ESCAPE_ARTIST)],
                              skill.FLY: [0, skill.SkillClasses[skill.FLY](skill.FLY)],
                              skill.HANDLE_ANIMAL: [1, skill.SkillClasses[skill.HANDLE_ANIMAL](skill.HANDLE_ANIMAL)],
                              skill.HEAL: [3, skill.SkillClasses[skill.HEAL](skill.HEAL)],
                              skill.INTIMIDATE: [1, skill.SkillClasses[skill.INTIMIDATE](skill.INTIMIDATE)],
                              skill.KNOWLEDGE_ARCANA: [3, skill.SkillClasses[skill.KNOWLEDGE_ARCANA](skill.KNOWLEDGE_ARCANA)],
                              skill.KNOWLEDGE_DUNGEONEERING: [0, skill.SkillClasses[skill.KNOWLEDGE_DUNGEONEERING](skill.KNOWLEDGE_DUNGEONEERING)],
                              skill.KNOWLEDGE_ENGINEERING: [0, skill.SkillClasses[skill.KNOWLEDGE_ENGINEERING](skill.KNOWLEDGE_ENGINEERING)],
                              skill.KNOWLEDGE_GEOGRAPHY: [0, skill.SkillClasses[skill.KNOWLEDGE_GEOGRAPHY](skill.KNOWLEDGE_GEOGRAPHY)],
                              skill.KNOWLEDGE_HISTORY: [1, skill.SkillClasses[skill.KNOWLEDGE_HISTORY](skill.KNOWLEDGE_HISTORY)],
                              skill.KNOWLEDGE_LOCAL: [0, skill.SkillClasses[skill.KNOWLEDGE_LOCAL](skill.KNOWLEDGE_LOCAL)],
                              skill.KNOWLEDGE_NATURE: [0, skill.SkillClasses[skill.KNOWLEDGE_NATURE](skill.KNOWLEDGE_NATURE)],
                              skill.KNOWLEDGE_NOBILITY: [0, skill.SkillClasses[skill.KNOWLEDGE_NOBILITY](skill.KNOWLEDGE_NOBILITY)],
                              skill.KNOWLEDGE_PLANES: [0, skill.SkillClasses[skill.KNOWLEDGE_PLANES](skill.KNOWLEDGE_PLANES)],
                              skill.KNOWLEDGE_RELIGION: [3, skill.SkillClasses[skill.KNOWLEDGE_RELIGION](skill.KNOWLEDGE_RELIGION)],
                              skill.LINGUISTICS: [1, skill.SkillClasses[skill.LINGUISTICS](skill.LINGUISTICS)],
                              skill.PERCEPTION: [1, skill.SkillClasses[skill.PERCEPTION](skill.PERCEPTION)],
                              skill.PERFORM1: [2, skill.SkillClasses[skill.PERFORM1](skill.PERFORM1)],
                              skill.PERFORM2: [2, skill.SkillClasses[skill.PERFORM2](skill.PERFORM2)],
                              skill.PROF1: [1, skill.SkillClasses[skill.PROF1](skill.PROF1)],
                              skill.PROF2: [1, skill.SkillClasses[skill.PROF2](skill.PROF2)],
                              skill.RIDE: [4, skill.SkillClasses[skill.RIDE](skill.RIDE)],
                              skill.SENSE_MOTIVE: [1, skill.SkillClasses[skill.SENSE_MOTIVE](skill.SENSE_MOTIVE)],
                              skill.SLEIGHT_OF_HAND: [0, skill.SkillClasses[skill.SLEIGHT_OF_HAND](skill.SLEIGHT_OF_HAND)],
                              skill.SPELLCRAFT: [1, skill.SkillClasses[skill.SPELLCRAFT](skill.SPELLCRAFT)],
                              skill.STEALTH: [0, skill.SkillClasses[skill.STEALTH](skill.STEALTH)],
                              skill.SURVIVAL: [0, skill.SkillClasses[skill.SURVIVAL](skill.SURVIVAL)],
                              skill.SWIM: [0, skill.SkillClasses[skill.SWIM](skill.SWIM)],
                              skill.USE_MAGIC_DEVICE: [0, skill.SkillClasses[skill.USE_MAGIC_DEVICE](skill.USE_MAGIC_DEVICE)]
                          },
                          inventory=None,
                          weapons=None,
                          height=41,
                          weight=43,
                          hairColor=color.BLUE,
                          eyeColor=color.GREEN,
                          alignment=alignment.Alignment(alignment.GOOD, alignment.NEUTRAL),
                          gender=gender.MALE,
                          age=71,
                          diety='Qi Zhong',
                          experience=33740,
                          abilities={
                              ability.STRENGTH: 10,
                              ability.DEXTERITY: 7,
                              ability.CONSTITUTION: 9,
                              ability.INTELLIGENCE: 16,
                              ability.WISDOM: 15,
                              ability.CHARISMA: 17
                          },
                          race=race.Gnome(),
                          classes=[
                              (characterclass.Cleric(char, 0), 5),
                              (characterclass.Sorcerer(char, 1), 1)
                          ],
                          hitDieMethod=character.AVERAGE,
                          withCompanion=True
                          )
        char.AddLeveledAbility(ability.DEXTERITY, 1)
        char.AddFavoredClassSkill(skill.RIDE, 3)
        char.AddFavoredClassHP(2)
        char.AddGold(2956.45)
        char.AddItem(item.Item("Spell Component Pouch", 2, 5), 1)
        char.AddItem(item.Item("Holy Symbol, Wooden", 0, 1), 1)
        char.AddItem(item.Item("Healer's Kit", 1, 50), 1)
        char.AddItem(item.Item("Backpack", 2, 2), 1)
        char.AddItem(item.Item("Pouch (Belt)", 1, 1), 1)
        char.AddItem(item.Item("Sack", 1, 0.1), 1)
        char.AddItem(item.Item("Bucket", 2, 0.5), 1)
        char.AddItem(item.Item("Lantern 15ft+15ft", 1, 0.1), 1)
        char.AddItem(item.Item("Oil, One Pint Flask", 1, 0.1), 5)
        char.AddItem(item.Item("Waterskin, Filled", 4, 1), 1)
        char.AddItem(item.Item("Ration  Per Day", 1, 0.5), 4)
        char.AddItem(item.Item("Bedroll", 5, 0.1), 1)
        char.AddItem(item.Item("Blanket", 3, 0.5), 1)
        char.AddItem(item.Item("Silk Rope", 5, 10), 1)
        char.AddItem(item.Item("Mirror", 1, 10), 1)
        char.AddItem(item.Item("Wistle, signal", 0, 0.8), 1)
        char.AddItem(item.Item("Compass", 0.5, 10), 1)
        char.AddItem(item.Item("Dagger", 1, 2), 1)
        char.AddItem(item.Item("Dragonclaw Brooch", 0, 0), 1)
        char.AddItem(item.Item("Code Book", 0, 0), 1)
        char.AddItem(item.Item("Codex", 0, 0), 1)
        char.AddItem(item.Item("Boots of Swampwalking", 2, 0), 1)
        char.AddItem(item.Item("Unlit Torch", 1, 0), 1)
        char.AddItem(item.Item("Magic Dragon Orb", 5, 0), 1)
        char.AddItem(item.Item("Heavy Horse, Combat Trained", 3000, 300), 0)
        char.Companion.AddItem(item.Item("Saddle", 40, 60), 1)
        char.Companion.AddItem(item.Item("Saddlebags", 8, 4), 2)
        char.Companion.AddItem(item.Item("Banded Mail Armor (Horse)", 70, 1000), 1)
        char.Companion.AddItem(item.Item("Bilborn (Rider)", 43, 0), 1)
        char.Companion.AddItem(item.Item("Feed", 10, 0.05), 5)
        print format_spells.SpellDatabase['Spark']
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Spark']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Guidance']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Virtue']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Stabilize']), 0)
        char.LearnSpell(1, spell.Spell(format_spells.SpellDatabase['Ray of Frost']))
        char.LearnSpell(1, spell.Spell(format_spells.SpellDatabase['Mage Hand']))
        char.LearnSpell(1, spell.Spell(format_spells.SpellDatabase['Acid Splash']))
        char.LearnSpell(1, spell.Spell(format_spells.SpellDatabase['Flare']))
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Cure Light Wounds']), 0, True)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Sanctuary']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Inflict Light Wounds']), 0)
        char.LearnSpell(1, spell.Spell(format_spells.SpellDatabase['Magic Missile']))
        char.LearnSpell(1, spell.Spell(format_spells.SpellDatabase['Enlarge Person']))
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Shield Of Faith']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Magic Stone']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Inflict Moderate Wounds']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Cure Moderate Wounds']), 0, True)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Calm Emotions']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Spiritual Weapon']), 0)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Speak with Dead']), 0, True)
        char.PrepareSpell(0, spell.Spell(format_spells.SpellDatabase['Inflict Serious Wounds']), 0)
        print "\n" + char.ToString(False)

    def test_48_AddSpells(self):
        for i in range(100):
            spell_name = random.choice(format_spells.SpellDatabase.keys())
            # print 'Attempting', i+1, 'of 100:', spell_name
            # print format_spells.SpellDatabase[spell_name]
            spell.Spell(format_spells.SpellDatabase[spell_name])


unittest.main()
