
# TODO

import csv
import json


def ParseName(s):
    return s


def ParseType(s):
    return s


def ParseDescription(s):
    return s


def ParsePrerequisites(s):
    return s


def ParsePrerequisitesFeats(s):
    return s


def ParseBenefit(s):
    return s


def ParseNormal(s):
    return s


def ParseSpecial(s):
    return s


def ParseSource(s):
    return s


def ParseFulltext(s):
    return s


def ParseCritical(s):
    return s


def ParseGrit(s):
    return s


def ParseStyle(s):
    return s


def ParsePerformance(s):
    return s


def ParseRacial(s):
    return s


def ParseCompanionFamiliar(s):
    return s


def ParseRaceName(s):
    return s


def ParseNote(s):
    return s


def ParseGoal(s):
    return s


def ParseCompletionBenefit(s):
    return s


def ParseMultiples(s):
    return s


def ParseSuggestedTraits(s):
    return s


def parse():
    with open('featsDB.csv', 'rb') as f:
        reader = csv.reader(f, delimiter="\t")
        reader.next()
        i = 0
        FeatDatabase = []
        for row in reader:
            rec = {
                'id': i+1,
                'name': ParseName(row[0]),
                'type': ParseType(row[1]),
                'description': ParseDescription(row[2]),
                'prerequisites': ParsePrerequisites(row[3]),
                'prerequisites_feats': ParsePrerequisitesFeats(row[4]),
                'benefit': ParseBenefit(row[5]),
                'normal': ParseNormal(row[6]),
                'special': ParseSpecial(row[7]),
                'source': ParseSource(row[8]),
                'fulltext': ParseFulltext(row[9]),
                'critical': ParseCritical(row[10]),
                'grit': ParseGrit(row[11]),
                'style': ParseStyle(row[12]),
                'performance': ParsePerformance(row[13]),
                'racial': ParseRacial(row[14]),
                'companion_familiar': ParseCompanionFamiliar(row[15]),
                'race_name': ParseRaceName(row[16]),
                'note': ParseNote(row[17]),
                'goal': ParseGoal(row[18]),
                'completion_benefit': ParseCompletionBenefit(row[19]),
                'multiples': ParseMultiples(row[20]),
                'suggested_traits': ParseSuggestedTraits(row[21])
            }
            i += 1
            FeatDatabase.append(rec)
        with open('feats.json', 'w') as wf:
            wf.write(json.dumps(FeatDatabase))
