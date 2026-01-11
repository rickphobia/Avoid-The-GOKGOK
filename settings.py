class Setting:
    """a class to store settings"""

    def __init__(self):
        self.width = 0
        self.length = 0
        self.bg_color = (250,250,250)


        self.ship_limit = 3
        
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,0)
        self.bullet_ammount = 10
        self.game_level = 1

        self.speedup_scale = 1.01

        self._initialize_dynamic_settings()

        


    def _initialize_dynamic_settings(self):
        self.points_count = 0
        self.alien_points = 50 
        
        self.alien_speed_x = 2
        self.alien_speed_y = 6
        # 1 = right, -1 = left 
        self.alien_dir_x = 1 
        self.alien_dir_y = 1 
        self.game_level = 1 
    
        self.ship_speed = 300


    def increase_speed(self):
        self.alien_speed_x *= self.speedup_scale
        self.alien_speed_y *= (self.speedup_scale+1)
        self.game_level += 1 
        self.alien_points += 20


