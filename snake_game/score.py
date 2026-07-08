import pygame

from settings import *


class Score:
    """
    Отвечает за отображение количества очков.
    """

    def __init__(self):
        pygame.font.init()

        self.score = 0

        self.font = pygame.font.SysFont(
            "Arial",
            30
        )

    def increase(self):
        """
        Увеличивает счет.
        """

        self.score += 1

    def draw(self, screen):
        """
        Рисует счет.
        """

        text = self.font.render(
            f"Score: {self.score}",
            True,
            WHITE
        )

        screen.blit(text, (10, 10))