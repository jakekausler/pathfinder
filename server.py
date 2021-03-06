
# TODO: Simulate enemies, effects, and checks to see the changed scores
# TODO: Add rest endpoints for editing the character
# TODO: Save the character (for now) and eventually the party
# TODO: Allow creating a new character
# TODO: Add a party system that handles multiple characters, players being able to own multiple characters (representing companions)

from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
from urlparse import urlparse
from urlparse import parse_qs
import os
import json
import traceback
import pickle
import re

import config
import alignment
import race
import size
import color
import spell
import feat
import item
import roll

PORT = 8080
WEBROOT = 'web'
INDEXFILE = WEBROOT + '/index.html'


def GetCharacter(id):
    fn = id + ".chr"
    if os.access(fn, os.R_OK):
        return pickle.load(open(fn))
    else:
        return None


def SaveCharacter(char):
    try:
        pickle.dump(char, open(str(char.uuid) + '.chr', 'wb'))
        return True
    except Exception:
        traceback.print_exc()
        return False


def GetContentType(fn):
    if fn.find('.html') > -1:
        return 'text/html'
    elif fn.find('.css') > -1:
        return 'text/css'
    elif fn.find('.json') > -1:
        return 'application/json'
    else:
        return '.text'


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsedParams = urlparse(self.path)
        fn = WEBROOT + parsedParams.path
        if fn == 'web/':
            self.ServeIndex()
        elif fn == "web/character":
            self.ServeCharacter()
        elif fn == 'web/races':
            self.ServeRaces()
        elif fn == 'web/classes':
            self.ServeClasses()
        elif fn == 'web/skills':
            self.ServeSkills()
        elif fn == 'web/colors':
            self.ServeColors()
        elif fn == 'web/spells':
            self.ServeSpells()
        elif fn == 'web/feats':
            self.ServeFeats()
        elif fn == 'web/equipableitems':
            self.ServeEquipableItems()
        elif os.access(fn, os.R_OK):
            self.ServeFile(fn)
        else:
            self.Failure("Could not parse request")

    def do_POST(self):
        parsedParams = urlparse(self.path)
        query = parsedParams.path
        params = parse_qs(parsedParams.query)
        if query.startswith("/character"):
            if 'id' not in params or len(params['id']) < 1:
                self.Failure("No id provided")
            else:
                if query == "/character/skill/rank":
                    char = GetCharacter(params['id'][0])
                    if not char:
                        self.Failure("Character not found")
                    if 'skillid' not in params or len(params['skillid']) < 1:
                        self.Failure("No skillid provided")
                    else:
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        else:
                            try:
                                char.SetSkillRanks(int(params['skillid'][0]), int(params['value'][0]))
                                SaveCharacter(char)
                                self.Success("Success")
                            except ValueError:
                                self.Failure("Unable to convert skillid or value to int")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Could not save character")
                        self.Failure("Failed to save character")
                elif query == "/character/skill/applyfcpoints":
                    char = GetCharacter(params['id'][0])
                    if not char:
                        self.Failure("Character not found")
                    if 'value' not in params or len(params['value']) < 1:
                        self.Failure("No value provided")
                    if 'skillid' not in params or len(params['skillid']) < 1:
                        self.Failure("No skillid provided")
                    else:
                        try:
                            char.AddFavoredClassSkill(int(params['skillid'][0]), int(params['value'][0]))
                            SaveCharacter(char)
                            self.Success('Success')
                        except ValueError:
                            self.Failure("Unable to convert to int")
                        except Exception:
                            traceback.print_exc()
                            self.Failure("Unable to save character")
                elif query.startswith("/character/health/"):
                    if query == "/character/health/damage":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            try:
                                char.Harm(int(params['amount'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except ValueError:
                                self.Failure("Unable to convert amount to int")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to save character")
                    elif query == "/character/health/damagenonlethal":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            try:
                                char.HarmNonLethal(int(params['amount'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except ValueError:
                                self.Failure("Unable to convert amount to int")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to save character")
                    elif query == "/character/health/heal":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            try:
                                char.Heal(int(params['amount'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except ValueError:
                                self.Failure("Unable to convert amount to int")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to save character")
                    elif query == "/character/health/healnonlethal":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            try:
                                char.HealNonLethal(int(params['amount'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except ValueError:
                                self.Failure("Unable to convert amount to int")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to save character")
                    elif query == "/character/health/applyfcpoints":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            try:
                                char.AddFavoredClassHP(int(params['amount'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except ValueError:
                                self.Failure("Unable to convert amount to int")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to save character")
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/ability/"):
                    if query == "/character/ability/increase":
                        print params
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            if 'ability' not in params or len(params['ability']) < 1:
                                self.Failure("No ability provided")
                            else:
                                a = config.NONE
                                if a in config.AbilityNameToId:
                                    a = config.AbilityNameToId[params['ability'][0]]
                                if a == config.NONE:
                                    self.Failure("Ability not found")
                                else:
                                    try:
                                        amount = int(params['amount'][0])
                                        if char.AbilityPointsLeft() >= amount:
                                            char.AddLeveledAbility(a, amount)
                                        else:
                                            char.AddMiscAbility(a, amount)
                                        SaveCharacter(char)
                                        self.Success('Success')
                                    except ValueError:
                                        self.Failure("Unable to convert amount to int")
                                    except Exception:
                                        traceback.print_exc()
                                        self.Failure("Unable to save character")
                    elif query == "/character/ability/decrease":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            if 'ability' not in params or len(params['ability']) < 1:
                                self.Failure("No ability provided")
                            else:
                                a = config.NONE
                                if a in config.ConfigNameToId:
                                    a = config.ConfigNameToId[params['ability'][0]]
                                if a == config.NONE:
                                    self.Failure("Ability not found")
                                else:
                                    try:
                                        amount = int(params['amount'][0])
                                        char.AddPenaltyAbility(a, amount)
                                        SaveCharacter(char)
                                        self.Success('Success')
                                    except ValueError:
                                        self.Failure("Unable to convert amount to int")
                                    except Exception:
                                        traceback.print_exc()
                                        self.Failure("Unable to save character")
                    elif query == "/character/ability/tempincrease":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            if 'ability' not in params or len(params['ability']) < 1:
                                self.Failure("No ability provided")
                            else:
                                a = config.NONE
                                if a in config.AbilityNameToId:
                                    a = config.AbilityNameToId[params['ability'][0]]
                                if a == config.NONE:
                                    self.Failure("Ability not found")
                                else:
                                    try:
                                        amount = int(params['amount'][0])
                                        char.IncreaseTempAbility(a, amount)
                                        SaveCharacter(char)
                                        self.Success('Success')
                                    except ValueError:
                                        self.Failure("Unable to convert amount to int")
                                    except Exception:
                                        traceback.print_exc()
                                        self.Failure("Unable to save character")
                    elif query == "/character/ability/tempdecrease":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'amount' not in params or len(params['amount']) < 1:
                            self.Failure("No amount provided")
                        else:
                            if 'ability' not in params or len(params['ability']) < 1:
                                self.Failure("No ability provided")
                            else:
                                a = config.NONE
                                if a in config.AbilityNameToId:
                                    a = config.AbilityNameToId[params['ability'][0]]
                                if a == config.NONE:
                                    self.Failure("Ability not found")
                                else:
                                    try:
                                        amount = int(params['amount'][0])
                                        char.DecreaseTempAbility(a, amount)
                                        SaveCharacter(char)
                                        self.Success('Success')
                                    except ValueError:
                                        self.Failure("Unable to convert amount to int")
                                    except Exception:
                                        traceback.print_exc()
                                        self.Failure("Unable to save character")
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/language/"):
                    if query == "/character/language/learn":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if "value" in params and len(params["value"]) > 0:
                            try:
                                char.LearnLanguage(params["value"][0])
                                SaveCharacter(char)
                                self.Success("Success")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to learn language")
                        else:
                            self.Failure("No value provided")
                    elif query == "/character/language/forget":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if "value" in params and len(params["value"]) > 0:
                            try:
                                char.ForgetLanguage(params["value"][0])
                                SaveCharacter(char)
                                self.Success("Success")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to forget language")
                        else:
                            self.Failure("No value provided")
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/feat"):
                    if query == "/character/feat/learn":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if "value" in params and len(params["value"]) > 0:
                            try:
                                char.LearnFeat(int(params["value"][0]))
                                SaveCharacter(char)
                                self.Success("Success")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to learn feat")
                        else:
                            self.Failure("No value provided")
                    elif query == "/character/feat/forget":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if "value" in params and len(params["value"]) > 0:
                            try:
                                char.ForgetFeat(int(params["value"][0]))
                                SaveCharacter(char)
                                self.Success("Success")
                            except Exception:
                                traceback.print_exc()
                                self.Failure("Unable to forget feat")
                        else:
                            self.Failure("No value provided")
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/information"):
                    if query.startswith("/character/information/name"):
                        if query == "/character/information/name/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                char.Name = params['value'][0]
                                SaveCharacter(char)
                                self.Success('Success')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/player"):
                        if query == "/character/information/player/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                char.PlayerName = params['value'][0]
                                SaveCharacter(char)
                                self.Success('Success')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/alignment"):
                        if query == "/character/information/alignment/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                lc = config.ALIGNMENT_NEUTRAL
                                ge = config.ALIGNMENT_NEUTRAL
                                a = params['value'][0].split(" ")
                                print 'alignment', a
                                if a[0] == "Lawful":
                                    lc = config.ALIGNMENT_LAWFUL
                                elif a[0] == 'Neutral':
                                    lc = config.ALIGNMENT_NEUTRAL
                                elif a[0] == 'Chaotic':
                                    lc = config.ALIGNMENT_CHAOTIC
                                else:
                                    self.Failure("Alignment not found")
                                if a[1] == "Good":
                                    ge = config.ALIGNMENT_GOOD
                                elif a[1] == 'Neutral':
                                    ge = config.ALIGNMENT_NEUTRAL
                                elif a[1] == 'Evil':
                                    ge = config.ALIGNMENT_EVIL
                                else:
                                    self.Failure("Alignment not found")
                                char.Alignment = alignment.Alignment(lc, ge)
                                SaveCharacter(char)
                                self.Success('Success')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/race"):
                        if query == "/character/information/race/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                r = params['value'][0]
                                if r in config.RaceNameToId:
                                    char.Race = race.RaceDict[config.RaceNameToId[r]]()
                                    SaveCharacter(char)
                                    self.Success('Success')
                                else:
                                    self.Failure("Race not found")
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/diety"):
                        if query == "/character/information/diety/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                char.Diety = params['value'][0]
                                SaveCharacter(char)
                                self.Success('Success')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/size"):
                        if query == "/character/information/size/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                s = params['value'][0]
                                if s in config.SizeNameToId:
                                    char.Race.Size = size.sizeDict[config.SizeNameToId[s]]()
                                    SaveCharacter(char)
                                    self.Success('Success')
                                else:
                                    self.Failure("Size not found")
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/gender"):
                        if query == "/character/information/gender/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                g = config.NONE
                                if params['value'][0] in config.GenderNameToId:
                                    g = config.GenderNameToId[params['value'][0]]
                                if g == config.NONE:
                                    self.Failure("Gender not found")
                                else:
                                    char.Gender = g
                                    SaveCharacter(char)
                                    self.Success('Success')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/age"):
                        if query == "/character/information/age/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                try:
                                    char.Age = int(params['value'][0])
                                    SaveCharacter(char)
                                    self.Success('Success')
                                except Exception:
                                    self.Failure('Unable to parse age')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/height"):
                        if query == "/character/information/height/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                try:
                                    char.Height = int(params['value'][0])
                                    SaveCharacter(char)
                                    self.Success('Success')
                                except Exception:
                                    traceback.print_exc()
                                    self.Failure('Unable to parse age')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/weight"):
                        if query == "/character/information/weight/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                try:
                                    char.Weight = int(params['value'][0])
                                    SaveCharacter(char)
                                    self.Success('Success')
                                except Exception:
                                    traceback.print_exc()
                                    self.Failure('Unable to parse age')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/hair"):
                        if query == "/character/information/hair/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                c = config.NONE
                                if params['value'][0] in config.ColorNameToId:
                                    c = config.ColorNameToId[params['value'][0]]
                                if c == config.NONE:
                                    self.Failure("Color not found")
                                else:
                                    char.HairColor = c
                                    SaveCharacter(char)
                                    self.Success('Success')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/eye"):
                        if query == "/character/information/eye/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                c = config.NONE
                                if params['value'][0] in config.ColorNameToId:
                                    c = config.ColorNameToId[params['value'][0]]
                                if c == config.NONE:
                                    self.Failure("Color not found")
                                else:
                                    char.EyeColor = c
                                    SaveCharacter(char)
                                    self.Success('Success')
                        else:
                            self.Failure("Could not parse request")
                    elif query.startswith("/character/information/homeland"):
                        if query == "/character/information/homeland/change":
                            char = GetCharacter(params['id'][0])
                            if not char:
                                self.Failure("Character not found")
                            if 'value' not in params or len(params['value']) < 1:
                                self.Failure("No value provided")
                            else:
                                char.Homeland = params['value'][0]
                                SaveCharacter(char)
                                self.Success('Success')
                        else:
                            self.Failure("Could not parse request")
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/class"):
                    if query == "/character/class/add":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        elif 'classidx' not in params or len(params['classidx']) < 1:
                            self.Failure("No classidx provided")
                        else:
                            try:
                                char.AddClass(int(params['classidx'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse amount')
                        return
                    elif query == "/character/class/remove":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        elif 'classidx' not in params or len(params['classidx']) < 1:
                            self.Failure("No classidx provided")
                        else:
                            try:
                                char.RemoveClass(int(params['classidx'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse amount')
                    elif query == "/character/class/increase":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        elif 'classidx' not in params or len(params['classidx']) < 1:
                            self.Failure("No classidx provided")
                        else:
                            try:
                                char.IncreaseClassLevel(int(params['classidx'][0]), int(params['value'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse amount')
                    elif query == "/character/class/decrease":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        elif 'classidx' not in params or len(params['classidx']) < 1:
                            self.Failure("No classidx provided")
                        else:
                            try:
                                char.DecreaseClassLevel(int(params['classidx'][0]), int(params['value'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse amount')
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/gold"):
                    if query == "/character/gold/spend":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        else:
                            try:
                                char.SpendGold(int(params['value'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse amount')
                    elif query == "/character/gold/gain":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        else:
                            try:
                                char.AddGold(int(params['value'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse amount')
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/experience"):
                    if query == "/character/experience/increase":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        else:
                            try:
                                char.IncreaseExperience(int(params['value'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse amount')
                    elif query == "/character/experience/reduce":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        else:
                            try:
                                char.DecreaseExperience(int(params['value'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse amount')
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/equipment"):
                    if query == "/character/equipment/equip":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'slot' not in params or len(params['slot']) < 1:
                            self.Failure("No slot provided")
                        elif 'itemid' not in params or len(params['itemid']) < 1:
                            self.Failure("No itemid provided")
                        else:
                            try:
                                char.Inventory.WearItem(int(params['itemid'][0]), int(params['slot'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    elif query == "/character/equipment/unequip":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'slot' not in params or len(params['slot']) < 1:
                            self.Failure("No slot provided")
                        else:
                            try:
                                char.Inventory.RemoveWornItem(int(params['slot'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/item"):
                    if query.startswith("/character/item/add"):
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                            return
                        if 'name' not in params or len(params['name']) < 1:
                            self.Failure("No name provided")
                            return
                        if 'quantity' not in params or len(params['quantity']) < 1:
                            self.Failure("No quantity provided")
                            return
                        if 'weight' not in params or len(params['weight']) < 1:
                            self.Failure("No weight provided")
                            return
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                            return
                        name = ''
                        quantity = 0
                        weight = 0
                        value = 0
                        try:
                            name = params['name'][0]
                            quantity = int(params['quantity'][0])
                            weight = float(params['weight'][0])
                            value = float(params['value'][0])
                        except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                                return
                        if query == "/character/item/add/item":
                            char.Inventory.AddItem(item.Item(name, weight, value), quantity)
                            SaveCharacter(char)
                            self.Success('Success')
                        elif query.startswith('/character/item/add/weapon'):
                            if 'damage' not in params or len(params['damage']) < 1:
                                self.Failure("No damage provided")
                                return
                            if 'critical' not in params or len(params['critical']) < 1:
                                self.Failure("No critical provided")
                                return
                            if 'range' not in params or len(params['range']) < 1:
                                self.Failure("No range provided")
                                return
                            if 'enchantment' not in params or len(params['enchantment']) < 1:
                                self.Failure("No enchantment provided")
                                return
                            if 'size' not in params or len(params['size']) < 1:
                                self.Failure("No size provided")
                                return
                            damage = ''
                            critical = ''
                            criticalRange = [20, 20]
                            criticalMultiplier = 2
                            range = 0
                            types = config.NONE
                            useAllTypes = False
                            specials = config.NONE
                            useAllSpecials = False
                            twoHanded = False
                            light = False
                            martial = False
                            exotic = False
                            masterwork = False
                            enchantment = False
                            siz = size.Medium()
                            try:
                                damage = params['damage'][0]
                                damage = damage.strip()
                                if damage == '':
                                    damage = roll.Dice(4, 1, addition=1)
                                else:
                                    r = re.compile(r'([0-9]+)d([0-9]+)( ?\+ ?([0-9]+))?')
                                    m = r.match(damage)
                                    if m:
                                        if not (m.groups()[0] and m.groups()[1]):
                                            raise Exception("Unable to parse damage")
                                        addition = 0
                                        if m.groups()[3]:
                                            addition = int(m.groups()[3])
                                        damage = roll.Dice(int(m.groups()[1]), int(m.groups()[0]), addition=addition)
                                    else:
                                        self.Failure("Unable to parse damage")
                                        return
                                critical = params['critical'][0]
                                critical = critical.strip()
                                if critical != '':
                                    r = re.compile(r'((([0-9]+)-)?([0-9]+)/)?x([0-9]+)')
                                    m = r.match(critical)
                                    if m:
                                        if not m.groups()[4]:
                                            raise Exception("Unable to parse critical")
                                        if m.groups()[2]:
                                            criticalRange[0] = int(m.groups()[2])
                                        if m.groups()[3]:
                                            criticalRange[1] = int(m.groups()[3])
                                            if not m.groups()[2]:
                                                criticalRange[0] = int(m.groups()[3])
                                        criticalMultiplier = int(m.groups()[4])
                                    else:
                                        self.Failure("Unable to parse critical")
                                        return
                                range = float(params['weight'][0])
                                if 'types' in params:
                                    types = params['types']
                                    t = config.NONE
                                    for type in types:
                                        t |= config.WeaponTypeDict[type]
                                    types = t
                                if 'usealltypes' in params:
                                    useAllTypes = params['usealltypes'][0] == True
                                if 'specials' in params:
                                    specials = params['specials']
                                    t = config.NONE
                                    for type in specials:
                                        t |= config.WeaponSpecialDict[type]
                                    specials = t
                                if 'useallspecials' in params:
                                    useAllSpecials = params['useallspecials'][0] == True
                                if 'twohanded' in params:
                                    twoHanded = params['twohanded'][0] == True
                                if 'light' in params:
                                    light = params['light'][0] == True
                                if 'martial' in params:
                                    martial = params['martial'][0] == True
                                if 'exotic' in params:
                                    exotic = params['exotic'][0] == True
                                if 'masterwork' in params:
                                    masterwork = params['masterwork'][0] == True
                                if 'enchantment' in params:
                                    enchantment = int(params['enchantment'][0])
                                if 'size' in params:
                                    siz = size.sizeDict[config.SizeNameToId[params['size'][0]]]()
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                            if query == "/character/item/add/weapon/unarmed":
                                cancelSlots = []
                                applicableSlots = []
                                if 'applicableslots' in params:
                                    applicableSlots = params['applicableslots']
                                if 'cancelsslots' in params:
                                    cancelSlots = params['cancelsslots']
                                char.Inventory.AddItem(item.MeleeWeapon(name, weight, value, damage=damage, size=siz, criticalRange=criticalRange, criticalMultiplier=criticalMultiplier, range=range, type=types, typeJoin=config.JOIN_AND if useAllTypes else config.JOIN_OR, special=specials, specialJoin=config.JOIN_AND if useAllSpecials else config.JOIN_OR, isTwoHanded=twoHanded, isLight=light, isMartial=martial, isExotic=exotic, isMasterwork=masterwork, enchantment=enchantment, applicableSlots=applicableSlots, cancelSlots=cancelSlots), quantity)
                                SaveCharacter(char)
                                self.Success('Success')
                            elif query == "/character/item/add/weapon/melee":
                                char.Inventory.AddItem(item.MeleeWeapon(name, weight, value, damage=damage, size=siz, criticalRange=criticalRange, criticalMultiplier=criticalMultiplier, range=range, type=types, typeJoin=config.JOIN_AND if useAllTypes else config.JOIN_OR, special=specials, specialJoin=config.JOIN_AND if useAllSpecials else config.JOIN_OR, isTwoHanded=twoHanded, isLight=light, isMartial=martial, isExotic=exotic, isMasterwork=masterwork, enchantment=enchantment), quantity)
                                SaveCharacter(char)
                                self.Success('Success')
                            elif query == "/character/item/add/weapon/ranged":
                                if 'ammotype' not in params or len(params['ammotype']) < 1:
                                    self.Failure("No ammotype provided")
                                    return
                                ammoType = config.AmmoTypeDict[params["ammotype"]]
                                char.Inventory.AddItem(item.MeleeWeapon(name, weight, value, damage=damage, size=siz, criticalRange=criticalRange, criticalMultiplier=criticalMultiplier, range=range, type=types, typeJoin=config.JOIN_AND if useAllTypes else config.JOIN_OR, special=specials, specialJoin=config.JOIN_AND if useAllSpecials else config.JOIN_OR, isTwoHanded=twoHanded, isLight=light, isMartial=martial, isExotic=exotic, isMasterwork=masterwork, enchantment=enchantment, ammoType=ammoType), quantity)
                                SaveCharacter(char)
                                self.Success('Success')
                            else:
                                traceback.print_exc()
                                self.Failure("Could not parse request")
                        elif query.startswith('/character/item/add/wearable'):
                            if query == "/character/item/add/wearable/armor":
                                if 'weighttype' not in params or len(params['weighttype']) < 1:
                                    self.Failure("No weighttype provided")
                                    return
                                if 'size' not in params or len(params['size']) < 1:
                                    self.Failure("No size provided")
                                    return
                                if 'armorclass' not in params or len(params['armorclass']) < 1:
                                    self.Failure("No armorclass provided")
                                    return
                                if 'armorcheckpenalty' not in params or len(params['armorcheckpenalty']) < 1:
                                    self.Failure("No armorcheckpenalty provided")
                                    return
                                if 'maxdexbonus' not in params or len(params['maxdexbonus']) < 1:
                                    self.Failure("No maxdexbonus provided")
                                    return
                                if 'enchantment' not in params or len(params['enchantment']) < 1:
                                    self.Failure("No enchantment provided")
                                    return
                                weightType = config.NONE
                                siz = size.Medium()
                                armorClass = 0
                                armorCheckPenalty = 0
                                maxDexBonus = 0
                                enchantment = 0
                                masterwork = False
                                try:
                                    weightType = config.ArmorTypeDict[params['weighttype'][0]]
                                    siz = size.sizeDict[config.SizeNameToId[params['size'][0]]]()
                                    armorClass = int(params['armorclass'][0])
                                    armorCheckPenalty = int(params['armorcheckpenalty'][0])
                                    maxDexBonus = int(params['maxdexbonus'][0])
                                    enchantment = int(params['enchantment'][0])
                                    masterwork = params['masterwork'][0] == True
                                    char.Inventory.AddItem(item.Armor(name, weight, value, weightType=weightType, armorClass=armorClass, maxDexBonus=maxDexBonus, armorCheckPenalty=armorCheckPenalty, spellFailureChance=spellFailureChance, size=siz, masterwork=masterwork, enchantment=enchantment), quantity)
                                except Exception:
                                    traceback.print_exc()
                                    self.Failure("Could not parse request")
                                    return
                            elif query == "/character/item/add/wearable/shield":
                                if 'weighttype' not in params or len(params['weighttype']) < 1:
                                    self.Failure("No weighttype provided")
                                    return
                                if 'size' not in params or len(params['size']) < 1:
                                    self.Failure("No size provided")
                                    return
                                if 'armorclass' not in params or len(params['armorclass']) < 1:
                                    self.Failure("No armorclass provided")
                                    return
                                if 'armorcheckpenalty' not in params or len(params['armorcheckpenalty']) < 1:
                                    self.Failure("No armorcheckpenalty provided")
                                    return
                                if 'maxdexbonus' not in params or len(params['maxdexbonus']) < 1:
                                    self.Failure("No maxdexbonus provided")
                                    return
                                if 'enchantment' not in params or len(params['enchantment']) < 1:
                                    self.Failure("No enchantment provided")
                                    return
                                weightType = config.NONE
                                siz = size.Medium()
                                armorClass = 0
                                armorCheckPenalty = 0
                                maxDexBonus = 0
                                enchantment = 0
                                masterwork = False
                                try:
                                    weightType = config.ArmorTypeDict[params['weighttype'][0]]
                                    siz = size.sizeDict[config.SizeNameToId[params['size'][0]]]()
                                    armorClass = int(params['armorclass'][0])
                                    armorCheckPenalty = int(params['armorcheckpenalty'][0])
                                    maxDexBonus = int(params['maxdexbonus'][0])
                                    enchantment = int(params['enchantment'][0])
                                    masterwork = params['masterwork'][0] == True
                                    char.Inventory.AddItem(item.Shield(name, weight, value, weightType=weightType, armorClass=armorClass, maxDexBonus=maxDexBonus, armorCheckPenalty=armorCheckPenalty, spellFailureChance=spellFailureChance, size=siz, masterwork=masterwork, enchantment=enchantment), quantity)
                                except Exception:
                                    traceback.print_exc()
                                    self.Failure("Could not parse request")
                                    return
                            elif query == "/character/item/add/wearable/magicalprotection":
                                cancelSlots = []
                                applicableSlots = []
                                if 'applicableslots' in params:
                                    applicableSlots = params['applicableslots']
                                if 'cancelsslots' in params:
                                    cancelSlots = params['cancelsslots']
                                char.Inventory.AddItem(item.MagicalProtection(name, weight, value, damage=damage, size=siz, criticalRange=criticalRange, criticalMultiplier=criticalMultiplier, range=range, type=types, typeJoin=config.JOIN_AND if useAllTypes else config.JOIN_OR, special=specials, specialJoin=config.JOIN_AND if useAllSpecials else config.JOIN_OR, isTwoHanded=twoHanded, isLight=light, isMartial=martial, isExotic=exotic, isMasterwork=masterwork, enchantment=enchantment, applicableSlots=applicableSlots, cancelSlots=cancelSlots), quantity)
                                SaveCharacter(char)
                                self.Success('Success')
                            elif query == "/character/item/add/wearable/other":
                                cancelSlots = []
                                applicableSlots = []
                                if 'applicableslots' in params:
                                    applicableSlots = params['applicableslots']
                                if 'cancelsslots' in params:
                                    cancelSlots = params['cancelsslots']
                                char.Inventory.AddItem(item.WearableItem(name, weight, value, damage=damage, size=siz, criticalRange=criticalRange, criticalMultiplier=criticalMultiplier, range=range, type=types, typeJoin=config.JOIN_AND if useAllTypes else config.JOIN_OR, special=specials, specialJoin=config.JOIN_AND if useAllSpecials else config.JOIN_OR, isTwoHanded=twoHanded, isLight=light, isMartial=martial, isExotic=exotic, isMasterwork=masterwork, enchantment=enchantment, applicableSlots=applicableSlots, cancelSlots=cancelSlots), quantity)
                                SaveCharacter(char)
                                self.Success('Success')
                            else:
                                self.Failure("Could not parse request")
                        elif query == "/character/item/add/ammunition":
                            if 'ammotype' not in params or len(params['ammotype']) < 1:
                                self.Failure("No ammotype provided")
                                return
                            try:
                                ammoType = config.AmmoTypeDict[params["ammotype"]]
                                extraDamage = 0
                                extraRange = 0
                                extraAttack = 0
                                if 'extradamage' in params:
                                    extraDamage = int(params["extradamage"][0])
                                if 'extrarange' in params:
                                    extraRange = int(params["extrarange"][0])
                                if 'extraattack' in params:
                                    extraAttack = int(params["extraattack"][0])
                                char.Inventory.AddItem(item.RangedWeapon(name, weight, value, extraDamage=extraDamage, extraRange=extraRange, extraAttack=extraAttack, type=ammoType), quantity)
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                                return False
                        else:
                            self.Failure("Could not parse request")
                    elif query == "/character/item/remove":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'itemindex' not in params or len(params['itemindex']) < 1:
                            self.Failure("No itemindex provided")
                        else:
                            try:
                                char.RemoveItem(int(params['itemindex'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    elif query == "/character/item/edit":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'itemindex' not in params or len(params['itemindex']) < 1:
                            self.Failure("No itemindex provided")
                        if 'name' not in params or len(params['name']) < 1:
                            self.Failure("No name provided")
                        if 'weight' not in params or len(params['weight']) < 1:
                            self.Failure("No weight provided")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        if 'quantity' not in params or len(params['quantity']) < 1:
                            self.Failure("No quantity provided")
                        else:
                            try:
                                char.EditItem(int(params['itemindex'][0]), params['name'][0], int(params['quantity'][0]), float(params['value'][0]), float(params['weight'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                                return False
                    else:
                        self.Failure("Could not parse request")
                elif query.startswith("/character/spell"):
                    if query == "/character/spell/use":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        elif 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        elif 'level' not in params or len(params['level']) < 1:
                            self.Failure("No level provided")
                        elif 'spellidx' not in params or len(params['spellidx']) < 1:
                            self.Failure("No spellidx provided")
                        else:
                            try:
                                domain = False
                                if 'domain' in params or len(params['domain']) > 0:
                                    domain = params['domain'][0] == 'true'
                                char.UseSpell(int(params['classindex'][0]), int(params['level'][0]), int(params['spellidx'][0]), int(params['value'][0]), domain)
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                                return False
                    elif query == "/character/spell/learn":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        elif 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        else:
                            try:
                                domain = False
                                if 'domain' in params or len(params['domain']) > 0:
                                    domain = params['domain'][0] == 'true'
                                char.LearnSpell(int(params['classindex'][0]), spell.LoadSpellById(int(params['value'][0])))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                                return False
                        return
                    elif query == "/character/spell/forget":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        elif 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        elif 'level' not in params or len(params['level']) < 1:
                            self.Failure("No level provided")
                        elif 'spellidx' not in params or len(params['spellidx']) < 1:
                            self.Failure("No spellidx provided")
                        else:
                            try:
                                domain = False
                                if 'domain' in params or len(params['domain']) > 0:
                                    domain = params['domain'][0] == 'true'
                                char.ForgetSpell(int(params['classindex'][0]), int(params['level'][0]), int(params['spellidx'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                        return
                        return
                    elif query == "/character/spell/prepare":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        elif 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        else:
                            try:
                                domain = False
                                if 'domain' in params or len(params['domain']) > 0:
                                    domain = params['domain'][0] == 'true'
                                char.PrepareSpell(int(params['classindex'][0]), spell.LoadSpellById(int(params['value'][0])), 0, domain)
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    elif query == "/character/spell/removeexisting":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        elif 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        elif 'level' not in params or len(params['level']) < 1:
                            self.Failure("No level provided")
                        elif 'spellidx' not in params or len(params['spellidx']) < 1:
                            self.Failure("No spellidx provided")
                        else:
                            try:
                                domain = False
                                if 'domain' in params or len(params['domain']) > 0:
                                    domain = params['domain'][0] == 'true'
                                char.RemoveSpell(int(params['classindex'][0]), int(params['level'][0]), int(params['spellidx'][0]), domain)
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                        return
                    elif query == "/character/spell/prepareexisting":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        elif 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        elif 'level' not in params or len(params['level']) < 1:
                            self.Failure("No level provided")
                        elif 'spellidx' not in params or len(params['spellidx']) < 1:
                            self.Failure("No spellidx provided")
                        else:
                            try:
                                domain = False
                                if 'domain' in params or len(params['domain']) > 0:
                                    domain = params['domain'][0] == 'true'
                                char.PrepareExistingSpell(int(params['classindex'][0]), int(params['level'][0]), int(params['spellidx'][0]), int(params['value'][0]), domain)
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    elif query == "/character/spell/unprepare":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'value' not in params or len(params['value']) < 1:
                            self.Failure("No value provided")
                        elif 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        elif 'level' not in params or len(params['level']) < 1:
                            self.Failure("No level provided")
                        elif 'spellidx' not in params or len(params['spellidx']) < 1:
                            self.Failure("No spellidx provided")
                        else:
                            try:
                                domain = False
                                if 'domain' in params or len(params['domain']) > 0:
                                    domain = params['domain'][0] == 'true'
                                char.UnPrepareSpell(int(params['classindex'][0]), int(params['level'][0]), int(params['spellidx'][0]), int(params['value'][0]), domain)
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    elif query == "/character/spell/resetall":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        else:
                            try:
                                char.ResetSpells()
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    elif query == "/character/spell/resetclass":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        else:
                            try:
                                char.ResetClassSpellLevels(int(params['classindex'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    elif query == "/character/spell/resetlevel":
                        char = GetCharacter(params['id'][0])
                        if not char:
                            self.Failure("Character not found")
                        if 'classindex' not in params or len(params['classindex']) < 1:
                            self.Failure("No classindex provided")
                        elif 'level' not in params or len(params['level']) < 1:
                            self.Failure("No level provided")
                        else:
                            try:
                                char.ResetClassSpellLevel(int(params['classindex'][0]), int(params['level'][0]))
                                SaveCharacter(char)
                                self.Success('Success')
                            except Exception:
                                traceback.print_exc()
                                self.Failure('Unable to parse')
                    else:
                        self.Failure("Could not parse request")
                else:
                    self.Failure("Could not parse request")
        else:
            self.Failure("Could not parse request")

    def Success(self, s=""):
        self.send_response(200)
        self.wfile.write(s)

    def Failure(self, s=""):
        print s
        self.send_response(404)
        self.end_headers()
        self.wfile.write(s)

    def ServeIndex(self):
        self.ServeFile(INDEXFILE)

    def ServeFile(self, fn):
        self.send_response(200)
        self.send_header('Content-Type', GetContentType(fn))
        self.end_headers()
        with open(fn, 'r') as f:
            self.copyfile(f, self.wfile)

    def ServeCharacter(self):
        parsedParams = urlparse(self.path)
        params = parse_qs(parsedParams.query)
        if 'id' not in params or len(params['id']) < 1:
            self.Failure("No id provided")
        c = None
        try:
            c = GetCharacter(params['id'][0])
            if not c:
                self.Failure("Character not found")
            self.send_response(200)
            self.send_header('Content-Type', GetContentType('.json'))
            self.end_headers()
            self.wfile.write(json.dumps(c.ToJson()))
        except Exception:
            traceback.print_exc()
            self.Failure("Could not get character")

    def ServeRaces(self):
        try:
            races = race.GetRaceNames()
            self.send_response(200)
            self.send_header('Content-Type', GetContentType('.json'))
            self.end_headers()
            self.wfile.write(json.dumps(races))
        except Exception:
            traceback.print_exc()
            self.Failure("Could not get races")

    def ServeClasses(self):
        try:
            classes = []
            for key in config.ClassNameToId:
                classes.append({
                    'Name': key,
                    'Id': config.ClassNameToId[key]
                })
            self.send_response(200)
            self.send_header('Content-Type', GetContentType('.json'))
            self.end_headers()
            self.wfile.write(json.dumps(classes))
        except Exception:
            traceback.print_exc()
            self.Failure("Could not get classes")

    def ServeSkills(self):
        try:
            skills = []
            for key in config.SkillNameToId:
                skills.append({
                    'Name': key,
                    'Id': config.SkillNameToId[key]
                })
            self.send_response(200)
            self.send_header('Content-Type', GetContentType('.json'))
            self.end_headers()
            self.wfile.write(json.dumps(skills))
        except Exception:
            traceback.print_exc()
            self.Failure("Could not get classes")

    def ServeColors(self):
        try:
            colors = color.GetColorNames()
            self.send_response(200)
            self.send_header('Content-Type', GetContentType('.json'))
            self.end_headers()
            self.wfile.write(json.dumps(colors))
        except Exception:
            traceback.print_exc()
            self.Failure("Could not get colors")

    def ServeSpells(self):
        parsedParams = urlparse(self.path)
        params = parse_qs(parsedParams.query)
        if 'id' not in params or len(params['id']) < 1:
            self.Failure("No id provided")
        c = None
        try:
            c = GetCharacter(params['id'][0])
            if not c:
                self.Failure("Character not found")
            if 'classidx' not in params or len(params['classidx']) < 1:
                self.Failure("No class provided")
            elif 'level' not in params or len(params['level']) < 1:
                self.Failure("No level provided")
            else:
                spells = c.Classes[int(params['classidx'][0])][0].GetValidSpellsJson(int(params['level'][0]))
                domain = False
                if 'domain' in params and len(params['domain']) > 0:
                    domain = params['domain'][0] == "true"
                searchtext = ''
                if 'searchtext' in params and len(params['searchtext']) > 0:
                    searchtext = params['searchtext'][0].lower()
                i = len(spells)-1
                while i >= 0:
                    if spells[i]['Name'].lower().find(searchtext) == -1:
                        del spells[i]
                        i -= 1
                        continue
                    if domain:
                        if not spells[i]['IsDomainSpell']:
                            del spells[i]
                            i -= 1
                            continue
                    else:
                        if not spells[i]['IsNormalSpell']:
                            del spells[i]
                            i -= 1
                            continue
                    i -= 1
                self.send_response(200)
                self.send_header('Content-Type', GetContentType('.json'))
                self.end_headers()
                self.wfile.write(json.dumps(spells))
        except Exception:
            traceback.print_exc()
            self.Failure("Could not get spells")

    def ServeFeats(self):
        parsedParams = urlparse(self.path)
        params = parse_qs(parsedParams.query)
        if 'id' not in params or len(params['id']) < 1:
            self.Failure("No id provided")
        else:
            c = None
            try:
                c = GetCharacter(params['id'][0])
                if not c:
                    self.Failure("Character not found")
                feats = feat.GetValidFeats(c)
                if 'searchtext' in params and len(params['searchtext']) > 0:
                    i = len(feats)-1
                    while i >= 0:
                        if feats[i].Name.lower().find(params['searchtext'][0].lower()) == -1:
                            del feats[i]
                        i -= 1
                self.send_response(200)
                self.send_header('Content-Type', GetContentType('.json'))
                self.end_headers()
                self.wfile.write(json.dumps([f.ToJson() for f in feats]))
            except Exception:
                traceback.print_exc()
                self.Failure("Could not get feats")

    def ServeEquipableItems(self):
        parsedParams = urlparse(self.path)
        params = parse_qs(parsedParams.query)
        if 'id' not in params or len(params['id']) < 1:
            self.Failure("No id provided")
        elif 'slot' not in params or len(params['slot']) < 1:
            self.Failure("No slot provided")
        else:
            c = None
            try:
                c = GetCharacter(params['id'][0])
                if not c:
                    self.Failure("Character not found")
                slot = int(params['slot'][0])
                items = c.Inventory.GetEquipableItems(slot)
                self.send_response(200)
                self.send_header('Content-Type', GetContentType('.json'))
                self.end_headers()
                self.wfile.write(json.dumps(items))
            except Exception:
                traceback.print_exc()
                self.Failure("Could not get equipable items")


httpd = SocketServer.TCPServer(("", PORT), Handler)
print "Serving at port", PORT
httpd.serve_forever()
