import pygame
from settings import *


class Snake:
    """
    Класс Snake отвечает за:
    - хранение тела змейки
    - движение
    - рост
    - отрисовку
    """

    def __init__(self):
        # Начальное тело змейки
        self.body = [
            (10, 10),
            (9, 10),
            (8, 10)
        ]

        # Начальное направление
        self.direction = (1, 0)

        # Нужно ли увеличить длину
        self.grow = False

    def move(self):
        """
        Перемещение змейки.
        """

        head_x, head_y = self.body[0]

        dx, dy = self.direction

        new_head = (
            head_x + dx,
            head_y + dy
        )

        # Добавляем новую голову
        self.body.insert(0, new_head)

        # Если еду не съели — удаляем хвост
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        """
        Меняет направление движения.
        Запрещаем разворот на 180 градусов.
        """

        dx, dy = self.direction

        new_dx, new_dy = new_direction

        if (dx + new_dx, dy + new_dy) != (0, 0):
            self.direction = new_direction

    def grow_up(self):
        """
        Увеличивает длину змейки.
        """

        self.grow = True

    def draw(self, screen):
        """
        Рисует змейку.
        """

        for x, y in self.body:

            rect = pygame.Rect(
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(
                screen,
                GREEN,
                rect
            )

    def check_self_collision(self):
        """
        Проверяет столкновение головы
        с собственным телом.
        """

        return self.body[0] in self.body[1:]

    def check_wall_collision(self):
        """
        Проверяет столкновение со стенами.
        """

        x, y = self.body[0]

        if x < 0:
            return True

        if x >= COLS:
            return True

        if y < 0:
            return True

        if y >= ROWS:
            return True

        return False