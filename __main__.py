
import config
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
import feat

import pickle

if __name__ == '__main__':
        char = character.Character()
        char.CreateCustom("Bilborn Tantix",
                                            "Jake Kausler",
                                            homeland='Sas Arkan',
                                            growth=config.GROWTH_MEDIUM,
                                            armor=None,
                                            shield=None,
                                            magicalProtection=None,
                                            languages=['Common', 'Sylvan', 'Gnome', 'Orc', 'Goblin', 'Giant', 'Celestial'],
                                            skills={
                                                    config.SKILL_ACROBATICS: [0, skill.SkillClasses[config.SKILL_ACROBATICS](config.SKILL_ACROBATICS)],
                                                    config.SKILL_APPRAISE: [0, skill.SkillClasses[config.SKILL_APPRAISE](config.SKILL_APPRAISE)],
                                                    config.SKILL_BLUFF: [0, skill.SkillClasses[config.SKILL_BLUFF](config.SKILL_BLUFF)],
                                                    config.SKILL_CLIMB: [0, skill.SkillClasses[config.SKILL_CLIMB](config.SKILL_CLIMB)],
                                                    config.SKILL_CRAFT1: [1, skill.SkillClasses[config.SKILL_CRAFT1](config.SKILL_CRAFT1)],
                                                    config.SKILL_CRAFT2: [0, skill.SkillClasses[config.SKILL_CRAFT2](config.SKILL_CRAFT2)],
                                                    config.SKILL_DIPLOMACY: [3, skill.SkillClasses[config.SKILL_DIPLOMACY](config.SKILL_DIPLOMACY)],
                                                    config.SKILL_DISABLE_DEVICE: [0, skill.SkillClasses[config.SKILL_DISABLE_DEVICE](config.SKILL_DISABLE_DEVICE)],
                                                    config.SKILL_DISGUISE: [0, skill.SkillClasses[config.SKILL_DISGUISE](config.SKILL_DISGUISE)],
                                                    config.SKILL_ESCAPE_ARTIST: [0, skill.SkillClasses[config.SKILL_ESCAPE_ARTIST](config.SKILL_ESCAPE_ARTIST)],
                                                    config.SKILL_FLY: [0, skill.SkillClasses[config.SKILL_FLY](config.SKILL_FLY)],
                                                    config.SKILL_HANDLE_ANIMAL: [1, skill.SkillClasses[config.SKILL_HANDLE_ANIMAL](config.SKILL_HANDLE_ANIMAL)],
                                                    config.SKILL_HEAL: [3, skill.SkillClasses[config.SKILL_HEAL](config.SKILL_HEAL)],
                                                    config.SKILL_INTIMIDATE: [1, skill.SkillClasses[config.SKILL_INTIMIDATE](config.SKILL_INTIMIDATE)],
                                                    config.SKILL_KNOWLEDGE_ARCANA: [3, skill.SkillClasses[config.SKILL_KNOWLEDGE_ARCANA](config.SKILL_KNOWLEDGE_ARCANA)],
                                                    config.SKILL_KNOWLEDGE_DUNGEONEERING: [0, skill.SkillClasses[config.SKILL_KNOWLEDGE_DUNGEONEERING](config.SKILL_KNOWLEDGE_DUNGEONEERING)],
                                                    config.SKILL_KNOWLEDGE_ENGINEERING: [0, skill.SkillClasses[config.SKILL_KNOWLEDGE_ENGINEERING](config.SKILL_KNOWLEDGE_ENGINEERING)],
                                                    config.SKILL_KNOWLEDGE_GEOGRAPHY: [0, skill.SkillClasses[config.SKILL_KNOWLEDGE_GEOGRAPHY](config.SKILL_KNOWLEDGE_GEOGRAPHY)],
                                                    config.SKILL_KNOWLEDGE_HISTORY: [1, skill.SkillClasses[config.SKILL_KNOWLEDGE_HISTORY](config.SKILL_KNOWLEDGE_HISTORY)],
                                                    config.SKILL_KNOWLEDGE_LOCAL: [0, skill.SkillClasses[config.SKILL_KNOWLEDGE_LOCAL](config.SKILL_KNOWLEDGE_LOCAL)],
                                                    config.SKILL_KNOWLEDGE_NATURE: [0, skill.SkillClasses[config.SKILL_KNOWLEDGE_NATURE](config.SKILL_KNOWLEDGE_NATURE)],
                                                    config.SKILL_KNOWLEDGE_NOBILITY: [0, skill.SkillClasses[config.SKILL_KNOWLEDGE_NOBILITY](config.SKILL_KNOWLEDGE_NOBILITY)],
                                                    config.SKILL_KNOWLEDGE_PLANES: [0, skill.SkillClasses[config.SKILL_KNOWLEDGE_PLANES](config.SKILL_KNOWLEDGE_PLANES)],
                                                    config.SKILL_KNOWLEDGE_RELIGION: [3, skill.SkillClasses[config.SKILL_KNOWLEDGE_RELIGION](config.SKILL_KNOWLEDGE_RELIGION)],
                                                    config.SKILL_LINGUISTICS: [1, skill.SkillClasses[config.SKILL_LINGUISTICS](config.SKILL_LINGUISTICS)],
                                                    config.SKILL_PERCEPTION: [1, skill.SkillClasses[config.SKILL_PERCEPTION](config.SKILL_PERCEPTION)],
                                                    config.SKILL_PERFORM1: [2, skill.SkillClasses[config.SKILL_PERFORM1](config.SKILL_PERFORM1)],
                                                    config.SKILL_PERFORM2: [2, skill.SkillClasses[config.SKILL_PERFORM2](config.SKILL_PERFORM2)],
                                                    config.SKILL_PROF1: [1, skill.SkillClasses[config.SKILL_PROF1](config.SKILL_PROF1)],
                                                    config.SKILL_PROF2: [1, skill.SkillClasses[config.SKILL_PROF2](config.SKILL_PROF2)],
                                                    config.SKILL_RIDE: [4, skill.SkillClasses[config.SKILL_RIDE](config.SKILL_RIDE)],
                                                    config.SKILL_SENSE_MOTIVE: [1, skill.SkillClasses[config.SKILL_SENSE_MOTIVE](config.SKILL_SENSE_MOTIVE)],
                                                    config.SKILL_SLEIGHT_OF_HAND: [0, skill.SkillClasses[config.SKILL_SLEIGHT_OF_HAND](config.SKILL_SLEIGHT_OF_HAND)],
                                                    config.SKILL_SPELLCRAFT: [1, skill.SkillClasses[config.SKILL_SPELLCRAFT](config.SKILL_SPELLCRAFT)],
                                                    config.SKILL_STEALTH: [0, skill.SkillClasses[config.SKILL_STEALTH](config.SKILL_STEALTH)],
                                                    config.SKILL_SURVIVAL: [0, skill.SkillClasses[config.SKILL_SURVIVAL](config.SKILL_SURVIVAL)],
                                                    config.SKILL_SWIM: [0, skill.SkillClasses[config.SKILL_SWIM](config.SKILL_SWIM)],
                                                    config.SKILL_USE_MAGIC_DEVICE: [0, skill.SkillClasses[config.SKILL_USE_MAGIC_DEVICE](config.SKILL_USE_MAGIC_DEVICE)]
                                            },
                                            inventory=None,
                                            weapons=None,
                                            height=41,
                                            weight=43,
                                            hairColor=config.COLOR_BLUE,
                                            eyeColor=config.COLOR_GREEN,
                                            alignment=alignment.Alignment(config.ALIGNMENT_NEUTRAL, config.ALIGNMENT_GOOD),
                                            gender=config.GENDER_MALE,
                                            age=71,
                                            diety='Qi Zhong',
                                            experience=33740,
                                            abilities={
                                                    config.ABILITY_STRENGTH: 10,
                                                    config.ABILITY_DEXTERITY: 7,
                                                    config.ABILITY_CONSTITUTION: 9,
                                                    config.ABILITY_INTELLIGENCE: 16,
                                                    config.ABILITY_WISDOM: 15,
                                                    config.ABILITY_CHARISMA: 17
                                            },
                                            race=race.Gnome(),
                                            classes=[
                                                    (characterclass.Cleric(char, 0), 5),
                                                    (characterclass.Sorcerer(char, 1), 1)
                                            ],
                                            hitDieMethod=config.HIT_DIE_AVERAGE
                                            )
        char.AddEffect(feat.LoadFeatByName("Improved Initiative"), config.EFFECT_LEARNED_FEAT)
        char.AddEffect(feat.LoadFeatByName("Persuasive"), config.EFFECT_LEARNED_FEAT)
        char.AddEffect(feat.LoadFeatByName("Animal Affinity"), config.EFFECT_LEARNED_FEAT)
        char.AddLeveledAbility(config.ABILITY_DEXTERITY, 1)
        char.AddFavoredClassSkill(config.SKILL_RIDE, 3)
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
        char.AddItem(item.Item("Ration    Per Day", 1, 0.5), 4)
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
        # char.Companion.AddItem(item.Item("Saddle", 40, 60), 1)
        # char.Companion.AddItem(item.Item("Saddlebags", 8, 4), 2)
        # char.Companion.AddItem(item.Item("Banded Mail Armor (Horse)", 70, 1000), 1)
        # char.Companion.AddItem(item.Item("Bilborn (Rider)", 43, 0), 1)
        # char.Companion.AddItem(item.Item("Feed", 10, 0.05), 5)
        char.PrepareSpell(0, spell.LoadSpellByName('Spark'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Guidance'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Virtue'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Stabilize'), 0)
        char.LearnSpell(1, spell.LoadSpellByName('Ray of Frost'))
        char.LearnSpell(1, spell.LoadSpellByName('Mage Hand'))
        char.LearnSpell(1, spell.LoadSpellByName('Acid Splash'))
        char.LearnSpell(1, spell.LoadSpellByName('Flare'))
        char.PrepareSpell(0, spell.LoadSpellByName('Cure Light Wounds'), 0, True)
        char.PrepareSpell(0, spell.LoadSpellByName('Sanctuary'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Inflict Light Wounds'), 0)
        char.LearnSpell(1, spell.LoadSpellByName('Magic Missile'))
        char.LearnSpell(1, spell.LoadSpellByName('Enlarge Person'))
        char.PrepareSpell(0, spell.LoadSpellByName('Shield Of Faith'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Magic Stone'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Inflict Moderate Wounds'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Cure Moderate Wounds'), 0, True)
        char.PrepareSpell(0, spell.LoadSpellByName('Calm Emotions'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Spiritual Weapon'), 0)
        char.PrepareSpell(0, spell.LoadSpellByName('Speak with Dead'), 0, True)
        char.PrepareSpell(0, spell.LoadSpellByName('Inflict Serious Wounds'), 0)
        char.AddDomain(0, config.DOMAIN_AIR)

        pickle.dump(char, open(str(char.uuid) + '.chr', 'wb'))
