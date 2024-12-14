# Window
class Window:
    def __init__(self):
        self.DEVICE_WIDTH = pygame.display.Info().current_w
        self.DEVICE_HEIGHT = pygame.display.Info().current_h
        self.DESIGN_WIDTH = 1080
        self.DESIGN_HEIGHT = 1920
        self.SCALE_X = self.DEVICE_WIDTH / self.DESIGN_WIDTH
        self.SCALE_Y = self.DEVICE_HEIGHT / self.DESIGN_HEIGHT
        self.FPS = 60

    def scale_position(self, x, y):
        return(x  * self.SCALE_X , y * self.SCALE_Y)

    def scale_size(self, width, height):
        scale_width = width * self.SCALE_X
        scale_height = height * self.SCALE_Y
        return(scale_width, scale_height)