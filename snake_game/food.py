import random
import pygame

from settings import *


class Food:
    """
    Класс Food отвечает за:
    - случайное появление яблока;
    - хранение его координат;
    - отрисовку.
    """

    def __init__(self):
        self.position = (0, 0)
        self.randomize()

    def randomize(self):
        """
        Генерирует новую случайную позицию.
        """

        self.position = (
            random.randint(0, COLS - 1),
            random.randint(0, ROWS - 1)
        )

    def draw(self, screen):
        """
        Рисует яблоко.
        """

        x, y = self.position

        rect = pygame.Rect(
            x * CELL_SIZE,
            y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )

        pygame.draw.rect(
            screen,
            RED,
            rect
        )