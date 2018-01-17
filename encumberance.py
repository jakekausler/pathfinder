
import config


def GetEncumberanceString(n):
    if n == config.ENCUMBERANCE_LIGHT:
        return 'Light'
    if n == config.ENCUMBERANCE_MEDIUM:
        return 'Medium'
    if n == config.ENCUMBERANCE_HEAVY:
        return 'Heavy'
    if n == config.ENCUMBERANCE_OVER:
        return 'Over'
    return ''


def GetEncumberance(character):
    if character.Abilities()[config.ABILITY_STRENGTH] > 29 or character.Abilities()[config.ABILITY_STRENGTH] < 1:
        return config.ENCUMBERANCE_LIGHT
    weight = character.Inventory.GetTotalWeight()
    use = config.encumberances[character.Abilities()[config.ABILITY_STRENGTH] - 1]
    if weight < use[0]*character.Size().CarryingCapacity:
        return config.ENCUMBERANCE_LIGHT
    if weight < use[1]*character.Size().CarryingCapacity:
        return config.ENCUMBERANCE_MEDIUM
    if weight < use[2]*character.Size().CarryingCapacity:
        return config.ENCUMBERANCE_HEAVY
    return config.ENCUMBERANCE_OVER
