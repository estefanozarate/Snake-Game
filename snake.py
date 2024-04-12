import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
cell_size = 20
fps = 10

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('SNAKE')

clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.snake_length = 1
        self.snake_list = []
        self.direction = "RIGHT"
        self.head = [screen_width / 2, screen_height / 2]

    def move(self):
        if self.direction == "UP":
            self.head[1] -= cell_size
        elif self.direction == "DOWN":
            self.head[1] += cell_size
        elif self.direction == "LEFT":
            self.head[0] -= cell_size
        elif self.direction == "RIGHT":
            self.head[0] += cell_size
        if self.head[0] >= screen_width:
            self.head[0] = 0
        elif self.head[0] < 0:
            self.head[0] = screen_width - cell_size
        elif self.head[1] >= screen_height:
            self.head[1] = 0
        elif self.head[1] < 0:
            self.head[1] = screen_height - cell_size

        self.snake_list.append(list(self.head))
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def draw(self):
        for segment in self.snake_list:
            pygame.draw.rect(screen, green, pygame.Rect(segment[0], segment[1], cell_size, cell_size))

    def check_collision(self):
        for segment in self.snake_list[:-1]:
            if segment == self.head:
                return True
        return False

    def increase_length(self):
        self.snake_length += 1
class Apple:
    def __init__(self):
        self.position = [random.randrange(1, (screen_width // cell_size)) * cell_size,
                         random.randrange(1, (screen_height // cell_size)) * cell_size]

    def draw(self):
        pygame.draw.rect(screen, red, pygame.Rect(self.position[0], self.position[1], cell_size, cell_size))

def main():
    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
        screen.fill(black)
        snake.move()
        snake.draw()
        apple.draw()
        if snake.head == apple.position:
            apple.position = [random.randrange(1, (screen_width // cell_size)) * cell_size,
                              random.randrange(1, (screen_height // cell_size)) * cell_size]
            snake.increase_length()

        if snake.check_collision():
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
