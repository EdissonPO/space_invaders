class Settings:

    def __init__(self):
        """Inicializa la configuración del juego."""
        # Configuración de la pantalla.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (218,214,193)
        self.FPS = 60

        # Configuración de la nave.
        self.ship_speed = 12

        # Configuración de los proyectiles.
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5