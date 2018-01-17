
import csv
import re
import json

import config


def ParseSchool(s):
    if s == 'conjuration':
        s = config.SCHOOL_CONJURATION
    elif s == 'enchantment':
        s = config.SCHOOL_ENCHANTMENT
    elif s == 'transmutation':
        s = config.SCHOOL_TRANSMUTATION
    elif s == 'abjuration':
        s = config.SCHOOL_ABJURATION
    elif s == 'divination':
        s = config.SCHOOL_DIVINATION
    elif s == 'necromancy':
        s = config.SCHOOL_NECROMANCY
    elif s == 'universal':
        s = config.SCHOOL_UNIVERSAL
    elif s == 'evocation':
        s = config.SCHOOL_EVOCATION
    elif s == 'illusion':
        s = config.SCHOOL_ILLUSION
    elif s == 'transformation':
        s = config.SCHOOL_TRANSFORMATION
    else:
        s = config.NONE
    return s


def ParseSubSchools(s):
    schools = []
    for i in s.split(', '):
        if i.endswith('UM'):
            i = i[:-2]
        if i.startswith(' or '):
            i = i[5:]
        if i == "":
            continue
        if i.find(' or ') > -1:
            schools.append(i[:i.find(' or ')])
            schools.append(i[i.find(' or ')+4:])
            continue
        schools.append(i)
    for i in range(len(schools)):
        if schools[i] == 'creation':
            schools[i] = config.SUBSCHOOL_CREATION
        elif schools[i] == 'compulsion':
                schools[i] = config.SUBSCHOOL_COMPULSION
        elif schools[i] == 'polymorph':
                schools[i] = config.SUBSCHOOL_POLYMORPH
        elif schools[i] == 'scrying':
                schools[i] = config.SUBSCHOOL_SCRYING
        elif schools[i] == 'glamer':
                schools[i] = config.SUBSCHOOL_GLAMER
        elif schools[i] == 'healing':
                schools[i] = config.SUBSCHOOL_HEALING
        elif schools[i] == 'charm':
                schools[i] = config.SUBSCHOOL_CHARM
        elif schools[i] == 'pattern':
                schools[i] = config.SUBSCHOOL_PATTERN
        elif schools[i] == 'summoning':
                schools[i] = config.SUBSCHOOL_SUMMONING
        elif schools[i] == 'teleportation':
                schools[i] = config.SUBSCHOOL_TELEPORTATION
        elif schools[i] == 'phantasm':
                schools[i] = config.SUBSCHOOL_PHANTASM
        elif schools[i] == 'figment':
                schools[i] = config.SUBSCHOOL_FIGMENT
        elif schools[i] == 'calling':
                schools[i] = config.SUBSCHOOL_CALLING
        elif schools[i] == 'shadow':
                schools[i] = config.SUBSCHOOL_SHADOW
        elif schools[i] == 'light':
                schools[i] = config.SUBSCHOOL_LIGHT
        elif schools[i] == 'creation':
                schools[i] = config.SUBSCHOOL_CREATION
        elif schools[i] == 'haunted':
                schools[i] = config.SUBSCHOOL_HAUNTED
        else:
            print 'Inproper Subschool:', schools[i]
    return schools


def ParseDescriptors(s):
    descriptors = []
    for i in s.split(', '):
        if i.endswith('UM'):
            i = i[:-2]
        if i.startswith(' or '):
            i = i[5:]
        j = i.split(' or ')
        for k in j:
            k = k.replace('see text', '')
            k = k.replace('see below', '')
            k = k.replace(' for lesser planar ally', '')
            k = k.replace(' for lesser planar binding', '')
            k = k.replace('or ', '')
            k = k.replace(';', '')
            k = k.replace(' ', '')
            if k == '':
                continue
            descriptors.append(k)
    for i in range(len(descriptors)):
        if descriptors[i] == 'acid':
            descriptors[i] = config.DESCRIPTOR_ACID
        elif descriptors[i] == 'mind-affecting':
            descriptors[i] = config.DESCRIPTOR_MIND_AFFECTING
        elif descriptors[i] == 'air':
            descriptors[i] = config.DESCRIPTOR_AIR
        elif descriptors[i] == 'sonic':
            descriptors[i] = config.DESCRIPTOR_SONIC
        elif descriptors[i] == 'evil':
            descriptors[i] = config.DESCRIPTOR_EVIL
        elif descriptors[i] == 'emotion':
            descriptors[i] = config.DESCRIPTOR_EMOTION
        elif descriptors[i] == 'fear':
            descriptors[i] = config.DESCRIPTOR_FEAR
        elif descriptors[i] == 'curse':
            descriptors[i] = config.DESCRIPTOR_CURSE
        elif descriptors[i] == 'force':
            descriptors[i] = config.DESCRIPTOR_FORCE
        elif descriptors[i] == 'good':
            descriptors[i] = config.DESCRIPTOR_GOOD
        elif descriptors[i] == 'fire':
            descriptors[i] = config.DESCRIPTOR_FIRE
        elif descriptors[i] == 'electricity':
            descriptors[i] = config.DESCRIPTOR_ELECTRICITY
        elif descriptors[i] == 'chaotic':
            descriptors[i] = config.DESCRIPTOR_CHAOTIC
        elif descriptors[i] == 'cold':
            descriptors[i] = config.DESCRIPTOR_COLD
        elif descriptors[i] == 'death':
            descriptors[i] = config.DESCRIPTOR_DEATH
        elif descriptors[i] == 'language-dependent':
            descriptors[i] = config.DESCRIPTOR_LANGUAGE_DEPENDENT
        elif descriptors[i] == 'light':
            descriptors[i] = config.DESCRIPTOR_LIGHT
        elif descriptors[i] == 'water':
            descriptors[i] = config.DESCRIPTOR_WATER
        elif descriptors[i] == 'darkness':
            descriptors[i] = config.DESCRIPTOR_DARKNESS
        elif descriptors[i] == 'lawful':
            descriptors[i] = config.DESCRIPTOR_LAWFUL
        elif descriptors[i] == 'earth':
            descriptors[i] = config.DESCRIPTOR_EARTH
        elif descriptors[i] == 'pain':
            descriptors[i] = config.DESCRIPTOR_PAIN
        elif descriptors[i] == 'poison':
            descriptors[i] = config.DESCRIPTOR_POISON
        elif descriptors[i] == 'shadow':
            descriptors[i] = config.DESCRIPTOR_SHADOW
        elif descriptors[i] == 'figment':
            descriptors[i] = config.DESCRIPTOR_FIGMENT
        elif descriptors[i] == 'law':
            descriptors[i] = config.DESCRIPTOR_LAW
        elif descriptors[i] == 'disease':
            descriptors[i] = config.DESCRIPTOR_DISEASE
        elif descriptors[i] == 'chaos':
            descriptors[i] = config.DESCRIPTOR_CHAOS
        elif descriptors[i] == 'variable':
            descriptors[i] = config.DESCRIPTOR_VARIABLE
        elif descriptors[i] == 'travel':
            descriptors[i] = config.DESCRIPTOR_TRAVEL
        elif descriptors[i] == 'phantasm':
            descriptors[i] = config.DESCRIPTOR_PHANTASM
        elif descriptors[i] == 'ruse':
            descriptors[i] = config.DESCRIPTOR_RUSE
        elif descriptors[i] == 'draconic':
            descriptors[i] = config.DESCRIPTOR_DRACONIC
        elif descriptors[i] == 'meditative':
            descriptors[i] = config.DESCRIPTOR_MEDITATIVE
        else:
            print 'Inproper descriptor:', descriptors[i]
    return descriptors


def IsNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def ParseCastingTime(s, n):
    amount = 0
    unit = config.NONE
    actionType = config.NONE
    if s == 'see text':
        return
    s = s.replace(',', '')
    s = s.replace(';', '')
    s = s.replace('Casting time ', '')
    s = s.replace('see text', '')
    s = s.replace('at least ', '')
    s = s.replace('/lb.', '')
    s = s.replace('/HD', '')
    s = s.split(' ')
    if IsNumber(s[0]) and int(s[0]) > 0:
        amount = int(s[0])
    elif len(s) > 1 and s[1].lower() == 'action':
        amount = 1
        unit = config.UNIT_ACTION
        if s[0].lower() == 'standard':
            actionType = config.ACTION_STANDARD
        if s[0].lower() == 'quick':
            actionType = config.ACTION_QUICK
        if s[0].lower() == 'immediate':
            actionType = config.ACTION_IMMEDIATE
        if s[0].lower() == 'swift':
            actionType = config.ACTION_SWIFT
        if s[0].lower() == 'full-round':
            actionType = config.ACTION_FULL
    if len(s) > 2 and (s[2].lower() == 'action' or s[2].lower() == 'actions'):
        unit = config.UNIT_ACTION
        if s[1].lower() == 'standard':
            actionType = config.ACTION_STANDARD
        if s[1].lower() == 'quick':
            actionType = config.ACTION_QUICK
        if s[1].lower() == 'immediate':
            actionType = config.ACTION_IMMEDIATE
        if s[1].lower() == 'swift':
            actionType = config.ACTION_SWIFT
        if s[1].lower() == 'full-round':
            actionType = config.ACTION_FULL
    elif len(s) > 2 and (s[2].lower() == 'round' or s[2].lower() == 'rounds'):
        unit = config.UNIT_ROUND
    elif len(s) > 1:
        if s[1].lower() == 'minute' or s[1].lower() == 'minutes':
            unit = config.UNIT_MINUTE
        if s[1].lower() == 'round' or s[1].lower() == 'rounds':
            unit = config.UNIT_ROUND
        if s[1].lower() == 'hour' or s[1].lower() == 'hours':
            unit = config.UNIT_HOUR
        if s[1].lower() == 'day' or s[1].lower() == 'days':
            unit = config.UNIT_DAY
        if s[1].lower() == 'month' or s[1].lower() == 'months':
            unit = config.UNIT_MONTH
        if s[1].lower() == 'week' or s[1].lower() == 'weeks':
            unit = config.UNIT_WEEK
        if s[1].lower() == 'standard':
            unit = config.UNIT_ACTION
            actionType = config.ACTION_STANDARD
    if not amount:
        print 'Expecting amount:', n, s
    if not unit:
        print 'Expecting unit:', n, s
    if unit == config.UNIT_ACTION and not actionType:
        print 'Expecting action type:', n, s

    return (amount, unit, actionType)


def ParseComponents(s):
    r = re.compile(r'(?:[^,(]|\([^)]*\))+')
    components = r.findall(s)
    ret = [False, False, [False, []], [False, []], [False, []]]
    for i in components:
        i = i.strip()
        if i.lower().startswith('v'):
            ret[0] = True
        elif i.lower().startswith('s'):
            ret[1] = True
        elif i.lower() == 'm':
            ret[2][0] = True
        elif i.lower() == 'f' or i.lower() == 'af':
            ret[3][0] = True
        elif i.lower() == 'df':
            ret[4][0] = True
        elif i.lower() == 'm/df':
            ret[2][0] = True
            ret[4][0] = True
        elif i.lower() == 'f/df':
            ret[3][0] = True
            ret[4][0] = True
        elif i.lower().startswith('m ('):
            ret[2][0] = True
            ret[2][1] = [i[i.find('(')+1:i.find(')')]]
        elif i.lower().startswith('f (') or i.lower().startswith('af ('):
            ret[3][0] = True
            ret[3][1] = [i[i.find('(')+1:i.find(')')]]
        elif i.lower().startswith('df ('):
            ret[4][0] = True
            ret[4][1] = [i[i.find('(')+1:i.find(')')]]
        elif i.lower().startswith('m/df (') or i.lower().startswith('df/m (') or i.lower().startswith('df or m'):
            ret[2][0] = True
            ret[2][1] = [i[i.find('(')+1:i.find(')')]]
            ret[4][0] = True
            ret[4][1] = [i[i.find('(')+1:i.find(')')]]
        elif i.lower().startswith('f/df (') or i.lower().startswith('df/f ('):
            ret[3][0] = True
            ret[3][1] = [i[i.find('(')+1:i.find(')')]]
            ret[4][0] = True
            ret[4][1] = [i[i.find('(')+1:i.find(')')]]
        else:
            print 'Component Not found:', i, s
    return ret


def ParseRange(s):
    ret = {}
    s = s.replace(' (see text)', '')
    s = s.replace(' (object)', '')
    s = s.replace('see text', '')
    s = s.replace(';', '')
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace('feet', 'ft')
    s = s.replace('miles', 'mile')
    s = s.replace('levels', 'level')
    s = s.replace('caster level', 'level')
    s = s.replace('half-elf only', '')
    s = s.replace('up to', '')
    s = s.replace('plus', '+')
    s = s.replace('f t', 'ft')
    s = s.split('(')
    ret['distance'] = 0
    ret['distanceUnit'] = config.UNIT_FEET
    ret['additional'] = 0
    ret['perlevel'] = 0
    s[0] = s[0].strip()
    if s[0].lower() == 'close' or s[0].lower() == 'medium' or s[0].lower() == 'long' or s[0].lower() == 'short':
        s.pop(0)
    if s[0] == '':
        return ret
    if len(s) > 1:
        s[1] = s[1][:-1]
        s[1] = s[1].strip()
        if s[1] == '':
            s.pop(1)
    parsed1 = False
    parsed2 = len(s) == 1
    if s[0].lower() == 'touch':
        ret['touch'] = True
        parsed1 = True
        if len(s) == 1:
            return ret
    elif s[0].lower() == 'personal':
        ret['personal'] = True
        parsed1 = True
        if len(s) == 1:
            return ret
    elif s[0].lower() == 'you':
        ret['personal'] = True
        parsed1 = True
        if len(s) == 1:
            return ret
    elif s[0].lower() == 'unlimited':
        ret['unlimited'] = True
        parsed1 = True
        if len(s) == 1:
            return ret
    else:
        spl = s[0].split('or')
        for i in spl:
            i = i.strip()
            if i.lower() == 'touch':
                ret['touch'] = True
                parsed1 = True
            elif i.lower() == 'personal':
                ret['personal'] = True
                parsed1 = True
        if parsed1 and len(s) == 1:
            return ret
        spl = s[0].split('and')
        for i in spl:
            i = i.strip()
            if i.lower() == 'touch':
                ret['touch'] = True
                parsed1 = True
            elif i.lower() == 'personal':
                ret['personal'] = True
                parsed1 = True
        if parsed1 and len(s) == 1:
            return ret
        if len(s) == 1:
            r = re.compile(r'[0-9]+ ft$')
            if r.match(s[0].lower()):
                ret['distanceUnit'] = config.UNIT_FEET
                ret['distance'] = int(s[0][:s[0].find(' ')])
                parsed1 = True
            if parsed1 and len(s) == 1:
                return ret
            r = re.compile(r'[0-9]+ mile$')
            if r.match(s[0].lower()):
                ret['distanceUnit'] = config.UNIT_MILE
                ret['distance'] = int(s[0][:s[0].find(' ')])
                parsed1 = True
            if parsed1 and len(s) == 1:
                return ret
            r = re.compile(r'[0-9]+ hex$')
            if r.match(s[0].lower()):
                ret['distanceUnit'] = config.UNIT_HEX
                ret['distance'] = int(s[0][:s[0].find(' ')])
                parsed1 = True
            if parsed1 and len(s) == 1:
                return ret
            r = re.compile(r'(([0-9]+) ?(ft|mile) ?\+ ?)?(([0-9]+) ?(ft|mile) ?/([0-9]+)? ?level)?')
            m = r.match(s[0].lower())
            if m:
                ret['distance'] = int(m.groups()[1]) if m.groups()[1] else 0
                ret['distanceUnit'] = m.groups()[2] if m.groups()[2] else (m.groups()[5] if m.groups()[5] else 'ft')
                if ret['distanceUnit'] == 'ft':
                    ret['distanceUnit'] = config.UNIT_FEET
                elif ret['distanceUnit'] == 'mile':
                    ret['distanceUnit'] = config.UNIT_MILE
                else:
                    print 'Unexpected Range:', s
                    return ret
                ret['additional'] = int(m.groups()[4]) if m.groups()[4] else 0
                ret['perlevel'] = int(m.groups()[6]) if m.groups()[6] else 0
                parsed1 = True
            if parsed1 and len(s) == 1:
                return ret
        else:
            r = re.compile(r'(([0-9]+) ?(ft|mile) ?\+ ?)?(([0-9]+) ?(ft|mile) ?/([0-9]+)? ?(level))?')
            m = r.match(s[1].lower())
            if m:
                ret['distance'] = int(m.groups()[1]) if m.groups()[1] else 0
                ret['distanceUnit'] = m.groups()[2] if m.groups()[2] else (m.groups()[5] if m.groups()[5] else 'ft')
                if ret['distanceUnit'] == 'ft':
                    ret['distanceUnit'] = config.UNIT_FEET
                elif ret['distanceUnit'] == 'mile':
                    ret['distanceUnit'] = config.UNIT_MILE
                else:
                    print 'Unexpected Range:', s
                    return ret
                ret['additional'] = int(m.groups()[4]) if m.groups()[4] else 0
                ret['perlevel'] = int(m.groups()[6]) if m.groups()[6] else (1 if m.groups()[7] else 0)
                parsed2 = True
    if (not parsed1) or (not parsed2):
        print 'Unexpected Range:', s
    return ret


def FormatReplacement(d):
    return "//[{}] + [{}] / [{}]:({})({})({})//".format(d['base'], d['add'], d['per'], d['unit'], d['min'], d['max'])


# This will be used to replace things. The format:
# //[BASE] + [ADDITIONAL] / [PERLEVEL]:(UNIT)(MINIMUM)(MAXIMUM)//
def ParseArea(s):
    changes = []
    base = 0
    add = 0
    per = 0
    unit = 'ft'
    minimum = -99999
    maximum = 99999
    s = s.replace('-', ' ')
    s = s.replace(' (see text)', '')
    s = s.replace(' (object)', '')
    s = s.replace('see text', '')
    s = s.replace(';', '')
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace('feet', 'ft')
    s = s.replace('foot', 'ft')
    s = s.replace('miles', 'mile')
    s = s.replace('levels', 'level')
    s = s.replace('caster level', 'level')
    s = s.replace('half-elf only', '')
    s = s.replace('up to', '')
    s = s.replace('plus', '+')
    s = s.replace('f t', 'ft')
    s = s.replace(' one or more', 'multiple')
    s = s.replace(' one', ' 1')
    s = s.replace(' two', ' 2')
    s = s.replace(' three', ' 3')
    s = s.replace(' four', ' 4')
    s = s.replace(' seven', ' 5')
    s = s.strip()
    original = s
    # r = re.compile(r'([0-9]+)? ([0-9]+) ?(ft|mile|square|cube) ?(\+)?(([a-z]+)? ?/( [0-9]+)? (level))? ?([a-z]+)? ?([a-z]+)?')
    # r = re.compile(r'([0-9]+)? ([0-9]+) ?(ft|mile|square|cube) ([a-z]+) ?/? ?([0-9]+)? ?(level)')
    exp = r'((([0-9]+)? ([0-9]+) ?([A-z]+ )+ ? ?\+ ?)?([0-9]+)? ([0-9]+) ?([A-z ]+)([Pp]er|/)(([0-9]+) ?)?level)'
    '''
    Groups:
        0: Whole String
        1: Whole Base
        2: Base Amount
        3: Base Unit Number Part (or Base Amount if empty)
        4: Base Unit String Part
        5: Add Amount
        6: Add Unit Number Part (or Add Amount if empty)
        7: Add Unit String Part
        8: Slash or Per, for division
        9: Per Level, without space
        10: Per Level, with possible space
    '''
    r = re.compile(exp)
    m = r.finditer(s)
    for i in m:
        if i.groups()[2]:
            base = int(i.groups()[2])
        elif i.groups()[3]:
            base = int(i.groups()[3])
        else:
            base = 0
        if i.groups()[2] and i.groups()[3] and i.groups()[4]:
            unit = i.groups()[3] + " " + i.groups()[4]
        elif not i.groups()[2] and i.groups()[4]:
            unit = i.groups()[4]
        elif i.groups()[5] and i.groups()[6] and i.groups()[7]:
            unit = i.groups()[6] + " " + i.groups()[7]
        else:
            unit = i.groups()[7]
        if i.groups()[5]:
            add = int(i.groups()[5])
        else:
            add = int(i.groups()[6])
        if i.groups()[9]:
            per = int(i.groups()[9])
        else:
            per = 1
        changes.append([i.groups()[0], {"base": base, 'add': add, 'per': per, 'unit': unit, 'min': minimum, 'max': maximum}])
        original = original.replace(changes[len(changes)-1][0], FormatReplacement(changes[len(changes)-1][1]))
    return original


def ParseEffects(s):
    # TODO
    return s


def ParseTargets(s):
    # TODO
    return s


def ParseDuration(s):
    # Amount, PerLevel, Unit
    ret = [0, 0, config.NONE]

    s = s.replace('min.', 'minute')
    s = s.replace('.', '')
    s = s.replace('?', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace(';', '')
    s = s.replace('one ', '1')
    s = s.replace('One ', '1')
    s = s.replace('1day', '1 day')
    s = s.replace('1usage', '1 day')
    s = s.replace('1week', '1 day')
    s = s.replace('caster level', 'level')
    s = s.replace(',', '')
    s = s.replace('/ ', '/')
    s = s.replace('up to', '')
    s = s.replace(' (D)', '')
    s = s.replace('/minutes', ' minutes')
    s = s.replace('/round', ' round')
    s = s.replace('per level', '/level')
    s = s.replace(' D', '')
    s = s.replace('see text', '')
    s = s.replace('special', '')
    s = s.replace('see below', '')
    s = s.replace('See text', '')
    s = s.replace('no more than', '')
    s = s.replace('full round', 'round')
    s = s.replace('or more ', '')
    s = re.sub(r'[0-9]+d[0-9]+(\+[0-9]+)?', '-1', s)
    s = s.strip()
    if s == '':
        return ret

    original = s
    if s.lower().startswith('concentration'):
        ret[2] = config.UNIT_CONCENTRATION
        return ret
    if s.lower().startswith('until'):
        ret[2] = config.UNIT_UNTIL
        return ret
    if s.lower().startswith('instantaneous') or s.lower().startswith('instantiations') or s.lower().startswith('instant'):
        ret[2] = config.UNIT_INSTANTANEOUS
        return ret
    if s.find(' ') > -1:
        s = [s[:s.find(" ")], s[s.find(' ')+1:]]
    else:
        s = [s]
    try:
        i = int(s[0])
        ret[0] = i
        if len(s) > 1:
            s = s[1].split('/')
            if s[0].lower() == 'instantaneous' or s[0].lower() == 'instantiations':
                ret[2] = config.UNIT_INSTANTANEOUS
                return ret
            if len(s) > 1:
                s[1] = s[1].split(' ')
            if len(s) > 1 and s[1][0].strip() == 'level':
                ret[1] = 1
            elif len(s) > 1 and len(s[1]) > 1 and (s[1][1].lower() == 'level' or s[1][1].lower() == 'levels'):
                try:
                    i = int(s[1][0])
                    ret[1] = i
                except ValueError:
                    print 'Unexpected Duration:', original
            s = s[0].split(' ')
            if s[0].lower() == 'hour' or s[0].lower() == 'hours':
                ret[2] = config.UNIT_HOUR
            elif s[0].lower() == 'round' or s[0].lower() == 'rounds':
                ret[2] = config.UNIT_ROUND
            elif s[0].lower() == 'minute' or s[0].lower() == 'minutes' or s[0].lower() == 'min':
                ret[2] = config.UNIT_MINUTE
            elif s[0].lower() == 'day' or s[0].lower() == 'days':
                ret[2] = config.UNIT_DAY
            elif s[0].lower() == 'year' or s[0].lower() == 'years':
                ret[2] = config.UNIT_YEAR
            elif s[0].lower() == 'week' or s[0].lower() == 'weeks':
                ret[2] = config.UNIT_WEEK
            elif s[0].lower() == 'month' or s[0].lower() == 'months':
                ret[2] = config.UNIT_MONTH
            elif s[0].lower() == 'battle' or s[0].lower() == 'battles':
                ret[2] = config.UNIT_BATTLE
            elif s[0].lower() == 'usage' or s[0].lower() == 'usages':
                ret[2] = config.UNIT_USAGE
            else:
                print 'Unexpected Duration:', original, s
    except ValueError:
        if s[0].lower() == 'permanent':
            ret[2] = config.UNIT_PERMANENT
        elif s[0].lower() == 'instantaneous' or s[0].lower() == 'instantiations':
            ret[2] = config.UNIT_INSTANTANEOUS
        else:
            print 'Unexpected Duration:', original

    return ret


def ParseSavingThrow(s):
    types = []
    if s == '' or s == 'none':
        return types
    else:
        s = s.split(' ')
        for i in range(len(s)):
            s[i] = s[i].replace('.', '')
            s[i] = s[i].replace(';', '')
            s[i] = s[i].replace('(', '')
            s[i] = s[i].replace(')', '')
            s[i] = s[i].replace(',', '')
            s[i] = s[i].replace(' ', '')
            s[i] = s[i].replace('see', '')
            s[i] = s[i].replace('text', '')
            s[i] = s[i].replace('object', '')
            s[i] = s[i].replace('none', '')
        start = 0
        while start < len(s):
            if start < len(s) and not (s[start].lower() != 'fortitude' and s[start].lower() != 'fort' and s[start].lower() != 'reflex' and s[start].lower() != 'will'):
                if start >= len(s):
                    return types
                t = config.NONE
                if s[start].lower() == 'fortitude' or s[start].lower() == 'fort':
                    t = config.SAVING_THROW_FORTITUDE
                if s[start].lower() == 'will':
                    t = config.SAVING_THROW_WILL
                if s[start].lower() == 'reflex':
                    t = config.SAVING_THROW_REFLEX
                harmless = False
                for i in range(start+1, len(s)):
                    if not (s[i].lower() != 'fortitude' and s[i].lower() != 'fort' and s[i].lower() != 'reflex' and s[i].lower() != 'will'):
                        break
                    if s[i].lower() == 'harmless':
                        harmless = True
                        break
                action = config.NONE
                for i in range(start+1, len(s)):
                    if not (s[i].lower() != 'fortitude' and s[i].lower() != 'fort' and s[i].lower() != 'reflex' and s[i].lower() != 'will'):
                        break
                    if s[i].lower() == 'negates' or s[i].lower() == 'negate':
                        action = config.SAVING_THROW_NEGATES
                        break
                    if s[i].lower() == 'half' or s[i].lower() == 'halves':
                        action = config.SAVING_THROW_HALVES
                        break
                    if s[i].lower() == 'partial':
                        action = config.SAVING_THROW_PARTIAL
                        break
                    if s[i].lower() == 'disbelief' or s[i].lower() == 'disbelieves':
                        action = config.SAVING_THROW_DISBELIEF
                        break
                nextStart = len(s)
                for i in range(start+1, len(s)):
                    if (s[i].lower() != 'fortitude' and s[i].lower() != 'fort' and s[i].lower() != 'reflex' and s[i].lower() != 'will'):
                        nextStart = i
                        break
                start = nextStart
                if t and action:
                    types.append((t, action, harmless))
            else:
                start += 1
        return types


def ParseSpellResistance(s):
    if s == '':
        return (False, True)
    else:
        s = s.split(' (')
        if len(s) > 1:
            return (s[0] == "yes", s[1][:-1] == "harmless")
        else:
            return (s[0] == "yes", False)


def FormatDice(d, pointsOfDamageString):
    return "//[{}] d [{}] / [{}] + [{}] / [{}]//{}".format(d['rolls'], d['sides'], d['per'], d['add'], d['addper'], (" " + pointsOfDamageString if pointsOfDamageString else ''))


# This will be used to replace things. For Non-Rolls:
# //[BASE] + [ADDITIONAL] / [PERLEVEL]:(UNIT)(MINIMUM)(MAXIMUM)//
# For Rolls. Additional is either "level" to add the level, or a number:
# //[NumRolls] d [Sides] / [PERLEVEL] + [ADDITIONAL] / [ADDITIONALPERLEVEL]//
def ParseDescription(s):
    changes = []
    rolls = 1
    sides = 1
    per = 0
    add = 0
    addper = 0
    s = s.replace('-', ' ')
    s = s.replace(' (see text)', '')
    s = s.replace(' (object)', '')
    s = s.replace('see text', '')
    s = s.replace('ft.', '')
    s = s.replace('feet', 'ft')
    s = s.replace('foot', 'ft')
    s = s.replace('miles', 'mile')
    s = s.replace('levels', 'level')
    s = s.replace('caster level', 'level')
    s = s.replace('f t', 'ft')
    s = s.replace(' one or more', 'multiple')
    s = s.replace(' one', ' 1')
    s = s.replace(' two', ' 2')
    s = s.replace(' three', ' 3')
    s = s.replace(' four', ' 4')
    s = s.replace(' seven', ' 5')
    s = s.replace('plus', '+')
    s = s.replace('point ', '')
    s = s.strip()
    original = s

    exp = r'(([0-9]+)d([0-9]+) ?(points of ([A-z]+ )?damage )?(((per|/) ?([0-9]+ ?)level)|(\+ ?((level)|(([0-9]+) ?(per|/) ?([0-9]+ ?)level)))))'
    '''
    Groups:
        0: Whole String
        1: Rolls
        2: Sides
        3: Points of damage string
        4: Damage type
        5: Either Whole Per Level or Whole Additional
        6: Whole Per Level
        7: Per or Slash, for division
        8: Die Per Level
        9: Whole Addition
        10: Either "+ Level" or Addition
        11: Level *Use to check if adding level
        12: Level or Addition String
        13: Addition
        14: Per or Slash, for division
        15: Addition Per Level
    '''
    r = re.compile(exp)
    m = r.finditer(s)
    for i in m:
        rolls = int(i.groups()[1].strip())
        sides = int(i.groups()[2].strip())
        if i.groups()[8]:
            per = (i.groups()[8].strip())
        if i.groups()[11]:
            add = 'level'
        if i.groups()[13]:
            add = int(i.groups()[13].strip())
        if i.groups()[15]:
            addper = int(i.groups()[15].strip())
        changes.append([i.groups()[0], {'rolls': rolls, 'sides': sides, 'per': per, 'add': add, 'addper': addper}])
        original = original.replace(changes[len(changes)-1][0], FormatDice(changes[len(changes)-1][1], i.groups()[3]))

    base = 0
    add = 0
    per = 0
    unit = 'ft'
    minimum = -99999
    maximum = 99999

    exp = r'((([0-9]+)? ([0-9]+) ?([A-z]+ )+ ? ?\+ ?)?([0-9]+)? ([0-9]+) ?([A-z ]+)([Pp]er|/)(([0-9]+) ?)?level)'
    '''
    Groups:
        0: Whole String
        1: Whole Base
        2: Base Amount
        3: Base Unit Number Part (or Base Amount if empty)
        4: Base Unit String Part
        5: Add Amount
        6: Add Unit Number Part (or Add Amount if empty)
        7: Add Unit String Part
        8: Slash or Per, for division
        9: Per Level, without space
        10: Per Level, with possible space
    '''
    r = re.compile(exp)
    m = r.finditer(s)
    for i in m:
        # print
        # print s
        # print i.groups()
        if i.groups()[2]:
            base = int(i.groups()[2])
        elif i.groups()[3]:
            base = int(i.groups()[3])
        else:
            base = 0
        if i.groups()[2] and i.groups()[3] and i.groups()[4]:
            unit = i.groups()[3] + " " + i.groups()[4]
        elif not i.groups()[2] and i.groups()[4]:
            unit = i.groups()[4]
        elif i.groups()[5] and i.groups()[6] and i.groups()[7]:
            unit = i.groups()[6] + " " + i.groups()[7]
        else:
            unit = i.groups()[7]
        if i.groups()[5]:
            add = int(i.groups()[5])
        else:
            add = int(i.groups()[6])
        if i.groups()[9]:
            per = int(i.groups()[9])
        else:
            per = 1
        changes.append([i.groups()[0], {"base": base, 'add': add, 'per': per, 'unit': unit, 'min': minimum, 'max': maximum}])
        original = original.replace(changes[len(changes)-1][0], FormatReplacement(changes[len(changes)-1][1]))
    # print original  
    return original


def ParseSource(s):
    if s == "Advanced Class Guide":
        s = config.SOURCE_ADVANCED_CLASS_GUIDE
    elif s == "Advanced Class Origins":
        s = config.SOURCE_ADVANCED_CLASS_ORIGINS
    elif s == "Advanced Race Guide":
        s = config.SOURCE_ADVANCED_RACE_GUIDE
    elif s == "Agents Of Evil":
        s = config.SOURCE_AGENTS_OF_EVIL
    elif s == "Andoran":
        s = config.SOURCE_ANDORAN
    elif s == "Animal Archive":
        s = config.SOURCE_ANIMAL_ARCHIVE
    elif s == "AP 102":
        s = config.SOURCE_AP_102
    elif s == "AP 107":
        s = config.SOURCE_AP_107
    elif s == "AP 110":
        s = config.SOURCE_AP_110
    elif s == "AP 29":
        s = config.SOURCE_AP_29
    elif s == "AP 30":
        s = config.SOURCE_AP_30
    elif s == "AP 35":
        s = config.SOURCE_AP_35
    elif s == "AP 42":
        s = config.SOURCE_AP_42
    elif s == "AP 50":
        s = config.SOURCE_AP_50
    elif s == "AP 55":
        s = config.SOURCE_AP_55
    elif s == "AP 56":
        s = config.SOURCE_AP_56
    elif s == "AP 62":
        s = config.SOURCE_AP_62
    elif s == "AP 64":
        s = config.SOURCE_AP_64
    elif s == "AP 65":
        s = config.SOURCE_AP_65
    elif s == "AP 67":
        s = config.SOURCE_AP_67
    elif s == "AP 68":
        s = config.SOURCE_AP_68
    elif s == "AP 69":
        s = config.SOURCE_AP_69
    elif s == "AP 71":
        s = config.SOURCE_AP_71
    elif s == "AP 74":
        s = config.SOURCE_AP_74
    elif s == "AP 77":
        s = config.SOURCE_AP_77
    elif s == "AP 78":
        s = config.SOURCE_AP_78
    elif s == "AP 80":
        s = config.SOURCE_AP_80
    elif s == "AP 81":
        s = config.SOURCE_AP_81
    elif s == "AP 82":
        s = config.SOURCE_AP_82
    elif s == "AP 84":
        s = config.SOURCE_AP_84
    elif s == "AP 86":
        s = config.SOURCE_AP_86
    elif s == "AP 89":
        s = config.SOURCE_AP_89
    elif s == "AP 91":
        s = config.SOURCE_AP_91
    elif s == "AP 93":
        s = config.SOURCE_AP_93
    elif s == "AP 95":
        s = config.SOURCE_AP_95
    elif s == "AP 99":
        s = config.SOURCE_AP_99
    elif s == "APG":
        s = config.SOURCE_APG
    elif s == "Arcane Anthology":
        s = config.SOURCE_ARCANE_ANTHOLOGY
    elif s == "Armor Masters Handbook":
        s = config.SOURCE_ARMOR_MASTERS_HANDBOOK
    elif s == "Black Markets":
        s = config.SOURCE_BLACK_MARKETS
    elif s == "Blood Of Shadows":
        s = config.SOURCE_BLOOD_OF_SHADOWS
    elif s == "Blood Of The Elements":
        s = config.SOURCE_BLOOD_OF_THE_ELEMENTS
    elif s == "Blood Of The Moon":
        s = config.SOURCE_BLOOD_OF_THE_MOON
    elif s == "Blood Of The Night":
        s = config.SOURCE_BLOOD_OF_THE_NIGHT
    elif s == "Book of the Dammed V1":
        s = config.SOURCE_BOOK_OF_THE_DAMMED_V1
    elif s == "Book of the Damned V2":
        s = config.SOURCE_BOOK_OF_THE_DAMNED_V2
    elif s == "Champions Of Balance":
        s = config.SOURCE_CHAMPIONS_OF_BALANCE
    elif s == "Champions Of Corruption":
        s = config.SOURCE_CHAMPIONS_OF_CORRUPTION
    elif s == "Champions Of Purity":
        s = config.SOURCE_CHAMPIONS_OF_PURITY
    elif s == "Cheliax Empire Of Devils":
        s = config.SOURCE_CHELIAX_EMPIRE_OF_DEVILS
    elif s == "Chronicle Of The Righteous":
        s = config.SOURCE_CHRONICLE_OF_THE_RIGHTEOUS
    elif s == "Classic Treasures":
        s = config.SOURCE_CLASSIC_TREASURES
    elif s == "Cohorts & Companions":
        s = config.SOURCE_COHORTS_AND_COMPANIONS
    elif s == "Condition Cards":
        s = config.SOURCE_CONDITION_CARDS
    elif s == "Demon Hunter's Handbook":
        s = config.SOURCE_DEMON_HUNTERS_HANDBOOK
    elif s == "Demons Revisited":
        s = config.SOURCE_DEMONS_REVISITED
    elif s == "Dirty Tactics Toolbox":
        s = config.SOURCE_DIRTY_TACTICS_TOOLBOX
    elif s == "Divine Anthology":
        s = config.SOURCE_DIVINE_ANTHOLOGY
    elif s == "Dragon Empires Primer":
        s = config.SOURCE_DRAGON_EMPIRES_PRIMER
    elif s == "Dragonslayer's Handbook":
        s = config.SOURCE_DRAGONSLAYERS_HANDBOOK
    elif s == "Dungeoneers Handbook":
        s = config.SOURCE_DUNGEONEERS_HANDBOOK
    elif s == "Dungeons Of Golarion":
        s = config.SOURCE_DUNGEONS_OF_GOLARION
    elif s == "Dwarves of Golarion":
        s = config.SOURCE_DWARVES_OF_GOLARION
    elif s == "Faction Guide":
        s = config.SOURCE_FACTION_GUIDE
    elif s == "Faiths & Philosophies":
        s = config.SOURCE_FAITHS_AND_PHILOSOPHIES
    elif s == "Faiths Of Corruption":
        s = config.SOURCE_FAITHS_OF_CORRUPTION
    elif s == "Faiths Of Purity":
        s = config.SOURCE_FAITHS_OF_PURITY
    elif s == "Familiar Folio":
        s = config.SOURCE_FAMILIAR_FOLIO
    elif s == "Giant Hunters Handbook":
        s = config.SOURCE_GIANT_HUNTERS_HANDBOOK
    elif s == "Gnomes Of Golarion":
        s = config.SOURCE_GNOMES_OF_GOLARION
    elif s == "Goblins Of Golarion":
        s = config.SOURCE_GOBLINS_OF_GOLARION
    elif s == "Haunted Heroes Handbook":
        s = config.SOURCE_HAUNTED_HEROES_HANDBOOK
    elif s == "Heroes Of The Streets":
        s = config.SOURCE_HEROES_OF_THE_STREETS
    elif s == "Heroes Of The Wild":
        s = config.SOURCE_HEROES_OF_THE_WILD
    elif s == "Horror Adventures":
        s = config.SOURCE_HORROR_ADVENTURES
    elif s == "Horsemen Of The Apocalypse":
        s = config.SOURCE_HORSEMEN_OF_THE_APOCALYPSE
    elif s == "Humans Of Golarion":
        s = config.SOURCE_HUMANS_OF_GOLARION
    elif s == "Inner Sea Gods":
        s = config.SOURCE_INNER_SEA_GODS
    elif s == "Inner Sea Intrigue":
        s = config.SOURCE_INNER_SEA_INTRIGUE
    elif s == "Inner Sea Magic":
        s = config.SOURCE_INNER_SEA_MAGIC
    elif s == "Inner Sea Monster Codex":
        s = config.SOURCE_INNER_SEA_MONSTER_CODEX
    elif s == "Inner Sea Races":
        s = config.SOURCE_INNER_SEA_RACES
    elif s == "Inner Sea World Guide":
        s = config.SOURCE_INNER_SEA_WORLD_GUIDE
    elif s == "Knights Of The Inner Sea":
        s = config.SOURCE_KNIGHTS_OF_THE_INNER_SEA
    elif s == "Kobolds Of Golarion":
        s = config.SOURCE_KOBOLDS_OF_GOLARION
    elif s == "Legacy Of Dragons":
        s = config.SOURCE_LEGACY_OF_DRAGONS
    elif s == "Lost Kingdoms":
        s = config.SOURCE_LOST_KINGDOMS
    elif s == "Magic Tactics Toolbox":
        s = config.SOURCE_MAGIC_TACTICS_TOOLBOX
    elif s == "Magical Marketplace":
        s = config.SOURCE_MAGICAL_MARKETPLACE
    elif s == "Melee Tactics Toolbox":
        s = config.SOURCE_MELEE_TACTICS_TOOLBOX
    elif s == "Monster Codex":
        s = config.SOURCE_MONSTER_CODEX
    elif s == "Monster Summoner's Handbook":
        s = config.SOURCE_MONSTER_SUMMONERS_HANDBOOK
    elif s == "Mythic Adventures":
        s = config.SOURCE_MYTHIC_ADVENTURES
    elif s == "Mythic Origins":
        s = config.SOURCE_MYTHIC_ORIGINS
    elif s == "Occult Adventures":
        s = config.SOURCE_OCCULT_ADVENTURES
    elif s == "Occult Mysteries":
        s = config.SOURCE_OCCULT_MYSTERIES
    elif s == "Occult Origins":
        s = config.SOURCE_OCCULT_ORIGINS
    elif s == "Occult Realms":
        s = config.SOURCE_OCCULT_REALMS
    elif s == "Orcs of Golarion":
        s = config.SOURCE_ORCS_OF_GOLARION
    elif s == "Osirion, Legacy Of Pharaohs":
        s = config.SOURCE_OSIRION_LEGACY_OF_PHARAOHS
    elif s == "Paizo Blog":
        s = config.SOURCE_PAIZO_BLOG
    elif s == "Path Of The Hellknight":
        s = config.SOURCE_PATH_OF_THE_HELLKNIGHT
    elif s == "Pathfinder Society Field Guide":
        s = config.SOURCE_PATHFINDER_SOCIETY_FIELD_GUIDE
    elif s == "Pathfinder Society Primer":
        s = config.SOURCE_PATHFINDER_SOCIETY_PRIMER
    elif s == "People Of The North":
        s = config.SOURCE_PEOPLE_OF_THE_NORTH
    elif s == "People Of The River":
        s = config.SOURCE_PEOPLE_OF_THE_RIVER
    elif s == "People Of The Sands":
        s = config.SOURCE_PEOPLE_OF_THE_SANDS
    elif s == "People Of The Stars":
        s = config.SOURCE_PEOPLE_OF_THE_STARS
    elif s == "PFRPG Core":
        s = config.SOURCE_P_F_R_P_G_CORE
    elif s == "PFS S3-09":
        s = config.SOURCE_PFS_S3_09
    elif s == "Pirates Of The Inner Sea":
        s = config.SOURCE_PIRATES_OF_THE_INNER_SEA
    elif s == "Planes Of Power":
        s = config.SOURCE_PLANES_OF_POWER
    elif s == "Quests and Campaigns":
        s = config.SOURCE_QUESTS_AND_CAMPAIGNS
    elif s == "Ranged Tactics Toolbox":
        s = config.SOURCE_RANGED_TACTICS_TOOLBOX
    elif s == "Rival Guide":
        s = config.SOURCE_RIVAL_GUIDE
    elif s == "RotRL-AE-Appendix":
        s = config.SOURCE_ROT_R_L_A_E_APPENDIX
    elif s == "Sargava":
        s = config.SOURCE_SARGAVA
    elif s == "Spymaster's Handbook":
        s = config.SOURCE_SPYMASTERS_HANDBOOK
    elif s == "Technology Guide":
        s = config.SOURCE_TECHNOLOGY_GUIDE
    elif s == "The Dragon's Demand":
        s = config.SOURCE_THE_DRAGONS_DEMAND
    elif s == "The HarrowHandbook":
        s = config.SOURCE_THE_HARROW_HANDBOOK
    elif s == "Ultimate Combat":
        s = config.SOURCE_ULTIMATE_COMBAT
    elif s == "Ultimate Intrigue":
        s = config.SOURCE_ULTIMATE_INTRIGUE
    elif s == "Ultimate Magic":
        s = config.SOURCE_ULTIMATE_MAGIC
    elif s == "Undead Slayer's Handbook":
        s = config.SOURCE_UNDEAD_SLAYERS_HANDBOOK
    else:
        s = config.NONE
    return s


def ParseSpellLevels(arr, n):
    ret = []
    if arr[0] != 'NULL' and int(arr[0]) >= 0:
        ret.append((config.CLASS_SORCERER, int(arr[0])))
    if arr[1] != 'NULL' and int(arr[1]) >= 0:
        ret.append((config.CLASS_WIZARD, int(arr[1])))
    if arr[2] != 'NULL' and int(arr[2]) >= 0:
        ret.append((config.CLASS_CLERIC, int(arr[2])))
    if arr[3] != 'NULL' and int(arr[3]) >= 0:
        ret.append((config.CLASS_DRUID, int(arr[3])))
    if arr[4] != 'NULL' and int(arr[4]) >= 0:
        ret.append((config.CLASS_RANGER, int(arr[4])))
    if arr[5] != 'NULL' and int(arr[5]) >= 0:
        ret.append((config.CLASS_BARD, int(arr[5])))
    if arr[6] != 'NULL' and int(arr[6]) >= 0:
        ret.append((config.CLASS_PALADIN, int(arr[6])))
    if arr[7] != 'NULL' and int(arr[7]) >= 0:
        ret.append((config.CLASS_ALCHEMIST, int(arr[7])))
    if arr[8] != 'NULL' and int(arr[8]) >= 0:
        ret.append((config.CLASS_SUMMONER, int(arr[8])))
    if arr[9] != 'NULL' and int(arr[9]) >= 0:
        ret.append((config.CLASS_WITCH, int(arr[9])))
    if arr[10] != 'NULL' and int(arr[10]) >= 0:
        ret.append((config.CLASS_INQUISITOR, int(arr[10])))
    if arr[11] != 'NULL' and int(arr[11]) >= 0:
        ret.append((config.CLASS_ORACLE, int(arr[11])))
    if arr[12] != 'NULL' and int(arr[12]) >= 0:
        ret.append((config.CLASS_ANTIPALADIN, int(arr[12])))
    if arr[13] != 'NULL' and int(arr[13]) >= 0:
        ret.append((config.CLASS_MAGUS, int(arr[13])))
    if arr[14] != 'NULL' and int(arr[14]) >= 0:
        ret.append((config.CLASS_ADEPT, int(arr[14])))
    return ret


def parse():
    with open('spelldb.csv', 'rb') as f:
        reader = csv.reader(f, delimiter="\t")
        reader.next()
        i = 0
        SpellDatabase = []
        for row in reader:
            ct = ParseCastingTime(row[5], row[0])
            rec = {
                'id': i+1,
                'name': row[0],
                'school': ParseSchool(row[1]),
                'subschools': ParseSubSchools(row[2]),
                'descriptors': ParseDescriptors(row[3]),
                'casting_time': ct if ct else [0, config.NONE, config.NONE],
                'components': ParseComponents(row[6]),
                'costly_materials': int(row[7]) == 1,
                'range': ParseRange(row[8]),
                'area': ParseArea(row[9]),
                'effects': ParseArea(row[10]),
                'targets': ParseTargets(row[11]),
                'duration': ParseDuration(row[12]),
                'dismissable': int(row[13]) == 1,
                'shapeable': int(row[14]) == 1,
                'saving_throw': ParseSavingThrow(row[15]),
                'spell_resistence': ParseSpellResistance(row[16]),
                'description': (ParseDescription(row[17]), row[20]),
                'source': ParseSource(row[19]),
                'spell_levels': ParseSpellLevels(row[26:], row[0])
            }
            i += 1
            SpellDatabase.append(rec)
        with open('spells.json', 'w') as wf:
            wf.write(json.dumps(SpellDatabase))
