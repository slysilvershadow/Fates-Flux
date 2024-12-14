"""
Main entry point for the application.

This file initializes the Kivy application, sets up the screen manager,
and imports the game loop and game state modules.
"""
import pygame
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import game_loop  
from kivy.graphics import Rectangle
import game_state  

class MainApp(App):
    """
    Main application class that manages the screens of the game.
    """
    def build(self):
        """
        Build the application interface by creating the ScreenManager
        and adding the main menu and game screens.
        """
        # Create the ScreenManager
        self.screen_manager = ScreenManager()

        # Add screens to the ScreenManager
        self.screen_manager.add_widget(Screen(name='main_menu'))
        self.screen_manager.add_widget(Screen(name='game'))

        return self.screen_manager

if __name__ == '__main__':
    MainApp().run()

class PygameWidget(Image):
    """
    Custom widget that integrates Pygame with Kivy for rendering.
    """
    def __init__(self, **kwargs):
        """
        Initialize the PygameWidget and set up Pygame.
        """
        super().__init__(**kwargs)
        self.init_pygame()
        Clock.schedule_interval(self.update_pygame, 1 / 60.0)

    def init_pygame(self):
        """Initialize Pygame and set up the display."""
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

    def update_pygame(self, dt):
        """Update the Pygame display and handle game logic."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Here you can add your game drawing logic
        # For example, drawing a simple rectangle
        pygame.draw.rect(self.screen, (255, 0, 0), (50, 50, 100, 100))

        # Update the texture for the Kivy Image
        self.texture = Texture.create(size=(self.width, self.height))
        self.texture.blit_buffer(pygame.image.tostring(self.screen, 'RGBA', True), colorfmt='rgba', bufferfmt='ubyte')
        self.canvas.before.clear()
        with self.canvas.before:
            Rectangle(texture=self.texture, pos=self.pos, size=self.size)
import pygame
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import game_loop  
from kivy.graphics import Rectangle
import game_state  

class MainApp(App):
    def build(self):
        # Create the ScreenManager
        self.screen_manager = ScreenManager()

        # Add screens to the ScreenManager
        self.screen_manager.add_widget(Screen(name='main_menu'))
        self.screen_manager.add_widget(Screen(name='game'))

        return self.screen_manager

if __name__ == '__main__':
    MainApp().run()

class PygameWidget(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_pygame()
        Clock.schedule_interval(self.update_pygame, 1 / 60.0)

    def init_pygame(self):
        """Initialize Pygame and set up the display."""
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

    def update_pygame(self, dt):
        """Update the Pygame display and handle game logic."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Here you can add your game drawing logic
        # For example, drawing a simple rectangle
        pygame.draw.rect(self.screen, (255, 0, 0), (50, 50, 100, 100))

        # Update the texture for the Kivy Image
        self.texture = Texture.create(size=(self.width, self.height))
        self.texture.blit_buffer(pygame.image.tostring(self.screen, 'RGBA', True), colorfmt='rgba', bufferfmt='ubyte')
        self.canvas.before.clear()
        with self.canvas.before:
            Rectangle(texture=self.texture, pos=self.pos, size=self.size)
