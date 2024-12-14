# constants.py

# This module contains various constants used throughout the application, including asset paths,
# biome definitions, time settings, character needs, stats, skills, and AI responses.

# Asset Paths
ASSETS = {
    'Character': lambda age_stage, sex, gender, tone, undertone, height, bodyshape, bodysize, haircolor, hairtexture, hairlength, eyeshape, eyecolor, noseprofile, noseshape, mouthshape, earshape, earsize: 
        f'src/assets/visual/characters/{age_stage}/{sex}/{gender}/{tone}_{undertone}/{height}/{bodyshape}_{bodysize}/{haircolor}_{hairtexture}_{hairlength}/{eyeshape}_{eyecolor}/{noseprofile}_{noseshape}/{mouthshape}/{earshape}_{earsize}',
    'Clothing' : lambda cloth_asset: f'src/assets/visual/clothing/{cloth_asset}',
    'Wall' : lambda wall_asset: f'src/assets/visual/wall/{wall_asset}',
    'Tile' : lambda tile_asset: f'src/assets/visual/tile/{tile_asset}',
    'Animal' : lambda animal_asset: f'src/assets/visual/animal/{animal_asset}',
    'Tool' : lambda tool_asset: f'src/assets/visual/tool/{tool_asset}',
    'Plant' : lambda plant_asset: f'src/assets/visual/plant/{plant_asset}',
    'Food' : lambda food_asset: f'src/assets/visual/food/{food_asset}',
    'Rock' : lambda rock_asset: f'src/assets/visual/rock/{rock_asset}',
    'Collectable' : lambda collect_asset: f'src/assets/visual/collectable/{collect_asset}',
    'Work Station' : lambda station_asset: f'src/assets/visual/station/{station_asset}',
    'VFX' : lambda vfx_asset: f'src/assets/visual/vfx/{vfx_asset}',
    'UI' : lambda ui_asset: f'src/assets/visual/ui/{ui_asset}',
    'SFX' : lambda sfx_asset: f'src/assets/audio/sfx/{sfx_asset}'
}

# Window Settings
class Window:
    """Class to manage window settings and scaling for the application."""
    
    def __init__(self):
        self.DEVICE_WIDTH = pygame.display.Info().current_w
        self.DEVICE_HEIGHT = pygame.display.Info().current_h
        self.DESIGN_WIDTH = 1080
        self.DESIGN_HEIGHT = 1920
        self.SCALE_X = self.DEVICE_WIDTH / self.DESIGN_WIDTH
        self.SCALE_Y = self.DEVICE_HEIGHT / self.DESIGN_HEIGHT
        self.FPS = 60

    def scale_position(self, x, y):
        """Scale the position based on the design dimensions."""
        return (x * self.SCALE_X, y * self.SCALE_Y)

    def scale_size(self, width, height):
        """Scale the size based on the design dimensions."""
        scale_width = width * self.SCALE_X
        scale_height = height * self.SCALE_Y
        return (scale_width, scale_height)

# Time Settings
# Constants defining the lengths of various time units
HOUR_LEN = 60
DAY_LEN = 24
WEEK_LEN = 10
MONTH_LEN = 30
YEAR_LEN = 10

# Time of day definitions
MORNING = [6, 7, 8, 9, 10, 11]
AFTERNOON = [12, 13, 14, 15, 16]
EVENING = [17, 18, 19, 20, 21, 22]
NIGHT = [23, 24, 1, 2, 3, 4, 5]

# Month and day names for the in-game calendar
MONTH_NAMES = ['Brigide', 'Imbolka', 'Floralis', 'Lithara',
               'Heliax', 'Aestium', 'Mabonel', 'Ceresio', 'Yulith', 'Hibernis']
DAY_NAMES = ['Restony', 'Serement', 'Chronesis', 'Tempetude', 'Solament',
             'Helioris', 'Duratonis', 'Resporal', 'Sabbathal', 'Noctitude']

# Character Traits
# Dictionary defining various character traits and their possible values
TRAITS = {
    'sex': ['x', 'y'],
    'gender': ['masc', 'fem', 'androgynous'],
    'tone': ['pale', 'medium', 'tan', 'dark', 'deep'],
    'undertone': ['warm', 'neutral', 'cool'],
    'height': ['short', 'average', 'tall'],
    'bshape': ['slim', 'average', 'athletic', 'curvy'],
    'bsize': ['small', 'medium', 'large'],
    'hcolor': ['black', 'brown', 'blonde', 'ginger'],
    'htext': ['straight', 'wavy', 'curly'],
    'eshape': ['round', 'almond', 'upturned', 'downturned', 'hooded'],
    'ecolor': ['brown', 'hazel', 'green', 'blue', 'grey'],
    'nprofile': ['small', 'medium', 'tall'],
    'nshape': ['refined', 'hero', 'soft', 'perky', 'dainty', 'strong', 'bulb'],
    'mshape': ['thin', 'round', 'wide', 'fuller lower', 'fuller upper', 'downturned', 'bowshaped', 'full', 'heartshaped'],
    'rshape': ['round', 'pointed'],
    'rsize': ['small', 'medium', 'large'],
}

# Age Definitions
# Dictionary defining age categories and their corresponding age ranges
AGES = {
    'infant': (0, 2),
    'sprout': (3, 4),
    'youth': (5, 12),
    'adolescent': (13, 17),
    'prime': (18, 29),
    'mature': (30, 59),
    'sage': (60, 120)
}

# Character Traits
# Dictionary defining character traits with positive, neutral, and negative attributes
TRAITS = {
    'temperament': {
        'positive': [
            'easy-going',
            'adaptable',
            'content',
            'cheerful',
            'calm'
        ],
        'neutral': [
            'active',
            'regular',
            'slow-to-warm-up',
            'moderate',
            'observant'
        ],
        'negative': [
            'fussy',
            'irritable',
            'unpredictable',
            'restless',
            'overactive'
        ]
    },
    'socialization': {
        'positive': [
            'sociable',
            'playful',
            'affectionate',
            'friendly',
            'outgoing'
        ],
        'neutral': [
            'observant',
            'independent',
            'cautious',
            'curious',
            'mellow'
        ],
        'negative': [
            'clingy',
            'irritable',
            'withdrawn',
            'hyperactive',
            'impulsive'
        ]
    },
    'emotional': {
        'positive': [
            'cheerful',
            'passionate',
            'optimistic',
            'joyful',
            'hopeful'
        ],
        'neutral': [
            'sensitive',
            'calm',
            'reflective',
            'balanced',
            'realistic'
        ],
        'negative': [
            'moody',
            'anxious',
            'gloomy',
            'aggressive',
            'doubtful'
        ]
    },
    'interaction': {
        'positive': [
            'cooperative',
            'empathetic',
            'supportive',
            'generous',
            'trustworthy'
        ],
        'neutral': [
            'reserved',
            'independent',
            'adaptable',
            'neutral',
            'pragmatic'
        ],
        'negative': [
            'shy',
            'confrontational',
            'manipulative',
            'aloof',
            'dismissive'
        ]
    },
    'cognition': {
        'positive': [
            'curious',
            'diligent',
            'creative',
            'inquisitive',
            'motivated'
        ],
        'neutral': [
            'practical',
            'analytical',
            'intuitive',
            'theoretical',
            'exploratory'
        ],
        'negative': [
            'distracted',
            'stubborn',
            'uncritical',
            'complacent',
            'disinterested'
        ]
    },
    'identity': {
        'positive': [
            'confident',
            'principled',
            'open-minded',
            'self-aware',
            'authentic'
        ],
        'neutral': [
            'questioning',
            'experimental',
            'idealistic',
            'reflective',
            'curious'
        ],
        'negative': [
            'insecure',
            'conformist',
            'rebellious',
            'conflicted',
            'doubtful'
        ]
    },
    'ambition': {
        'positive': [
            'ambitious',
            'dedicated',
            'innovative',
            'goal-oriented',
            'driven'
        ],
        'neutral': [
            'flexible',
            'specialized',
            'risk-taking',
            'pragmatic',
            'adaptable'
        ],
        'negative': [
            'unmotivated',
            'workaholic',
            'indecisive',
            'complacent',
            'disengaged'
        ]
    },
    'morals': {
        'positive': [
            'honest',
            'compassionate',
            'resilient',
            'fair-minded',
            'generous'
        ],
        'neutral': [
            'traditional',
            'pragmatic',
            'individualistic',
            'balanced',
            'neutral'
        ],
        'negative': [
            'materialistic',
            'judgmental',
            'hedonistic',
            'selfish',
            'cynical'
        ]
    },
    'perspective': {
        'positive': [
            'wise',
            'content',
            'grateful',
            'optimistic',
            'hopeful'
        ],
        'neutral': [
            'philosophical',
            'nostalgic',
            'accepting',
            'realistic',
            'pragmatic'
        ],
        'negative': [
            'cynical',
            'regretful',
            'bitter',
            'despondent',
            'resentful'
        ]
    },
    'legacy': {
        'positive': [
            'mentoring',
            'philanthropic',
            'inspiring',
            'guiding',
            'visionary'
        ],
        'neutral': [
            'reflective',
            'private',
            'traditional',
            'conservative',
            'practical'
        ],
        'negative': [
            'disengaged',
            'controlling',
            'resentful',
            'manipulative',
            'detached'
        ]
    }
}

# Biomes
# List of ground tiles available in the game
GROUND_TILES = [
    'Lush Grass',
    'Dry Grass',
    'Rich Soil',
    'Dry Soil',
    'Clay Soil',
    'Granite',
    'Limestone',
    'Sedimentary Rock',
    'Sand',
    'Dry Mud',
    'Wet Mud',
    'Shallow Fresh Water',
    'Deep Fresh Water',
    'Shallow Salt Water',
    'Deep Salt Water',
    'Snow',
    'Ice',
    'Permafrost'
]

# Dictionary defining various biomes and their corresponding ground tiles
BIOMES = {
    'Tropical Rainforest': [GROUND_TILES[0], GROUND_TILES[2], GROUND_TILES[10]],  # 'Lush Grass', 'Rich Soil', 'Wet Mud'
    'Tropical Savanna': [GROUND_TILES[1], GROUND_TILES[3], GROUND_TILES[4]],  # 'Dry Grass', 'Dry Soil', 'Clay Soil'
    'Mediterranean Scrub': [GROUND_TILES[1], GROUND_TILES[4], GROUND_TILES[5]],  # 'Dry Grass', 'Clay Soil', 'Granite'
    'Temperate Grassland': [GROUND_TILES[1], GROUND_TILES[2], GROUND_TILES[7]],  # 'Dry Grass', 'Rich Soil', 'Sedimentary Rock'
    'Temperate Deciduous Forest': [GROUND_TILES[0], GROUND_TILES[2], GROUND_TILES[4]],  # 'Lush Grass', 'Rich Soil', 'Clay Soil'
    'Temperate Rainforest': [GROUND_TILES[0], GROUND_TILES[2], GROUND_TILES[10]],  # 'Lush Grass', 'Rich Soil', 'Wet Mud'
    'Boreal Forest': [GROUND_TILES[1], GROUND_TILES[4], GROUND_TILES[6]],  # 'Dry Grass', 'Clay Soil', 'Granite'
    'Tundra ': [GROUND_TILES[15], GROUND_TILES[16], GROUND_TILES[14]],  # 'Snow', 'Ice', 'Permafrost'
    'Montane Forest': [GROUND_TILES[0], GROUND_TILES[4], GROUND_TILES[7]],  # 'Lush Grass', 'Clay Soil', 'Sedimentary Rock'
    'Polar Ice Cap': [GROUND_TILES[15], GROUND_TILES[16]],  # 'Ice', 'Permafrost'
    'River': [GROUND_TILES[11], GROUND_TILES[12]],  # 'Shallow Fresh Water', 'Deep Fresh Water'
    'Lake': [GROUND_TILES[11], GROUND_TILES[12]],  # 'Shallow Fresh Water', 'Deep Fresh Water'
    'Wetland': [GROUND_TILES[10], GROUND_TILES[2]],  # 'Wet Mud', 'Rich Soil'
    'Ocean': [GROUND_TILES[13], GROUND_TILES[14]],  # 'Shallow Salt Water', 'Deep Salt Water'
    'Coral Reef': [GROUND_TILES[13]],  # 'Shallow Salt Water'
    'Estuary': [GROUND_TILES[11], GROUND_TILES[13]],  # 'Shallow Fresh Water', 'Shallow Salt Water'
}

# Character Needs
# Max Need Value
MAX_HUNGER = 100
MAX_THIRST = 100
MAX_ENERGY = 100
MAX_SOCIAL = 100
MAX_RELIEF = 100
MAX_CLEANLINESS = 100
MAX_COMFORT = 100
MAX_SAFETY = 100
MAX_HEALTH = 100

# Minimum Need Value
MIN_HUNGER = 0
MIN_THIRST = 0
MIN_ENERGY = 0
MIN_SOCIAL = 0
MIN_RELIEF = 0
MIN_CLEANLINESS = 0
MIN_COMFORT = 0
MIN_SAFETY = 0
MIN_HEALTH = 0

# Default Decay rates
HUNGER_DECAY = 2  # 2 points every in-game hour
THIRST_DECAY = 3  # 3 points every in-game hour
ENERGY_DECAY = 1  # 1 point every in-game hour
SOCIAL_DECAY = 1  # 1 point every in-game hour
RELIEF_DECAY = 2  # 2 points every in-game hour
CLEANLINESS_DECAY = 0.5  # 0.5 points every in-game hour
COMFORT_DECAY = 1  # 1 point every in-game hour
SAFETY_DECAY = 0.2  # 0.2 points every in-game hour
HEALTH_DECAY = 0.1  # 0.1 points every in-game hour

# Stats
# Dictionary defining core and advanced stats for characters
STATS = {
    'core': {
        'stamina': int,
        'strength': int,
        'dexterity': int,
        'perception': int,
        'willpower': int
    },
    'advanced': {
        'endurance': int,
        'prowess': int,
        'finess': int,
        'conviction': int,
        'vitality': int
    }
}

# Skills
# Dictionary defining various skills available to characters
SKILLS = {
    'survival': ['foraging', 'hunting', 'fishing', 'cooking', 'fire-making', 'shelter-building', 'farming', 'tool crafting', 'animal husbandry'],
    'combat': ['melee', 'archery', 'defense', 'tactics', 'martial arts'],
    'crafting': ['woodworking', 'stoneworking', 'metalworking', 'textile crafting', 'pottery', 'building', 'leatherworking'],
    'artisan': ['painting', 'writing', 'sculpting', 'music'],
    'communication': ['bartering', 'leadership', 'teaching', 'diplomacy', 'persuasion'],
    'healing': ['herbalisim', 'first aid', 'surgery', 'midwifery', 'spiritual healing'],
    'mental': ['meditation', 'philosophy', 'spiritual leadership'],
    'exploration': ['navigation', 'cartography', 'swimming', 'climbing'],
    'domestic': ['cleaning', 'child rearing', 'clothing maintenance'],
    'magic': ['elemental', 'divination', 'alchemy', 'enchanting']
}
LEVEL_UP_THRESHOLD = 100
MAX_SKILL_LEVEL = 20

# Possible responses from AI
RESPONSES = ['receptive', 'motive', 'apprehensive', 'refusal']
REWARD_AMOUNT = 1
PENALTY_AMOUNT = 1

# Character Roles
"""
Hunter/Gatherer: Focuses on hunting animals and gathering wild plants for food and resources.
Artist/Entertainer: Engages in creative pursuits, such as music, painting, or storytelling, to boost morale and culture within the community.
Mentor: Imparts knowledge and skills to others, helping to develop the next generation of characters.
Defender: Responsible for protecting the community from threats, such as wild animals or rival tribes.
Diplomat: Skilled in negotiation and conflict resolution, maintaining relationships with other tribes or factions.
Scout/Explorer: Focuses on exploring new areas, gathering information about the environment, and identifying resources or threats.
Leader: Guides the tribe and makes strategic decisions for the community.
Builder: Constructs and improves structures for the community.
Healer: Uses natural remedies and knowledge to heal injuries and illnesses.
Crafter: Creates items using gathered resources, focusing on craftsmanship and skill.
Farmer: Cultivates crops and raises livestock to provide food for the community.
Warrior: Engages in combat to protect the community and defend against threats.
Mage: Utilizes magical abilities to influence the environment or assist the community.
Rogue: Operates stealthily, often engaging in activities that require cunning and agility.
Merchant: Specializes in commerce, buying and selling goods to maximize resources for the community.
"""

# Action Categories
"""
Social: Actions that involve interaction with other characters.
Work: Actions related to job tasks or skill development.
Combat: Actions related to fighting or defense.
Magic: Actions that involve the use of magical abilities.
Crafting: Actions focused on creating items or tools.
Farming: Actions related to cultivating crops and raising livestock.
Mining: Actions focused on extracting resources from the environment.
Exploration: Actions that involve discovering new areas or resources.
Research: Actions that involve studying or gathering knowledge.
"""

# Social Actions
"""
Negotiate Trade: Engage in discussions to exchange goods with other characters or tribes.
Host Gathering: Organize a community event to strengthen social bonds and improve morale.
Resolve Conflict: Mediate disputes between characters to maintain harmony.
Share Stories: Tell tales or share experiences to entertain and educate others.
Form Alliances: Establish partnerships with other characters or tribes for mutual benefit.
"""

# Work Actions
"""
Build Structure: Construct buildings or facilities to improve community infrastructure.
Repair Equipment: Fix broken tools or structures to ensure functionality.
Assist in Tasks: Help other characters with their work to foster teamwork.
Organize Work Schedule: Plan and assign tasks to optimize productivity within the community.
Train Workers: Provide training to improve the skills of other characters in their respective roles.
"""

# Combat Actions
"""
Engage in Battle: Participate in combat to defend the community from threats.
Train in Combat: Practice combat skills to improve proficiency in fighting.
Set Traps: Create traps to catch enemies or wild animals.
Scout Enemy Positions: Gather intelligence on enemy locations and movements.
Defend Territory: Protect the community's borders from intruders or hostile forces.
"""

# Magic Actions
"""
Cast Spell: Use magical abilities to influence the environment or assist allies.
Enchant Item: Imbue an item with magical properties to enhance its effectiveness.
Study Magic: Research magical theories or practices to improve magical skills.
Create Potions: Brew potions that provide various effects, such as healing or enhancement.
Summon Familiar: Call forth a magical creature to assist in tasks or combat.
"""

# Crafting Actions
"""
Create Item: Use resources to craft tools, weapons, or other items.
Upgrade Equipment: Enhance existing items to improve their performance.
Gather Materials: Collect resources needed for crafting.
Design Blueprints: Create plans for new items or structures to guide crafting efforts.
Repair Items: Fix damaged items to restore their functionality.
"""

# Farming Actions
"""
Plant Crops: Sow seeds to grow food for the community.
Harvest Produce: Collect mature crops for consumption or trade.
Tend Livestock: Care for animals to ensure their health and productivity.
Irrigate Fields: Set up systems to provide water to crops for better growth.
Rotate Crops: Change the types of crops grown in a field to maintain soil health.
"""

# Mining Actions
"""
Extract Resources: Mine for minerals, gems, or other valuable materials.
Survey Land: Assess areas for potential mining opportunities.
Refine Materials: Process raw materials into usable forms.
Create Mine Shafts: Construct tunnels or shafts to access deeper resources.
Transport Resources: Move mined materials back to the community for use.
"""

# Exploration Actions
"""
Scout Area: Investigate new territories to gather information about resources or threats.
Map Terrain: Create maps of explored areas for future reference.
Discover Landmarks: Identify significant locations that may benefit the community.
Identify Resources: Locate and document valuable resources in the environment.
Navigate Hazards: Learn to avoid or overcome natural dangers in the wilderness.
"""

# Research Actions
"""
Conduct Experiments: Test theories or ideas to gain new knowledge.
Study Environment: Observe natural phenomena to understand the ecosystem better.
Document Findings: Record discoveries to share with the community or future generations.
Analyze Resources: Investigate the properties of materials to improve crafting techniques.
Develop New Techniques: Innovate new methods for farming, crafting, or combat.
"""
