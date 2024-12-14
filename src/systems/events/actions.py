# actions.py

class Interaction:
    """
    Represents an interaction between entities in the game.

    Attributes:
        entity_a (Entity): The first entity involved in the interaction.
        entity_b (Entity): The second entity involved in the interaction.
    """
    def __init__(self, entity_a, entity_b):
        """
        Initialize a new interaction between two entities.

        Parameters:
            entity_a (Entity): The first entity involved in the interaction.
            entity_b (Entity): The second entity involved in the interaction.
        """
        self.entity_a = entity_a
        self.entity_b = entity_b

    def check_viable_actions(self):
        """
        Check if the interaction between the two entities is viable.

        Returns:
            bool: True if the interaction is viable, otherwise False.
        """
        # Placeholder for actual viability check logic
        return True

    def trigger_action(self):
        """
        Trigger the action associated with the interaction.

        Returns:
            str: A message indicating the result of the action.
        """
        # Placeholder for action triggering logic
        return f"Interaction between {self.entity_a} and {self.entity_b} triggered."

    def perform_interaction(self):
        """
        Perform the interaction between the two entities.

        Returns:
            str: A message indicating the outcome of the interaction.
        """
        if self.check_viable_actions():
            return self.trigger_action()
        else:
            return "Interaction is not viable."
