import pygame
import sys

from settings import *
from snake import Snake
from food import Food
from score import Score


class Game:

    def __init__(self):

        # Создаем окно
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption("Snake")


        # Игровые объекты
        self.snake = Snake()
        self.food = Food()
        self.score = Score()


        # Направление движения
        self.direction = "RIGHT"


        # Игровые часы
        self.clock = pygame.time.Clock()



    def run(self):

        """
        Главный игровой цикл
        """

        while True:

            self.events()

            self.update()

            self.draw()

            self.clock.tick(FPS)



    def events(self):

        """
        Обработка нажатий клавиш
        """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_UP:
                    if self.direction != "DOWN":
                        self.direction = "UP"



                elif event.key == pygame.K_DOWN:
                    if self.direction != "UP":
                        self.direction = "DOWN"



                elif event.key == pygame.K_LEFT:
                    if self.direction != "RIGHT":
                        self.direction = "LEFT"



                elif event.key == pygame.K_RIGHT:
                    if self.direction != "LEFT":
                        self.direction = "RIGHT"





    def update(self):

        """
        Обновление состояния игры
        """

        # двигаем змейку
        self.snake.move(
            self.direction
        )



        # проверяем еду

        if self.snake.body[0] == self.food.position:

            self.snake.grow()

            self.food.randomize()

            self.score.increase()



        # проверяем столкновение со стеной

        head = self.snake.body[0]


        if (
            head[0] < 0 or
            head[0] >= WIDTH or
            head[1] < 0 or
            head[1] >= HEIGHT
        ):

            self.game_over()



        # проверяем столкновение с собой

        if head in self.snake.body[1:]:

            self.game_over()




    def draw(self):

        """
        Отрисовка игры
        """


        self.screen.fill(BLACK)


        self.food.draw(
            self.screen
        )


        self.snake.draw(
            self.screen
        )


        self.score.draw(
            self.screen
        )


        pygame.display.update()




    def game_over(self):

        """
        Завершение игры
        """

        pygame.quit()

        sys.exit()