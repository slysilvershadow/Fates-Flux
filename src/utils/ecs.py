# ecs.py

import uuid

class Entity:
    """
    Represents an entity in the game, which can have multiple components.

    Attributes:
        id (UUID): A unique identifier for the entity.
        components (dict): A dictionary to hold the components associated with the entity.
    """
    def __init__(self):
        """
        Initialize a new entity with a unique identifier and an empty component dictionary.
        """
        self.id = uuid.uuid4()
        self.components = {}

    def add_component(self, component):
        """
        Add a component to the entity.

        Parameters:
            component (Component): The component to add to the entity.
        """
        component_type = type(component).__name__  # Get the component type name
        if component_type not in self.components:
            self.components[component_type] = (set(), 0)  # Initialize a new set and count
        component_set, count = self.components[component_type]
        component_set.add(component)  # Add the component instance to the set
        self.components[component_type] = (component_set, count + 1)  # Increment the count

    def get_component(self, component_type):
        """
        Retrieve a component of a specific type from the entity.

        Parameters:
            component_type (type): The type of the component to retrieve.

        Returns:
            Component or None: The requested component if it exists, otherwise None.
        """
        return self.components.get(component_type, None)

    def remove_component(self, component_type):
        """
        Remove a component of a specific type from the entity.

        Parameters:
            component_type (type): The type of the component to remove.
        """
        if component_type in self.components:
            del self.components[component_type]

    def use_component(self, component):
        """
        Placeholder method for using a component.

        Parameters:
            component (Component): The component to use.
        """
        pass

class Component:
    """
    Represents a component that can be added to an entity.

    Attributes:
        id (UUID): A unique identifier for the component.
    """
    def __init__(self):
        """
        Initialize a new component with a unique identifier.
        """
        self.id = uuid.uuid4()

class System:
    """
    Represents a system that manages entities and their components.
    """
    def __init__(self):
        self.entities = []

    def add_entity(self, entity, required_components: List[type] = None):
        """
        Add an entity to the system if it meets the required components.

        Parameters:
            entity (Entity): The entity to add.
            required_components (List[type]): A list of component types that the entity must have.
        """
        if required_components is None:
            required_components = []
        if self.filter(entity, required_components):
            self.entities.append(entity)

    def remove_entity(self, entity):
        """
        Remove an entity from the system.

        Parameters:
            entity (Entity): The entity to remove.
        """
        if entity in self.entities:
            self.entities.remove(entity)

    def filter(self, entity: Entity, required_components: List[type]) -> bool:
        """
        Check if an entity has the required components.

        Parameters:
            entity (Entity): The entity to check.
            required_components (List[type]): A list of component types that must be present.

        Returns:
            bool: True if the entity has all required components, otherwise False.
        """
        for component in required_components:
            if entity.get_component(component) is None:
                return False
        return True

class EntityManager:
    """
    Manages the creation and removal of entities in the game.
    """
    def __init__(self):
        """
        Initialize a new entity manager to create and manage entities.

        Attributes:
            entities (dict): A dictionary to store entities by their unique identifier.
        """
        self.entities = {}

    def create_entity(self):
        """
        Create a new entity and store it in the manager.

        Returns:
            Entity: The newly created entity.
        """
        entity = Entity()
        self.entities[entity.id] = entity
        return entity

    def remove_entity(self, entity_id):
        """
        Remove an entity from the manager by its unique identifier.

        Parameters:
            entity_id (UUID): The unique identifier of the entity to remove.
        """
        if entity_id in self.entities:
            del self.entities[entity_id]

class SystemManager:
    """
    Manages multiple systems in the game.
    """
    def __init__(self):
        """
        Initialize a new system manager to manage multiple systems.

        Attributes:
            systems (list): A list of systems registered with the manager.
        """
        self.systems = []

    def add_system(self, system):
        """
        Register a system with the manager.

        Parameters:
            system (System): The system to register.
        """
        self.systems.append(system)

    def update(self, entities, dt):
        """
        Update all systems with the relevant entities.

        Parameters:
            entities (list): A list of entities to update.
            dt (float): The time delta since the last update.
        """
        for system in self.systems:
            for entity in entities:
                if entity not in system.entities:
                    system.add_entity(entity)
                # No need to recheck `filter` if already removed.
            system.update(dt)
