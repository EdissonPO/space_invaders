import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una clase para gestionar proyectiles disparados desde la nave."""

    def __init__(self, ai_game):
        """Crea un objeto para el proyectil en la posición actual de la nave."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crea un rectángulo para el proyectil en (0, 0) y luego establece la posición correcta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Almacena la posición del proyectil como un valor decimal.
        self.y = float(self.rect.y)

    def update(self):
        """Mueve el proyectil hacia arriba de la pantalla."""
        # Actualiza la posición decimal del proyectil.
        self.y -= self.settings.bullet_speed
        # Actualiza la posición del rectángulo.
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibuja el proyectil en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)