class Settings():
    def __init__(self):
        # screen settings
        self.screen_width = 1300
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # ship settings
        self.ship_moving_factor = 2.5

        # bullet settings
        self.bullet_color = (0, 0, 0)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 1.5

        # setting the limit of bullets allowed at one time in screen
        self.bullets_allowed = 3
