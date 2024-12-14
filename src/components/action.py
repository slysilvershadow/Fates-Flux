# actions.py
from typing import Dict, Optional, List
from .skills import Skill

class Action:
    """
    Represents an action that can be performed by a character in the game.

    Attributes:
        name (str): The name of the action.
        skill_impacts (dict): A dictionary mapping skill names to experience points.
        requirements (list): A list of requirements needed to perform the action.
    """
    def __init__(self, name: str, skill_impacts: Optional[Dict[str, int]] = None, requirements: Optional[List[str]] = None):
        """
        Initialize an action object.

        Parameters:
        - name (str): The name of the action.
        - skill_impacts (dict): A dictionary mapping skill names to experience points.
        """
        self.name: str = name
        self.skill_impacts: Dict[str, int] = skill_impacts or {}
        self.requirements: List[str] = requirements or []

    def apply(self, character_skills: Dict[str, 'Skill']) -> None:
        """
        Apply the action's impact to the character's skills.

        Parameters:
        - character_skills (dict): A dictionary of the character's skills, where keys are skill names, and values are Skill objects.
        
        This method checks if the skill already exists in the character's skills. If it does, it adds experience points to that skill. 
        If the skill does not exist, it unlocks a new skill and adds experience points to it.
        """
        for skill_name, exp in self.skill_impacts.items():
            # Check if the skill already exists in the character's skills
            if skill_name in character_skills:
                character_skills[skill_name].add_exp(exp)
                print(f"{self.name} added {exp} experience to {skill_name}.")
            else:
                # Unlock new skill
                new_skill = Skill(name=skill_name, group='default')
                character_skills[skill_name] = new_skill
                new_skill.add_exp(exp)  # Add exp to the newly gained skill
                print(f"{self.name} unlocked {skill_name} and added {exp} experience points to it.")
