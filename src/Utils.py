from random import randrange

import pygame.display
import pygame.draw

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500 
ROWS = 20

def initWindow():
    win = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_icon(pygame.image.load('Icons/SnakeIcon.png'))
    pygame.display.set_caption('Snake Game')
    return win

def drawGrid(surface) -> None:
    z = SCREEN_HEIGHT // ROWS

    x = 0
    y = 0

    for i in range(20):
        x += z
        y += z
        
        pygame.draw.line(surface, (100, 100, 100), (x,0),(x,SCREEN_WIDTH))
        pygame.draw.line(surface, (100, 100, 100), (0,y),(SCREEN_HEIGHT,y))

def update(surface, snake, snack) -> None:
    surface.fill((0, 0, 0))
    snake.draw()
    snack.draw(surface)
    drawGrid(surface)
    pygame.display.update()

def randomSnack(rows, snake) -> tuple:
    positions = snake.body

    validPos = False
    while not validPos:
        x = randrange(rows)
        y = randrange(rows)

        if len(list(filter(lambda z:z.pos == (x,y), positions))) == 0:
            validPos = True
    
    return (x, y)


class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
        # TODO: eliminar lo siguiente si no lo utilizamos
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, selected):
		if selected:
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size):
    return pygame.font.Font("fonts/8-BIT WONDER.TTF", size)

def getHighestScore():
    with open('data/playerInfo.txt', 'r') as file:
        score = int(file.readline())
        file.close()
    return score

def actualizeHighestScore(score):
    with open('data/playerInfo.txt', 'r+') as file:
        highestScore = int(file.readline())
        if score > highestScore:
            file.seek(0)
            file.write(str(score))
    file.close()
        
