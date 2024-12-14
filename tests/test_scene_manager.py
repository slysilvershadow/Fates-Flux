import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

"""
test_scene_manager.py

This script tests the functionality of the scene manager.
"""

from utils.scene_manager import load_scene, switch_scene, unload_scene

def test_scene_management():
    print("Testing Scene Management...")
    
    # Load initial scene
    load_scene("Main Menu")
    
    # Switch to another scene
    switch_scene("Game Scene")
    
    # Unload the current scene
    unload_scene()

if __name__ == "__main__":
    test_scene_management()
