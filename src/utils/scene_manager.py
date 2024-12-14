"""
scene_manager.py

This module manages the different scenes in the application.
"""

class Scene:
    """
    Represents a scene in the application.
    """
    def __init__(self, name):
        self.name = name

    def initialize(self):
        """
        Initialize the scene.
        """
        print(f"Initializing scene: {self.name}")

    def cleanup(self):
        """
        Cleanup the scene.
        """
        print(f"Cleaning up scene: {self.name}")

current_scene = None

def load_scene(scene_name):
    """
    Load a specific scene by name.

    Parameters:
        scene_name (str): The name of the scene to load.
    """
    global current_scene
    if current_scene:
        current_scene.cleanup()
    
    current_scene = Scene(scene_name)
    current_scene.initialize()

def switch_scene(scene_name):
    """
    Switch to a different scene.

    Parameters:
        scene_name (str): The name of the scene to switch to.
    """
    print(f"Switching to scene: {scene_name}")
    load_scene(scene_name)

def unload_scene():
    """
    Unload the current scene.
    """
    global current_scene
    if current_scene:
        current_scene.cleanup()
        current_scene = None
        print("Current scene unloaded.")
