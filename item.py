
# TODO: Weapon and armor and ammunition extra effects
# TODO: Item materials
# TODO: Weapon and armor magical special abilities
# TODO: Allow choosing ammuntion for ranged weapons

import config
import encumberance
import roll
import size

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

    def GetEquippedWeapons(self):
        ret = []
        for slot in self.Worn.Items:
            if self.Worn.Items[slot] and isinstance(self.Worn.Items[slot], Weapon):
                ret.append(self.Worn.Items[slot])
        return ret

    def GetEquippedArmor(self):
        ret = []
        for slot in self.Worn.Items:
            if self.Worn.Items[slot] and isinstance(self.Worn.Items[slot], Armor):
                ret.append(self.Worn.Items[slot])
        return ret

    def GetEquippedShield(self):
        ret = []
        for slot in self.Worn.Items:
            if self.Worn.Items[slot] and isinstance(self.Worn.Items[slot], Shield):
                ret.append(self.Worn.Items[slot])
        return ret

    def GetEquippedMagicalProtectives(self):
        ret = []
        for slot in self.Worn.Items:
            if self.Worn.Items[slot] and isinstance(self.Worn.Items[slot], MagicalProtection):
                ret.append(self.Worn.Items[slot])
        return ret

    def WearItem(self, itemIdx, slot=config.NONE):
        if isinstance(self.Items[itemIdx][0], WearableItem):
            self.Worn.WearItem(self.Items[itemIdx][0], slot)

    def RemoveWornItem(self, slot):
        self.Worn.RemoveItem(slot)

    def RemoveItem(self, idx):
        del self.Items[idx]

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

    def GetEquipableItems(self, slot):
        items = []
        for i in range(len(self.Items)):
            if isinstance(self.Items[i][0], WearableItem):
                if self.Worn.CanWearItem(self.Items[i][0], slot):
                    items.append([self.Items[i][0].Name, i])
        return items

    def TotalValue(self):
        return round(sum(i[1] * i[0].Value for i in self.Items), 2)

    def TotalWeight(self):
        return round(sum(i[1] * i[0].Weight for i in self.Items), 2)

    def ToJson(self):
        j = {}
        j['Gold'] = self.Gold
        j['Worn'] = self.Worn.ToJson()
        j['Items'] = []
        idx = 0
        for i in self.Items:
            j['Items'].append({'Item': i[0].ToJson(), 'Quantity': i[1]})
            if isinstance(i[0], WearableItem):
                j['Items'][idx]['Item']['IsWearable'] = True
                j['Items'][idx]['Item']['PossibleLocations'] = self.Worn.WhereCanItEquip(i[0])
            idx += 1
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

SlotNames = {
    config.ITEM_SLOT_HEADBAND: 'Headband',
    config.ITEM_SLOT_EYES: 'Eyes',
    config.ITEM_SLOT_NECK: 'Neck',
    config.ITEM_SLOT_CHEST: 'Chest',
    config.ITEM_SLOT_ARMOR: 'Armor',
    config.ITEM_SLOT_BELT: 'Belt',
    config.ITEM_SLOT_WRISTS: 'Wrists',
    config.ITEM_SLOT_RING1: 'Ring1',
    config.ITEM_SLOT_RING2: 'Ring2',
    config.ITEM_SLOT_SHOULDERS: 'Shoulders',
    config.ITEM_SLOT_FEET: 'Feet',
    config.ITEM_SLOT_HEAD: 'Head',
    config.ITEM_SLOT_HANDS: 'Hands',
    config.ITEM_SLOT_BODY: 'Body',
    config.ITEM_SLOT_MAINHAND: 'Mainhand',
    config.ITEM_SLOT_OFFHAND: 'Offhand',
}


class WornItems:

    def __init__(self, character):
        # A dictionary of Slot Type: Item
        self.Items = {}

        # A dictionary of Slot Type: [Item Tag, ]
        # For example, hooved quadrapeds can only have horseshoes on thier feet
        # If the Slot Type Entry leads to a list with only 'None' in it, don't allow anything there
        self.SlotLimits = {}
        self.AddEmptyItemSlots()
        self.Character = character

    def AddEmptyItemSlots(self):
        for key in GetAllItemSlots():
            self.Items[key] = 0
        for key in GetAllItemSlots():
            self.SlotLimits[key] = []

    def WearItem(self, item, slot):
        if slot in self.Items and self.Items[slot]:
            self.RemoveItem(slot)
        if self.CanWearItem(item, slot):
            if item.CancelSlots:
                for s in item.CancelSlots:
                    if s in self.SlotLimits:
                        self.SlotLimits[s].append('None')
            self.Items[slot] = item
            self.Items[slot].ApplyEffects(self.Character)
            self.Items[slot].EquippedAtSlot = [slot, SlotNames[slot]]

    # If there is no limit on that slot, or
    #    that slot can have an item and
    #    the item has an item tag that that slot can have
    def CanWearItem(self, item, slot):
        if slot not in item.ApplicableSlots:
            return False
        if slot in self.SlotLimits:
            if self.SlotLimits[slot]:
                return any(i != 'None' and i & Item.Tags == 0 for i in self.SlotLimits[slot])
            else:
                if item.CancelSlots:
                    for s in item.CancelSlots:
                        if self.Items[s]:
                            return False
        else:
            return True

    def WhereCanItEquip(self, item):
        locations = []
        for slot in self.Items:
            if self.Items[slot]:
                continue
            if self.CanWearItem(item, slot):
                locations.append(slot)
        for i in range(len(locations)):
            locations[i] = [locations[i], SlotNames[locations[i]]]
        return locations

    def RemoveItem(self, slot):
        if self.Items[slot].CancelSlots:
            for s in self.Items[slot].CancelSlots:
                if s in self.SlotLimits:
                    self.SlotLimits[s].remove('None')
        self.Items[slot].RemoveEffects(self.Character)
        self.Items[slot].EquippedAtSlot = [-1, '']
        self.Items[slot] = None

    def ToJson(self):
        j = {}
        j['Headband'] = [config.ITEM_SLOT_HEADBAND, self.Items[config.ITEM_SLOT_HEADBAND] if not self.Items[config.ITEM_SLOT_HEADBAND] else self.Items[config.ITEM_SLOT_HEADBAND].ToJson()]
        j['Eyes'] = [config.ITEM_SLOT_EYES, self.Items[config.ITEM_SLOT_EYES] if not self.Items[config.ITEM_SLOT_EYES] else self.Items[config.ITEM_SLOT_EYES].ToJson()]
        j['Neck'] = [config.ITEM_SLOT_NECK, self.Items[config.ITEM_SLOT_NECK] if not self.Items[config.ITEM_SLOT_NECK] else self.Items[config.ITEM_SLOT_NECK].ToJson()]
        j['Chest'] = [config.ITEM_SLOT_CHEST, self.Items[config.ITEM_SLOT_CHEST] if not self.Items[config.ITEM_SLOT_CHEST] else self.Items[config.ITEM_SLOT_CHEST].ToJson()]
        j['Armor'] = [config.ITEM_SLOT_ARMOR, self.Items[config.ITEM_SLOT_ARMOR] if not self.Items[config.ITEM_SLOT_ARMOR] else self.Items[config.ITEM_SLOT_ARMOR].ToJson()]
        j['Belt'] = [config.ITEM_SLOT_BELT, self.Items[config.ITEM_SLOT_BELT] if not self.Items[config.ITEM_SLOT_BELT] else self.Items[config.ITEM_SLOT_BELT].ToJson()]
        j['Wrists'] = [config.ITEM_SLOT_WRISTS, self.Items[config.ITEM_SLOT_WRISTS] if not self.Items[config.ITEM_SLOT_WRISTS] else self.Items[config.ITEM_SLOT_WRISTS].ToJson()]
        j['Ring1'] = [config.ITEM_SLOT_RING1, self.Items[config.ITEM_SLOT_RING1] if not self.Items[config.ITEM_SLOT_RING1] else self.Items[config.ITEM_SLOT_RING1].ToJson()]
        j['Ring2'] = [config.ITEM_SLOT_RING2, self.Items[config.ITEM_SLOT_RING2] if not self.Items[config.ITEM_SLOT_RING2] else self.Items[config.ITEM_SLOT_RING2].ToJson()]
        j['Shoulders'] = [config.ITEM_SLOT_SHOULDERS, self.Items[config.ITEM_SLOT_SHOULDERS] if not self.Items[config.ITEM_SLOT_SHOULDERS] else self.Items[config.ITEM_SLOT_SHOULDERS].ToJson()]
        j['Feet'] = [config.ITEM_SLOT_FEET, self.Items[config.ITEM_SLOT_FEET] if not self.Items[config.ITEM_SLOT_FEET] else self.Items[config.ITEM_SLOT_FEET].ToJson()]
        j['Head'] = [config.ITEM_SLOT_HEAD, self.Items[config.ITEM_SLOT_HEAD] if not self.Items[config.ITEM_SLOT_HEAD] else self.Items[config.ITEM_SLOT_HEAD].ToJson()]
        j['Hands'] = [config.ITEM_SLOT_HANDS, self.Items[config.ITEM_SLOT_HANDS] if not self.Items[config.ITEM_SLOT_HANDS] else self.Items[config.ITEM_SLOT_HANDS].ToJson()]
        j['Main Hand'] = [config.ITEM_SLOT_MAINHAND, self.Items[config.ITEM_SLOT_MAINHAND] if not self.Items[config.ITEM_SLOT_MAINHAND] else self.Items[config.ITEM_SLOT_MAINHAND].ToJson()]
        j['Off Hand'] = [config.ITEM_SLOT_OFFHAND, self.Items[config.ITEM_SLOT_OFFHAND] if not self.Items[config.ITEM_SLOT_OFFHAND] else self.Items[config.ITEM_SLOT_OFFHAND].ToJson()]
        j['Body'] = [config.ITEM_SLOT_BODY, self.Items[config.ITEM_SLOT_BODY] if not self.Items[config.ITEM_SLOT_BODY] else self.Items[config.ITEM_SLOT_BODY].ToJson()]
        return j

    def __str__(self):
        ret = ""
        for key in self.Items:
            if self.Items[key]:
                t = ""
                if key in SlotNames:
                    t = SlotNames[key]
                ret += "{0:<11}{1:>20}".format(t, self.Items[key].Name)
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

    def __init__(self, name, weight=0, value=0, tags=config.NONE):
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

    def ApplyEffects(self, character):
        return

    def RemoveEffects(self, character):
        return

    def __eq__(self, other):
        return self.Name == other.Name


class WearableItem(Item):

    def __init__(self, name="", weight=0, value=0, tags=config.NONE, applicableSlots=[], cancelSlots=[]):
        super(WearableItem, self).__init__(name, weight, value, tags)
        self.ApplicableSlots = []  # List of slots in which this can be worn
        self.CancelSlots = []  # List of slots that must be empty if this can be worn
        for i in applicableSlots:
            self.ApplicableSlots.append(i)
        for i in cancelSlots:
            self.CancelSlots.append(i)
        self.EquippedAtSlot = [-1, '']

    def ToJson(self):
        ret = super(WearableItem, self).ToJson()
        ret['EquippedAtSlot'] = self.EquippedAtSlot
        return ret


class Weapon(WearableItem):

    def __init__(self, name="", value=0, weight=0, tags=config.NONE, damage=roll.Dice(4, 1, addition=1), size=size.Size(), criticalRange=[20, 20], criticalMultiplier=2, range=0, source=config.NONE, type=config.NONE, typeJoin=config.JOIN_OR, special=config.NONE, specialJoin=config.JOIN_AND, specialValue=0, isTwoHanded=False, isLight=False, isMartial=False, isExotic=False, isMasterwork=False, enchantment=0, materials=[], abilities=[], applicableSlots=[], cancelSlots=[]):
        super(Weapon, self).__init__(name, weight, value, tags, applicableSlots, cancelSlots)
        self.Size = size
        self.Damage = self.DamageBySize(damage)
        self.Weight = self.WeightBySize(self.Weight)
        self.CriticalRange = criticalRange
        self.CriticalMultiplier = criticalMultiplier
        self.Range = range
        self.Type = type
        self.TypeJoin = typeJoin
        self.Special = special
        self.SpecialJoin = specialJoin
        self.SpecialValue = specialValue  # Used for strength weapons
        self.Source = source
        if isTwoHanded:
            self.CancelSlots.append(config.ITEM_SLOT_MAINHAND)
            self.CancelSlots.append(config.ITEM_SLOT_OFFHAND)
        self.Light = isLight
        self.Martial = isMartial
        self.Exotic = isExotic
        self.Masterwork = isMasterwork
        self.Enchantment = enchantment
        self.Effects = []
        self.Materials = []
        self.Abilities = []
        self.CanThrow = False
        self.Value = self.GetValue()

    def GetValue(self):
        # TODO: Apply materials, masterwork, size, enchantments
        return self.Value

    def Use(self, character):
        return

    def DamageBySize(self, damage):
        if self.Size.ID == config.SIZE_MEDIUM:
            return damage
        elif self.Size.ID == config.SIZE_TINY:
            return config.WeaponDamageDieOrder[damage][0]
        elif self.Size.ID == config.SIZE_SMALL:
            return config.WeaponDamageDieOrder[damage][1]
        elif self.Size.ID == config.SIZE_LARGE:
            return config.WeaponDamageDieOrder[damage][2]
        else:
            return roll.Dice(4, 0)

    def GetEnchantmentBonus(self):
        return max((1 if self.Masterwork else 0), self.Enchantment)

    def GetDamage(self):
        dmg = self.Damage.Copy()
        dmg.addition += self.GetEnchantmentBonus()
        return dmg

    def GetAttack(self, character):
        attack = character.MeleeAttack() + self.GetEnchantmentBonus()
        if not character.Race.IsProficient(self):
            attack -= 4
        for i in character.Inventory.GetEquippedArmor():
            if not character.Race.IsProficient(i):
                attack -= i.GetArmorCheckPenalty()
        for i in character.Inventory.GetEquippedShield():
            if not character.Race.IsProficient(i):
                attack -= i.GetArmorCheckPenalty()
        return attack

    def GetAbilityModifier(self, character):
        if self.EquippedAtSlot[0] == config.ITEM_SLOT_MAINHAND:
            return character.AbilityModifiers()[config.ABILITY_STRENGTH]
        else:
            return character.AbilityModifiers()[config.ABILITY_STRENGTH]/2

    def GetAttackDamage(self, character):
        dmg = self.Damage.Copy()
        dmg.addition += self.GetAbilityModifier(character)
        return dmg

    def GetCritical(self):
        crit = ''
        if not(self.CriticalRange[1] == 20 and self.CriticalRange[0] == 20):
            crit += str(self.CriticalRange[0]) + '-' + str(self.CriticalRange[1]) + '/'
        return crit + 'x' + str(self.CriticalMultiplier)

    def GetRange(self):
        return self.Range

    def GetEffects(self):
        return self.Effects

    def WeightBySize(self, weight):
        return self.Size.CarryingCapacity * weight

    def IsBludgeoning(self):
        return self.Type & config.WEAPON_TYPE_BLUDGEONING != 0

    def IsSlashing(self):
        return self.Type & config.WEAPON_TYPE_SLASHING != 0

    def IsPeircing(self):
        return self.Type & config.WEAPON_TYPE_PEIRCING != 0

    def IsBlocking(self):
        return self.Special & config.WEAPON_SPECIAL_BLOCKING != 0

    def IsBrace(self):
        return self.Special & config.WEAPON_SPECIAL_BRACE != 0

    def IsDeadly(self):
        return self.Special & config.WEAPON_SPECIAL_DEADLY != 0

    def IsDisarm(self):
        return self.Special & config.WEAPON_SPECIAL_DISARM != 0

    def IsDistracting(self):
        return self.Special & config.WEAPON_SPECIAL_DISTRACTING != 0

    def IsDouble(self):
        return self.Special & config.WEAPON_SPECIAL_DOUBLE != 0

    def IsFragile(self):
        return self.Special & config.WEAPON_SPECIAL_FRAGILE != 0

    def IsGrapple(self):
        return self.Special & config.WEAPON_SPECIAL_GRAPPLE != 0

    def IsMonk(self):
        return self.Special & config.WEAPON_SPECIAL_MONK != 0

    def IsNonlethal(self):
        return self.Special & config.WEAPON_SPECIAL_NONLETHAL != 0

    def IsPerformance(self):
        return self.Special & config.WEAPON_SPECIAL_PERFORMANCE != 0

    def IsReach(self):
        return self.Special & config.WEAPON_SPECIAL_REACH != 0

    def IsStrength(self):
        return self.Special & config.WEAPON_SPECIAL_STRENGTH != 0

    def IsSunder(self):
        return self.Special & config.WEAPON_SPECIAL_SUNDER != 0

    def IsTrip(self):
        return self.Special & config.WEAPON_SPECIAL_TRIP != 0

    def ToJson(self):
        item = super(Weapon, self).ToJson()
        item['Bludgeoning'] = self.IsBludgeoning()
        item['Slashing'] = self.IsSlashing()
        item['Peircing'] = self.IsPeircing()
        item['Blocking'] = self.IsBlocking()
        item['Brace'] = self.IsBrace()
        item['Deadly'] = self.IsDeadly()
        item['Disarm'] = self.IsDisarm()
        item['Distracting'] = self.IsDistracting()
        item['Double'] = self.IsDouble()
        item['Fragile'] = self.IsFragile()
        item['Grapple'] = self.IsGrapple()
        item['Monk'] = self.IsMonk()
        item['Nonlethal'] = self.IsNonlethal()
        item['Performance'] = self.IsPerformance()
        item['Reach'] = self.IsReach()
        item['Strength'] = self.IsStrength()
        item['Sunder'] = self.IsSunder()
        item['Trip'] = self.IsTrip()
        item['Size'] = self.Size.Name
        item['Damage'] = self.Damage.ToJson()
        item['Weight'] = self.Weight
        item['Critical'] = self.GetCritical()
        item['Range'] = self.Range
        item['Type'] = self.Type
        item['TypeJoin'] = self.TypeJoin
        item['Special'] = self.Special
        item['SpecialJoin'] = self.SpecialJoin
        item['SpecialValue'] = self.SpecialValue
        item['Source'] = self.Source
        item['Light'] = self.Light
        item['Martial'] = self.Martial
        item['Exotic'] = self.Exotic
        item['Masterwork'] = self.Masterwork
        item['Enchantment'] = self.Enchantment
        item['Effects'] = [i.ToJson() for i in self.Effects]
        item['Materials'] = [i.ToJson() for i in self.Materials]
        item['Abilities'] = [i.ToJson() for i in self.Abilities]
        return item


class UnarmedMeleeWeapon(Weapon):

    def __init__(self, name="", weight=0, value=0, tags=config.NONE, damage=roll.Dice(4, 0, addition=1), size=size.Size(), criticalRange=[20, 20], criticalMultiplier=2, range=5, source=config.NONE, type=config.NONE, typeJoin=config.JOIN_OR, special=config.NONE, specialJoin=config.JOIN_AND, specialValue=0, isTwoHanded=False, isLight=False, isMartial=False, isExotic=False, isMasterwork=False, enchantment=0, materials=[], abilities=[], applicableSlots=[], cancelSlots=[]):
        super(UnarmedMeleeWeapon, self).__init__(name, weight, value, tags, damage, size, criticalRange, criticalMultiplier, range, source, type, typeJoin, special, specialJoin, specialValue, isTwoHanded, isLight, isMartial, isExotic, isMasterwork, enchantment, materials, abilities, applicableSlots, cancelSlots)


class MeleeWeapon(Weapon):

    def __init__(self, name="", weight=0, value=0, tags=config.NONE, damage=roll.Dice(4, 0, addition=1), size=size.Size(), criticalRange=[20, 20], criticalMultiplier=2, range=5, source=config.NONE, type=config.NONE, typeJoin=config.JOIN_OR, special=config.NONE, specialJoin=config.JOIN_AND, specialValue=0, isTwoHanded=False, isLight=False, isMartial=False, isExotic=False, isMasterwork=False, enchantment=0, materials=[], abilities=[], applicableSlots=[], cancelSlots=[]):
        super(MeleeWeapon, self).__init__(name, weight, value, tags, damage, size, criticalRange, criticalMultiplier, range, source, type, typeJoin, special, specialJoin, specialValue, isTwoHanded, isLight, isMartial, isExotic, isMasterwork, enchantment, materials, abilities, applicableSlots, cancelSlots)
        self.ApplicableSlots.append(config.ITEM_SLOT_MAINHAND)
        self.ApplicableSlots.append(config.ITEM_SLOT_OFFHAND)
        self.MadeToThrow = False
        if self.Range == 0:
            self.Range = 10
            self.MadeToThrow = False
        self.CriticalRangeThrow = [20, 20]
        self.CriticalMultiplierThrow = 2
        self.CanThrow = True

    def GetAttackThrow(self, character):
        attack = character.RangedAttack() + self.GetEnchantmentBonus()
        if not character.Race.IsProficient(self):
            attack -= 4
        for i in character.Inventory.GetEquippedArmor():
            if not character.Race.IsProficient(i):
                attack -= i.GetArmorCheckPenalty()
        for i in character.Inventory.GetEquippedShield():
            if not character.Race.IsProficient(i):
                attack -= i.GetArmorCheckPenalty()
        if not self.MadeToThrow:
            attack -= 4
        return attack

    def GetAttackDamageThrow(self, character):
        dmg = super(MeleeWeapon, self).GetAttackDamage(character)
        return dmg

    def GetCriticalThrow(self):
        if not self.MadeToThrow:
            crit = ''
            if not(self.CriticalRangeThrow[1] == 20 and self.CriticalRangeThrow[0] == 20):
                crit += str(self.CriticalRangeThrow[0]) + '-' + str(self.CriticalRangeThrow[1]) + '/'
            return crit + 'x' + str(self.CriticalMultiplierThrow)
        else:
            return self.GetCritical()


class RangedWeapon(Weapon):

    def __init__(self, name="", weight=0, value=0, tags=config.NONE, damage=roll.Dice(4, 0, addition=1), size=size.Size(), criticalRange=[20, 20], criticalMultiplier=2, range=5, source=config.NONE, type=config.NONE, typeJoin=config.JOIN_OR, special=config.NONE, specialJoin=config.JOIN_AND, specialValue=0, isTwoHanded=False, isLight=False, isMartial=False, isExotic=False, isMasterwork=False, enchantment=0, materials=[], abilities=[], ammoType=config.NONE, applicableSlots=[], cancelSlots=[]):
        super(RangedWeapon, self).__init__(name, weight, value, tags, damage, size, criticalRange, criticalMultiplier, range, source, type, typeJoin, special, specialJoin, specialValue, isTwoHanded, isLight, isMartial, isExotic, isMasterwork, enchantment, materials, abilities, applicableSlots, cancelSlots)
        self.ApplicableSlots.append(config.ITEM_SLOT_MAINHAND)
        self.ApplicableSlots.append(config.ITEM_SLOT_OFFHAND)
        self.AmmoType = ammoType
        self.ChosenAmmunitionIdx = -1

    def Use(self, character):
        if self.ChosenAmmunitionIdx >= 0 and self.ChosenAmmunitionIdx < len(character.Inventory.Items):
            character.Inventory.Items[self.ChosenAmmunitionIdx][1] -= 1

    def GetDamage(self, ammo=None):
        dmg = super(RangedWeapon, self).GetDamage()
        if ammo and isinstance(ammo, Ammunition):
            dmg.addition += ammo.ExtraDamage
        return dmg

    def GetRange(self, ammo=None):
        range = super(RangedWeapon, self).GetRange()
        if ammo and isinstance(ammo, Ammunition):
            return range + ammo.ExtraRange
        else:
            return range

    def GetEffects(self, ammo=None):
        effects = super(RangedWeapon, self).GetRange()
        if ammo and isinstance(ammo, Ammunition):
            effects = set(effects)
            for e in ammo.Effects:
                effects.Add(e)
            return list(effects)
        else:
            return effects

    def GetAttack(self, character):
        attack = character.RangedAttack() + self.GetEnchantmentBonus()
        if self.ChosenAmmunition and isinstance(ammo, Ammunition):
            attack += self.ChosenAmmunition.ExtraAttack
        if not character.Race.IsProficient(self):
            attack -= 4
        for i in character.Inventory.GetEquippedArmor():
            if not character.Race.IsProficient(i):
                attack -= i.GetArmorCheckPenalty()
        for i in character.Inventory.GetEquippedShield():
            if not character.Race.IsProficient(i):
                attack -= i.GetArmorCheckPenalty()
        return attack

    def ToJson(self):
        ret = super(RangedWeapon, self).ToJson()
        ret['AmmoType'] = self.AmmoType
        return ret


class Ammunition(Item):

    def __init__(self, name="", weight=0, value=0, tags=config.NONE, extraDamage=0, extraRange=0, extraAttack=0, effects=[], type=config.NONE, materials=[], applicableSlots=[], cancelSlots=[]):
        super(Ammunition, self).__init__(name, weight, value, tags, applicableSlots, cancelSlots)
        self.Type = type
        self.ExtraDamage = extraDamage
        self.ExtraRange = extraRange
        self.ExtraRange = extraAttack
        self.Effects = effects
        self.Materials = materials
        self.Value = self.GetValue()

    def GetValue(self):
        # TODO: Apply materials, masterwork, size, enchantments
        return self.Value

    def ToJson(self):
        ret = super(Ammunition, self).ToJson()
        ret['Type'] = self.Type
        ret['ExtraDamage'] = self.ExtraDamage
        ret['ExtraRange'] = self.ExtraRange
        ret['ExtraRange'] = self.ExtraRange
        ret['Effects'] = [i.ToJson() for i in self.Effects]
        ret['Materials'] = [i.ToJson() for i in self.Materials]
        return ret


class Armor(WearableItem):

    def __init__(self, name="", weight=0, value=0, tags=config.NONE, weightType=config.ARMOR_LIGHT, armorClass=0, maxDexBonus=99999, armorCheckPenalty=0, spellFailureChance=0, s=size.Size(), masterwork=False, enchantment=0, materials=[], abilities=[], applicableSlots=[], cancelSlots=[]):
        super(Armor, self).__init__(name, weight, value, tags, applicableSlots, cancelSlots)
        self.ApplicableSlots.append(config.ITEM_SLOT_ARMOR)
        self.WeightType = weightType
        self.ArmorClass = armorClass
        self.ArmorCheckPenalty = armorCheckPenalty
        self.MaxDexBonus = maxDexBonus
        self.Size = s
        self.Weight = self.WeightBySize(self.weight)
        self.Enchament = enchantment
        self.Masterwork = masterwork
        self.Materials = materials
        self.Abilities = abilities
        self.Value = self.GetValue()

    def GetValue(self):
        # TODO: Apply materials, masterwork, size, enchantments
        return self.Value

    def WeightBySize(self, weight):
        return self.Size.CarryingCapacity * weight

    def GetArmorClass(self):
        return self.ArmorClass + self.Enchament

    def GetArmorCheckPenalty(self):
        return self.ArmorCheckPenalty + (1 if self.Masterwork else 0)

    def ToJson(self):
        ret = super(Ammunition, self).ToJson()
        ret['WeightType'] = self.WeightType
        ret['ArmorClass'] = self.ArmorClass
        ret['Size'] = self.Size.Name
        ret['Enchantment'] = self.Enchantment
        ret['Masterwork'] = self.Masterwork
        ret['Abilities'] = [i.ToJson() for i in self.Abilities]
        ret['Materials'] = [i.ToJson() for i in self.Materials]
        return ret


class Barding(Armor):
    def __init__(self, name="", weight=0, value=0, tags=config.NONE, applicableSlots=[], cancelSlots=[]):
        super(Shield, self).__init__(name, weight, value, tags, weightType, armorClass, maxDexBonus, armorCheckPenalty, spellFailureChance, s, masterwork, enchantment, materials, abilities, cancelSlots)
        self.ApplicableSlots.append(config.ITEM_SLOT_NECK)
        self.ApplicableSlots.append(config.ITEM_SLOT_HEAD)
        self.ApplicableSlots.append(config.ITEM_SLOT_CHEST)
        self.ApplicableSlots.append(config.ITEM_SLOT_BODY)
        self.CancelSlots.append(config.ITEM_SLOT_NECK)
        self.CancelSlots.append(config.ITEM_SLOT_HEAD)
        self.CancelSlots.append(config.ITEM_SLOT_CHEST)
        self.CancelSlots.append(config.ITEM_SLOT_BODY)


class Shield(Armor):

    def __init__(self, name="", weight=0, value=0, tags=config.NONE, applicableSlots=[], cancelSlots=[]):
        super(Shield, self).__init__(name, weight, value, tags, applicableSlots, cancelSlots, weightType, armorClass, maxDexBonus, armorCheckPenalty, spellFailureChance, s, masterwork, enchantment, materials, abilities)
        self.ApplicableSlots.append(config.ITEM_SLOT_MAINHAND)
        self.ApplicableSlots.append(config.ITEM_SLOT_OFFHAND)


class MagicalProtection(WearableItem):
    # TODO

    def __init__(self, name="", weight=0, value=0, tags=config.NONE, applicableSlots=[], cancelSlots=[]):
        super(MagicalProtection, self).__init__(name, weight, value, tags, applicableSlots, cancelsSlots)


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
            config.ITEM_SLOT_MAINHAND,
            config.ITEM_SLOT_OFFHAND,
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