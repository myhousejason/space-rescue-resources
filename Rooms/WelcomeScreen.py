from GameFrame import Level
from Rooms.WelcomeScreen import WelcomeScreen
class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)