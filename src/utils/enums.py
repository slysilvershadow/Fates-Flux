# enums.py

from enum import Enum

class Ages(Enum):
    INFANT = 1
    SPROUT = 2
    YOUTH = 3
    ADOLESCENT = 4
    PRIME = 5
    MATURE = 6
    SAGE = 7

class Sex(Enum):
    X = 1
    Y = 2

class Gender(Enum):
    MASC = 1
    FEM = 2
    ANDROGYNOUS = 3

class Tone(Enum):
    PALE = 1
    MEDIUM = 2
    TAN = 3
    DARK = 4
    DEEP = 5

class Undertone(Enum):
    WARM = 1
    NEUTRAL = 2
    COOL = 3

class Height(Enum):
    SHORT = 1
    AVERAGE = 2
    TALL = 3

class BodyShape(Enum):
    SLIM = 1
    AVERAGE = 2
    ATHLETIC = 3
    CURVY = 4

class BodySize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class HairColor(Enum):
    BLACK = 1
    BROWN = 2
    BLONDE = 3
    GINGER = 4

class HairTexture(Enum):
    STRAIGHT = 1
    WAVY = 2
    CURLY = 3

class HairLength(Enum):
    BALD = 1
    SHORT = 2
    MEDIUM = 3
    LONG = 4

class EyeShape(Enum):
    ROUND = 1
    ALMOND = 2
    UPTURNED = 3
    DOWNTURNED = 4
    HOODED = 5

class EyeColor(Enum):
    BROWN = 1
    HAZEL = 2
    GREEN = 3
    BLUE = 4
    GREY = 5

class NoseProfile(Enum):
    SMALL = 1
    MEDIUM = 2
    TALL = 3

class NoseShape(Enum):
    REFINED = 1
    HERO = 2
    SOFT = 3
    PERKY = 4
    DAINTY = 5
    STRONG = 6
    BULB = 7

class MouthShape(Enum):
    THIN = 1
    ROUND = 2
    WIDE = 3
    FULLER_LOWER = 4
    FULLER_UPPER = 5
    DOWNTURNED = 6
    BOWSHAPED = 7
    FULL = 8
    HEARTSHAPED = 9

class EarShape(Enum):
    ROUND = 1
    POINTED = 2

class EarSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Biome(Enum):
    TROPICAL_RAINFOREST = 1
    TROPICAL_SAVANNA = 2
    MEDITERRANEAN_SCRUB = 3
    TEMPERATE_GRASSLAND = 4
    TEMPERATE_DECIDUOUS_FOREST = 5
    TEMPERATE_RAINFOREST = 6
    BOREAL_FOREST = 7
    TUNDRA = 8
    MONTANE_FOREST = 9
    POLAR_ICE_CAP = 10
    RIVER = 11
    LAKE = 12
    WETLAND = 13
    OCEAN = 14
    CORAL_REEF = 15
    ESTUARY = 16

class TimePeriod(Enum):
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3
    NIGHT = 4

class DayOfWeek(Enum):
    RESTONY = 1
    SEREMENT = 2
    CHRONESIS = 3
    TEMPESTUDE = 4
    SOLAMENT = 5
    HELIORIS = 6
    DURATONIS = 7
    RESPORAL = 8
    SABBATHAL = 9
    NOCTITUDE = 10

class MonthOfYear(Enum):
    BRIGIDE = 1
    IMBOLKA = 2
    FLORALIS = 3
    LITHARA = 4
    HELIAX = 5
    AESTIUM = 6
    MABONEL = 7
    CERESIO = 8
    YULITH = 9