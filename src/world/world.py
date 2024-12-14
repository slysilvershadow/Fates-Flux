# world.py

from ..utils import constants as con 

biome = con.BIOMES
print(str(biome))

class World:
    """
    Represents the game world, managing entities and their interactions.

    Attributes:
        entities (dict): A dictionary to hold all entities in the world.
        systems (list): A list of systems that operate within the world.
        next_entity_id (int): The ID to assign to the next entity created.
    """
    def __init__(self):
        """
        Initialize a new world with an empty entity dictionary and system list.
        """
        self.entities = {}
        self.systems = []
        self.next_entity_id = 0
    
    def create_entity(self):
        """
        Create a new entity and add it to the world.

        Returns:
            Entity: The newly created entity.
        """
        entity = Entity(self.next_entity_id)
        self.entities[self.next_entity_id] = entity
        self.next_entity_id += 1
        return entity
