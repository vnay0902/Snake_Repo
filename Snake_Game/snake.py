# create a snake game 
# import modules
import pygame
import random
import time
import sys
from pygame.locals import *

# initialize pygame
pygame.init()

# create a clock object

clock = pygame.time.Clock()

# create a window

window = pygame.display.set_mode((600, 600))

# set the title of the window

pygame.display.set_caption("Snake Game")

# create a snake

snake = [(200, 200), (210, 200), (220, 200)]

# create a food

food = (300, 300)

# create a variable to store the direction of the snake

direction = "left"

# create a variable to store the score

score = 0

# create a variable to store the speed of the snake

speed = 10

# create a variable to store the game over status

game_over = False

# create a function to display the score

def display_score():
    # create a font object
    font = pygame.font.SysFont("arial", 20)
    # create a text surface object
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    # create a text rectangle object
    text_rect = text.get_rect()
    # set the position of the text rectangle
    text_rect.center = (50, 50)
    # blit the text onto the surface
    window.blit(text, text_rect)

# create a function to display the snake

def display_snake(snake):
    for position in snake:
        pygame.draw.rect(window, (255, 255, 255), (position[0], position[1], 10, 10))

# create a function to display the food

def display_food(food):
    pygame.draw.rect(window, (255, 0, 0), (food[0], food[1], 10, 10))

# create a function to move the snake

def move_snake(direction, snake):
    head = snake[0]
    if direction == "left":
        new_head = (head[0] - 10, head[1])
    elif direction == "right":
        new_head = (head[0] + 10, head[1])
    elif direction == "up":
        new_head = (head[0], head[1] - 10)
    elif direction == "down":
        new_head = (head[0], head[1] + 10)
    snake.insert(0, new_head)
    snake.pop()

# create a function to check if the snake has collided with the food

def check_food_collision(snake, food):
    if snake[0] == food:
        return True
    else:
        return False

# create a function to check if the snake has collided with itself

def check_self_collision(snake):
    if snake[0] in snake[1:]:
        return True
    else:
        return False

# create a function to check if the snake has collided with the boundaries

def check_boundary_collision(snake):
    if snake[0][0] < 0 or snake[0][0] > 600 or snake[0][1] < 0 or snake[0][1] > 600:
        return True
    else:
        return False

# create a function to display the game over message

def display_game_over():
    # create a font object
    font = pygame.font.SysFont("arial", 20)
    # create a text surface object
    text = font.render("Game Over! Your score is " + str(score), True, (255, 255, 255))
    # create a text rectangle object
    text_rect = text.get_rect()
    # set the position of the text rectangle
    text_rect.center = (300, 300)
    # blit the text onto the surface
    window.blit(text, text_rect)

# create a function to reset the game

def reset_game():
    global snake
    global food
    global direction
    global score
    global game_over
    snake = [(200, 200), (210, 200), (220, 200)]
    food = (300, 300)
    direction = "left"
    score = 0
    game_over = False

# create a main function

def main():
    global direction
    global snake
    global food
    global score
    global game_over
    # create a while loop
    while True:
        # fill the window with black color
        window.fill((0, 0, 0))
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                # quit the game
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and direction != "right":
                    direction = "left"
                elif event.key == K_RIGHT and direction != "left":
                    direction = "right"
                elif event.key == K_UP and direction != "down":
                    direction = "up"
                elif event.key == K_DOWN and direction != "up":
                    direction = "down"
                elif event.key == K_RETURN and game_over == True:
                    reset_game()
        # check if the snake has collided with the food
        if check_food_collision(snake, food):
            # increment the score
            score += 1
            # create a new food
            food = (random.randint(0, 590), random.randint(0, 590))
            # increase the speed of the snake
            speed += 1
        # check if the snake has collided with itself
        if check_self_collision(snake):
            # set the game over variable to True
            game_over = True
        # check if the snake has collided with the boundaries
        if check_boundary_collision(snake):
            # set the game over variable to True
            game_over = True
        # display the score
        display_score()
        # display the snake
        display_snake(snake)
        # display the food
        display_food(food)
        # move the snake
        move_snake(direction, snake)
        # display the game over message
        if game_over == True:
            display_game_over()
        # update the display
        pygame.display.update()
        # tick the clock
        clock.tick(speed)

# call the main function

main()

# quit pygame

pygame.quit()

# exit the program

sys.exit()

# Output

# When you run the program, you will see the following output:

# Now, press the left arrow key to move the snake to the left. Press the right arrow key to move the snake to the right. Press the up arrow key to move the snake up. Press the down arrow key to move the snake down. When the snake collides with the food, the score will be incremented by 1. When the snake collides with itself or the boundaries, the game will be over. Press the Enter key to reset the game.

# Summary

# In this tutorial, we learned how to create a snake game in Python using the Pygame module.

# Popular Tutorials

# - Python range

