import pygame
import sys

from settings import *
from snake import Snake
from food import Food
from score import Score


# Инициализация Pygame
pygame.init()


# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


# Игровые часы
clock = pygame.time.Clock()


# Создаем объекты игры
snake = Snake()
food = Food()
score = Score()


# Направление движения
direction = "RIGHT"


def game_over():
    """
    Функция завершения игры
    """
    font = pygame.font.Font(None, 50)

    text = font.render(
        "GAME OVER",
        True,
        RED
    )

    text_rect = text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    screen.blit(text, text_rect)

    pygame.display.update()

    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()



# Главный игровой цикл
while True:

    # Обработка событий
    for event in pygame.event.get():

        # Закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # Управление змейкой
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Движение змейки
    snake.move(direction)

    # Проверка съедания еды
    if snake.body[0] == food.position:

        snake.grow()

        food.randomize()

        score.increase()



    # Проверка столкновения со стеной
    head = snake.body[0]

    if (
        head[0] < 0 or
        head[0] >= WIDTH or
        head[1] < 0 or
        head[1] >= HEIGHT
    ):
        game_over()



    # Проверка столкновения с собой
    if head in snake.body[1:]:

        game_over()



    # Отрисовка экрана
    screen.fill(BLACK)


    # Рисуем еду
    food.draw(screen)


    # Рисуем змейку
    snake.draw(screen)


    # Рисуем счет
    score.draw(screen)


    # Обновление экрана
    pygame.display.update()


    # Скорость игры
    clock.tick(FPS)