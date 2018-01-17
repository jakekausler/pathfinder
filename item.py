
import config
import encumberance

import random


def RandomType():
    return random.choice([
        config.BODY_TYPE_AVIAN,
        config.BODY_TYPE_BIPEDCLAWED,
        config.BODY_TYPE_BIPEDHANDS,
        config.BODY_TYPE_PISCINE,
        config.BODY_TYPE_QUADRIPEDCLAWED,
        config.BODY_TYPE_QUADRIPEDHEXAPOD,
        config.BODY_TYPE_QUADRIPEDHOOVES,
        config.BODY_TYPE_QUADRIPEDSQUATBODY,
        config.BODY_TYPE_SARUIANBODY,
        config.BODY_TYPE_SERPENTINE,
        config.BODY_TYPE_VERMINOUS
    ])


class Inventory:

    def __init__(self, character, bodyType=config.BODY_TYPE_BIPEDHANDS):
        self.Character = character
        self.Gold = 0
        self.Items = []  # List of [item, quantity]
        self.Worn = BodyTypeDict[bodyType](character)

    def WearItem(self, itemIdx):
        if isinstance(self.Items[itemIdx], WearableItem):
            self.Worn.WearItem(self.Items[itemIdx])

    def RemoveWornItem(self, slot):
        self.Worn.RemoveItem(slot)

    def GetTotalWeight(self):
        return sum([item[0].Weight * item[1] for item in self.Items])

    def AddItem(self, item, qty=1):
        if self.FindIndex(item) >= 0:
            self.Items[self.FindIndex(item)][1] += qty
        self.Items.append([item, qty])

    def FindIndex(self, item):
        for i in range(len(self.Items)):
            if (self.Items[i][0] == item):
                return i
        return -1

    def TotalValue(self):
        return round(sum(i[1] * i[0].Value for i in self.Items), 2)

    def TotalWeight(self):
        return round(sum(i[1] * i[0].Weight for i in self.Items), 2)

    def ToJson(self):
        j = {}
        j['Gold'] = self.Gold
        j['Worn'] = self.Worn.ToJson()
        j['Items'] = [{'Item': i[0].ToJson(), 'Quantity': i[1]} for i in self.Items]
        j['TotalValue'] = self.TotalValue()
        j['TotalWeight'] = self.TotalWeight()
        return j

    def __str__(self):
        ret = ""
        ret += "Gold: {0:>10}\n".format(FormatMoney(self.Gold))
        ret += "\n"
        ret += "Equiped Items"
        eq = str(self.Worn)
        for line in eq.split('\n'):
            ret += '\t' + line + '\n'
        ret += "\n"
        ret += "Inventory\n"
        ret += "\t{0:^30}{1:^6}{2:^9}{3:^15}\n".format("Item", "Qty", "Weight", "Value")
        for item in self.Items:
            ret += "\t{0:<30}{1:^6}{2:^9}{3:^15}\n".format(item[0].Name, item[1], str(item[0].Weight) + " lbs", FormatMoney(item[0].Value))
        enc = encumberance.GetEncumberance(self.Character)
        if enc == config.ENCUMBERANCE_LIGHT:
            enc = "Light"
        elif enc == config.ENCUMBERANCE_MEDIUM:
            enc = "Medium"
        elif enc == config.ENCUMBERANCE_HEAVY:
            enc = "Heavy"
        else:
            enc = "Over"
        ret += "\tTotal Weight: {0:>4} ({1} Encumberance)".format(self.GetTotalWeight(), enc)
        return ret


class WornItems:

    def __init__(self, character):
        self.Items = {}

        # A dictionary of Slot Type: [Item Tag, ]
        # For example, hooved quadrapeds can only have horseshoes on thier feet
        self.SlotLimits = {}
        self.AddEmptyItemSlots()
        self.Character = character

    def AddEmptyItemSlots(self):
        for key in GetAllItemSlots():
            self.Items[key] = 0

    def WearItem(self, item, slotIndex=0):
        slot = item.ApplicableSlots[slotIndex]
        if slot in self.SlotLimits and self.SlotLimits[slot] and any(i & Item.Tags == 0 for i in self.SlotLimits[slot]):
            self.Items[slot] = item
            self.Items[slot].ApplyEffects(self.Character)

    def RemoveItem(self, slot):
        self.Items[slot].RemoveEffects(self.Character)
        self.Items[slot] = None

    def ToJson(self):
        j = {}
        j['Headband'] = self.Items[config.ITEM_SLOT_HEADBAND]
        j['Eyes'] = self.Items[config.ITEM_SLOT_EYES]
        j['Neck'] = self.Items[config.ITEM_SLOT_NECK]
        j['Chest'] = self.Items[config.ITEM_SLOT_CHEST]
        j['Armor'] = self.Items[config.ITEM_SLOT_ARMOR]
        j['Belt'] = self.Items[config.ITEM_SLOT_BELT]
        j['Wrists'] = self.Items[config.ITEM_SLOT_WRISTS]
        j['Ring1'] = self.Items[config.ITEM_SLOT_RING1]
        j['Ring2'] = self.Items[config.ITEM_SLOT_RING2]
        j['Shoulders'] = self.Items[config.ITEM_SLOT_SHOULDERS]
        j['Feet'] = self.Items[config.ITEM_SLOT_FEET]
        j['Head'] = self.Items[config.ITEM_SLOT_HEAD]
        j['Hands'] = self.Items[config.ITEM_SLOT_HANDS]
        j['Body'] = self.Items[config.ITEM_SLOT_BODY]
        return j

    def __str__(self):
        ret = ""
        for key in self.Items:
            if (self.Items[key]):
                t = ""
                if key == config.ITEM_SLOT_HEADBAND:
                    t = "Headband:"
                if key == config.ITEM_SLOT_EYES:
                    t = "Eyes:"
                if key == config.ITEM_SLOT_NECK:
                    t = "Neck:"
                if key == config.ITEM_SLOT_CHEST:
                    t = "Chest:"
                if key == config.ITEM_SLOT_ARMOR:
                    t = "Armor:"
                if key == config.ITEM_SLOT_BELT:
                    t = "Belt:"
                if key == config.ITEM_SLOT_WRISTS:
                    t = "Wrists:"
                if key == config.ITEM_SLOT_RING1:
                    t = "Ring1:"
                if key == config.ITEM_SLOT_RING2:
                    t = "Ring2:"
                if key == config.ITEM_SLOT_SHOULDERS:
                    t = "Shoulders:"
                if key == config.ITEM_SLOT_FEET:
                    t = "Feet:"
                if key == config.ITEM_SLOT_HEAD:
                    t = "Head:"
                if key == config.ITEM_SLOT_HANDS:
                    t = "Hands:"
                if key == config.ITEM_SLOT_BODY:
                    t = "Body:"
                ret += "{0:<11}{1:>20}".format(t, item.Name)
        return ret


class AvianWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetAvianItemSlots():
            self.Items[key] = None


class BipedClawedWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetBipedClawedItemSlots():
            self.Items[key] = None


class BipedHandsWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetBipedHandsItemSlots():
            self.Items[key] = None


class PiscineWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetPiscineItemSlots():
            self.Items[key] = None
        self.SlotLimits[config.ITEM_SLOT_CHEST] |= config.ITEM_TAG_SADDLE


class QuadripedClawedWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetQuadripedClawedItemSlots():
            self.Items[key] = None
        self.SlotLimits[config.ITEM_SLOT_BELT] |= config.ITEM_TAG_SADDLE


class QuadripedHexapodWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetQuadripedHexapodItemSlots():
            self.Items[key] = None
        self.SlotLimits[config.ITEM_SLOT_CHEST] |= config.ITEM_TAG_SADDLE


class QuadripedHoovesWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetQuadripedHoovesItemSlots():
            self.Items[key] = None
        self.SlotLimits[config.ITEM_SLOT_CHEST] |= config.ITEM_TAG_SADDLE
        self.SlotLimits[config.ITEM_SLOT_FEET] |= config.ITEM_TAG_HORSESHOES


class QuadripedSquatBodyWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetQuadripedSquatBodyItemSlots():
            self.Items[key] = None


class SaruianBodyWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetSaruianBodyItemSlots():
            self.Items[key] = None
        self.SlotLimits[config.ITEM_SLOT_BELT] |= config.ITEM_TAG_SADDLE


class SerpentineWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetSerpentineItemSlots():
            self.Items[key] = None


class VerminousWornItems(WornItems):

    def AddEmptyItemSlots(self):
        for key in GetVerminousItemSlots():
            self.Items[key] = None


BodyTypeDict = {
    config.BODY_TYPE_AVIAN: AvianWornItems,
    config.BODY_TYPE_BIPEDCLAWED: BipedClawedWornItems,
    config.BODY_TYPE_BIPEDHANDS: BipedHandsWornItems,
    config.BODY_TYPE_PISCINE: PiscineWornItems,
    config.BODY_TYPE_QUADRIPEDCLAWED: QuadripedClawedWornItems,
    config.BODY_TYPE_QUADRIPEDHEXAPOD: QuadripedHexapodWornItems,
    config.BODY_TYPE_QUADRIPEDHOOVES: QuadripedHoovesWornItems,
    config.BODY_TYPE_QUADRIPEDSQUATBODY: QuadripedSquatBodyWornItems,
    config.BODY_TYPE_SARUIANBODY: SaruianBodyWornItems,
    config.BODY_TYPE_SERPENTINE: SerpentineWornItems,
    config.BODY_TYPE_VERMINOUS: VerminousWornItems
}


class Item(object):

    def __init__(self, name, weight=0, value=0, tags=[]):
        self.Name = name
        self.Weight = weight
        self.Value = value
        self.Tags = tags  # Used for item slots. And together new ones

    def ToJson(self):
        j = {}
        j['Name'] = self.Name
        j['Weight'] = self.Weight
        j['Value'] = self.Value
        j['Tags'] = self.Tags
        return j

    def __eq__(self, other):
        return self.Name == other.Name


class WearableItem(Item):

    def __Init__(self):
        super(WearableItem, self).__init__()
        self.ApplicableSlots = []


def FormatMoney(num):
    gp = int(num)
    rem = num - int(num)
    rem *= 10
    sp = int(rem)
    rem = rem - int(rem)
    rem *= 10
    cp = int(round(rem))
    ret = ""
    ret += str(gp) + "gp"
    if sp:
        ret += " " + str(sp) + "sp"
    if cp:
        ret += " " + str(cp) + "cp"
    return ret


def GetAllItemSlots():
    return [config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_BELT,
            config.ITEM_SLOT_WRISTS,
            config.ITEM_SLOT_RING1,
            config.ITEM_SLOT_RING2,
            config.ITEM_SLOT_SHOULDERS,
            config.ITEM_SLOT_FEET,
            config.ITEM_SLOT_HEAD,
            config.ITEM_SLOT_HANDS
            ]


def GetAvianItemSlots():
    return [config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_BELT,
            config.ITEM_SLOT_WRISTS,
            config.ITEM_SLOT_RING1,
            config.ITEM_SLOT_RING2
            ]


def GetBipedClawedItemSlots():
    return [config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_SHOULDERS,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_BELT,
            config.ITEM_SLOT_WRISTS,
            config.ITEM_SLOT_RING1,
            config.ITEM_SLOT_RING2
            ]


def GetBipedHandsItemSlots():
    return [config.ITEM_SLOT_HEAD,
            config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_SHOULDERS,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_BODY,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_BELT,
            config.ITEM_SLOT_WRISTS,
            config.ITEM_SLOT_HANDS,
            config.ITEM_SLOT_RING1,
            config.ITEM_SLOT_RING2,
            config.ITEM_SLOT_FEET
            ]


def GetPiscineItemSlots():
    return [config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_BELT
            ]


def GetQuadripedClawedItemSlots():
    return [config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_SHOULDERS,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_BELT,
            config.ITEM_SLOT_WRISTS
            ]


def GetQuadripedHexapodItemSlots():
    return [config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_SHOULDERS,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_BELT,
            config.ITEM_SLOT_WRISTS
            ]


def GetQuadripedHoovesItemSlots():
    return [config.ITEM_SLOT_HEAD,
            config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_SHOULDERS,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_BELT,
            config.ITEM_SLOT_WRISTS,
            config.ITEM_SLOT_FEET
            ]


def GetQuadripedSquatBodyItemSlots():
    return [config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_SHOULDERS,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_WRISTS
            ]


def GetSaruianBodyItemSlots():
    return [config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_NECK,
            config.ITEM_SLOT_CHEST,
            config.ITEM_SLOT_ARMOR,
            config.ITEM_SLOT_BELT
            ]


def GetSerpentineItemSlots():
    return [config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_HEADBAND,
            config.ITEM_SLOT_BELT
            ]


def GetVerminousItemSlots():
    return [config.ITEM_SLOT_EYES,
            config.ITEM_SLOT_BELT
            ]