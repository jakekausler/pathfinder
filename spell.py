
import config
import characterclass

import re
import json

# TODO: SpAbility Class, SuAbility Class


def GetSpells():
    return [
        config.SPELL_ACID_ARROW,
        config.SPELL_ACID_FOG,
        config.SPELL_ACID_SPLASH,
        config.SPELL_AID,
        config.SPELL_AIR_WALK,
        config.SPELL_ALIGN_WEAPON,
        config.SPELL_ALTER_SELF,
        config.SPELL_ALARM,
        config.SPELL_ANALYZE_DWEOMER,
        config.SPELL_ANIMAL_GROWTH,
        config.SPELL_ANIMAL_MESSENGER,
        config.SPELL_ANIMAL_SHAPES,
        config.SPELL_ANIMAL_TRANCE,
        config.SPELL_ANIMATE_DEAD,
        config.SPELL_ANIMATE_OBJECTS,
        config.SPELL_ANIMATE_PLANTS,
        config.SPELL_ANIMATE_ROPE,
        config.SPELL_ANTILIFE_SHELL,
        config.SPELL_ANTIMAGIC_FIELD,
        config.SPELL_ANTIPATHY,
        config.SPELL_ANTIPLANT_SHELL,
        config.SPELL_ARCANE_EYE,
        config.SPELL_ARCANE_LOCK,
        config.SPELL_ARCANE_MARK,
        config.SPELL_ARCANE_SIGHT,
        config.SPELL_ARCANE_SIGHT_GREATER,
        config.SPELL_ASTRAL_PROJECTION,
        config.SPELL_ATONEMENT,
        config.SPELL_AUGURY,
        config.SPELL_AWAKEN,
        config.SPELL_BANE,
        config.SPELL_BANISHMENT,
        config.SPELL_BARKSKIN,
        config.SPELL_BEAR_S_ENDURANCE,
        config.SPELL_BEAR_S_ENDURANCE_MASS,
        config.SPELL_BEAST_SHAPE_I,
        config.SPELL_BEAST_SHAPE_I_I,
        config.SPELL_BEAST_SHAPE_I_I_I,
        config.SPELL_BEAST_SHAPE_I_V,
        config.SPELL_BESTOW_CURSE,
        config.SPELL_BINDING,
        config.SPELL_BLACK_TENTACLES,
        config.SPELL_BLADE_BARRIER,
        config.SPELL_BLASPHEMY,
        config.SPELL_BLEED,
        config.SPELL_BLESS,
        config.SPELL_BLESS_WATER,
        config.SPELL_BLESS_WEAPON,
        config.SPELL_BLIGHT,
        config.SPELL_BLINDNESS_DEAFNESS,
        config.SPELL_BLINK,
        config.SPELL_BLUR,
        config.SPELL_BREAK_ENCHANTMENT,
        config.SPELL_BREATH_OF_LIFE,
        config.SPELL_BULL_S_STRENGTH,
        config.SPELL_BULL_S_STRENGTH_MASS,
        config.SPELL_BURNING_HANDS,
        config.SPELL_CALL_LIGHTNING,
        config.SPELL_CALL_LIGHTNING_STORM,
        config.SPELL_CALM_ANIMALS,
        config.SPELL_CALM_EMOTIONS,
        config.SPELL_CAT_S_GRACE,
        config.SPELL_CAT_S_GRACE_MASS,
        config.SPELL_CAUSE_FEAR,
        config.SPELL_CHAIN_LIGHTNING,
        config.SPELL_CHANGESTAFF,
        config.SPELL_CHAOS_HAMMER,
        config.SPELL_CHARM_PERSON,
        config.SPELL_CHARM_ANIMAL,
        config.SPELL_CHARM_MONSTER,
        config.SPELL_CHARM_MONSTER_MASS,
        config.SPELL_CHILL_METAL,
        config.SPELL_CHILL_TOUCH,
        config.SPELL_CIRCLE_OF_DEATH,
        config.SPELL_CLAIRAUDIENCE_CLAIRVOYANCE,
        config.SPELL_CLENCHED_FIST,
        config.SPELL_CLOAK_OF_CHAOS,
        config.SPELL_CLONE,
        config.SPELL_CLOUDKILL,
        config.SPELL_COLOR_SPRAY,
        config.SPELL_COMMAND,
        config.SPELL_COMMAND_GREATER,
        config.SPELL_COMMAND_PLANTS,
        config.SPELL_COMMAND_UNDEAD,
        config.SPELL_COMMUNE,
        config.SPELL_COMMUNE_WITH_NATURE,
        config.SPELL_COMPREHEND_LANGUAGES,
        config.SPELL_CONE_OF_COLD,
        config.SPELL_CONFUSION,
        config.SPELL_CONFUSION_LESSER,
        config.SPELL_CONSECRATE,
        config.SPELL_CONTACT_OTHER_PLANE,
        config.SPELL_CONTAGION,
        config.SPELL_CONTINGENCY,
        config.SPELL_CONTINUAL_FLAME,
        config.SPELL_CONTROL_PLANTS,
        config.SPELL_CONTROL_UNDEAD,
        config.SPELL_CONTROL_WATER,
        config.SPELL_CONTROL_WEATHER,
        config.SPELL_CONTROL_WINDS,
        config.SPELL_CREATE_FOOD_AND_WATER,
        config.SPELL_CREATE_UNDEAD,
        config.SPELL_CREATE_GREATER_UNDEAD,
        config.SPELL_CREATE_WATER,
        config.SPELL_CREEPING_DOOM,
        config.SPELL_CRUSHING_DESPAIR,
        config.SPELL_CRUSHING_HAND,
        config.SPELL_CURE_LIGHT_WOUNDS,
        config.SPELL_CURE_CRITICAL_WOUNDS,
        config.SPELL_CURE_LIGHT_WOUNDS_MASS,
        config.SPELL_CURE_CRITICAL_WOUNDS_MASS,
        config.SPELL_CURE_MODERATE_WOUNDS,
        config.SPELL_CURE_MODERATE_WOUNDS_MASS,
        config.SPELL_CURE_SERIOUS_WOUNDS,
        config.SPELL_CURE_SERIOUS_WOUNDS_MASS,
        config.SPELL_CURSE_WATER,
        config.SPELL_DANCING_LIGHTS,
        config.SPELL_DARKNESS,
        config.SPELL_DARKVISION,
        config.SPELL_DAYLIGHT,
        config.SPELL_DAZE,
        config.SPELL_DAZE_MONSTER,
        config.SPELL_DEATH_KNELL,
        config.SPELL_DEATH_WARD,
        config.SPELL_DEATHWATCH,
        config.SPELL_DEEPER_DARKNESS,
        config.SPELL_DEEP_SLUMBER,
        config.SPELL_DELAYED_BLAST_FIREBALL,
        config.SPELL_DELAY_POISON,
        config.SPELL_DEMAND,
        config.SPELL_DESECRATE,
        config.SPELL_DESTRUCTION,
        config.SPELL_DETECT_ANIMALS_OR_PLANTS,
        config.SPELL_DETECT_CHAOS,
        config.SPELL_DETECT_EVIL,
        config.SPELL_DETECT_GOOD,
        config.SPELL_DETECT_LAW,
        config.SPELL_DETECT_MAGIC,
        config.SPELL_DETECT_POISON,
        config.SPELL_DETECT_SCRYING,
        config.SPELL_DETECT_SECRET_DOORS,
        config.SPELL_DETECT_SNARES_AND_PITS,
        config.SPELL_DETECT_THOUGHTS,
        config.SPELL_DETECT_UNDEAD,
        config.SPELL_DICTUM,
        config.SPELL_DIMENSIONAL_ANCHOR,
        config.SPELL_DIMENSIONAL_LOCK,
        config.SPELL_DIMENSION_DOOR,
        config.SPELL_DIMINISH_PLANTS,
        config.SPELL_DISCERN_LIES,
        config.SPELL_DISCERN_LOCATION,
        config.SPELL_DISGUISE_SELF,
        config.SPELL_DISINTEGRATE,
        config.SPELL_DISMISSAL,
        config.SPELL_DISPEL_CHAOS,
        config.SPELL_DISPEL_EVIL,
        config.SPELL_DISPEL_GOOD,
        config.SPELL_DISPEL_LAW,
        config.SPELL_DISPEL_MAGIC,
        config.SPELL_DISPEL_MAGIC_GREATER,
        config.SPELL_DISPLACEMENT,
        config.SPELL_DISRUPTING_WEAPON,
        config.SPELL_DISRUPT_UNDEAD,
        config.SPELL_DIVINATION,
        config.SPELL_DIVINE_FAVOR,
        config.SPELL_DIVINE_POWER,
        config.SPELL_DOMINATE_ANIMAL,
        config.SPELL_DOMINATE_MONSTER,
        config.SPELL_DOMINATE_PERSON,
        config.SPELL_DOOM,
        config.SPELL_DREAM,
        config.SPELL_EAGLE_S_SPLENDOR,
        config.SPELL_EAGLE_S_SPLENDOR_MASS,
        config.SPELL_EARTHQUAKE,
        config.SPELL_ELEMENTAL_BODY_I,
        config.SPELL_ELEMENTAL_BODY_I_I,
        config.SPELL_ELEMENTAL_BODY_I_I_I,
        config.SPELL_ELEMENTAL_BODY_I_V,
        config.SPELL_ELEMENTAL_SWARM,
        config.SPELL_ENDURE_ELEMENTS,
        config.SPELL_ENERGY_DRAIN,
        config.SPELL_ENERVATION,
        config.SPELL_ENLARGE_PERSON,
        config.SPELL_ENLARGE_PERSON_MASS,
        config.SPELL_ENTANGLE,
        config.SPELL_ENTHRALL,
        config.SPELL_ENTROPIC_SHIELD,
        config.SPELL_ERASE,
        config.SPELL_ETHEREAL_JAUNT,
        config.SPELL_ETHEREALNESS,
        config.SPELL_EXPEDITIOUS_RETREAT,
        config.SPELL_EXPLOSIVE_RUNES,
        config.SPELL_EYEBITE,
        config.SPELL_FABRICATE,
        config.SPELL_FAERIE_FIRE,
        config.SPELL_FALSE_LIFE,
        config.SPELL_FALSE_VISION,
        config.SPELL_FEATHER_FALL,
        config.SPELL_FEEBLEMIND,
        config.SPELL_FIND_THE_PATH,
        config.SPELL_FIND_TRAPS,
        config.SPELL_FINGER_OF_DEATH,
        config.SPELL_FIRE_SHIELD,
        config.SPELL_FIRE_SEEDS,
        config.SPELL_FIRE_STORM,
        config.SPELL_FIRE_TRAP,
        config.SPELL_FIREBALL,
        config.SPELL_FLAME_ARROW,
        config.SPELL_FLAME_BLADE,
        config.SPELL_FLAME_STRIKE,
        config.SPELL_FLAMING_SPHERE,
        config.SPELL_FLARE,
        config.SPELL_FLESH_TO_STONE,
        config.SPELL_FLOATING_DISK,
        config.SPELL_FLY,
        config.SPELL_FOG_CLOUD,
        config.SPELL_FORBIDDANCE,
        config.SPELL_FORCECAGE,
        config.SPELL_FORCEFUL_HAND,
        config.SPELL_FORESIGHT,
        config.SPELL_FORM_OF_THE_DRAGON_I,
        config.SPELL_FORM_OF_THE_DRAGON_I_I,
        config.SPELL_FORM_OF_THE_DRAGON_I_I_I,
        config.SPELL_FOX_S_CUNNING,
        config.SPELL_FOX_S_CUNNING_MASS,
        config.SPELL_FREEDOM,
        config.SPELL_FREEDOM_OF_MOVEMENT,
        config.SPELL_FREEZING_SPHERE,
        config.SPELL_GASEOUS_FORM,
        config.SPELL_GATE,
        config.SPELL_GEAS_QUEST,
        config.SPELL_GEAS_LESSER,
        config.SPELL_GENTLE_REPOSE,
        config.SPELL_GHOST_SOUND,
        config.SPELL_GHOUL_TOUCH,
        config.SPELL_GIANT_FORM_I,
        config.SPELL_GIANT_FORM_I_I,
        config.SPELL_GIANT_VERMIN,
        config.SPELL_GLIBNESS,
        config.SPELL_GLITTERDUST,
        config.SPELL_GLOBE_OF_INVULNERABILITY_LESSER,
        config.SPELL_GLOBE_OF_INVULNERABILITY,
        config.SPELL_GLYPH_OF_WARDING,
        config.SPELL_GLYPH_OF_WARDING_GREATER,
        config.SPELL_GOODBERRY,
        config.SPELL_GOOD_HOPE,
        config.SPELL_GRASPING_HAND,
        config.SPELL_GREASE,
        config.SPELL_GUARDS_AND_WARDS,
        config.SPELL_GUIDANCE,
        config.SPELL_GUST_OF_WIND,
        config.SPELL_HALLOW,
        config.SPELL_HALLUCINATORY_TERRAIN,
        config.SPELL_HALT_UNDEAD,
        config.SPELL_HARM,
        config.SPELL_HASTE,
        config.SPELL_HEAL,
        config.SPELL_HEAL_MASS,
        config.SPELL_HEAL_MOUNT,
        config.SPELL_HEAT_METAL,
        config.SPELL_HELPING_HAND,
        config.SPELL_HEROES_FEAST,
        config.SPELL_HEROISM,
        config.SPELL_HEROISM_GREATER,
        config.SPELL_HIDE_FROM_ANIMALS,
        config.SPELL_HIDE_FROM_UNDEAD,
        config.SPELL_HIDEOUS_LAUGHTER,
        config.SPELL_HOLD_PERSON,
        config.SPELL_HOLD_MONSTER,
        config.SPELL_HOLD_MONSTER_MASS,
        config.SPELL_HOLD_PERSON_MASS,
        config.SPELL_HOLD_PORTAL,
        config.SPELL_HOLY_AURA,
        config.SPELL_HOLY_SMITE,
        config.SPELL_HOLY_SWORD,
        config.SPELL_HOLY_WORD,
        config.SPELL_HORRID_WILTING,
        config.SPELL_HYPNOTIC_PATTERN,
        config.SPELL_HYPNOTISM,
        config.SPELL_ICE_STORM,
        config.SPELL_IDENTIFY,
        config.SPELL_ILLUSORY_SCRIPT,
        config.SPELL_ILLUSORY_WALL,
        config.SPELL_IMBUE_WITH_SPELL_ABILITY,
        config.SPELL_IMPLOSION,
        config.SPELL_IMPRISONMENT,
        config.SPELL_INCENDIARY_CLOUD,
        config.SPELL_INFLICT_LIGHT_WOUNDS,
        config.SPELL_INFLICT_CRITICAL_WOUNDS,
        config.SPELL_INFLICT_CRITICAL_WOUNDS_MASS,
        config.SPELL_INFLICT_LIGHT_WOUNDS_MASS,
        config.SPELL_INFLICT_MODERATE_WOUNDS,
        config.SPELL_INFLICT_MODERATE_WOUNDS_MASS,
        config.SPELL_INFLICT_SERIOUS_WOUNDS,
        config.SPELL_INFLICT_SERIOUS_WOUNDS_MASS,
        config.SPELL_INSANITY,
        config.SPELL_INTERPOSING_HAND,
        config.SPELL_INVISIBILITY,
        config.SPELL_INVISIBILITY_GREATER,
        config.SPELL_INVISIBILITY_MASS,
        config.SPELL_INVISIBILITY_PURGE,
        config.SPELL_INVISIBILITY_SPHERE,
        config.SPELL_IRON_BODY,
        config.SPELL_IRONWOOD,
        config.SPELL_IRRESISTIBLE_DANCE,
        config.SPELL_JUMP,
        config.SPELL_KEEN_EDGE,
        config.SPELL_KNOCK,
        config.SPELL_KNOW_DIRECTION,
        config.SPELL_LEGEND_LORE,
        config.SPELL_LEVITATE,
        config.SPELL_LIGHT,
        config.SPELL_LIGHTNING_BOLT,
        config.SPELL_LIMITED_WISH,
        config.SPELL_LIVEOAK,
        config.SPELL_LOCATE_OBJECT,
        config.SPELL_LOCATE_CREATURE,
        config.SPELL_LONGSTRIDER,
        config.SPELL_LULLABY,
        config.SPELL_MAGE_ARMOR,
        config.SPELL_MAGE_HAND,
        config.SPELL_MAGE_S_DISJUNCTION,
        config.SPELL_MAGE_S_FAITHFUL_HOUND,
        config.SPELL_MAGE_S_LUCUBRATION,
        config.SPELL_MAGE_S_MAGNIFICENT_MANSION,
        config.SPELL_MAGE_S_PRIVATE_SANCTUM,
        config.SPELL_MAGE_S_SWORD,
        config.SPELL_MAGIC_AURA,
        config.SPELL_MAGIC_CIRCLE_AGAINST_EVIL,
        config.SPELL_MAGIC_CIRCLE_AGAINST_CHAOS,
        config.SPELL_MAGIC_CIRCLE_AGAINST_GOOD,
        config.SPELL_MAGIC_CIRCLE_AGAINST_LAW,
        config.SPELL_MAGIC_FANG,
        config.SPELL_MAGIC_FANG_GREATER,
        config.SPELL_MAGIC_JAR,
        config.SPELL_MAGIC_MISSILE,
        config.SPELL_MAGIC_MOUTH,
        config.SPELL_MAGIC_STONE,
        config.SPELL_MAGIC_VESTMENT,
        config.SPELL_MAGIC_WEAPON,
        config.SPELL_MAGIC_WEAPON_GREATER,
        config.SPELL_MINOR_CREATION,
        config.SPELL_MAJOR_CREATION,
        config.SPELL_MAJOR_IMAGE,
        config.SPELL_MAKE_WHOLE,
        config.SPELL_MARK_OF_JUSTICE,
        config.SPELL_MAZE,
        config.SPELL_MELD_INTO_STONE,
        config.SPELL_MENDING,
        config.SPELL_MESSAGE,
        config.SPELL_METEOR_SWARM,
        config.SPELL_MIND_BLANK,
        config.SPELL_MIND_FOG,
        config.SPELL_MINOR_IMAGE,
        config.SPELL_MIRACLE,
        config.SPELL_MIRAGE_ARCANA,
        config.SPELL_MIRROR_IMAGE,
        config.SPELL_MISDIRECTION,
        config.SPELL_MISLEAD,
        config.SPELL_MNEMONIC_ENHANCER,
        config.SPELL_MODIFY_MEMORY,
        config.SPELL_MOMENT_OF_PRESCIENCE,
        config.SPELL_MOUNT,
        config.SPELL_MOVE_EARTH,
        config.SPELL_NEUTRALIZE_POISON,
        config.SPELL_NIGHTMARE,
        config.SPELL_NONDETECTION,
        config.SPELL_OBSCURE_OBJECT,
        config.SPELL_OBSCURING_MIST,
        config.SPELL_OPEN_CLOSE,
        config.SPELL_ORDER_S_WRATH,
        config.SPELL_OVERLAND_FLIGHT,
        config.SPELL_OWL_S_WISDOM,
        config.SPELL_OWL_S_WISDOM_MASS,
        config.SPELL_PASSWALL,
        config.SPELL_PASS_WITHOUT_TRACE,
        config.SPELL_PERMANENCY,
        config.SPELL_PERMANENT_IMAGE,
        config.SPELL_PERSISTENT_IMAGE,
        config.SPELL_PHANTASMAL_KILLER,
        config.SPELL_PHANTOM_STEED,
        config.SPELL_PHANTOM_TRAP,
        config.SPELL_PHASE_DOOR,
        config.SPELL_PLANAR_ALLY_LESSER,
        config.SPELL_PLANAR_ALLY,
        config.SPELL_PLANAR_ALLY_GREATER,
        config.SPELL_PLANAR_BINDING_LESSER,
        config.SPELL_PLANAR_BINDING,
        config.SPELL_PLANAR_BINDING_GREATER,
        config.SPELL_PLANE_SHIFT,
        config.SPELL_PLANT_GROWTH,
        config.SPELL_PLANT_SHAPE_I,
        config.SPELL_PLANT_SHAPE_I_I,
        config.SPELL_PLANT_SHAPE_I_I_I,
        config.SPELL_POISON,
        config.SPELL_POLAR_RAY,
        config.SPELL_POLYMORPH,
        config.SPELL_POLYMORPH_GREATER,
        config.SPELL_POLYMORPH_ANY_OBJECT,
        config.SPELL_POWER_WORD_BLIND,
        config.SPELL_POWER_WORD_KILL,
        config.SPELL_POWER_WORD_STUN,
        config.SPELL_PRAYER,
        config.SPELL_PRESTIDIGITATION,
        config.SPELL_PRISMATIC_SPHERE,
        config.SPELL_PRISMATIC_SPRAY,
        config.SPELL_PRISMATIC_WALL,
        config.SPELL_PRYING_EYES_GREATER,
        config.SPELL_PRODUCE_FLAME,
        config.SPELL_PROGRAMMED_IMAGE,
        config.SPELL_PROJECT_IMAGE,
        config.SPELL_PROTECTION_FROM_ARROWS,
        config.SPELL_PROTECTION_FROM_CHAOS,
        config.SPELL_PROTECTION_FROM_EVIL,
        config.SPELL_PROTECTION_FROM_GOOD,
        config.SPELL_PROTECTION_FROM_LAW,
        config.SPELL_PROTECTION_FROM_SPELLS,
        config.SPELL_PURIFY_FOOD_AND_DRINK,
        config.SPELL_PYROTECHNICS,
        config.SPELL_QUENCH,
        config.SPELL_RAGE,
        config.SPELL_RAINBOW_PATTERN,
        config.SPELL_RAISE_DEAD,
        config.SPELL_RAY_OF_ENFEEBLEMENT,
        config.SPELL_RAY_OF_EXHAUSTION,
        config.SPELL_RAY_OF_FROST,
        config.SPELL_READ_MAGIC,
        config.SPELL_REDUCE_PERSON,
        config.SPELL_REDUCE_ANIMAL,
        config.SPELL_REDUCE_PERSON_MASS,
        config.SPELL_REFUGE,
        config.SPELL_REGENERATE,
        config.SPELL_REINCARNATE,
        config.SPELL_REMOVE_BLINDNESS_DEAFNESS,
        config.SPELL_REMOVE_CURSE,
        config.SPELL_REMOVE_DISEASE,
        config.SPELL_REMOVE_FEAR,
        config.SPELL_REMOVE_PARALYSIS,
        config.SPELL_REPEL_METAL_OR_STONE,
        config.SPELL_REPEL_VERMIN,
        config.SPELL_REPEL_WOOD,
        config.SPELL_REPULSION,
        config.SPELL_RESILIENT_SPHERE,
        config.SPELL_RESISTANCE,
        config.SPELL_RESIST_ENERGY,
        config.SPELL_RESTORATION,
        config.SPELL_RESTORATION_GREATER,
        config.SPELL_RESTORATION_LESSER,
        config.SPELL_RESURRECTION,
        config.SPELL_REVERSE_GRAVITY,
        config.SPELL_RIGHTEOUS_MIGHT,
        config.SPELL_ROPE_TRICK,
        config.SPELL_RUSTING_GRASP,
        config.SPELL_SANCTUARY,
        config.SPELL_SCARE,
        config.SPELL_SCINTILLATING_PATTERN,
        config.SPELL_SCORCHING_RAY,
        config.SPELL_SCREEN,
        config.SPELL_SCRYING,
        config.SPELL_SCRYING_GREATER,
        config.SPELL_SCULPT_SOUND,
        config.SPELL_SEARING_LIGHT,
        config.SPELL_SECRET_CHEST,
        config.SPELL_SECRET_PAGE,
        config.SPELL_SECURE_SHELTER,
        config.SPELL_SEE_INVISIBILITY,
        config.SPELL_SEEMING,
        config.SPELL_SENDING,
        config.SPELL_SEPIA_SNAKE_SIGIL,
        config.SPELL_SEQUESTER,
        config.SPELL_SHADOW_CONJURATION,
        config.SPELL_SHADES,
        config.SPELL_SHADOW_CONJURATION_GREATER,
        config.SPELL_SHADOW_EVOCATION,
        config.SPELL_SHADOW_EVOCATION_GREATER,
        config.SPELL_SHADOW_WALK,
        config.SPELL_SHAMBLER,
        config.SPELL_SHAPECHANGE,
        config.SPELL_SHATTER,
        config.SPELL_SHIELD,
        config.SPELL_SHIELD_OF_FAITH,
        config.SPELL_SHIELD_OF_LAW,
        config.SPELL_SHIELD_OTHER,
        config.SPELL_SHILLELAGH,
        config.SPELL_SHRINK_ITEM,
        config.SPELL_SHOCKING_GRASP,
        config.SPELL_SHOUT,
        config.SPELL_SHOUT_GREATER,
        config.SPELL_SILENCE,
        config.SPELL_SILENT_IMAGE,
        config.SPELL_SIMULACRUM,
        config.SPELL_SLAY_LIVING,
        config.SPELL_SLEEP,
        config.SPELL_SLEET_STORM,
        config.SPELL_SLOW,
        config.SPELL_SNARE,
        config.SPELL_SOFTEN_EARTH_AND_STONE,
        config.SPELL_SOLID_FOG,
        config.SPELL_SONG_OF_DISCORD,
        config.SPELL_SOUL_BIND,
        config.SPELL_SOUND_BURST,
        config.SPELL_SPEAK_WITH_ANIMALS,
        config.SPELL_SPEAK_WITH_DEAD,
        config.SPELL_SPEAK_WITH_PLANTS,
        config.SPELL_SPECTRAL_HAND,
        config.SPELL_SPELL_IMMUNITY,
        config.SPELL_SPELL_IMMUNITY_GREATER,
        config.SPELL_SPELL_RESISTANCE,
        config.SPELL_SPELLSTAFF,
        config.SPELL_SPELL_TURNING,
        config.SPELL_SPIDER_CLIMB,
        config.SPELL_SPIKE_GROWTH,
        config.SPELL_SPIKE_STONES,
        config.SPELL_SPIRITUAL_WEAPON,
        config.SPELL_STABILIZE,
        config.SPELL_STATUE,
        config.SPELL_STATUS,
        config.SPELL_STINKING_CLOUD,
        config.SPELL_STONE_SHAPE,
        config.SPELL_STONESKIN,
        config.SPELL_STONE_TELL,
        config.SPELL_STONE_TO_FLESH,
        config.SPELL_STORM_OF_VENGEANCE,
        config.SPELL_SUGGESTION,
        config.SPELL_SUGGESTION_MASS,
        config.SPELL_SUMMON_INSTRUMENT,
        config.SPELL_SUMMON_MONSTER_I,
        config.SPELL_SUMMON_MONSTER_I_I,
        config.SPELL_SUMMON_MONSTER_I_I_I,
        config.SPELL_SUMMON_MONSTER_I_V,
        config.SPELL_SUMMON_MONSTER_V,
        config.SPELL_SUMMON_MONSTER_V_I,
        config.SPELL_SUMMON_MONSTER_V_I_I_I,
        config.SPELL_SUMMON_MONSTER_V_I_I,
        config.SPELL_SUMMON_MONSTER_I_X,
        config.SPELL_SUMMON_NATURE_S_ALLY_I,
        config.SPELL_SUMMON_NATURE_S_ALLY_I_I,
        config.SPELL_SUMMON_NATURE_S_ALLY_I_I_I,
        config.SPELL_SUMMON_NATURE_S_ALLY_I_V,
        config.SPELL_SUMMON_NATURE_S_ALLY_V,
        config.SPELL_SUMMON_NATURE_S_ALLY_V_I,
        config.SPELL_SUMMON_NATURE_S_ALLY_V_I_I,
        config.SPELL_SUMMON_NATURE_S_ALLY_V_I_I_I,
        config.SPELL_SUMMON_NATURE_S_ALLY_I_X,
        config.SPELL_SUMMON_SWARM,
        config.SPELL_SUNBEAM,
        config.SPELL_SUNBURST,
        config.SPELL_SYMBOL_OF_DEATH,
        config.SPELL_SYMBOL_OF_FEAR,
        config.SPELL_SYMBOL_OF_INSANITY,
        config.SPELL_SYMBOL_OF_PAIN,
        config.SPELL_SYMBOL_OF_PERSUASION,
        config.SPELL_SYMBOL_OF_SLEEP,
        config.SPELL_SYMBOL_OF_STUNNING,
        config.SPELL_SYMBOL_OF_WEAKNESS,
        config.SPELL_SYMPATHETIC_VIBRATION,
        config.SPELL_SYMPATHY,
        config.SPELL_TELEKINESIS,
        config.SPELL_TELEKINETIC_SPHERE,
        config.SPELL_TELEPATHIC_BOND,
        config.SPELL_TELEPORT,
        config.SPELL_TELEPORT_GREATER,
        config.SPELL_TELEPORT_OBJECT,
        config.SPELL_TELEPORTATION_CIRCLE,
        config.SPELL_TEMPORAL_STASIS,
        config.SPELL_TIME_STOP,
        config.SPELL_TINY_HUT,
        config.SPELL_TONGUES,
        config.SPELL_TOUCH_OF_FATIGUE,
        config.SPELL_TOUCH_OF_IDIOCY,
        config.SPELL_TRANSFORMATION,
        config.SPELL_TRANSMUTE_METAL_TO_WOOD,
        config.SPELL_TRANSMUTE_MUD_TO_ROCK,
        config.SPELL_TRANSMUTE_ROCK_TO_MUD,
        config.SPELL_TRANSPORT_VIA_PLANTS,
        config.SPELL_TRAP_THE_SOUL,
        config.SPELL_TREE_SHAPE,
        config.SPELL_TREE_STRIDE,
        config.SPELL_TRUE_RESURRECTION,
        config.SPELL_TRUE_SEEING,
        config.SPELL_TRUE_STRIKE,
        config.SPELL_UNDEATH_TO_DEATH,
        config.SPELL_UNDETECTABLE_ALIGNMENT,
        config.SPELL_UNHALLOW,
        config.SPELL_UNHOLY_AURA,
        config.SPELL_UNHOLY_BLIGHT,
        config.SPELL_UNSEEN_SERVANT,
        config.SPELL_VAMPIRIC_TOUCH,
        config.SPELL_VEIL,
        config.SPELL_VENTRILOQUISM,
        config.SPELL_VIRTUE,
        config.SPELL_VISION,
        config.SPELL_WAIL_OF_THE_BANSHEE,
        config.SPELL_WALL_OF_FIRE,
        config.SPELL_WALL_OF_FORCE,
        config.SPELL_WALL_OF_ICE,
        config.SPELL_WALL_OF_IRON,
        config.SPELL_WALL_OF_THORNS,
        config.SPELL_WARP_WOOD,
        config.SPELL_WATER_BREATHING,
        config.SPELL_WATER_WALK,
        config.SPELL_WAVES_OF_EXHAUSTION,
        config.SPELL_WAVES_OF_FATIGUE,
        config.SPELL_WEB,
        config.SPELL_WEIRD,
        config.SPELL_WHIRLWIND,
        config.SPELL_WHISPERING_WIND,
        config.SPELL_WIND_WALK,
        config.SPELL_WIND_WALL,
        config.SPELL_WISH,
        config.SPELL_WOOD_SHAPE,
        config.SPELL_WORD_OF_RECALL,
        config.SPELL_WORD_OF_CHAOS,
        config.SPELL_ZONE_OF_SILENCE,
        config.SPELL_ZONE_OF_TRUTH,
        config.SPELL_WALL_OF_STONE,
        config.SPELL_AGONIZE,
        config.SPELL_HELLFIRE_RAY,
        config.SPELL_SACRIFICE,
        config.SPELL_BURNING_DISARM,
        config.SPELL_DIRGE_OF_THE_VICTORIOUS_KNIGHTS,
        config.SPELL_DWEOMER_RETALIATION,
        config.SPELL_EMERGENCY_FORCE_SPHERE,
        config.SPELL_SIGNIFER_S_RALLY,
        config.SPELL_TWINE_DOUBLE,
        config.SPELL_FEAR,
        config.SPELL_HOLD_ANIMAL,
        config.SPELL_INSECT_PLAGUE,
        config.SPELL_BALEFUL_POLYMORPH,
        config.SPELL_PRYING_EYES,
        config.SPELL_INSTANT_SUMMONS,
        config.SPELL_SPELLCASTING_CONTRACT_LESSER,
        config.SPELL_SPELLCASTING_CONTRACT,
        config.SPELL_SPELLCASTING_CONTRACT_GREATER,
        config.SPELL_ANCESTRAL_COMMUNION,
        config.SPELL_ANCESTRAL_GIFT,
        config.SPELL_SUMMON_ANCESTRAL_GUARDIAN,
        config.SPELL_SEE_THROUGH_STONE,
        config.SPELL_RUNE_OF_DURABILITY,
        config.SPELL_RUNE_OF_WARDING,
        config.SPELL_DETECT_CHARM,
        config.SPELL_LIBERATING_COMAND,
        config.SPELL_SUPPRES_CHARMS_AND_COMPULSIONS,
        config.SPELL_SUMMON_FLIGHT_OF_EAGLES,
        config.SPELL_GENIUS_AVARICIOUS,
        config.SPELL_PROTECTION_FROM_ENERGY,
        config.SPELL_RETRIEVE_ITEM,
        config.SPELL_SPHERESCRY,
        config.SPELL_ILLUSORY_POISON,
        config.SPELL_ARCANE_REINFORCEMENT,
        config.SPELL_CANOPIC_CONVERSION,
        config.SPELL_CHASTISE,
        config.SPELL_SUMMON_ELEMENTAL_STEED,
        config.SPELL_HIBERNATE,
        config.SPELL_MARK_OF_BLOOD,
        config.SPELL_SOTTO_VOCE,
        config.SPELL_TOMB_LEGION,
        config.SPELL_TRIPVINE,
        config.SPELL_APE_WALK,
        config.SPELL_DEFOLIATE,
        config.SPELL_HEATSTROKE,
        config.SPELL_SWALLOW_YOUR_FEAR,
        config.SPELL_BLOOD_RAGE,
        config.SPELL_SHIELD_THE_BANNER,
        config.SPELL_VIGOR,
        config.SPELL_ABSORBING_TOUCH,
        config.SPELL_ACCELERATE_POISON,
        config.SPELL_ACID_PIT,
        config.SPELL_ALCHEMICAL_ALLOCATION,
        config.SPELL_ALLFOOD,
        config.SPELL_ALTER_WINDS,
        config.SPELL_AMPLIFY_ELIXIR,
        config.SPELL_ANT_HAUL,
        config.SPELL_AQUEOUS_ORB,
        config.SPELL_ARCANE_CONCORDANCE,
        config.SPELL_ARROW_ERUPTION,
        config.SPELL_ASPECT_OF_THE_BEAR,
        config.SPELL_ASPECT_OF_THE_FALCON,
        config.SPELL_ASPECT_OF_THE_STAG,
        config.SPELL_ASPECT_OF_THE_WOLF,
        config.SPELL_AURA_OF_GREATER_COURAGE,
        config.SPELL_BALL_LIGHTNING,
        config.SPELL_BANISH_SEEMING,
        config.SPELL_BARD_S_ESCAPE,
        config.SPELL_BEGUILING_GIFT,
        config.SPELL_BESTOW_GRACE,
        config.SPELL_BLAZE_OF_GLORY,
        config.SPELL_BLESSING_OF_FERVOR,
        config.SPELL_BLESSING_OF_THE_SALAMANDER,
        config.SPELL_BLOOD_BIOGRAPHY,
        config.SPELL_BLOODHOUND,
        config.SPELL_BLOODY_CLAWS,
        config.SPELL_BOMBER_S_EYE,
        config.SPELL_BORROW_FORTUNE,
        config.SPELL_BORROW_SKILL,
        config.SPELL_BOW_SPIRIT,
        config.SPELL_BRAND,
        config.SPELL_BRAND_GREATER,
        config.SPELL_BREAK,
        config.SPELL_BRILLIANT_INSPIRATION,
        config.SPELL_BRISTLE,
        config.SPELL_BURNING_GAZE,
        config.SPELL_BURST_BONDS,
        config.SPELL_CACOPHONOUS_CALL,
        config.SPELL_CACOPHONOUS_CALL_MASS,
        config.SPELL_CALCIFIC_TOUCH,
        config.SPELL_CALL_ANIMAL,
        config.SPELL_CAMPFIRE_WALL,
        config.SPELL_CAST_OUT,
        config.SPELL_CASTIGATE,
        config.SPELL_CASTIGATE_MASS,
        config.SPELL_CHALLENGE_EVIL,
        config.SPELL_CHAMELEON_STRIDE,
        config.SPELL_CLASHING_ROCKS,
        config.SPELL_CLEANSE,
        config.SPELL_CLOAK_OF_DREAMS,
        config.SPELL_CLOAK_OF_SHADE,
        config.SPELL_CLOAK_OF_WINDS,
        config.SPELL_CONFESS,
        config.SPELL_CONTAGIOUS_FLAME,
        config.SPELL_COORDINATED_EFFORT,
        config.SPELL_CORRUPTION_RESISTANCE,
        config.SPELL_COWARD_S_LAMENT,
        config.SPELL_CRAFTER_S_CURSE,
        config.SPELL_CRAFTER_S_FORTUNE,
        config.SPELL_CREATE_PIT,
        config.SPELL_CREATE_TREASURE_MAP,
        config.SPELL_CUP_OF_DUST,
        config.SPELL_DANCING_LANTERN,
        config.SPELL_DEADLY_FINALE,
        config.SPELL_DEAFENING_SONG_BOLT,
        config.SPELL_DEFILE_ARMOR,
        config.SPELL_DEFLECTION,
        config.SPELL_DELAYED_CONSUMPTION,
        config.SPELL_DENOUNCE,
        config.SPELL_DETECT_ABERRATION,
        config.SPELL_DETONATE,
        config.SPELL_DEVOLUTION,
        config.SPELL_DISCORDANT_BLAST,
        config.SPELL_DIVINE_TRANSFER,
        config.SPELL_DIVINE_VESSEL,
        config.SPELL_DRACONIC_RESERVOIR,
        config.SPELL_DRAGON_S_BREATH,
        config.SPELL_DUST_OF_TWILIGHT,
        config.SPELL_EAGLE_EYE,
        config.SPELL_ELEMENTAL_AURA,
        config.SPELL_ELEMENTAL_SPEECH,
        config.SPELL_ELEMENTAL_TOUCH,
        config.SPELL_ELUDE_TIME,
        config.SPELL_ENEMY_HAMMER,
        config.SPELL_ENTER_IMAGE,
        config.SPELL_EUPHORIC_TRANQUILITY,
        config.SPELL_EVOLUTION_SURGE_LESSER,
        config.SPELL_EVOLUTION_SURGE,
        config.SPELL_EVOLUTION_SURGE_GREATER,
        config.SPELL_EXPEDITIOUS_EXCAVATION,
        config.SPELL_EXPEND,
        config.SPELL_FEAST_OF_ASHES,
        config.SPELL_FEATHER_STEP,
        config.SPELL_FEATHER_STEP_MASS,
        config.SPELL_FESTER,
        config.SPELL_FESTER_MASS,
        config.SPELL_FIERY_BODY,
        config.SPELL_FIRE_BREATH,
        config.SPELL_FIRE_OF_ENTANGLEMENT,
        config.SPELL_FIRE_OF_JUDGMENT,
        config.SPELL_FIRE_OF_VENGEANCE,
        config.SPELL_FIRE_SNAKE,
        config.SPELL_FIREBRAND,
        config.SPELL_FIREFALL,
        config.SPELL_FLAMES_OF_THE_FAITHFUL,
        config.SPELL_FLARE_BURST,
        config.SPELL_FLUID_FORM,
        config.SPELL_FLY_MASS,
        config.SPELL_FOE_TO_FRIEND,
        config.SPELL_FOLLOW_AURA,
        config.SPELL_FOOL_S_FORBIDDANCE,
        config.SPELL_FORCED_REPENTANCE,
        config.SPELL_FROZEN_NOTE,
        config.SPELL_GALLANT_INSPIRATION,
        config.SPELL_GETAWAY,
        config.SPELL_GEYSER,
        config.SPELL_GHOSTBANE_DIRGE,
        config.SPELL_GHOSTBANE_DIRGE_MASS,
        config.SPELL_GLIDE,
        config.SPELL_GRACE,
        config.SPELL_GRAVITY_BOW,
        config.SPELL_GROVE_OF_RESPITE,
        config.SPELL_GUIDING_STAR,
        config.SPELL_HEROIC_FINALE,
        config.SPELL_HERO_S_DEFIANCE,
        config.SPELL_HIDDEN_SPEECH,
        config.SPELL_HIDE_CAMPSITE,
        config.SPELL_HOLY_WHISPER,
        config.SPELL_HONEYED_TONGUE,
        config.SPELL_HUNGRY_PIT,
        config.SPELL_HYDRAULIC_PUSH,
        config.SPELL_HYDRAULIC_TORRENT,
        config.SPELL_ILL_OMEN,
        config.SPELL_INNOCENCE,
        config.SPELL_INSTANT_ARMOR,
        config.SPELL_INSTANT_ENEMY,
        config.SPELL_INVIGORATE,
        config.SPELL_INVIGORATE_MASS,
        config.SPELL_JESTER_S_JAUNT,
        config.SPELL_KEEN_SENSES,
        config.SPELL_KING_S_CASTLE,
        config.SPELL_KNIGHT_S_CALLING,
        config.SPELL_LEAD_BLADES,
        config.SPELL_LIFE_BUBBLE,
        config.SPELL_LIGHT_LANCE,
        config.SPELL_LILY_PAD_STRIDE,
        config.SPELL_LOCKJAW,
        config.SPELL_MARKS_OF_FORBIDDANCE,
        config.SPELL_MASK_DWEOMER,
        config.SPELL_MEMORY_LAPSE,
        config.SPELL_MOONSTRUCK,
        config.SPELL_NAP_STACK,
        config.SPELL_NATURAL_RHYTHM,
        config.SPELL_NATURE_S_EXILE,
        config.SPELL_NEGATE_AROMA,
        config.SPELL_OATH_OF_PEACE,
        config.SPELL_ORACLE_S_BURDEN,
        config.SPELL_PAIN_STRIKE,
        config.SPELL_PAIN_STRIKE_MASS,
        config.SPELL_PALADIN_S_SACRIFICE,
        config.SPELL_PHANTASMAL_REVENGE,
        config.SPELL_PHANTASMAL_WEB,
        config.SPELL_PIED_PIPING,
        config.SPELL_PILLAR_OF_LIFE,
        config.SPELL_PLANAR_ADAPTATION,
        config.SPELL_PLANAR_ADAPTATION_MASS,
        config.SPELL_POX_PUSTULES,
        config.SPELL_PROTECTIVE_SPIRIT,
        config.SPELL_PURGING_FINALE,
        config.SPELL_PURIFIED_CALLING,
        config.SPELL_PUTREFY_FOOD_AND_DRINK,
        config.SPELL_RALLY_POINT,
        config.SPELL_REBUKE,
        config.SPELL_RAMPART,
        config.SPELL_REJUVENATE_EIDOLON_LESSER,
        config.SPELL_REJUVENATE_EIDOLON,
        config.SPELL_REJUVENATE_EIDOLON_GREATER,
        config.SPELL_RESOUNDING_BLOW,
        config.SPELL_REST_ETERNAL,
        config.SPELL_RESTFUL_SLEEP,
        config.SPELL_RESURGENT_TRANSFORMATION,
        config.SPELL_RETRIBUTION,
        config.SPELL_REVIVING_FINALE,
        config.SPELL_RIGHTEOUS_VIGOR,
        config.SPELL_RIVER_OF_WIND,
        config.SPELL_SACRED_BOND,
        config.SPELL_SACRIFICIAL_OATH,
        config.SPELL_SADDLE_SURGE,
        config.SPELL_SANCTIFY_ARMOR,
        config.SPELL_SAVING_FINALE,
        config.SPELL_SCENT_TRAIL,
        config.SPELL_SCREECH,
        config.SPELL_SCULPT_CORPSE,
        config.SPELL_SEAMANTLE,
        config.SPELL_SEEK_THOUGHTS,
        config.SPELL_SHARE_LANGUAGE,
        config.SPELL_SHADOW_PROJECTION,
        config.SPELL_SHARE_SENSES,
        config.SPELL_SHIFTING_SAND,
        config.SPELL_SHARED_WRATH,
        config.SPELL_SIFT,
        config.SPELL_SIROCCO,
        config.SPELL_SLEEPWALK,
        config.SPELL_SLIPSTREAM,
        config.SPELL_SNAKE_STAFF,
        config.SPELL_SOLID_NOTE,
        config.SPELL_SPARK,
        config.SPELL_SPIKED_PIT,
        config.SPELL_SPIRITUAL_ALLY,
        config.SPELL_SPITE,
        config.SPELL_STAY_THE_HAND,
        config.SPELL_STONE_CALL,
        config.SPELL_STONE_FIST,
        config.SPELL_STORMBOLTS,
        config.SPELL_STRONG_JAW,
        config.SPELL_STUMBLE_GAP,
        config.SPELL_STUNNING_FINALE,
        config.SPELL_SUFFOCATION,
        config.SPELL_SUFFOCATION_MASS,
        config.SPELL_SUMMON_EIDOLON,
        config.SPELL_SWARM_SKIN,
        config.SPELL_THORN_BODY,
        config.SPELL_THREEFOLD_ASPECT,
        config.SPELL_THUNDERING_DRUMS,
        config.SPELL_TIMELY_INSPIRATION,
        config.SPELL_TIRELESS_PURSUIT,
        config.SPELL_TIRELESS_PURSUERS,
        config.SPELL_TOUCH_OF_GRACELESSNESS,
        config.SPELL_TOUCH_OF_THE_SEA,
        config.SPELL_TRANSMOGRIFY,
        config.SPELL_TRANSMUTE_POTION_TO_POISON,
        config.SPELL_TREASURE_STITCHING,
        config.SPELL_TRUE_FORM,
        config.SPELL_TSUNAMI,
        config.SPELL_TWILIGHT_KNIFE,
        config.SPELL_TWIN_FORM,
        config.SPELL_UNFETTER,
        config.SPELL_UNIVERSAL_FORMULA,
        config.SPELL_UNWILLING_SHIELD,
        config.SPELL_UNWITTING_ALLY,
        config.SPELL_VANISH,
        config.SPELL_VEIL_OF_POSITIVE_ENERGY,
        config.SPELL_VENOMOUS_BOLT,
        config.SPELL_VERSATILE_WEAPON,
        config.SPELL_VOMIT_SWARM,
        config.SPELL_VORTEX,
        config.SPELL_WAKE_OF_LIGHT,
        config.SPELL_WALL_OF_LAVA,
        config.SPELL_WALL_OF_SUPPRESSION,
        config.SPELL_WANDERING_STAR_MOTES,
        config.SPELL_WARD_THE_FAITHFUL,
        config.SPELL_WEAPON_OF_AWE,
        config.SPELL_WINDS_OF_VENGEANCE,
        config.SPELL_WORLD_WAVE,
        config.SPELL_WRATH,
        config.SPELL_WRATHFUL_MANTLE,
        config.SPELL_HUNTER_S_EYE,
        config.SPELL_HUNTER_S_HOWL,
        config.SPELL_PERCEIVE_CUES,
        config.SPELL_RESIDUAL_TRACKING,
        config.SPELL_BLESSING_OF_COURAGE_AND_LIFE,
        config.SPELL_RIFT_OF_RUIN,
        config.SPELL_CONSTRICTING_COILS,
        config.SPELL_ANCESTRAL_MEMORY,
        config.SPELL_GORUM_S_ARMOR,
        config.SPELL_HARROWING,
        config.SPELL_INFERNAL_HEALING,
        config.SPELL_INFERNAL_HEALING_GREATER,
        config.SPELL_LOVER_S_VENGEANCE,
        config.SPELL_SHIELD_OF_THE_DAWNFLOWER,
        config.SPELL_TELEPORT_TRAP,
        config.SPELL_UNBREAKABLE_HEART,
        config.SPELL_VISION_OF_LAMASHTU,
        config.SPELL_WATERS_OF_LAMASHTU,
        config.SPELL_TRAIL_OF_THE_ROSE,
        config.SPELL_ACIDIC_SPRAY,
        config.SPELL_ACUTE_SENSES,
        config.SPELL_AGE_RESISTANCE_LESSER,
        config.SPELL_AGE_RESISTANCE_GREATER,
        config.SPELL_AGE_RESISTANCE,
        config.SPELL_ALLEGRO,
        config.SPELL_ANIMATE_DEAD_LESSER,
        config.SPELL_ANTHROPOMORPHIC_ANIMAL,
        config.SPELL_ANTICIPATE_PERIL,
        config.SPELL_ARBOREAL_HAMMER,
        config.SPELL_ARCANA_THEFT,
        config.SPELL_ARCHON_S_AURA,
        config.SPELL_ARROW_OF_LAW,
        config.SPELL_ASH_STORM,
        config.SPELL_ASTRAL_PROJECTION_LESSER,
        config.SPELL_ATAVISM,
        config.SPELL_ATAVISM_MASS,
        config.SPELL_AURA_OF_DOOM,
        config.SPELL_BADGER_S_FEROCITY,
        config.SPELL_BATTLEMIND_LINK,
        config.SPELL_BESTOW_GRACE_OF_THE_CHAMPION,
        config.SPELL_BLADE_OF_BRIGHT_VICTORY,
        config.SPELL_BLADE_OF_DARK_TRIUMPH,
        config.SPELL_BLESSING_OF_THE_MOLE,
        config.SPELL_BLOOD_CROW_STRIKE,
        config.SPELL_BLOOD_MIST,
        config.SPELL_BLOOD_TRANSCRIPTION,
        config.SPELL_BOILING_BLOOD,
        config.SPELL_BUNGLE,
        config.SPELL_BURROW,
        config.SPELL_BURST_OF_NETTLES,
        config.SPELL_CACKLING_SKULL,
        config.SPELL_CALL_CONSTRUCT,
        config.SPELL_CAPE_OF_WASPS,
        config.SPELL_CAUSTIC_ERUPTION,
        config.SPELL_CHORD_OF_SHARDS,
        config.SPELL_CIRCLE_OF_CLARITY,
        config.SPELL_COLD_ICE_STRIKE,
        config.SPELL_COMPASSIONATE_ALLY,
        config.SPELL_CONJURE_BLACK_PUDDING,
        config.SPELL_CONTAGION_GREATER,
        config.SPELL_CONTROL_CONSTRUCT,
        config.SPELL_CONTROL_SUMMONED_CREATURE,
        config.SPELL_CORROSIVE_CONSUMPTION,
        config.SPELL_CORROSIVE_TOUCH,
        config.SPELL_COUNTLESS_EYES,
        config.SPELL_CREATE_DEMIPLANE,
        config.SPELL_CREATE_DEMIPLANE_LESSER,
        config.SPELL_CREATE_DEMIPLANE_GREATER,
        config.SPELL_CURSE_MAJOR,
        config.SPELL_CURSE_OF_DISGUST,
        config.SPELL_CURSE_OF_MAGIC_NEGATION,
        config.SPELL_CURSED_EARTH,
        config.SPELL_CUSHIONING_BANDS,
        config.SPELL_DANCE_OF_A_HUNDRED_CUTS,
        config.SPELL_DANCE_OF_A_THOUSAND_CUTS,
        config.SPELL_DARKVISION_GREATER,
        config.SPELL_DAZE_MASS,
        config.SPELL_DECOMPOSE_CORPSE,
        config.SPELL_DEFENSIVE_SHOCK,
        config.SPELL_DELAY_PAIN,
        config.SPELL_DELUSIONAL_PRIDE,
        config.SPELL_DIAGNOSE_DISEASE,
        config.SPELL_DISFIGURING_TOUCH,
        config.SPELL_DISGUISE_OTHER,
        config.SPELL_DISTRACTING_CACOPHONY,
        config.SPELL_DISTRESSING_TONE,
        config.SPELL_DIVINE_PURSUIT,
        config.SPELL_DREAD_BOLT,
        config.SPELL_EAGLE_AERIE,
        config.SPELL_EAR_PIERCING_SCREAM,
        config.SPELL_ECHOLOCATION,
        config.SPELL_ELDRITCH_FEVER,
        config.SPELL_ENVIOUS_URGE,
        config.SPELL_EPIDEMIC,
        config.SPELL_ERUPTIVE_PUSTULES,
        config.SPELL_EXCRUCIATING_DEFORMATION,
        config.SPELL_EXQUISITE_ACCOMPANIMENT,
        config.SPELL_FALSE_LIFE_GREATER,
        config.SPELL_FAMILIAR_MELDING,
        config.SPELL_FICKLE_WINDS,
        config.SPELL_FLESHWORM_INFESTATION,
        config.SPELL_FORBID_ACTION,
        config.SPELL_FORBID_ACTION_GREATER,
        config.SPELL_FORCE_HOOK_CHARGE,
        config.SPELL_FORCE_PUNCH,
        config.SPELL_FORCED_QUIET,
        config.SPELL_FRIGID_TOUCH,
        config.SPELL_FROSTBITE,
        config.SPELL_FUMBLETONGUE,
        config.SPELL_FUNGAL_INFESTATION,
        config.SPELL_GHOSTLY_DISGUISE,
        config.SPELL_HAUNTING_CHOIR,
        config.SPELL_HAUNTING_MISTS,
        config.SPELL_HEX_WARD,
        config.SPELL_HOLY_ICE,
        config.SPELL_HOLY_SHIELD,
        config.SPELL_HORN_OF_PURSUIT,
        config.SPELL_HOWLING_AGONY,
        config.SPELL_ICE_BODY,
        config.SPELL_ICE_CRYSTAL_TELEPORT,
        config.SPELL_ICICLE_DAGGER,
        config.SPELL_ICY_PRISON,
        config.SPELL_ICY_PRISON_MASS,
        config.SPELL_IMBUE_WITH_AURA,
        config.SPELL_INTERPLANETARY_TELEPORT,
        config.SPELL_INTERROGATION,
        config.SPELL_INTERROGATION_GREATER,
        config.SPELL_JOYFUL_RAPTURE,
        config.SPELL_KI_ARROW,
        config.SPELL_KI_LEECH,
        config.SPELL_KI_SHOUT,
        config.SPELL_KNOW_THE_ENEMY,
        config.SPELL_LEASHED_SHACKLES,
        config.SPELL_LEND_JUDGMENT,
        config.SPELL_LEND_JUDGMENT_GREATER,
        config.SPELL_LIGHTNING_ARC,
        config.SPELL_LOATHSOME_VEIL,
        config.SPELL_LUNAR_VEIL,
        config.SPELL_MAD_HALLUCINATION,
        config.SPELL_MAD_MONKEYS,
        config.SPELL_MALFUNCTION,
        config.SPELL_MALICIOUS_SPITE,
        config.SPELL_MARIONETTE_POSSESSION,
        config.SPELL_MASTERWORK_TRANSFORMATION,
        config.SPELL_MISERABLE_PITY,
        config.SPELL_MONSTROUS_PHYSIQUE_I,
        config.SPELL_MONSTROUS_PHYSIQUE_I_I,
        config.SPELL_MONSTROUS_PHYSIQUE_I_I_I,
        config.SPELL_MONSTROUS_PHYSIQUE_I_V,
        config.SPELL_MURDEROUS_COMMAND,
        config.SPELL_OPPRESSIVE_BOREDOM,
        config.SPELL_ORACLE_S_VESSEL,
        config.SPELL_ORB_OF_THE_VOID,
        config.SPELL_OVERWHELMING_GRIEF,
        config.SPELL_OVERWHELMING_PRESENCE,
        config.SPELL_PERNICIOUS_POISON,
        config.SPELL_PERSUASIVE_GOAD,
        config.SPELL_PIERCING_SHRIEK,
        config.SPELL_PLAGUE_CARRIER,
        config.SPELL_PLAGUE_STORM,
        config.SPELL_PLAY_INSTRUMENT,
        config.SPELL_POLAR_MIDNIGHT,
        config.SPELL_POLYPURPOSE_PANACEA,
        config.SPELL_POSSESS_OBJECT,
        config.SPELL_PREDICTION_OF_FAILURE,
        config.SPELL_PRIMAL_SCREAM,
        config.SPELL_PROTECTIVE_PENUMBRA,
        config.SPELL_RAIN_OF_FROGS,
        config.SPELL_RAISE_ANIMAL_COMPANION,
        config.SPELL_RAPID_REPAIR,
        config.SPELL_RAY_OF_SICKENING,
        config.SPELL_RECKLESS_INFATUATION,
        config.SPELL_REMOVE_SICKNESS,
        config.SPELL_REPROBATION,
        config.SPELL_RESONATING_WORD,
        config.SPELL_RESTORE_CORPSE,
        config.SPELL_RESTORE_EIDOLON,
        config.SPELL_RESTORE_EIDOLON_LESSER,
        config.SPELL_RIDE_THE_LIGHTNING,
        config.SPELL_RIDE_THE_WAVES,
        config.SPELL_SANCTIFY_CORPSE,
        config.SPELL_SANDS_OF_TIME,
        config.SPELL_SCOURING_WINDS,
        config.SPELL_SCULPT_SIMULACRUM,
        config.SPELL_SERENITY,
        config.SPELL_SHADOWBARD,
        config.SPELL_SHADOW_STEP,
        config.SPELL_SHADOW_WEAPON,
        config.SPELL_SHARD_OF_CHAOS,
        config.SPELL_SHARE_MEMORY,
        config.SPELL_SIMULACRUM_LESSER,
        config.SPELL_SKINSEND,
        config.SPELL_SMUG_NARCISSISM,
        config.SPELL_SNAPDRAGON_FIREWORKS,
        config.SPELL_SONIC_THRUST,
        config.SPELL_SOOTHE_CONSTRUCT,
        config.SPELL_SPEAR_OF_PURITY,
        config.SPELL_SPIT_VENOM,
        config.SPELL_STEAL_VOICE,
        config.SPELL_STRANGLING_HAIR,
        config.SPELL_SUMMON_ELDER_WORM,
        config.SPELL_SUMMON_FROGHEMOTH,
        config.SPELL_SUMMON_MINOR_ALLY,
        config.SPELL_SUMMON_MINOR_MONSTER,
        config.SPELL_SURMOUNT_AFFLICTION,
        config.SPELL_SYMBOL_OF_HEALING,
        config.SPELL_SYMBOL_OF_MIRRORING,
        config.SPELL_SYMBOL_OF_REVELATION,
        config.SPELL_SYMBOL_OF_SCRYING,
        config.SPELL_SYMBOL_OF_SEALING,
        config.SPELL_SYMBOL_OF_SLOWING,
        config.SPELL_SYMBOL_OF_STRIFE,
        config.SPELL_SYMBOL_OF_VULNERABILITY,
        config.SPELL_TAR_BALL,
        config.SPELL_TEMPORARY_RESURRECTION,
        config.SPELL_TERRIBLE_REMORSE,
        config.SPELL_TOUCH_OF_SLIME,
        config.SPELL_TOXIC_GIFT,
        config.SPELL_TRANSMUTE_BLOOD_TO_ACID,
        config.SPELL_UNADULTERATED_LOATHING,
        config.SPELL_UNBREAKABLE_CONSTRUCT,
        config.SPELL_UNDEAD_ANATOMY_I,
        config.SPELL_UNDEAD_ANATOMY_I_I,
        config.SPELL_UNDEAD_ANATOMY_I_I_I,
        config.SPELL_UNDEAD_ANATOMY_I_V,
        config.SPELL_UNHOLY_ICE,
        config.SPELL_UNHOLY_SWORD,
        config.SPELL_UNNATURAL_LUST,
        config.SPELL_UNPREPARED_COMBATANT,
        config.SPELL_UNSHAKABLE_CHILL,
        config.SPELL_UTTER_CONTEMPT,
        config.SPELL_VENGEFUL_OUTRAGE,
        config.SPELL_VERMIN_SHAPE_I,
        config.SPELL_VERMIN_SHAPE_I_I,
        config.SPELL_VESTMENT_OF_THE_CHAMPION,
        config.SPELL_VIRTUOSO_PERFORMANCE,
        config.SPELL_VISION_OF_HELL,
        config.SPELL_VITRIOLIC_MIST,
        config.SPELL_VOCAL_ALTERATION,
        config.SPELL_VOLCANIC_STORM,
        config.SPELL_WALL_OF_SOUND,
        config.SPELL_WARTRAIN_MOUNT,
        config.SPELL_WAVES_OF_ECSTASY,
        config.SPELL_WEB_SHELTER,
        config.SPELL_WITNESS,
        config.SPELL_WOODEN_PHALANX,
        config.SPELL_WORD_OF_RESOLVE,
        config.SPELL_YOUTHFUL_APPEARANCE,
        config.SPELL_STAGGERING_FALL,
        config.SPELL_GREENSIGHT,
        config.SPELL_SHEET_LIGHTNING,
        config.SPELL_BREEZE,
        config.SPELL_DRENCH,
        config.SPELL_JOLT,
        config.SPELL_PENUMBRA,
        config.SPELL_ROOT,
        config.SPELL_SCOOP,
        config.SPELL_DAZZLING_BLADE,
        config.SPELL_DAZZLING_BLADE_MASS,
        config.SPELL_SUMMON_ACCUSER,
        config.SPELL_SUMMON_INFERNAL_HOST,
        config.SPELL_ECHEAN_S_EXCELLENT_ENCLOSURE,
        config.SPELL_ABLATIVE_SPHERE,
        config.SPELL_BURNING_ARC,
        config.SPELL_SNOW_SHAPE,
        config.SPELL_SUMMON_TOTEM_CREATURE,
        config.SPELL_BATTERING_BLAST,
        config.SPELL_UNDEATH_WARD,
        config.SPELL_SILK_TO_STEEL,
        config.SPELL_ARAM_ZEY_S_FOCUS,
        config.SPELL_ARAM_ZEY_S_TRAP_WARD,
        config.SPELL_BITE_THE_HAND,
        config.SPELL_BITE_THE_HAND_MASS,
        config.SPELL_CORPSE_LANTERNS,
        config.SPELL_GILDED_WHISPERS,
        config.SPELL_LIPSTITCH,
        config.SPELL_PETULENGRO_S_VALIDATION,
        config.SPELL_SEQUESTER_THOUGHTS,
        config.SPELL_SHARESISTER,
        config.SPELL_STALWART_RESOLVE,
        config.SPELL_STOLEN_LIGHT,
        config.SPELL_TWISTED_INNARDS,
        config.SPELL_BLOT,
        config.SPELL_FIRE_SNEEZE,
        config.SPELL_LIMP_LASH,
        config.SPELL_ARODEN_S_SPELLBANE,
        config.SPELL_BLADED_DASH,
        config.SPELL_BLADED_DASH_GREATER,
        config.SPELL_BLAST_BARRIER,
        config.SPELL_CALL_WEAPON,
        config.SPELL_CRUSADER_S_EDGE,
        config.SPELL_EAGLESOUL,
        config.SPELL_ELDRITCH_CONDUIT,
        config.SPELL_ELDRITCH_CONDUIT_GREATER,
        config.SPELL_FLESHCURDLE,
        config.SPELL_FORCEFUL_STRIKE,
        config.SPELL_GEB_S_HAMMER,
        config.SPELL_GENIEKIND,
        config.SPELL_HUNGRY_DARKNESS,
        config.SPELL_HUNTER_S_LORE,
        config.SPELL_IMPART_MIND,
        config.SPELL_KHAIN_S_ARMY,
        config.SPELL_KISS_OF_THE_FIRST_WORLD,
        config.SPELL_LIGHT_OF_IOMEDAE,
        config.SPELL_MARTIAL_MARIONETTE,
        config.SPELL_MARTYR_S_BARGAIN,
        config.SPELL_MUSIC_OF_THE_SPHERES,
        config.SPELL_ORCHID_S_DROP,
        config.SPELL_PUGWAMPI_S_GRACE,
        config.SPELL_SHADOW_BARBS,
        config.SPELL_SHINING_CORD,
        config.SPELL_SIPHON_MAGIC,
        config.SPELL_SONG_OF_KYONIN,
        config.SPELL_SPELL_ABSORPTION,
        config.SPELL_SPELL_ABSORPTION_GREATER,
        config.SPELL_SPELLSCAR,
        config.SPELL_SUPPRESS_PRIMAL_MAGIC,
        config.SPELL_TATTOO_POTION,
        config.SPELL_TRANSFER_TATTOO,
        config.SPELL_VENGEFUL_COMETS,
        config.SPELL_VEX_GIANT,
        config.SPELL_WEAPONWAND,
        config.SPELL_ZONE_OF_FOUL_FLAMES,
        config.SPELL_ABLATIVE_BARRIER,
        config.SPELL_ABSORB_TOXICITY,
        config.SPELL_ABUNDANT_AMMUNITION,
        config.SPELL_ADJURING_STEP,
        config.SPELL_ADORATION,
        config.SPELL_AIR_BUBBLE,
        config.SPELL_AIR_WALK_COMMUNAL,
        config.SPELL_ANIMAL_ASPECT,
        config.SPELL_ANIMAL_ASPECT_GREATER,
        config.SPELL_ANT_HAUL_COMMUNAL,
        config.SPELL_ARCANE_CANNON,
        config.SPELL_BESTOW_WEAPON_PROFICIENCY,
        config.SPELL_BLISTERING_INVECTIVE,
        config.SPELL_BOWSTAFF,
        config.SPELL_BROW_GASHER,
        config.SPELL_BULLET_SHIELD,
        config.SPELL_BURST_OF_SPEED,
        config.SPELL_CAGING_BOMB_ADMIXTURE,
        config.SPELL_CERTAIN_GRIP,
        config.SPELL_CHAIN_OF_PERDITION,
        config.SPELL_COMPANION_MIND_LINK,
        config.SPELL_COMPEL_HOSTILITY,
        config.SPELL_DAMP_POWDER,
        config.SPELL_DARKVISION_COMMUNAL,
        config.SPELL_DAYBREAK_ARROW,
        config.SPELL_DEADLY_JUGGERNAUT,
        config.SPELL_DEADEYE_S_LORE,
        config.SPELL_DEBILITATING_PORTENT,
        config.SPELL_DELAY_POISON_COMMUNAL,
        config.SPELL_DESTABILIZE_POWDER,
        config.SPELL_DISCOVERY_TORCH,
        config.SPELL_DIVINE_ARROW,
        config.SPELL_DUST_FORM,
        config.SPELL_EFFORTLESS_ARMOR,
        config.SPELL_ENDURE_ELEMENTS_COMMUNAL,
        config.SPELL_ENERGY_SIEGE_SHOT,
        config.SPELL_ENERGY_SIEGE_SHOT_GREATER,
        config.SPELL_FABRICATE_BULLETS,
        config.SPELL_FIERY_SHURIKEN,
        config.SPELL_FIND_QUARRY,
        config.SPELL_FLASH_FIRE,
        config.SPELL_FOREST_FRIEND,
        config.SPELL_FRIGHTFUL_ASPECT,
        config.SPELL_FROST_FALL,
        config.SPELL_HAUNTED_FEY_ASPECT,
        config.SPELL_HEALING_THIEF,
        config.SPELL_HEROIC_INVOCATION,
        config.SPELL_HOSTILE_JUXTAPOSITION,
        config.SPELL_HOSTILE_JUXTAPOSITION_GREATER,
        config.SPELL_HOSTILE_LEVITATION,
        config.SPELL_ILLUSION_OF_CALM,
        config.SPELL_INSTRUMENT_OF_AGONY,
        config.SPELL_JOLTING_PORTENT,
        config.SPELL_JUDGMENT_LIGHT,
        config.SPELL_JURY_RIG,
        config.SPELL_KINETIC_REVERBERATION,
        config.SPELL_LANGUID_BOMB_ADMIXTURE,
        config.SPELL_LIBERATING_COMMAND,
        config.SPELL_LIFE_CONDUIT,
        config.SPELL_LIFE_CONDUIT_GREATER,
        config.SPELL_LIFE_CONDUIT_IMPROVED,
        config.SPELL_LIGHTNING_LASH_BOMB_ADMIXTURE,
        config.SPELL_LITANY_OF_DEFENSE,
        config.SPELL_LITANY_OF_ELOQUENCE,
        config.SPELL_LITANY_OF_ENTANGLEMENT,
        config.SPELL_LITANY_OF_ESCAPE,
        config.SPELL_LITANY_OF_MADNESS,
        config.SPELL_LITANY_OF_RIGHTEOUSNESS,
        config.SPELL_LITANY_OF_SIGHT,
        config.SPELL_LITANY_OF_SLOTH,
        config.SPELL_LITANY_OF_THUNDER,
        config.SPELL_LITANY_OF_VENGEANCE,
        config.SPELL_LITANY_OF_WARDING,
        config.SPELL_LITANY_OF_WEAKNESS,
        config.SPELL_LOCATE_WEAKNESS,
        config.SPELL_LOCK_GAZE,
        config.SPELL_LONGSHOT,
        config.SPELL_MAGIC_SIEGE_ENGINE,
        config.SPELL_MAGIC_SIEGE_ENGINE_GREATER,
        config.SPELL_MASK_DWEOMER_COMMUNAL,
        config.SPELL_MIND_BLANK_COMMUNAL,
        config.SPELL_MIRROR_STRIKE,
        config.SPELL_MOMENT_OF_GREATNESS,
        config.SPELL_MOUNT_COMMUNAL,
        config.SPELL_MUTAGENIC_TOUCH,
        config.SPELL_NAMED_BULLET,
        config.SPELL_NAMED_BULLET_GREATER,
        config.SPELL_NEGATIVE_REACTION,
        config.SPELL_NONDETECTION_COMMUNAL,
        config.SPELL_OBSIDIAN_FLOW,
        config.SPELL_PEACEBOND,
        config.SPELL_PELLET_BLAST,
        config.SPELL_PHANTOM_CHARIOT,
        config.SPELL_PHANTOM_DRIVER,
        config.SPELL_PHANTOM_STEED_COMMUNAL,
        config.SPELL_PILFERING_HAND,
        config.SPELL_PROTECTION_FROM_ARROWS_COMMUNAL,
        config.SPELL_PROTECTION_FROM_CHAOS_COMMUNAL,
        config.SPELL_PROTECTION_FROM_ENERGY_COMMUNAL,
        config.SPELL_PROTECTION_FROM_EVIL_COMMUNAL,
        config.SPELL_PROTECTION_FROM_GOOD_COMMUNAL,
        config.SPELL_PROTECTION_FROM_LAW_COMMUNAL,
        config.SPELL_PUP_SHAPE,
        config.SPELL_QUALM,
        config.SPELL_RECOIL_FIRE,
        config.SPELL_REINFORCE_ARMAMENTS,
        config.SPELL_REINFORCE_ARMAMENTS_COMMUNAL,
        config.SPELL_RELOADING_HANDS,
        config.SPELL_RESINOUS_SKIN,
        config.SPELL_RESIST_ENERGY_COMMUNAL,
        config.SPELL_RETURNING_WEAPON,
        config.SPELL_RETURNING_WEAPON_COMMUNAL,
        config.SPELL_RICOCHET_SHOT,
        config.SPELL_SEE_ALIGNMENT,
        config.SPELL_SHADOW_BOMB_ADMIXTURE,
        config.SPELL_SHARE_LANGUAGE_COMMUNAL,
        config.SPELL_SHOCK_SHIELD,
        config.SPELL_SHOCKING_IMAGE,
        config.SPELL_SIEGE_OF_TREES,
        config.SPELL_SIEGE_OF_TREES_GREATER,
        config.SPELL_SPELL_IMMUNITY_COMMUNAL,
        config.SPELL_SPELL_IMMUNITY_GREATER_COMMUNAL,
        config.SPELL_SPIDER_CLIMB_COMMUNAL,
        config.SPELL_SPONTANEOUS_IMMOLATION,
        config.SPELL_STABILIZE_POWDER,
        config.SPELL_STONESKIN_COMMUNAL,
        config.SPELL_SUMMONER_CONDUIT,
        config.SPELL_SUN_METAL,
        config.SPELL_SYMBOL_OF_STRIKING,
        config.SPELL_TACTICAL_ACUMEN,
        config.SPELL_TAR_POOL,
        config.SPELL_TARGETED_BOMB_ADMIXTURE,
        config.SPELL_TELEKINETIC_ASSEMBLY,
        config.SPELL_TELEKINETIC_CHARGE,
        config.SPELL_TERRAIN_BOND,
        config.SPELL_THUNDER_FIRE,
        config.SPELL_TONGUES_COMMUNAL,
        config.SPELL_TOUCH_INJECTION,
        config.SPELL_TWISTED_SPACE,
        config.SPELL_UNERRING_WEAPON,
        config.SPELL_VIPER_BOMB_ADMIXTURE,
        config.SPELL_WALK_THROUGH_SPACE,
        config.SPELL_WARDING_WEAPON,
        config.SPELL_WATER_WALK_COMMUNAL,
        config.SPELL_WEAKEN_POWDER,
        config.SPELL_WILDERNESS_SOLDIERS,
        config.SPELL_WREATH_OF_BLADES,
        config.SPELL_ASPECT_OF_THE_NIGHTINGALE,
        config.SPELL_VAMPIRIC_HUNGER,
        config.SPELL_AWAKEN_THE_DEVOURED,
        config.SPELL_CHARON_S_DISPENSATION,
        config.SPELL_CREATE_SOUL_GEM,
        config.SPELL_DAEMON_WARD,
        config.SPELL_DEATH_KNELL_AURA,
        config.SPELL_DEATH_KNELL_AURA_GREATER,
        config.SPELL_LASH_OF_THE_ASTRADAEMON,
        config.SPELL_PARASITIC_SOUL,
        config.SPELL_SCOURGE_OF_THE_HORSEMEN,
        config.SPELL_SOUL_TRANSFER,
        config.SPELL_SUMMON_CACODAEMON,
        config.SPELL_SUMMON_CACODAEMON_GREATER,
        config.SPELL_SUMMON_CEUSTODAEMON,
        config.SPELL_SUMMON_DERGHODAEMON,
        config.SPELL_SUMMON_ERODAEMON,
        config.SPELL_SUMMON_MELADAEMON,
        config.SPELL_SUMMON_THANADAEMON,
        config.SPELL_CALL_THE_VOID,
        config.SPELL_BLACK_SPOT,
        config.SPELL_SALVAGE,
        config.SPELL_SKELETON_CREW,
        config.SPELL_TRACK_SHIP,
        config.SPELL_UNSEEN_CREW,
        config.SPELL_ADVANCED_SCURVY,
        config.SPELL_CLOUD_OF_SEASICKNESS,
        config.SPELL_SUBMERGE_SHIP,
        config.SPELL_HEROIC_FORTUNE,
        config.SPELL_HEROIC_FORTUNE_MASS,
        config.SPELL_MALEDICTION,
        config.SPELL_SEVERED_FATE,
        config.SPELL_UNRAVEL_DESTINY,
        config.SPELL_EMBRACE_DESTINY,
        config.SPELL_GROUNDSWELL,
        config.SPELL_IRONBEARD,
        config.SPELL_TOILSOME_CHANT,
        config.SPELL_BLEND,
        config.SPELL_WARD_OF_THE_SEASON,
        config.SPELL_WHISPERING_LORE,
        config.SPELL_DEATH_FROM_BELOW,
        config.SPELL_JITTERBUGS,
        config.SPELL_MAJOR_PHANTOM_OBJECT,
        config.SPELL_MINOR_DREAM,
        config.SPELL_MINOR_PHANTOM_OBJECT,
        config.SPELL_RECHARGE_INNATE_MAGIC,
        config.SPELL_FORGETFUL_SLUMBER,
        config.SPELL_PARAGON_SURGE,
        config.SPELL_RESILIENT_RESERVOIR,
        config.SPELL_URBAN_GRACE,
        config.SPELL_BATTLE_TRANCE,
        config.SPELL_GHOST_WOLF,
        config.SPELL_HALF_BLOOD_EXTRACTION,
        config.SPELL_LINEBREAKER,
        config.SPELL_SAVAGE_MAW,
        config.SPELL_BLESSING_OF_LUCK_AND_RESOLVE,
        config.SPELL_BLESSING_OF_LUCK_AND_RESOLVE_MASS,
        config.SPELL_ESCAPING_WARD,
        config.SPELL_FEARSOME_DUPLICATE,
        config.SPELL_VILLAGE_VEIL,
        config.SPELL_BESTOW_INSIGHT,
        config.SPELL_BLACK_MARK,
        config.SPELL_OLD_SALT_S_CURSE,
        config.SPELL_SACRED_SPACE,
        config.SPELL_TRUESPEAK,
        config.SPELL_VEIL_OF_HEAVEN,
        config.SPELL_NINE_LIVES,
        config.SPELL_STEAL_BREATH,
        config.SPELL_BLINDING_RAY,
        config.SPELL_LIFE_CHANNEL,
        config.SPELL_SPAWN_WARD,
        config.SPELL_ANCESTRAL_REGRESSION,
        config.SPELL_WEB_BOLT,
        config.SPELL_WEB_CLOUD,
        config.SPELL_GLOOMBLIND_BOLTS,
        config.SPELL_SHADOWY_HAVEN,
        config.SPELL_FIRE_TRAIL,
        config.SPELL_MUDBALL,
        config.SPELL_VOMIT_TWIN,
        config.SPELL_AGONIZING_REBUKE,
        config.SPELL_CHAINS_OF_FIRE,
        config.SPELL_DEATH_CANDLE,
        config.SPELL_FIRESTREAM,
        config.SPELL_FURY_OF_THE_SUN,
        config.SPELL_HEALING_WARMTH,
        config.SPELL_SCORCHING_ASH_FORM,
        config.SPELL_TOUCH_OF_COMBUSTION,
        config.SPELL_IMPROVE_TRAP,
        config.SPELL_BLOOD_BLAZE,
        config.SPELL_BLOOD_SCENT,
        config.SPELL_ENEMY_S_HEART,
        config.SPELL_SENTRY_SKULL,
        config.SPELL_BINDING_EARTH,
        config.SPELL_BINDING_EARTH_MASS,
        config.SPELL_MIGHTY_FIST_OF_THE_EARTH,
        config.SPELL_RAGING_RUBBLE,
        config.SPELL_STONE_SHIELD,
        config.SPELL_ALCHEMICAL_TINKERING,
        config.SPELL_DELAY_DISEASE,
        config.SPELL_SICKENING_STRIKES,
        config.SPELL_ABSORBING_INHALATION,
        config.SPELL_CLOUD_SHAPE,
        config.SPELL_GUSTING_SPHERE,
        config.SPELL_MIASMATIC_FORM,
        config.SPELL_PATH_OF_THE_WINDS,
        config.SPELL_WIND_BLADES,
        config.SPELL_WINDY_ESCAPE,
        config.SPELL_COMMUNE_WITH_BIRDS,
        config.SPELL_THEFT_WARD,
        config.SPELL_WINTER_FEATHERS,
        config.SPELL_DAMNATION_STRIDE,
        config.SPELL_HELLMOUTH_LASH,
        config.SPELL_MARID_S_MASTERY,
        config.SPELL_NEREID_S_GRACE,
        config.SPELL_NIXIE_S_LURE,
        config.SPELL_UNDINE_S_CURSE,
        config.SPELL_SOW_THOUGHT,
        config.SPELL_ABOLETH_S_LUNG,
        config.SPELL_FINS_TO_FEET,
        config.SPELL_KARMIC_BLESSING,
        config.SPELL_STRONG_WINGS,
        config.SPELL_IMBUE_WITH_ELEMENTAL_MIGHT,
        config.SPELL_EARTH_GLIDE,
        config.SPELL_PREHENSILE_PILFER,
        config.SPELL_SQUEEZE,
        config.SPELL_SHADOW_ANCHOR,
        config.SPELL_BLOOD_MONEY,
        config.SPELL_COVETOUS_AURA,
        config.SPELL_DEATHWINE,
        config.SPELL_SIGN_OF_WRATH,
        config.SPELL_SWIPE,
        config.SPELL_UNCONSCIOUS_AGENDA,
        config.SPELL_IRONBLOOM_SPROUTS,
        config.SPELL_BED_OF_IRON,
        config.SPELL_CARRY_COMPANION,
        config.SPELL_CLARION_CALL,
        config.SPELL_EMBLAZON_CREST,
        config.SPELL_KEEP_WATCH,
        config.SPELL_SERREN_S_ARMOR_LOCK,
        config.SPELL_SERREN_S_SWIFT_GIRDING,
        config.SPELL_WARD_SHIELD,
        config.SPELL_CURSE_ITEM,
        config.SPELL_LISSALAN_SNAKE_SIGIL,
        config.SPELL_DISPLAY_AVERSION,
        config.SPELL_DOMINATION_LINK,
        config.SPELL_PROJECT_WEAKNESS,
        config.SPELL_STEAL_YEARS,
        config.SPELL_STEAL_YEARS_GREATER,
        config.SPELL_TRANSMUTE_WINE_TO_BLOOD,
        config.SPELL_FROST_MAMMOTH,
        config.SPELL_WINTER_S_GRASP,
        config.SPELL_IRRISENI_MIRROR_SIGHT,
        config.SPELL_BLEED_FOR_YOUR_MASTER,
        config.SPELL_DIE_FOR_YOUR_MASTER,
        config.SPELL_FAMILIAR_FIGMENT,
        config.SPELL_HUNTER_S_FRIEND,
        config.SPELL_SCAMPER,
        config.SPELL_SEA_STEED,
        config.SPELL_SEA_STALLION,
        config.SPELL_SHARE_SHAPE,
        config.SPELL_SKY_STEED,
        config.SPELL_FLURRY_OF_SNOWBALLS,
        config.SPELL_SNOWBALL,
        config.SPELL_ICE_SPEARS,
        config.SPELL_MARTYR_S_LAST_BLESSING,
        config.SPELL_PEASANT_ARMAMENTS,
        config.SPELL_CONJURE_DEADFALL,
        config.SPELL_CREATE_HOLDS,
        config.SPELL_DETERMINE_DEPTH,
        config.SPELL_DISCERN_VALUE,
        config.SPELL_NATURE_S_RAVAGES,
        config.SPELL_NATURE_S_RAVAGES_GREATER,
        config.SPELL_CORPSE_HAMMER,
        config.SPELL_OATH_OF_JUSTICE,
        config.SPELL_TACTICAL_FORMATION,
        config.SPELL_SOOTHING_WORD,
        config.SPELL_FROSTHAMMER,
        config.SPELL_ACCEPT_AFFLICTION,
        config.SPELL_ANGELIC_ASPECT_LESSER,
        config.SPELL_ANGELIC_ASPECT_GREATER,
        config.SPELL_ANGELIC_ASPECT,
        config.SPELL_ARCHON_S_TRUMPET,
        config.SPELL_BURST_OF_RADIANCE,
        config.SPELL_CHAINS_OF_LIGHT,
        config.SPELL_TOUCH_OF_MERCY,
        config.SPELL_HYMN_OF_MERCY,
        config.SPELL_HYMN_OF_PEACE,
        config.SPELL_BLOOD_OF_THE_MARTYR,
        config.SPELL_CHARITABLE_IMPULSE,
        config.SPELL_ELEMENTAL_ASSESSOR,
        config.SPELL_SANCTIFY_WEAPONS,
        config.SPELL_SUMMON_STAMPEDE,
        config.SPELL_VINETRAP,
        config.SPELL_BLACK_SWORD_OF_WAR,
        config.SPELL_BLOODY_TEARS_AND_JAGGED_SMILE,
        config.SPELL_BLIGHTBURN_WEAPON,
        config.SPELL_CHAMELEON_SCALES,
        config.SPELL_DARK_LIGHT,
        config.SPELL_ENLARGE_TAIL,
        config.SPELL_LEAD_PLATING,
        config.SPELL_SHADOW_DRAGON_ASPECT,
        config.SPELL_STRIP_SCALES,
        config.SPELL_UNSEEN_ENGINEERS,
        config.SPELL_DETECT_RELATIONS,
        config.SPELL_BUSINESS_BOOMS,
        config.SPELL_PROSPEROUS_ROOM,
        config.SPELL_RENOVATION,
        config.SPELL_TELEPORT_STRUCTURE,
        config.SPELL_BLESS_ARMY,
        config.SPELL_IMBUE_ARMY_SPECIAL_ABILITY,
        config.SPELL_TACTICAL_INSIGHT,
        config.SPELL_CEREMONY,
        config.SPELL_DRAGON_TURTLE_SHELL,
        config.SPELL_DRACONIC_SUPPRESSION,
        config.SPELL_DRAGONVOICE,
        config.SPELL_DUNGEONSIGHT,
        config.SPELL_ERODE_DEFENSES,
        config.SPELL_GRAVITY_WELL,
        config.SPELL_HEART_OF_THE_MAMMOTH,
        config.SPELL_ILLUSORY_HOARD,
        config.SPELL_KREIGHTON_S_PERUSAL,
        config.SPELL_PAGE_BOUND_EPIPHANY,
        config.SPELL_COLLABORATIVE_THAUMATURGY,
        config.SPELL_SURE_CASTING,
        config.SPELL_CAUTERIZING_WEAPON,
        config.SPELL_TACTICAL_MISCALCULATION,
        config.SPELL_WALL_OF_LIGHT,
        config.SPELL_BLOOD_SONG,
        config.SPELL_HALLUCINOGENIC_SMOKE,
        config.SPELL_JUNGLE_MIND,
        config.SPELL_LAY_OF_THE_LAND,
        config.SPELL_SOURCE_SEVERANCE,
        config.SPELL_TECTONIC_COMMUNION,
        config.SPELL_ANTI_SUMMONING_SHIELD,
        config.SPELL_BURST_WITH_LIGHT,
        config.SPELL_DETECT_DEMON,
        config.SPELL_PROTECTION_FROM_OUTSIDERS,
        config.SPELL_RIGHTEOUS_BLOOD,
        config.SPELL_TELEPATHIC_CENSURE,
        config.SPELL_CONTACT_NALFESHNEE,
        config.SPELL_ASCENSION,
        config.SPELL_BLEED_GLORY,
        config.SPELL_DEATHLESS,
        config.SPELL_LEND_PATH,
        config.SPELL_MYTHIC_SEVERANCE,
        config.SPELL_RESTORE_MYTHIC_POWER,
        config.SPELL_SHARE_GLORY,
        config.SPELL_STEAL_POWER,
        config.SPELL_TERRAFORM,
        config.SPELL_APPARENT_TREACHERY,
        config.SPELL_FILM_OF_FILTH,
        config.SPELL_LIGHTNING_LASH,
        config.SPELL_MAW_OF_CHAOS,
        config.SPELL_SUMMON_GREATER_DEMON,
        config.SPELL_SUMMON_LESSER_DEMON,
        config.SPELL_UNLEASH_PANDEMONIUM,
        config.SPELL_VERMICIOUS_ASSUMPTION,
        config.SPELL_BORROWED_TIME,
        config.SPELL_ELEMENTAL_BOMBARDMENT,
        config.SPELL_IMBUE_WITH_FLIGHT,
        config.SPELL_SOULREAVER,
        config.SPELL_SUSTAINING_LEGEND,
        config.SPELL_ACCURSED_GLARE,
        config.SPELL_SHARE_SKIN,
        config.SPELL_SHARE_SKIN_GREATER,
        config.SPELL_HEAVY_WATER,
        config.SPELL_HYDROPHOBIA,
        config.SPELL_BLOOD_BOIL,
        config.SPELL_RUNE_OF_JANDELAY,
        config.SPELL_BLEEDING_STRIKE,
        config.SPELL_REVEAL_MIRAGE,
        config.SPELL_STORM_OF_BLADES,
        config.SPELL_SUMMON_GENIE_LESSER,
        config.SPELL_SUMMON_GENIE,
        config.SPELL_SUMMON_GENIE_GREATER,
        config.SPELL_INNER_FOCUS,
        config.SPELL_ABYSSAL_VERMIN,
        config.SPELL_EXPLOSION_OF_ROT,
        config.SPELL_ANTITHETICAL_CONSTRAINT,
        config.SPELL_ARBITRAMENT,
        config.SPELL_ARDOR_S_ONSLAUGHT,
        config.SPELL_COUNTERBALANCING_AURA,
        config.SPELL_DISPEL_BALANCE,
        config.SPELL_RECENTERING_DRONE,
        config.SPELL_STEAL_BOOK,
        config.SPELL_SUMMON_LESSER_PSYCHOPOMP,
        config.SPELL_SUMMON_VANTH,
        config.SPELL_POSSESSION_TRAP,
        config.SPELL_SPHERE_OF_WARDING,
        config.SPELL_CARRION_COMPASS,
        config.SPELL_EMPOWER_HOLY_WATER,
        config.SPELL_FORCE_ANCHOR,
        config.SPELL_LIFE_SHIELD,
        config.SPELL_NECROMANTIC_BURDEN,
        config.SPELL_UNDEATH_INVERSION,
        config.SPELL_ABADAR_S_TRUTHTELLING,
        config.SPELL_ABSTEMIOUSNESS,
        config.SPELL_BAPHOMET_S_BLESSING,
        config.SPELL_BEACON_OF_LUCK,
        config.SPELL_BLADE_SNARE,
        config.SPELL_BLESSING_OF_THE_WATCH,
        config.SPELL_BRITTLE_PORTAL,
        config.SPELL_BURST_OF_GLORY,
        config.SPELL_CAUSTIC_BLOOD,
        config.SPELL_CHANNEL_THE_GIFT,
        config.SPELL_CHANNEL_VIGOR,
        config.SPELL_DEAD_EYE_S_ARROW,
        config.SPELL_DEFENDING_BONE,
        config.SPELL_DREAM_FEAST,
        config.SPELL_EARLY_JUDGMENT,
        config.SPELL_ENHANCE_WATER,
        config.SPELL_FACE_OF_THE_DEVOURER,
        config.SPELL_FAIRNESS,
        config.SPELL_FALLBACK_STRATEGY,
        config.SPELL_FALSE_ALIBI,
        config.SPELL_FIREBELLY,
        config.SPELL_FRACTIONS_OF_HEAL_AND_HARM,
        config.SPELL_FREEDOM_S_TOAST,
        config.SPELL_GHOUL_HUNGER,
        config.SPELL_GOZREH_S_TRIDENT,
        config.SPELL_HAIRLINE_FRACTURES,
        config.SPELL_HAMMER_OF_MENDING,
        config.SPELL_HAZE_OF_DREAMS,
        config.SPELL_HUNTER_S_BLESSING,
        config.SPELL_ICE_ARMOR,
        config.SPELL_INHERITOR_S_SMITE,
        config.SPELL_LIGHT_PRISON,
        config.SPELL_LIGHTEN_OBJECT,
        config.SPELL_LIGHTEN_OBJECT_MASS,
        config.SPELL_LOSE_THE_TRAIL,
        config.SPELL_MADDENING_OUBLIETTE,
        config.SPELL_MONSTROUS_EXTREMITIES,
        config.SPELL_NIGHT_OF_BLADES,
        config.SPELL_PICK_YOUR_POISON,
        config.SPELL_PLAGUE_BEARER,
        config.SPELL_POISONED_EGG,
        config.SPELL_READ_WEATHER,
        config.SPELL_REPLENISH_KI,
        config.SPELL_ROVAGUG_S_FURY,
        config.SPELL_SADOMASOCHISM,
        config.SPELL_SECRET_SPEECH,
        config.SPELL_SEDUCER_S_EYES,
        config.SPELL_SHARED_SACRIFICE,
        config.SPELL_SHIELD_OF_THE_DAWNFLOWER_GREATER,
        config.SPELL_SKY_SWIM,
        config.SPELL_SMITE_ABOMINATION,
        config.SPELL_SPAWN_CALLING,
        config.SPELL_SPELL_GAUGE,
        config.SPELL_SPELL_SCOURGE,
        config.SPELL_SYMBOL_OF_DEBAUCHERY,
        config.SPELL_SYMBOL_OF_DISPELLING,
        config.SPELL_TAP_INNER_BEAUTY,
        config.SPELL_TOUCH_OF_BLOODLETTING,
        config.SPELL_TRACKING_MARK,
        config.SPELL_TRANSPLANT_VISAGE,
        config.SPELL_UNWELCOME_HALO,
        config.SPELL_VENGEFUL_STINGER,
        config.SPELL_VEXING_MISCALCULATION,
        config.SPELL_WEAPONS_AGAINST_EVIL,
        config.SPELL_CREATE_VARIANT_MUMMY,
        config.SPELL_VIRULENCE,
        config.SPELL_CALCULATED_LUCK,
        config.SPELL_CLEROMANCY,
        config.SPELL_LUCKY_NUMBER,
        config.SPELL_MATHEMATICAL_CURSE,
        config.SPELL_NUMEROLOGICAL_EVOCATION,
        config.SPELL_NUMEROLOGICAL_RESISTANCE,
        config.SPELL_SPECTRAL_SALUQI,
        config.SPELL_HARROWING_GREATER,
        config.SPELL_ABEYANCE,
        config.SPELL_AGGRAVATE_AFFLICTION,
        config.SPELL_BESTOW_CURSE_GREATER,
        config.SPELL_STORM_STEP,
        config.SPELL_BONESHATTER,
        config.SPELL_ALTER_RIVER,
        config.SPELL_DETECT_METAL,
        config.SPELL_HANSPUR_S_FLOTSAM_VESSEL,
        config.SPELL_MAGNETIC_FIELD,
        config.SPELL_RESOUNDING_CLANG,
        config.SPELL_RIVERSIGHT,
        config.SPELL_SABOTAGE_CONSTRUCT,
        config.SPELL_ANTITECH_FIELD,
        config.SPELL_DESTROY_ROBOT,
        config.SPELL_DETECT_RADIATION,
        config.SPELL_DISCHARGE,
        config.SPELL_DISCHARGE_GREATER,
        config.SPELL_INFUSE_ROBOT,
        config.SPELL_IRRADIATE,
        config.SPELL_MAGIC_CIRCLE_AGAINST_TECHNOLOGY,
        config.SPELL_MAKE_WHOLE_GREATER,
        config.SPELL_MEMORY_OF_FUNCTION,
        config.SPELL_PROTECTION_FROM_TECHNOLOGY,
        config.SPELL_REBUKE_TECHNOLOGY,
        config.SPELL_RECHARGE,
        config.SPELL_REMOVE_RADIOACTIVITY,
        config.SPELL_REMOVE_RADIOACTIVITY_GREATER,
        config.SPELL_TECHNOMANCY,
        config.SPELL_COSMIC_RAY,
        config.SPELL_GRAVITY_SPHERE,
        config.SPELL_PLANETARIUM,
        config.SPELL_PLANETARY_ADAPTATION,
        config.SPELL_PLANETARY_ADAPTATION_MASS,
        config.SPELL_REBOOT,
        config.SPELL_STARSIGHT,
        config.SPELL_ADHESIVE_BLOOD,
        config.SPELL_ADHESIVE_SPITTLE,
        config.SPELL_ADJUSTABLE_DISGUISE,
        config.SPELL_ADJUSTABLE_POLYMORPH,
        config.SPELL_AGGRESSIVE_THUNDERCLOUD,
        config.SPELL_AGGRESSIVE_THUNDERCLOUD_GREATER,
        config.SPELL_AIR_GEYSER,
        config.SPELL_AIR_STEP,
        config.SPELL_ALIGN_WEAPON_COMMUNAL,
        config.SPELL_ALTER_MUSICAL_INSTRUMENT,
        config.SPELL_ANCHORED_STEP,
        config.SPELL_ANIMAL_PURPOSE_TRAINING,
        config.SPELL_ANONYMOUS_INTERACTION,
        config.SPELL_ANTI_INCORPOREAL_SHELL,
        config.SPELL_AURA_SIGHT,
        config.SPELL_BANSHEE_BLAST,
        config.SPELL_BARROW_HAZE,
        config.SPELL_BEASTSPEAK,
        config.SPELL_BESTOW_AURAS,
        config.SPELL_BLADE_LASH,
        config.SPELL_BLAZING_RAINBOW,
        config.SPELL_BLESSED_FIST,
        config.SPELL_BLOATBOMB,
        config.SPELL_BLOOD_ARMOR,
        config.SPELL_BLOOD_SENTINEL,
        config.SPELL_BLURRED_MOVEMENT,
        config.SPELL_BODY_CAPACITANCE,
        config.SPELL_BULLET_WARD,
        config.SPELL_BUOYANCY,
        config.SPELL_CHAMELEON_STRIDE_GREATER,
        config.SPELL_CLIMBING_BEANSTALK,
        config.SPELL_COMPANION_LIFE_LINK,
        config.SPELL_CONTINGENT_ACTION,
        config.SPELL_CONTINGENT_SCROLL,
        config.SPELL_CREEPING_ICE,
        config.SPELL_CRIMSON_CONFESSION,
        config.SPELL_CURSE_OF_BURNING_SLEEP,
        config.SPELL_DIMENSIONAL_BOUNCE,
        config.SPELL_DISABLE_CONSTRUCT,
        config.SPELL_DISCERN_NEXT_OF_KIN,
        config.SPELL_DISGUISE_WEAPON,
        config.SPELL_ENCHANTMENT_FOIL,
        config.SPELL_ENEMY_INSIGHT,
        config.SPELL_EUPHORIC_CLOUD,
        config.SPELL_EXTREME_FLEXIBILITY,
        config.SPELL_EYES_OF_THE_VOID,
        config.SPELL_FAIRY_RING_RETREAT,
        config.SPELL_FAMILIAR_DOUBLE,
        config.SPELL_FEAST_ON_FEAR,
        config.SPELL_FLAMING_SPHERE_GREATER,
        config.SPELL_FLEXIBLE_FURY,
        config.SPELL_FOCUSED_SCRUTINY,
        config.SPELL_FONT_OF_SPIRIT_MAGIC,
        config.SPELL_GENTLE_BREEZE,
        config.SPELL_GLUE_SEAL,
        config.SPELL_GUARDIAN_OF_FAITH,
        config.SPELL_HEART_OF_THE_METAL,
        config.SPELL_HEIGHTENED_AWARENESS,
        config.SPELL_HEIGHTENED_REFLEXES,
        config.SPELL_HEX_GLYPH,
        config.SPELL_HEX_GLYPH_GREATER,
        config.SPELL_HEX_VULNERABILITY,
        config.SPELL_HOLY_ICE_WEAPON,
        config.SPELL_INVESTIGATIVE_MIND,
        config.SPELL_INVISIBILITY_ALARM,
        config.SPELL_LIFE_PACT,
        config.SPELL_LINE_IN_THE_SAND,
        config.SPELL_LONG_ARM,
        config.SPELL_LONGSTRIDER_GREATER,
        config.SPELL_MAGNIFYING_CHIME,
        config.SPELL_MANTLE_OF_CALM,
        config.SPELL_MARCHING_CHANT,
        config.SPELL_MARK_OF_OBVIOUS_ETHICS,
        config.SPELL_MEMORIZE_PAGE,
        config.SPELL_MINDLOCKED_MESSENGER,
        config.SPELL_MIRROR_HIDEAWAY,
        config.SPELL_MIRROR_POLISH,
        config.SPELL_MIRROR_TRANSPORT,
        config.SPELL_MOLTEN_ORB,
        config.SPELL_MONKEY_FISH,
        config.SPELL_MUFFLE_SOUND,
        config.SPELL_NAUSEATING_DART,
        config.SPELL_NAUSEATING_TRAIL,
        config.SPELL_PATH_OF_GLORY,
        config.SPELL_PATH_OF_GLORY_GREATER,
        config.SPELL_PERSISTENT_VIGOR,
        config.SPELL_PHANTOM_BLOOD,
        config.SPELL_PIERCE_DISGUISE,
        config.SPELL_PLANESLAYER_S_CALL,
        config.SPELL_POLYMORPH_FAMILIAR,
        config.SPELL_REFINE_IMPROVISED_WEAPON,
        config.SPELL_REPAIR_UNDEAD,
        config.SPELL_REPAIR_UNDEAD_MASS,
        config.SPELL_RIVER_WHIP,
        config.SPELL_SENSE_SPIRIT_MAGIC,
        config.SPELL_SHIELD_COMPANION,
        config.SPELL_SHIELD_OF_FORTIFICATION,
        config.SPELL_SHIELD_OF_FORTIFICATION_GREATER,
        config.SPELL_SICKENING_ENTANGLEMENT,
        config.SPELL_SILENT_TABLE,
        config.SPELL_SILVER_DARTS,
        config.SPELL_SLOWING_MUD,
        config.SPELL_SONIC_FORM,
        config.SPELL_SONIC_SCREAM,
        config.SPELL_SPEAK_WITH_HAUNT,
        config.SPELL_SPELLCRASH_LESSER,
        config.SPELL_SPELLCRASH_GREATER,
        config.SPELL_SPELLCRASH,
        config.SPELL_STENCH_OF_PREY,
        config.SPELL_STONE_DISCUS,
        config.SPELL_STRICKEN_HEART,
        config.SPELL_STUNNING_BARRIER,
        config.SPELL_STUNNING_BARRIER_GREATER,
        config.SPELL_SUNDER_BREAKER,
        config.SPELL_SUNDERING_SHARDS,
        config.SPELL_SYMBOL_OF_LAUGHTER,
        config.SPELL_THORN_JAVELIN,
        config.SPELL_THORNY_ENTANGLEMENT,
        config.SPELL_THUNDERSTOMP,
        config.SPELL_THUNDERSTOMP_GREATER,
        config.SPELL_TIME_SHUDDER,
        config.SPELL_TRIGGERED_SUGGESTION,
        config.SPELL_TWILIGHT_HAZE,
        config.SPELL_UNBEARABLE_BRIGHTNESS,
        config.SPELL_UNHOLY_ICE_WEAPON,
        config.SPELL_UNLIVING_RAGE,
        config.SPELL_VAMPIRIC_SHADOW_SHIELD,
        config.SPELL_WALL_OF_BLINDNESS_DEAFNESS,
        config.SPELL_WALL_OF_NAUSEA,
        config.SPELL_WAVE_SHIELD,
        config.SPELL_WHIP_OF_SPIDERS,
        config.SPELL_WHIP_OF_ANTS,
        config.SPELL_WHIP_OF_CENTIPEDES,
        config.SPELL_WIDEN_AURAS,
        config.SPELL_SEMBLANCE_OF_FLESH,
        config.SPELL_SHARED_SUFFERING,
        config.SPELL_WRACKING_RAY,
        config.SPELL_ACID_MAW,
        config.SPELL_ARCANE_DISRUPTION,
        config.SPELL_BLOOD_SALVATION,
        config.SPELL_ENERGY_HACK,
        config.SPELL_IMBUE_HEX,
        config.SPELL_PHANTOM_HUNT,
        config.SPELL_SPIRIT_CALL,
        config.SPELL_WRATHFUL_WEAPON,
        config.SPELL_AURA_OF_CANNIBALISM,
        config.SPELL_ISOLATE,
        config.SPELL_CONTROL_VERMIN,
        config.SPELL_DUST_WARD,
        config.SPELL_IRONSKIN,
        config.SPELL_ICE_SLICK,
        config.SPELL_MAGIC_BOULDER,
        config.SPELL_FLESHY_FACADE,
        config.SPELL_HUNGRY_EARTH,
        config.SPELL_AUGMENTING_WALL,
        config.SPELL_BLOODY_ARROWS,
        config.SPELL_CALM_AIR,
        config.SPELL_CONVERSING_WIND,
        config.SPELL_RAIN_OF_ARROWS,
        config.SPELL_TELEKINETIC_VOLLEY,
        config.SPELL_BOUNCY_BODY,
        config.SPELL_MUD_BUDDY,
        config.SPELL_ENDOTHERMIC_TOUCH,
        config.SPELL_SCALE_SPIKES,
        config.SPELL_SCALE_SPIKES_GREATER,
        config.SPELL_AIR_BREATHING,
        config.SPELL_BLOOD_IN_THE_WATER,
        config.SPELL_GIFT_OF_THE_DEEP,
        config.SPELL_SPELLSTEAL,
        config.SPELL_SUNDERED_SERPENT_COIL,
        config.SPELL_CURSE_OF_UNEXPECTED_DEATH,
        config.SPELL_BURDENED_THOUGHTS,
        config.SPELL_HOLLOW_BLADES,
        config.SPELL_RUNIC_OVERLOAD,
        config.SPELL_SIPHON_MIGHT,
        config.SPELL_STONE_THROWING,
        config.SPELL_STEAL_SIZE,
        config.SPELL_TWISTED_FUTURES,
        config.SPELL_AMPLIFY_STENCH,
        config.SPELL_MARK_OF_THE_REPTILE_GOD,
        config.SPELL_SWARM_OF_FANGS,
        config.SPELL_TRANSFER_REGENERATION,
        config.SPELL_TRIAL_OF_FIRE_AND_ACID,
        config.SPELL_CALLBACK,
        config.SPELL_CALLBACK_GREATER,
        config.SPELL_DISRUPT_LINK,
        config.SPELL_DUPLICATE_FAMILIAR,
        config.SPELL_EMPATHY_CONDUIT,
        config.SPELL_MERGE_WITH_FAMILIAR,
        config.SPELL_SOULSWITCH,
        config.SPELL_TRANSFER_FAMILIAR,
        config.SPELL_BEANSTALK,
        config.SPELL_FLAMING_AURA,
        config.SPELL_FROSTY_AURA,
        config.SPELL_QUICK_THROWING,
        config.SPELL_THUNDEROUS_FOOTFALLS,
        config.SPELL_THANATOTIC_FURY,
        config.SPELL_TITANIC_ANCHORING,
        config.SPELL_AURA_OF_INVIOLATE_OWNERSHIP,
        config.SPELL_BLADE_TUTOR_S_SPIRIT,
        config.SPELL_DARTING_DUPLICATE,
        config.SPELL_DIMENSIONAL_BLADE,
        config.SPELL_FIERY_RUNES,
        config.SPELL_INSTANT_WEAPON,
        config.SPELL_REAPER_S_COTERIE,
        config.SPELL_RUBBERSKIN,
        config.SPELL_UMBRAL_WEAPON,
        config.SPELL_VINE_STRIKE,
        config.SPELL_CHEETAH_S_SPRINT,
        config.SPELL_CLEAR_GROVE,
        config.SPELL_GLOBE_OF_TRANQUIL_WATER,
        config.SPELL_NATURE_S_PATHS,
        config.SPELL_OASIS,
        config.SPELL_PLANAR_REFUGE,
        config.SPELL_RAVEN_S_FLIGHT,
        config.SPELL_WILD_INSTINCT,
        config.SPELL_GRAVEL_VORTEX,
        config.SPELL_DAYWALKER,
        config.SPELL_PLANT_VOICE,
        config.SPELL_SPORE_BURST,
        config.SPELL_ALTER_SUMMONED_MONSTER,
        config.SPELL_FINAL_SACRIFICE,
        config.SPELL_GIRD_ALLY,
        config.SPELL_INSTANT_RESTORATION,
        config.SPELL_MASTER_S_ESCAPE,
        config.SPELL_MASTER_S_MUTATION,
        config.SPELL_SUMMON_LABORERS,
        config.SPELL_ILLUSORY_MAZE,
        config.SPELL_MAKE_LOST,
        config.SPELL_MIND_MAZE,
        config.SPELL_PUZZLE_BOX,
        config.SPELL_STOKE_THE_INNER_FIRE,
        config.SPELL_AKASHIC_FORM,
        config.SPELL_ANALYZE_AURA,
        config.SPELL_ANTICIPATE_THOUGHTS,
        config.SPELL_APPORT_OBJECT,
        config.SPELL_APPORT_ANIMAL,
        config.SPELL_AURA_ALTERATION,
        config.SPELL_DRAIN_POISON,
        config.SPELL_GARDEN_OF_PERIL,
        config.SPELL_INVIGORATING_POISON,
        config.SPELL_NEUTRALIZE_POISON_GREATER,
        config.SPELL_POISON_BREATH,
        config.SPELL_SWORD_TO_SNAKE,
        config.SPELL_TOXIC_RUPTURE,
        config.SPELL_VENOMOUS_BITE,
        config.SPELL_BLEND_WITH_SURROUNDINGS,
        config.SPELL_BODY_DOUBLE,
        config.SPELL_GRASPING_TENTACLES,
        config.SPELL_GREASE_GREATER,
        config.SPELL_HIDE_WEAPON,
        config.SPELL_SELECTIVE_INVISIBILITY,
        config.SPELL_SENSE_VITALS,
        config.SPELL_SHIFTING_SHADOWS,
        config.SPELL_BELOVED_OF_THE_FORGE,
        config.SPELL_BLESSING_OF_LIBERTY,
        config.SPELL_HARMLESS_FORM,
        config.SPELL_HARVEST_SEASON,
        config.SPELL_WALL_OF_CLOCKWORK,
        config.SPELL_CLOAK_OF_SECRETS,
        config.SPELL_COIN_SHOT,
        config.SPELL_EARS_OF_THE_CITY,
        config.SPELL_ILLUSORY_CROWD,
        config.SPELL_LOCKSIGHT,
        config.SPELL_PEACE_BOND,
        config.SPELL_SPEAK_LOCAL_LANGUAGE,
        config.SPELL_AVERSION,
        config.SPELL_AWAKEN_CONSTRUCT,
        config.SPELL_BABBLE,
        config.SPELL_BILOCATION,
        config.SPELL_BURST_OF_ADRENALINE,
        config.SPELL_BURST_OF_INSIGHT,
        config.SPELL_CALL_SPIRIT,
        config.SPELL_CALM_SPIRIT,
        config.SPELL_CATATONIA,
        config.SPELL_CHARGE_OBJECT,
        config.SPELL_COGNITIVE_BLOCK,
        config.SPELL_CONDENSED_ETHER,
        config.SPELL_CONTAGIOUS_ZEAL,
        config.SPELL_CREATE_MINDSCAPE,
        config.SPELL_CREATE_MINDSCAPE_GREATER,
        config.SPELL_DECREPIT_DISGUISE,
        config.SPELL_DEJA_VU,
        config.SPELL_DEMAND_OFFERING,
        config.SPELL_DETECT_MINDSCAPE,
        config.SPELL_DETECT_PSYCHIC_SIGNIFICANCE,
        config.SPELL_DIVIDE_MIND,
        config.SPELL_DREAM_COUNCIL,
        config.SPELL_DREAM_SCAN,
        config.SPELL_DREAM_TRAVEL,
        config.SPELL_DREAM_VOYAGE,
        config.SPELL_ECTOPLASMIC_ERUPTION,
        config.SPELL_ECTOPLASMIC_SNARE,
        config.SPELL_EGO_WHIP_I,
        config.SPELL_EGO_WHIP_I_I,
        config.SPELL_EGO_WHIP_I_I_I,
        config.SPELL_EGO_WHIP_I_V,
        config.SPELL_EGO_WHIP_V,
        config.SPELL_EMOTIVE_BLOCK,
        config.SPELL_ENSHROUD_THOUGHTS,
        config.SPELL_ENTRAP_SPIRIT,
        config.SPELL_ERASE_IMPRESSIONS,
        config.SPELL_ETHEREAL_ENVELOPE,
        config.SPELL_ETHEREAL_ENVELOPMENT,
        config.SPELL_ETHEREAL_FISTS,
        config.SPELL_ETHERIC_SHARDS,
        config.SPELL_EXPLODE_HEAD,
        config.SPELL_FOSTER_HATRED,
        config.SPELL_GHOST_WHIP,
        config.SPELL_GRAVE_WORDS,
        config.SPELL_HYPERCOGNITION,
        config.SPELL_ID_INSINUATION_I,
        config.SPELL_ID_INSINUATION_I_I,
        config.SPELL_ID_INSINUATION_I_I_I,
        config.SPELL_ID_INSINUATION_I_V,
        config.SPELL_IMPLANT_FALSE_READING,
        config.SPELL_INCORPOREAL_CHAINS,
        config.SPELL_INFLICT_PAIN,
        config.SPELL_INFLICT_PAIN_MASS,
        config.SPELL_INSTIGATE_PSYCHIC_DUEL,
        config.SPELL_INTELLECT_FORTRESS_I,
        config.SPELL_INTELLECT_FORTRESS_I_I,
        config.SPELL_INTELLECT_FORTRESS_I_I_I,
        config.SPELL_MENTAL_BARRIER_I,
        config.SPELL_MENTAL_BARRIER_I_I,
        config.SPELL_MENTAL_BARRIER_I_I_I,
        config.SPELL_MENTAL_BARRIER_I_V,
        config.SPELL_MENTAL_BARRIER_V,
        config.SPELL_MENTAL_BLOCK,
        config.SPELL_MICROCOSM,
        config.SPELL_MIND_PROBE,
        config.SPELL_MIND_SWAP,
        config.SPELL_MIND_SWAP_MAJOR,
        config.SPELL_MIND_THRUST_I,
        config.SPELL_MIND_THRUST_I_I,
        config.SPELL_MIND_THRUST_I_I_I,
        config.SPELL_MIND_THRUST_I_V,
        config.SPELL_MIND_THRUST_V,
        config.SPELL_MIND_THRUST_V_I,
        config.SPELL_MINDLINK,
        config.SPELL_MINDSCAPE_DOOR,
        config.SPELL_MINDWIPE,
        config.SPELL_NODE_OF_BLASTING,
        config.SPELL_OBJECT_POSSESSION,
        config.SPELL_OBJECT_POSSESSION_GREATER,
        config.SPELL_OBJECT_POSSESSION_LESSER,
        config.SPELL_OBJECT_READING,
        config.SPELL_ONEIRIC_HORROR,
        config.SPELL_ONEIRIC_HORROR_GREATER,
        config.SPELL_PARANOIA,
        config.SPELL_PARCHMENT_SWARM,
        config.SPELL_PLACEBO_EFFECT,
        config.SPELL_POSSESSION,
        config.SPELL_POSSESSION_GREATER,
        config.SPELL_PRIMAL_REGRESSION,
        config.SPELL_PSYCHIC_ASYLUM,
        config.SPELL_PSYCHIC_CRUSH_I,
        config.SPELL_PSYCHIC_CRUSH_I_I,
        config.SPELL_PSYCHIC_CRUSH_I_I_I,
        config.SPELL_PSYCHIC_CRUSH_I_V,
        config.SPELL_PSYCHIC_CRUSH_V,
        config.SPELL_PSYCHIC_IMAGE,
        config.SPELL_PSYCHIC_READING,
        config.SPELL_PSYCHIC_SURGERY,
        config.SPELL_PURGE_SPIRIT,
        config.SPELL_QUINTESSENCE,
        config.SPELL_REMOTE_VIEWING,
        config.SPELL_REPRESS_MEMORY,
        config.SPELL_RETROCOGNITION,
        config.SPELL_RIDING_POSSESSION,
        config.SPELL_SEALED_LIFE,
        config.SPELL_SEALED_LIFE_GREATER,
        config.SPELL_SESSILE_SPIRIT,
        config.SPELL_SHADOW_BODY,
        config.SPELL_SPIRIT_BOUND_BLADE,
        config.SPELL_SYNAPSE_OVERLOAD,
        config.SPELL_SYNAPTIC_PULSE,
        config.SPELL_SYNAPTIC_PULSE_GREATER,
        config.SPELL_SYNAPTIC_SCRAMBLE,
        config.SPELL_SYNESTHESIA,
        config.SPELL_SYNESTHESIA_MASS,
        config.SPELL_TALISMANIC_IMPLEMENT,
        config.SPELL_TELEKINETIC_MANEUVER,
        config.SPELL_TELEKINETIC_PROJECTILE,
        config.SPELL_TELEKINETIC_STORM,
        config.SPELL_TELEMPATHIC_PROJECTION,
        config.SPELL_TELEPATHY,
        config.SPELL_THAUMATURGIC_CIRCLE,
        config.SPELL_THOUGHT_ECHO,
        config.SPELL_THOUGHT_SHIELD_I,
        config.SPELL_THOUGHT_SHIELD_I_I,
        config.SPELL_THOUGHT_SHIELD_I_I_I,
        config.SPELL_THOUGHT_SHIELD_I_V,
        config.SPELL_THOUGHT_SHIELD_V,
        config.SPELL_THOUGHTSENSE,
        config.SPELL_TOWER_OF_IRON_WILL_I,
        config.SPELL_TOWER_OF_IRON_WILL_I_I,
        config.SPELL_TOWER_OF_IRON_WILL_I_I_I,
        config.SPELL_TOWER_OF_IRON_WILL_I_V,
        config.SPELL_TOWER_OF_IRON_WILL_V,
        config.SPELL_UNSHAKABLE_ZEAL,
        config.SPELL_WALL_OF_ECTOPLASM,
        config.SPELL_WITHDRAW_AFFLICTION,
        config.SPELL_AIR_OF_AUTHORITY,
        config.SPELL_BLEACHING_RESISTANCE,
        config.SPELL_BURN_CORRUPTION,
        config.SPELL_CHAMPION_S_BOUT,
        config.SPELL_DAMNATION_OF_MEMORY,
        config.SPELL_ELEMENTAL_MASTERY,
        config.SPELL_FABLE_TAPESTRY,
        config.SPELL_FIRE_S_FRIEND,
        config.SPELL_FLESHWARPING_SWARM,
        config.SPELL_LAMENT_OF_SUMMER_S_LAST_BREATH,
        config.SPELL_LOST_PASSAGE,
        config.SPELL_LOST_LOCALE,
        config.SPELL_MANTLE_OF_THE_MAGIC_WARRIORS,
        config.SPELL_MARTIAL_TELEKINESIS,
        config.SPELL_MIASMAL_DREAD,
        config.SPELL_MURDEROUS_CROW,
        config.SPELL_OVERLOOK,
        config.SPELL_PROBE_HISTORY,
        config.SPELL_RESPECTFUL_QUIET,
        config.SPELL_SHADOW_OF_DOUBT,
        config.SPELL_SIEGE_SCATTER,
        config.SPELL_SUMMON_GIANT_ALLY_I,
        config.SPELL_SUMMON_GIANT_ALLY_I_I,
        config.SPELL_SUMMON_GIANT_ALLY_I_I_I,
        config.SPELL_SUMMON_KAMI,
        config.SPELL_SUPPRESSING_STONE,
        config.SPELL_WALL_OF_BRINE,
        config.SPELL_ZEPHYR_S_FLEETNESS,
        config.SPELL_CREATE_DRUG,
        config.SPELL_DEATH_PACT,
        config.SPELL_FOOL_S_TELEPORT,
        config.SPELL_IMPLANTED_PROJECTION,
        config.SPELL_DREAM_SHIELD,
        config.SPELL_JEALOUS_RAGE,
        config.SPELL_MINDSHOCK,
        config.SPELL_PSYCHIC_LEECH,
        config.SPELL_QUELL_ENERGY,
        config.SPELL_RETRIBUTIVE_REPARATIONS,
        config.SPELL_SENSORY_AMPLIFIER,
        config.SPELL_SUBJECTIVE_REALITY,
        config.SPELL_ECTOPLASMIC_HAND,
        config.SPELL_MANTLE_OF_DOUBT,
        config.SPELL_MIND_OVER_MATTER,
        config.SPELL_OUT_OF_SIGHT,
        config.SPELL_PHANTOM_LIMB,
        config.SPELL_PSYCHONAUT_MANIFESTATION,
        config.SPELL_ALLEVIATE_ADDICTION,
        config.SPELL_CONTACT_HIGH,
        config.SPELL_IMBUE_WITH_ADDICTION,
        config.SPELL_NIGHT_BLINDNESS,
        config.SPELL_PESH_VIGOR,
        config.SPELL_COMPEL_TONGUE,
        config.SPELL_COMPEL_TONGUE_MASS,
        config.SPELL_FLEETING_MEMORY,
        config.SPELL_FLEETING_MEMORY_MASS,
        config.SPELL_SECRET_SIGN,
        config.SPELL_VENOMOUS_PROMISE,
        config.SPELL_ARCANE_POCKET,
        config.SPELL_VACUOUS_VESSEL,
        config.SPELL_ADROIT_RETRIEVAL,
        config.SPELL_AUTHENTICATING_GAZE,
        config.SPELL_CURSE_OF_KEEPING,
        config.SPELL_EVALUATOR_S_LENS,
        config.SPELL_FLEETING_DEFECT,
        config.SPELL_INCENDIARY_RUNES,
        config.SPELL_PEERLESS_INTEGRITY,
        config.SPELL_REMARKABLE_LEGERDEMAIN,
        config.SPELL_SECRET_COFFER,
        config.SPELL_SECRET_VAULT,
        config.SPELL_SHADOW_ENCHANTMENT,
        config.SPELL_SHADOW_ENCHANTMENT_GREATER,
        config.SPELL_DETECT_FIENDISH_PRESENCE,
        config.SPELL_DEVIL_SNARE,
        config.SPELL_PUNISHING_ARMOR,
        config.SPELL_UNHOLY_WARD,
        config.SPELL_BLOOD_TENTACLES,
        config.SPELL_CAUSTIC_SAFEGUARD,
        config.SPELL_COWARD_S_COWL,
        config.SPELL_DREAM_DALLIANCE,
        config.SPELL_ENTICING_ADULATION,
        config.SPELL_FURIOUS_FIRE_BARRAGE,
        config.SPELL_GOLDEN_GUISE,
        config.SPELL_SHADOW_ENDURANCE,
        config.SPELL_SEER_S_BANE,
        config.SPELL_ARODEN_S_MAGIC_ARMY,
        config.SPELL_ARODEN_S_SPELLSWORD,
        config.SPELL_BANISHING_BLADE,
        config.SPELL_CREATE_ARMAMENTS,
        config.SPELL_EXPEDITIOUS_CONSTRUCTION,
        config.SPELL_FORCE_SWORD,
        config.SPELL_GRAND_DESTINY,
        config.SPELL_GUARDIAN_MONUMENT_LESSER,
        config.SPELL_GUARDIAN_MONUMENT_GREATER,
        config.SPELL_HUMAN_POTENTIAL,
        config.SPELL_HUMAN_POTENTIAL_MASS,
        config.SPELL_LAST_AZLANTI_S_DEFENDING_SWORD,
        config.SPELL_LAST_AZLANTI_S_DEFENDING_SWORD_MASS,
        config.SPELL_LINKED_LEGACY,
        config.SPELL_SPLINTER_SPELL_RESISTANCE,
        config.SPELL_WINGED_SWORD,
        config.SPELL_CELESTIAL_HEALING,
        config.SPELL_CELESTIAL_HEALING_GREATER,
        config.SPELL_CYCLIC_REINCARNATION,
        config.SPELL_JATEMBE_S_IRE,
        config.SPELL_MASK_FROM_DIVINATION,
        config.SPELL_PLANAR_INQUIRY,
        config.SPELL_ARTIFICER_S_CURSE,
        config.SPELL_DEFT_DIGITS,
        config.SPELL_DISSOLUTION,
        config.SPELL_EMBLEM_OF_GREED,
        config.SPELL_FOOL_S_GOLD,
        config.SPELL_FULL_POUCH,
        config.SPELL_LEGENDARY_PROPORTIONS,
        config.SPELL_LIQUEFY,
        config.SPELL_OPEN_ARMS,
        config.SPELL_RAGS_TO_RICHES,
        config.SPELL_RUNE_OF_RUIN,
        config.SPELL_TEARS_TO_WINE,
        config.SPELL_TRANSMUTE_GOLEM,
        config.SPELL_FIND_FAULT,
        config.SPELL_FORETELL_FAILURE,
        config.SPELL_PERFECT_PLACEMENT,
        config.SPELL_HECKLE,
        config.SPELL_STAGE_FRIGHT,
        config.SPELL_TOUGH_CROWD,
        config.SPELL_FIRST_WORLD_REVISIONS,
        config.SPELL_DARKVAULT,
        config.SPELL_FEAR_THE_SUN,
        config.SPELL_IGNOBLE_FORM,
        config.SPELL_SHADOWMIND,
        config.SPELL_UMBRAL_STRIKE,
        config.SPELL_DANCING_DARKNESS,
        config.SPELL_MOTES_OF_DUSK_AND_DAWN,
        config.SPELL_MYDRIATIC_SPONTANEITY,
        config.SPELL_MYDRIATIC_SPONTANEITY_MASS,
        config.SPELL_PENUMBRAL_DISGUISE,
        config.SPELL_SHIELD_OF_DARKNESS,
        config.SPELL_SPOTLIGHT,
        config.SPELL_TOUCH_OF_BLINDNESS,
        config.SPELL_WALL_OF_SPLIT_ILLUMINATION,
        config.SPELL_BALEFUL_SHADOW_TRANSMUTATION,
        config.SPELL_MASOCHISTIC_SHADOW,
        config.SPELL_SHADOW_TRANSMUTATION,
        config.SPELL_SHADOW_TRANSMUTATION_GREATER,
        config.SPELL_SHADOW_TRAP,
        config.SPELL_SHADOWFORM,
        config.SPELL_UMBRAL_INFUSION,
        config.SPELL_UMBRAL_INFUSION_MASS,
        config.SPELL_ABSOLUTION,
        config.SPELL_AERIAL_TRACKS,
        config.SPELL_ANIMAL_AMBASSADOR,
        config.SPELL_APHASIA,
        config.SPELL_AUDITORY_HALLUCINATION,
        config.SPELL_AUDIOVISUAL_HALLUCINATION,
        config.SPELL_AURA_OF_THE_UNREMARKABLE,
        config.SPELL_BOUNTIFUL_BANQUET,
        config.SPELL_BREAK_GREATER,
        config.SPELL_BUILD_TRUST,
        config.SPELL_CHARM_PERSON_MASS,
        config.SPELL_CODESPEAK,
        config.SPELL_COMPLEX_HALLUCINATION,
        config.SPELL_COMPULSIVE_LIAR,
        config.SPELL_CONDITIONAL_CURSE,
        config.SPELL_CONDITIONAL_FAVOR,
        config.SPELL_CONJURATION_FOIL,
        config.SPELL_CONJURE_CARRIAGE,
        config.SPELL_CONTINGENT_VENOM,
        config.SPELL_CONTROLLED_FIREBALL,
        config.SPELL_CRIME_OF_OPPORTUNITY,
        config.SPELL_CRIME_WAVE,
        config.SPELL_CULTURAL_ADAPTATION,
        config.SPELL_CURSE_OF_THE_OUTCAST,
        config.SPELL_DARK_WHISPERS,
        config.SPELL_DEADMAN_S_CONTINGENCY,
        config.SPELL_DECEITFUL_VENEER,
        config.SPELL_DEFLECT_BLAME,
        config.SPELL_DEMANDING_MESSAGE,
        config.SPELL_DEMANDING_MESSAGE_MASS,
        config.SPELL_DESPERATE_WEAPON,
        config.SPELL_DETECT_ANXIETIES,
        config.SPELL_DETECT_DESIRES,
        config.SPELL_DETECT_MAGIC_GREATER,
        config.SPELL_DETECT_THE_FAITHFUL,
        config.SPELL_DISRUPT_SILENCE,
        config.SPELL_DRESS_CORPSE,
        config.SPELL_ENTICE_FEY,
        config.SPELL_ENTICE_FEY_GREATER,
        config.SPELL_ENTICE_FEY_LESSER,
        config.SPELL_FABRICATE_DISGUISE,
        config.SPELL_FALSE_BELIEF,
        config.SPELL_FALSE_FUTURE,
        config.SPELL_FALSE_RESURRECTION,
        config.SPELL_FALSE_RESURRECTION_GREATER,
        config.SPELL_FALSE_VISION_GREATER,
        config.SPELL_GHOST_BRAND,
        config.SPELL_GLIMPSE_OF_TRUTH,
        config.SPELL_HANDY_GRAPNEL,
        config.SPELL_HIDDEN_PRESENCE,
        config.SPELL_HOLLOW_HEROISM,
        config.SPELL_HOLLOW_HEROISM_GREATER,
        config.SPELL_ILLUSION_OF_TREACHERY,
        config.SPELL_ILLUSION_OF_TREACHERY_GREATER,
        config.SPELL_INSECT_SPIES,
        config.SPELL_INSECT_SPIES_GREATER,
        config.SPELL_INSTANT_FAKE,
        config.SPELL_INSTANT_SUMMONS_GREATER,
        config.SPELL_KNOW_PEERAGE,
        config.SPELL_LANGUID_VENOM,
        config.SPELL_LIFE_OF_CRIME,
        config.SPELL_MAGE_S_DECREE,
        config.SPELL_MAGIC_AURA_GREATER,
        config.SPELL_MAJESTIC_IMAGE,
        config.SPELL_MATCHMAKER,
        config.SPELL_METICULOUS_MATCH,
        config.SPELL_OBSCURE_POISON,
        config.SPELL_OPEN_AND_SHUT,
        config.SPELL_OPEN_BOOK,
        config.SPELL_OVERWHELMING_POISON,
        config.SPELL_PACK_EMPATHY,
        config.SPELL_PEACEBOND_GREATER,
        config.SPELL_PERMANENT_HALLUCINATION,
        config.SPELL_PHANTASMAL_AFFLICTION,
        config.SPELL_POCKETFUL_OF_VIPERS,
        config.SPELL_POISONOUS_BALM,
        config.SPELL_POX_OF_RUMORS,
        config.SPELL_PROGNOSTICATION,
        config.SPELL_QUIETING_WEAPONS,
        config.SPELL_RED_HAND_OF_THE_KILLER,
        config.SPELL_REINCARNATE_SPY,
        config.SPELL_RESPLENDENT_MANSION,
        config.SPELL_RUMORMONGER,
        config.SPELL_SCRIPTED_HALLUCINATION,
        config.SPELL_SELECTIVE_ALARM,
        config.SPELL_SHAMEFULLY_OVERDRESSED,
        config.SPELL_SHIFTED_STEPS,
        config.SPELL_SWALLOW_POISON,
        config.SPELL_THEY_KNOW,
        config.SPELL_TRACE_TELEPORT,
        config.SPELL_TRADE_ITEMS,
        config.SPELL_TREACHEROUS_TELEPORT,
        config.SPELL_TRIGGERED_HALLUCINATION,
        config.SPELL_TRUE_PROGNOSTICATION,
        config.SPELL_UNDERBRUSH_DECOY,
        config.SPELL_UNDETECTABLE_TRAP,
        config.SPELL_UNERRING_TRACKER,
        config.SPELL_URBAN_STEP,
        config.SPELL_VICARIOUS_VIEW,
        config.SPELL_VOLUMINOUS_VOCABULARY,
        config.SPELL_WIZENED_APPEARANCE,
        config.SPELL_GUARDIAN_ARMOR,
        config.SPELL_REVENANT_ARMOR,
        config.SPELL_SHIELD_OF_SHARDS,
        config.SPELL_SPIRITUAL_SQUIRE,
        config.SPELL_BONE_FISTS,
        config.SPELL_FLASH_FORWARD,
        config.SPELL_PARTICULATE_FORM,
        config.SPELL_PHASIC_CHALLENGE,
        config.SPELL_SPELLCURSE,
        config.SPELL_WARP_METAL,
        config.SPELL_BITING_WORDS,
        config.SPELL_BOUNCING_BOMB_ADMIXTURE,
        config.SPELL_RELEASE_THE_HOUNDS,
        config.SPELL_ROAMING_PIT,
        config.SPELL_WALL_OF_BONE,
        config.SPELL_AKASHIC_COMMUNION,
        config.SPELL_BIND_SAGE,
        config.SPELL_SECLUDED_GRIMOIRE,
        config.SPELL_ALAZNIST_S_JINX,
        config.SPELL_FLEXILE_CURSE,
        config.SPELL_IRREGULAR_SIZE,
        config.SPELL_ITCHING_CURSE,
        config.SPELL_KALISTOCRAT_S_NIGHTMARE,
        config.SPELL_LOST_LEGACY,
        config.SPELL_EARSEND,
        config.SPELL_HIDDEN_BLADES,
        config.SPELL_IMPENETRABLE_VEIL,
        config.SPELL_INNOCUOUS_SHAPE,
        config.SPELL_NONDETECTION_LESSER,
        config.SPELL_PHANTASMAL_REMINDER,
        config.SPELL_SYMBOL_OF_DISTRACTION,
        config.SPELL_TOUCH_OF_SLUMBER,
        config.SPELL_APATHY,
        config.SPELL_ASSUMED_LIKENESS,
        config.SPELL_BRIGHTEST_LIGHT,
        config.SPELL_CALISTRIA_S_GUARDIAN_WASPS,
        config.SPELL_COMMUNE_WITH_TEXTS,
        config.SPELL_DAGGERMARK_S_EXCHANGE,
        config.SPELL_DIMINISHED_DETECTION,
        config.SPELL_DONGUN_SHAPER_S_TOUCH,
        config.SPELL_DREAM_REALITY,
        config.SPELL_IMPLANT_URGE,
        config.SPELL_INVEIGLE_MONSTER,
        config.SPELL_INVEIGLE_PERSON,
        config.SPELL_NEX_S_SECRET_WORKSHOP,
        config.SPELL_OATH_OF_ANONYMITY,
        config.SPELL_RECORPOREAL_INCARNATION,
        config.SPELL_ROTTING_ALLIANCE,
        config.SPELL_SEALED_SENDING,
        config.SPELL_SEARCHING_SHADOWS,
        config.SPELL_SEEDS_OF_INFLUENCE,
        config.SPELL_SEEDS_OF_INFLUENCE_GREATER,
        config.SPELL_SEEK_SHELTER,
        config.SPELL_SUBSTITUTE_TRAIL,
        config.SPELL_TRANSFIGURING_TOUCH,
        config.SPELL_TRUE_SKILL,
        config.SPELL_VIOLENT_ACCIDENT,
        config.SPELL_WANDERING_TRAIL,
        config.SPELL_HERETIC_S_TONGUE,
        config.SPELL_BRAND_OF_CONFORMITY,
        config.SPELL_BRAND_OF_HOBBLING,
        config.SPELL_BRAND_OF_TRACKING,
        config.SPELL_INFERNAL_CHALLENGER,
        config.SPELL_SHACKLE,
        config.SPELL_WATCHFUL_ANIMAL,
        config.SPELL_TRIAL_BY_FIRE,
        config.SPELL_CLAIM_IDENTITY,
        config.SPELL_CLAIM_IDENTITY_GREATER,
        config.SPELL_EGORIAN_DIPLOMACY,
        config.SPELL_GARRULOUS_GRIN,
        config.SPELL_INSECT_SCOUTS,
        config.SPELL_PASSING_FANCY,
        config.SPELL_PASSING_FANCY_MASS,
        config.SPELL_SCRIBE_S_BINDING,
        config.SPELL_APSU_S_SHINING_SCALES,
        config.SPELL_DAHAK_S_RELEASE,
        config.SPELL_DRACONIC_ALLY,
        config.SPELL_DRACONIC_MALICE,
        config.SPELL_FORM_OF_THE_ALIEN_DRAGON_I,
        config.SPELL_FORM_OF_THE_ALIEN_DRAGON_I_I,
        config.SPELL_FORM_OF_THE_ALIEN_DRAGON_I_I_I,
        config.SPELL_FORM_OF_THE_EXOTIC_DRAGON_I,
        config.SPELL_FORM_OF_THE_EXOTIC_DRAGON_I_I,
        config.SPELL_FORM_OF_THE_EXOTIC_DRAGON_I_I_I,
        config.SPELL_HERMEAN_POTENTIAL,
        config.SPELL_SCALES_OF_DEFLECTION,
        config.SPELL_TAIL_STRIKE,
        config.SPELL_ABSURDITY,
        config.SPELL_ALLEVIATE_CORRUPTION,
        config.SPELL_APPEARANCE_OF_LIFE,
        config.SPELL_ASSUME_APPEARANCE,
        config.SPELL_ASSUME_APPEARANCE_GREATER,
        config.SPELL_BAN_CORRUPTION,
        config.SPELL_BARBED_CHAINS,
        config.SPELL_BLOOD_TIES,
        config.SPELL_BLOODBATH,
        config.SPELL_BONESHAKER,
        config.SPELL_BORROW_CORRUPTION,
        config.SPELL_CHARNEL_HOUSE,
        config.SPELL_COMPELLING_RANT,
        config.SPELL_CONTACT_ENTITY_I,
        config.SPELL_CONTACT_ENTITY_I_I,
        config.SPELL_CONTACT_ENTITY_I_I_I,
        config.SPELL_CONTACT_ENTITY_I_V,
        config.SPELL_CRUEL_JAUNT,
        config.SPELL_CURSE_OF_FELL_SEASONS,
        config.SPELL_CURSE_OF_NIGHT,
        config.SPELL_CURSE_TERRAIN_LESSER,
        config.SPELL_CURSE_TERRAIN,
        config.SPELL_CURSE_TERRAIN_GREATER,
        config.SPELL_CURSE_TERRAIN_SUPREME,
        config.SPELL_DAMNATION,
        config.SPELL_DEATH_CLUTCH,
        config.SPELL_DECAPITATE,
        config.SPELL_DECOLLATE,
        config.SPELL_DREADSCAPE,
        config.SPELL_FLESH_PUPPET,
        config.SPELL_FLESH_PUPPET_HORDE,
        config.SPELL_FLESH_WALL,
        config.SPELL_FLICKERING_LIGHTS,
        config.SPELL_GRASPING_CORPSE,
        config.SPELL_GREEN_CARESS,
        config.SPELL_HEDGING_WEAPONS,
        config.SPELL_HOLY_JAVELIN,
        config.SPELL_HORRIFIC_DOUBLES,
        config.SPELL_HUNGER_FOR_FLESH,
        config.SPELL_HUNGER_FOR_FLESH_MASS,
        config.SPELL_IMPOSSIBLE_ANGLES,
        config.SPELL_LIFE_BLAST,
        config.SPELL_LOCATE_GATE,
        config.SPELL_MAD_SULTAN_S_MELODY,
        config.SPELL_MASSACRE,
        config.SPELL_MAZE_OF_MADNESS_AND_SUFFERING,
        config.SPELL_NIGHT_TERRORS,
        config.SPELL_PESSIMISM,
        config.SPELL_PHANTASMAL_ASPHYXIATION,
        config.SPELL_PHANTASMAL_PUTREFACTION,
        config.SPELL_PHOBIA,
        config.SPELL_PLUNDERED_POWER,
        config.SPELL_PROFANE_NIMBUS,
        config.SPELL_PYROTECHNIC_ERUPTION,
        config.SPELL_QUICK_CHANGE,
        config.SPELL_RIGOR_MORTIS,
        config.SPELL_SACRAMENTAL_SEAL,
        config.SPELL_SACRED_NIMBUS,
        config.SPELL_SCREAMING_FLAMES,
        config.SPELL_SENSE_FEAR,
        config.SPELL_SENSE_MADNESS,
        config.SPELL_SLEEPWALKING_SUGGESTION,
        config.SPELL_SLOUGH,
        config.SPELL_STAVE_OFF_CORRUPTION,
        config.SPELL_STRAITJACKET,
        config.SPELL_SYMBOL_OF_EXSANGUINATION,
        config.SPELL_TEMPORARY_GRAFT,
        config.SPELL_TORPID_REANIMATION,
        config.SPELL_VERMINOUS_TRANSFORMATION,
        config.SPELL_VILE_DOG_TRANSFORMATION,
        config.SPELL_WAVES_OF_BLOOD,
        config.SPELL_WITHER_LIMB,
        config.SPELL_BESMARA_S_GRASPING_DEPTHS,
        config.SPELL_CRAFTER_S_NIGHTMARE,
        config.SPELL_FRIGID_SOULS,
        config.SPELL_GRIM_STALKER,
        config.SPELL_HORRIFYING_VISAGE,
        config.SPELL_MISCHIEVOUS_SHADOW,
        config.SPELL_SKIN_TAG,
        config.SPELL_UNSETTLING_PRESENCE,
        config.SPELL_URGATHOA_S_BEACON,
        config.SPELL_YELLOW_SIGN,
        config.SPELL_JANNI_S_JAUNT,
        config.SPELL_MEDUSA_S_BANE,
        config.SPELL_ENLIGHTENED_STEP,
        config.SPELL_FIREWALKER_S_MEDITATION,
        config.SPELL_RITE_OF_BODILY_PURITY,
        config.SPELL_RITE_OF_CENTERED_MIND,
        config.SPELL_SEE_BEYOND,
        config.SPELL_SPIRIT_BONDS,
        config.SPELL_VISUALIZATION_OF_THE_BODY,
        config.SPELL_VISUALIZATION_OF_THE_MIND
    ]


def GetSchoolName(n):
    if n == config.SCHOOL_CONJURATION:
        return 'Conjuration'
    if n == config.SCHOOL_ENCHANTMENT:
        return 'Enchantment'
    if n == config.SCHOOL_TRANSMUTATION:
        return 'Transmutation'
    if n == config.SCHOOL_ABJURATION:
        return 'Abjuration'
    if n == config.SCHOOL_DIVINATION:
        return 'Divination'
    if n == config.SCHOOL_NECROMANCY:
        return 'Necromancy'
    if n == config.SCHOOL_UNIVERSAL:
        return 'Universal'
    if n == config.SCHOOL_EVOCATION:
        return 'Evocation'
    if n == config.SCHOOL_ILLUSION:
        return 'Illusion'
    if n == config.SCHOOL_TRANSFORMATION:
        return 'Transformation'
    return ''


def GetSubschoolNames(n):
    names = []
    if n & config.SUBSCHOOL_CREATION != 0:
        names.append('Creation')
    if n & config.SUBSCHOOL_COMPULSION != 0:
        names.append('Compulsion')
    if n & config.SUBSCHOOL_POLYMORPH != 0:
        names.append('Polymorph')
    if n & config.SUBSCHOOL_SCRYING != 0:
        names.append('Scrying')
    if n & config.SUBSCHOOL_GLAMER != 0:
        names.append('Glamer')
    if n & config.SUBSCHOOL_HEALING != 0:
        names.append('Healing')
    if n & config.SUBSCHOOL_CHARM != 0:
        names.append('Charm')
    if n & config.SUBSCHOOL_PATTERN != 0:
        names.append('Pattern')
    if n & config.SUBSCHOOL_SUMMONING != 0:
        names.append('Summoning')
    if n & config.SUBSCHOOL_TELEPORTATION != 0:
        names.append('Teleportation')
    if n & config.SUBSCHOOL_PHANTASM != 0:
        names.append('Phantasm')
    if n & config.SUBSCHOOL_FIGMENT != 0:
        names.append('Figment')
    if n & config.SUBSCHOOL_CALLING != 0:
        names.append('Calling')
    if n & config.SUBSCHOOL_SHADOW != 0:
        names.append('Shadow')
    if n & config.SUBSCHOOL_LIGHT != 0:
        names.append('Light')
    if n & config.SUBSCHOOL_HAUNTED != 0:
        names.append('Haunted')
    return names


def GetDescriptorNames(n):
    names = []
    if n & config.DESCRIPTOR_MIND_AFFECTING != 0:
        names.append('MindAffecting')
    if n & config.DESCRIPTOR_AIR != 0:
        names.append('Air')
    if n & config.DESCRIPTOR_ACID != 0:
        names.append('Acid')
    if n & config.DESCRIPTOR_SONIC != 0:
        names.append('Sonic')
    if n & config.DESCRIPTOR_EVIL != 0:
        names.append('Evil')
    if n & config.DESCRIPTOR_EMOTION != 0:
        names.append('Emotion')
    if n & config.DESCRIPTOR_FEAR != 0:
        names.append('Fear')
    if n & config.DESCRIPTOR_CURSE != 0:
        names.append('Curse')
    if n & config.DESCRIPTOR_FORCE != 0:
        names.append('Force')
    if n & config.DESCRIPTOR_GOOD != 0:
        names.append('Good')
    if n & config.DESCRIPTOR_FIRE != 0:
        names.append('Fire')
    if n & config.DESCRIPTOR_ELECTRICITY != 0:
        names.append('Electricity')
    if n & config.DESCRIPTOR_CHAOTIC != 0:
        names.append('Chaotic')
    if n & config.DESCRIPTOR_COLD != 0:
        names.append('Cold')
    if n & config.DESCRIPTOR_DEATH != 0:
        names.append('Death')
    if n & config.DESCRIPTOR_LANGUAGE_DEPENDENT != 0:
        names.append('LanguageDependent')
    if n & config.DESCRIPTOR_LIGHT != 0:
        names.append('Light')
    if n & config.DESCRIPTOR_WATER != 0:
        names.append('Water')
    if n & config.DESCRIPTOR_DARKNESS != 0:
        names.append('Darkness')
    if n & config.DESCRIPTOR_LAWFUL != 0:
        names.append('Lawful')
    if n & config.DESCRIPTOR_EARTH != 0:
        names.append('Earth')
    if n & config.DESCRIPTOR_PAIN != 0:
        names.append('Pain')
    if n & config.DESCRIPTOR_POISON != 0:
        names.append('Poison')
    if n & config.DESCRIPTOR_SHADOW != 0:
        names.append('Shadow')
    if n & config.DESCRIPTOR_FIGMENT != 0:
        names.append('Figment')
    if n & config.DESCRIPTOR_LAW != 0:
        names.append('Law')
    if n & config.DESCRIPTOR_DISEASE != 0:
        names.append('Disease')
    if n & config.DESCRIPTOR_CHAOS != 0:
        names.append('Chaos')
    if n & config.DESCRIPTOR_VARIABLE != 0:
        names.append('Variable')
    if n & config.DESCRIPTOR_TRAVEL != 0:
        names.append('Travel')
    if n & config.DESCRIPTOR_PHANTASM != 0:
        names.append('Phantasm')
    if n & config.DESCRIPTOR_RUSE != 0:
        names.append('Ruse')
    if n & config.DESCRIPTOR_DRACONIC != 0:
        names.append('Draconic')
    if n & config.DESCRIPTOR_MEDITATIVE != 0:
        names.append('Meditative')
    return names


def GetSourceName(n):
    if n == config.SOURCE_ADVANCED_CLASS_GUIDE:
        return "Advanced Class Guide"
    if n == config.SOURCE_ADVANCED_CLASS_ORIGINS:
        return "Advanced Class Origins"
    if n == config.SOURCE_ADVANCED_RACE_GUIDE:
        return "Advanced Race Guide"
    if n == config.SOURCE_AGENTS_OF_EVIL:
        return "Agents Of Evil"
    if n == config.SOURCE_ANDORAN:
        return "Andoran"
    if n == config.SOURCE_ANIMAL_ARCHIVE:
        return "Animal Archive"
    if n == config.SOURCE_AP_102:
        return "AP 102"
    if n == config.SOURCE_AP_107:
        return "AP 107"
    if n == config.SOURCE_AP_110:
        return "AP 110"
    if n == config.SOURCE_AP_29:
        return "AP 29"
    if n == config.SOURCE_AP_30:
        return "AP 30"
    if n == config.SOURCE_AP_35:
        return "AP 35"
    if n == config.SOURCE_AP_42:
        return "AP 42"
    if n == config.SOURCE_AP_50:
        return "AP 50"
    if n == config.SOURCE_AP_55:
        return "AP 55"
    if n == config.SOURCE_AP_56:
        return "AP 56"
    if n == config.SOURCE_AP_62:
        return "AP 62"
    if n == config.SOURCE_AP_64:
        return "AP 64"
    if n == config.SOURCE_AP_65:
        return "AP 65"
    if n == config.SOURCE_AP_67:
        return "AP 67"
    if n == config.SOURCE_AP_68:
        return "AP 68"
    if n == config.SOURCE_AP_69:
        return "AP 69"
    if n == config.SOURCE_AP_71:
        return "AP 71"
    if n == config.SOURCE_AP_74:
        return "AP 74"
    if n == config.SOURCE_AP_77:
        return "AP 77"
    if n == config.SOURCE_AP_78:
        return "AP 78"
    if n == config.SOURCE_AP_80:
        return "AP 80"
    if n == config.SOURCE_AP_81:
        return "AP 81"
    if n == config.SOURCE_AP_82:
        return "AP 82"
    if n == config.SOURCE_AP_84:
        return "AP 84"
    if n == config.SOURCE_AP_86:
        return "AP 86"
    if n == config.SOURCE_AP_89:
        return "AP 89"
    if n == config.SOURCE_AP_91:
        return "AP 91"
    if n == config.SOURCE_AP_93:
        return "AP 93"
    if n == config.SOURCE_AP_95:
        return "AP 95"
    if n == config.SOURCE_AP_99:
        return "AP 99"
    if n == config.SOURCE_APG:
        return "APG"
    if n == config.SOURCE_ARCANE_ANTHOLOGY:
        return "Arcane Anthology"
    if n == config.SOURCE_ARMOR_MASTERS_HANDBOOK:
        return "Armor Masters Handbook"
    if n == config.SOURCE_BLACK_MARKETS:
        return "Black Markets"
    if n == config.SOURCE_BLOOD_OF_SHADOWS:
        return "Blood Of Shadows"
    if n == config.SOURCE_BLOOD_OF_THE_ELEMENTS:
        return "Blood Of The Elements"
    if n == config.SOURCE_BLOOD_OF_THE_MOON:
        return "Blood Of The Moon"
    if n == config.SOURCE_BLOOD_OF_THE_NIGHT:
        return "Blood Of The Night"
    if n == config.SOURCE_BOOK_OF_THE_DAMMED_V1:
        return "Book of the Dammed V1"
    if n == config.SOURCE_BOOK_OF_THE_DAMNED_V2:
        return "Book of the Damned V2"
    if n == config.SOURCE_CHAMPIONS_OF_BALANCE:
        return "Champions Of Balance"
    if n == config.SOURCE_CHAMPIONS_OF_CORRUPTION:
        return "Champions Of Corruption"
    if n == config.SOURCE_CHAMPIONS_OF_PURITY:
        return "Champions Of Purity"
    if n == config.SOURCE_CHELIAX_EMPIRE_OF_DEVILS:
        return "Cheliax Empire Of Devils"
    if n == config.SOURCE_CHRONICLE_OF_THE_RIGHTEOUS:
        return "Chronicle Of The Righteous"
    if n == config.SOURCE_CLASSIC_TREASURES:
        return "Classic Treasures"
    if n == config.SOURCE_COHORTS_AND_COMPANIONS:
        return "Cohorts & Companions"
    if n == config.SOURCE_CONDITION_CARDS:
        return "Condition Cards"
    if n == config.SOURCE_DEMON_HUNTERS_HANDBOOK:
        return "Demon Hunter's Handbook"
    if n == config.SOURCE_DEMONS_REVISITED:
        return "Demons Revisited"
    if n == config.SOURCE_DIRTY_TACTICS_TOOLBOX:
        return "Dirty Tactics Toolbox"
    if n == config.SOURCE_DIVINE_ANTHOLOGY:
        return "Divine Anthology"
    if n == config.SOURCE_DRAGON_EMPIRES_PRIMER:
        return "Dragon Empires Primer"
    if n == config.SOURCE_DRAGONSLAYERS_HANDBOOK:
        return "Dragonslayer's Handbook"
    if n == config.SOURCE_DUNGEONEERS_HANDBOOK:
        return "Dungeoneers Handbook"
    if n == config.SOURCE_DUNGEONS_OF_GOLARION:
        return "Dungeons Of Golarion"
    if n == config.SOURCE_DWARVES_OF_GOLARION:
        return "Dwarves of Golarion"
    if n == config.SOURCE_FACTION_GUIDE:
        return "Faction Guide"
    if n == config.SOURCE_FAITHS_AND_PHILOSOPHIES:
        return "Faiths & Philosophies"
    if n == config.SOURCE_FAITHS_OF_CORRUPTION:
        return "Faiths Of Corruption"
    if n == config.SOURCE_FAITHS_OF_PURITY:
        return "Faiths Of Purity"
    if n == config.SOURCE_FAMILIAR_FOLIO:
        return "Familiar Folio"
    if n == config.SOURCE_GIANT_HUNTERS_HANDBOOK:
        return "Giant Hunters Handbook"
    if n == config.SOURCE_GNOMES_OF_GOLARION:
        return "Gnomes Of Golarion"
    if n == config.SOURCE_GOBLINS_OF_GOLARION:
        return "Goblins Of Golarion"
    if n == config.SOURCE_HAUNTED_HEROES_HANDBOOK:
        return "Haunted Heroes Handbook"
    if n == config.SOURCE_HEROES_OF_THE_STREETS:
        return "Heroes Of The Streets"
    if n == config.SOURCE_HEROES_OF_THE_WILD:
        return "Heroes Of The Wild"
    if n == config.SOURCE_HORROR_ADVENTURES:
        return "Horror Adventures"
    if n == config.SOURCE_HORSEMEN_OF_THE_APOCALYPSE:
        return "Horsemen Of The Apocalypse"
    if n == config.SOURCE_HUMANS_OF_GOLARION:
        return "Humans Of Golarion"
    if n == config.SOURCE_INNER_SEA_GODS:
        return "Inner Sea Gods"
    if n == config.SOURCE_INNER_SEA_INTRIGUE:
        return "Inner Sea Intrigue"
    if n == config.SOURCE_INNER_SEA_MAGIC:
        return "Inner Sea Magic"
    if n == config.SOURCE_INNER_SEA_MONSTER_CODEX:
        return "Inner Sea Monster Codex"
    if n == config.SOURCE_INNER_SEA_RACES:
        return "Inner Sea Races"
    if n == config.SOURCE_INNER_SEA_WORLD_GUIDE:
        return "Inner Sea World Guide"
    if n == config.SOURCE_KNIGHTS_OF_THE_INNER_SEA:
        return "Knights Of The Inner Sea"
    if n == config.SOURCE_KOBOLDS_OF_GOLARION:
        return "Kobolds Of Golarion"
    if n == config.SOURCE_LEGACY_OF_DRAGONS:
        return "Legacy Of Dragons"
    if n == config.SOURCE_LOST_KINGDOMS:
        return "Lost Kingdoms"
    if n == config.SOURCE_MAGIC_TACTICS_TOOLBOX:
        return "Magic Tactics Toolbox"
    if n == config.SOURCE_MAGICAL_MARKETPLACE:
        return "Magical Marketplace"
    if n == config.SOURCE_MELEE_TACTICS_TOOLBOX:
        return "Melee Tactics Toolbox"
    if n == config.SOURCE_MONSTER_CODEX:
        return "Monster Codex"
    if n == config.SOURCE_MONSTER_SUMMONERS_HANDBOOK:
        return "Monster Summoner's Handbook"
    if n == config.SOURCE_MYTHIC_ADVENTURES:
        return "Mythic Adventures"
    if n == config.SOURCE_MYTHIC_ORIGINS:
        return "Mythic Origins"
    if n == config.SOURCE_OCCULT_ADVENTURES:
        return "Occult Adventures"
    if n == config.SOURCE_OCCULT_MYSTERIES:
        return "Occult Mysteries"
    if n == config.SOURCE_OCCULT_ORIGINS:
        return "Occult Origins"
    if n == config.SOURCE_OCCULT_REALMS:
        return "Occult Realms"
    if n == config.SOURCE_ORCS_OF_GOLARION:
        return "Orcs of Golarion"
    if n == config.SOURCE_OSIRION_LEGACY_OF_PHARAOHS:
        return "Osirion, Legacy Of Pharaohs"
    if n == config.SOURCE_PAIZO_BLOG:
        return "Paizo Blog"
    if n == config.SOURCE_PATH_OF_THE_HELLKNIGHT:
        return "Path Of The Hellknight"
    if n == config.SOURCE_PATHFINDER_SOCIETY_FIELD_GUIDE:
        return "Pathfinder Society Field Guide"
    if n == config.SOURCE_PATHFINDER_SOCIETY_PRIMER:
        return "Pathfinder Society Primer"
    if n == config.SOURCE_PEOPLE_OF_THE_NORTH:
        return "People Of The North"
    if n == config.SOURCE_PEOPLE_OF_THE_RIVER:
        return "People Of The River"
    if n == config.SOURCE_PEOPLE_OF_THE_SANDS:
        return "People Of The Sands"
    if n == config.SOURCE_PEOPLE_OF_THE_STARS:
        return "People Of The Stars"
    if n == config.SOURCE_P_F_R_P_G_CORE:
        return "PFRPG Core"
    if n == config.SOURCE_PFS_S3_09:
        return "PFS S3-09"
    if n == config.SOURCE_PIRATES_OF_THE_INNER_SEA:
        return "Pirates Of The Inner Sea"
    if n == config.SOURCE_PLANES_OF_POWER:
        return "Planes Of Power"
    if n == config.SOURCE_QUESTS_AND_CAMPAIGNS:
        return "Quests and Campaigns"
    if n == config.SOURCE_RANGED_TACTICS_TOOLBOX:
        return "Ranged Tactics Toolbox"
    if n == config.SOURCE_RIVAL_GUIDE:
        return "Rival Guide"
    if n == config.SOURCE_ROT_R_L_A_E_APPENDIX:
        return "RotRL-AE-Appendix"
    if n == config.SOURCE_SARGAVA:
        return "Sargava"
    if n == config.SOURCE_SPYMASTERS_HANDBOOK:
        return "Spymaster's Handbook"
    if n == config.SOURCE_TECHNOLOGY_GUIDE:
        return "Technology Guide"
    if n == config.SOURCE_THE_DRAGONS_DEMAND:
        return "The Dragon's Demand"
    if n == config.SOURCE_THE_HARROW_HANDBOOK:
        return "The HarrowHandbook"
    if n == config.SOURCE_ULTIMATE_COMBAT:
        return "Ultimate Combat"
    if n == config.SOURCE_ULTIMATE_INTRIGUE:
        return "Ultimate Intrigue"
    if n == config.SOURCE_ULTIMATE_MAGIC:
        return "Ultimate Magic"
    if n == config.SOURCE_UNDEAD_SLAYERS_HANDBOOK:
        return "Undead Slayer's Handbook"
    return ''


def GetTypeName(n):
    if n == config.SAVING_THROW_FORTITUDE:
        return 'FORTITUDE'
    if n == config.SAVING_THROW_REFLEX:
        return 'REFLEX'
    if n == config.SAVING_THROW_WILL:
        return 'WILL'
    return ''


def GetEffectName(n):
    if n == config.SAVING_THROW_NEGATES:
        return 'NEGATES'
    if n == config.SAVING_THROW_HALVES:
        return 'HALVES'
    if n == config.SAVING_THROW_PARTIAL:
        return 'PARTIAL'
    if n == config.SAVING_THROW_DISBELIEF:
        return 'DISBELIEF'
    return ''


def GetUnitName(n, ut, plural=False):
    if n == config.UNIT_FEET and ut == config.DIST_TYPE_DISTANCE:
        if plural:
            return 'Feet'
        else:
            return 'Foot'
    if n == config.UNIT_YARD and ut == config.DIST_TYPE_DISTANCE:
        if plural:
            return 'Yards'
        else:
            return 'Yard'
    if n == config.UNIT_MILE and ut == config.DIST_TYPE_DISTANCE:
        if plural:
            return 'Miles'
        else:
            return 'Mile'
    if n == config.UNIT_HEX and ut == config.DIST_TYPE_DISTANCE:
        if plural:
            return 'Hexes'
        else:
            return 'Hex'
    if n == config.UNIT_ACTION and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Actions'
        else:
            return 'Action'
    if n == config.UNIT_ROUND and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Rounds'
        else:
            return 'Round'
    if n == config.UNIT_MINUTE and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Minutes'
        else:
            return 'Minute'
    if n == config.UNIT_HOUR and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Hours'
        else:
            return 'Hour'
    if n == config.UNIT_DAY and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Days'
        else:
            return 'Day'
    if n == config.UNIT_MONTH and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Months'
        else:
            return 'Month'
    if n == config.UNIT_YEAR and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Years'
        else:
            return 'Year'
    if n == config.UNIT_WEEK and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Weeks'
        else:
            return 'Week'
    if n == config.UNIT_INSTANTANEOUS and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Instantaneous'
        else:
            return 'Instantaneous'
    if n == config.UNIT_PERMANENT and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Permanent'
        else:
            return 'Permanent'
    if n == config.UNIT_CONCENTRATION and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Concentrations'
        else:
            return 'Concentration'
    if n == config.UNIT_BATTLE and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Battles'
        else:
            return 'Battle'
    if n == config.UNIT_UNTIL and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Until'
        else:
            return 'Until'
    if n == config.UNIT_USAGE and ut == config.DIST_TYPE_TIME:
        if plural:
            return 'Usages'
        else:
            return 'Usage'
    return ''


def GetActionTypeString(at):
    if at == config.ACTION_STANDARD:
        return 'Standard'
    if at == config.ACTION_QUICK:
        return 'Quick'
    if at == config.ACTION_IMMEDIATE:
        return 'Immediate'
    if at == config.ACTION_SWIFT:
        return 'Swift'
    if at == config.ACTION_FULL:
        return 'Full'
    return


spellData = []
namesToIds = {}


def LoadSpellDatabase(fn='spells.json'):
    global spellData
    with open(fn) as f:
        spellData = json.loads(f.read())
        for i in range(len(spellData)):
            namesToIds[spellData[i]['name']] = i


def LoadSpellByName(name):
    global spellData
    if not spellData:
        LoadSpellDatabase()
    ret = Spell()
    if spellData and name in namesToIds:
        ret = Spell(spellData[namesToIds[name]])
    return ret


def GetValidSpells(char, classIdx, level, domains=[]):
    global spellData
    if not spellData:
        LoadSpellDatabase()
    retVal = []
    for spell in spellData:
        if Spell(spell).GetSpellLevel(char.Classes[classIdx][0], domains) == level:
            retVal.append(Spell(spell))
    return retVal


class Spell:

    def __init__(self, data=None):
        self.Id = 0
        self.Name = ""
        self.School = config.NONE
        self.Subschools = config.NONE  # Can or them together if it is more than one
        self.Descriptor = config.NONE  # Can or them together if it is more than one
        self.SpellLevel = {}  # Dict of class type: level
        self.CastingTime = Duration()
        self.VerbalComponent = False
        self.SomaticComponent = False
        self.MatericalComponent = [False, []]
        self.FocusComponent = [False, []]
        self.DivineFocusComponent = [False, []]
        self.HasCostlyComponent = False
        self.Personal = False
        self.Touch = False
        self.UnlimitedDistance = False
        self.Immediate = False
        self.Dismissable = False
        self.Shapeable = False
        self.SpellResistance = False
        self.Harmless = False
        self.Range = Range()
        self.Area = ""
        self.SavingThrow = []  # List of saving throw
        self.Description = ""
        self.Source = config.NONE
        if data:
            self.ParseData(data)

    def ParseData(self, data):
        self.Id = data['id']
        self.Name = data['name']
        self.School = data['school']
        for s in data['subschools']:
            self.Subschools |= s
        for s in data['descriptors']:
            self.Descriptor |= s
        for i in data['spell_levels']:
            self.SpellLevel[i[0]] = i[1]
        self.CastingTime = Duration(data['casting_time'][0], data['casting_time'][2], AmountPerLevel=data['casting_time'][1])
        self.Duration = Duration(data['duration'][0], data['duration'][2], AmountPerLevel=data['duration'][1])
        self.VerbalComponent = data['components'][0]
        self.SomaticComponent = data['components'][1]
        self.MaterialComponent = data['components'][2]
        self.FocusComponent = data['components'][3]
        self.DivineFocusComponent = data['components'][4]
        self.HasCostlyComponent = data['costly_materials']
        self.Personal = 'personal' in data['range'] and data['range']['personal']
        self.Touch = 'touch' in data['range'] and data['range']['touch']
        self.UnlimitedDistance = 'unlimited' in data['range'] and data['range']['unlimited']
        self.Immediate = self.CastingTime.Unit == config.UNIT_INSTANTANEOUS
        self.Dismissable = data['dismissable']
        self.Shapeable = data['shapeable']
        self.SpellResistance = data['spell_resistence'][0]
        self.Harmless = any(s[2] for s in data['saving_throw']) or data['spell_resistence'][1]
        self.Range = Range(data['range']['distance'], data['range']['additional'], data['range']['perlevel'], data['range']['distanceUnit'])
        self.Area = data['area']
        for s in data['saving_throw']:
            self.SavingThrow.append(SavingThrow(s[0], s[1]))
        # self.Description = data['description'][0]
        self.Description = data['description'][1]
        self.Source = data['source']

    def GetSpellLevel(self, charClass, domains=[]):
        levels = []
        if charClass.Type in self.SpellLevel:
            levels.append(min(9, max(0, self.SpellLevel[charClass.Type] + self.GetLevelChange())))
        for domain in domains:
            for key in config.DomainSpells[domain]:
                for spell in config.DomainSpells[domain][key]:
                    if spell == self.Id:
                        levels.append(key)
        return -1 if not levels else min(levels)

    def GetLevelChange(self):
        # TODO: Apply metamagics
        return 0

    def GetSpellHeaders(self):
        return "{:^20}".format("Name")

    def ToString(self, casterLevel):
        return "{:<20}".format(self.Name)

    def FormatDescription(self, level):
        ret = self.Description
        exp = r'(//\[([0-9]+)\] d \[([0-9]+)\] / \[([0-9]+)\] \+ \[(([0-9]+)|(level))\] / \[([0-9]+)\]//)'
        r = re.compile(exp)
        m = r.finditer(ret)
        for i in m:
            print i.groups()
            print ret
            rolls = int(i.groups()[1])
            sides = int(i.groups()[2])
            perLevel = int(i.groups()[3])
            additional = level if i.groups()[4] == 'level' else int(i.groups()[4])
            additionalPerLevel = int(i.groups()[7])
            addAmount = additional
            if additionalPerLevel > 0:
                addAmount = addAmount * level / additionalPerLevel
            if perLevel > 0:
                rolls = rolls * level / perLevel
            new = str(rolls) + "d" + str(sides)
            if addAmount > 0:
                new += " + " + str(addAmount)
            ret = ret.replace(i.groups()[0], new)
            print ret
        return ret

    def ToJson(self, level, modifier, spLevel):
        j = {}
        j['Id'] = self.Id
        j['Name'] = self.Name
        j['School'] = GetSchoolName(self.School)
        j['Subschools'] = GetSubschoolNames(self.Subschools)
        j['Descriptors'] = GetDescriptorNames(self.Descriptor)
        j['SpellLevel'] = [{'Class': characterclass.GetClassName(key), 'Level': self.SpellLevel[key]} for key in self.SpellLevel]
        j['CastingTime'] = self.CastingTime.ToJson(level)
        j['VerbalComponent'] = self.VerbalComponent
        j['SomaticComponent'] = self.SomaticComponent
        j['MaterialComponent'] = {'MaterialComponent': self.MaterialComponent}
        j['FocusComponent'] = {'FocusComponent': self.FocusComponent}
        j['DivineFocusComponent'] = {'DivineFocusComponent': self.DivineFocusComponent}
        j['HasCostlyComponent'] = self.HasCostlyComponent
        j['Personal'] = self.Personal
        j['Touch'] = self.Touch
        j['UnlimitedDistance'] = self.UnlimitedDistance
        j['Immediate'] = self.Immediate
        j['Dismissable'] = self.Dismissable
        j['Shapeable'] = self.Shapeable
        j['SpellResistance'] = self.SpellResistance
        j['Harmless'] = self.Harmless
        j['Range'] = self.Range.ToJson(level)
        j['Area'] = self.Area
        # j['Description'] = self.FormatDescription(level)
        j['Description'] = self.Description
        j['Source'] = GetSourceName(self.Source)
        j['SavingThrows'] = [s.ToJson(level, modifier, spLevel) for s in self.SavingThrow]
        return j

    def __eq__(self, other):
        return self.Id == other.Id


class Range:

    def __init__(self, base=0, extra=0, per=1, distanceUnit=config.NONE):
        self.BaseRange = base
        self.ExtraPerLevel = extra
        self.PerLevel = per
        self.DistanceUnit = distanceUnit

    def Total(self, level):
        if self.PerLevel == 0:
            return self.BaseRange + self.ExtraPerLevel
        return self.BaseRange + self.ExtraPerLevel * (level / self.PerLevel)

    def ToJson(self, level):
        return str(self.Total(level)) + " " + GetUnitName(self.DistanceUnit, config.DIST_TYPE_DISTANCE, self.Total(level) != 1)


class Duration:

    def __init__(self, Amount=0, Unit=config.UNIT_ACTION, ActionType=config.ACTION_STANDARD, AmountPerLevel=0):
        self.Unit = Unit
        self.ActionType = ActionType
        self.Amount = Amount
        self.AmountPerLevel = AmountPerLevel

    def GetDuration(self, level):
        if self.AmountPerLevel == 0:
            return self.AmountPerLevel
        return min(1, self.Amount * (level / self.AmountPerLevel))

    def ToJson(self, level):
        dur = self.GetDuration(level)
        un = GetUnitName(self.Unit, config.DIST_TYPE_TIME, dur != 1)
        at = GetActionTypeString(self.ActionType)
        if at != '' and (self.Unit == config.UNIT_ACTION or self.Unit == config.UNIT_ROUND):
            un = at + ' ' + un
        if dur == 0:
            return un
        if un == '':
            return ''
        return str(dur) + ' ' + un


class SavingThrow:

    def __init__(self, Type=config.NONE, Effect=config.NONE):
        self.Type = Type
        self.Effect = Effect

    def ToJson(self, level, modifier, spLevel):
        j = {}
        j['Type'] = GetTypeName(self.Type)
        j['Effect'] = GetEffectName(self.Effect)
        j['DC'] = 10 + modifier + spLevel
        return j


class SpAbility:

    def __init__(self):
        return

    def ToJson(self):
        return {}


class SuAbility:

    def __init__(self):
        return

    def ToJson(self):
        return {}
