# skills.py

class Skill:
    """
    Represents a skill that a character can possess in the game.

    Attributes:
        name (str): The name of the skill.
        lvl (int): The current level of the skill.
        exp (float): The current experience points for the skill.
        max_lvl (int): The maximum level a skill can reach.
    """
    def __init__(self, name: str, group: str, lvl: int = 0, exp: float = 0.0, max_lvl: int = 20):
        """
        Initialize a skill object.

        Parameters:
            name (str): The name of the skill.
            group (str): The category that the skill belongs to.
            lvl (int): The current level of the skill.
            exp (float): The current experience points for the skill.
            max_lvl (int): The maximum level a skill can reach.
        """
        self.name: str = name
        self.lvl: int = lvl
        self.exp: float = exp
        self.max_lvl: int = max_lvl

    def add_exp(self, amount: float) -> float:
        """
        Add experience points and check if the skill should level up or down.

        This method adds the specified amount of experience points to the skill. 
        If the experience points drop below zero, it levels down the skill. 
        If the experience points reach the threshold for the next level, it levels up the skill.

        Parameters:
            amount (float): The amount of experience to add.

        Returns:
            float: The updated experience points.
        """
        self.exp += amount

        while self.exp < 0 and self.lvl > 0:
            self.exp += self.exp_to_next_lvl()
            self.lvl_down()

        while self.lvl < self.max_lvl and self.exp >= self.exp_to_next_lvl():
            self.exp -= self.exp_to_next_lvl()
            self.lvl_up()

        return self.exp

    def exp_to_next_lvl(self) -> int:
        """
        Calculate the experience points required to reach the next level.

        Returns:
            int: The experience points required for the next level.
        """
        return 100 * (self.lvl + 1)

    def lvl_up(self) -> None:
        """
        Level up the skill if the current level is less than the maximum level.
        """
        if self.lvl < self.max_lvl:
            self.lvl += 1
            print(f"{self.name} leveled up to level {self.lvl}!")

    def lvl_down(self) -> None:
        """
        Level down the skill if the current level is greater than 0.
        """
        if self.lvl > 0:
            self.lvl -= 1
            print(f"{self.name} leveled down to level {self.lvl}!")
        else:
            pass
