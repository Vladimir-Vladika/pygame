import pygame
import sys

from settings import *
from snake import Snake
from food import Food
from score import Score


class Game:
    """
    Главный класс игры.
    Управляет:
    - змейкой
    - едой
    - счетом
    - игровым циклом
    """

    def __init__(self):

        # Создаем окно
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption("Snake")


        # Создаем объекты игры
        self.snake = Snake()
        self.food = Food()
        self.score = Score()


        # Игровые часы
        self.clock = pygame.time.Clock()



    def run(self):
        """
        Главный цикл игры.
        """

        while True:

            self.events()

            self.update()

            self.draw()

            self.clock.tick(FPS)



    def events(self):
        """
        Обработка событий и управления.
        """

        for event in pygame.event.get():

            # Закрытие окна
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()



            # Управление змейкой
            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_UP:

                    self.snake.change_direction(
                        (0, -1)
                    )


                elif event.key == pygame.K_DOWN:

                    self.snake.change_direction(
                        (0, 1)
                    )


                elif event.key == pygame.K_LEFT:

                    self.snake.change_direction(
                        (-1, 0)
                    )


                elif event.key == pygame.K_RIGHT:

                    self.snake.change_direction(
                        (1, 0)
                    )




    def update(self):
        """
        Обновление логики игры.
        """

        # Двигаем змейку
        self.snake.move()



        # Проверяем, съела ли змейка еду

        if self.snake.body[0] == self.food.position:

            self.snake.grow_up()

            self.food.randomize()

            self.score.increase()



        # Проверяем столкновение со стеной

        if self.snake.check_wall_collision():

            self.game_over()



        # Проверяем столкновение с собой

        if self.snake.check_self_collision():

            self.game_over()




    def draw(self):
        """
        Отрисовка всех объектов.
        """

        # Очистка экрана
        self.screen.fill(BLACK)



        # Рисуем еду
        self.food.draw(
            self.screen
        )



        # Рисуем змейку
        self.snake.draw(
            self.screen
        )



        # Рисуем счет
        self.score.draw(
            self.screen
        )



        # Обновляем экран
        pygame.display.update()




    def game_over(self):
        """
        Завершение игры.
        """

        pygame.quit()

        sys.exit()