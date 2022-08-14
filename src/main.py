import sys

import pygame

import Utils
from Cube import Cube
from Snake import Snake
from Utils import ROWS, Button


def menu(window) -> None:
    pygame.display.set_caption('Game Menu')
    clock = pygame.time.Clock()

    cursor = 0
    while True:
        pygame.time.delay(50)
        clock.tick(10)

        menuText = Utils.get_font(45).render('MAIN MENU', True, 'White')
        menuPanel = menuText.get_rect(center=(250, 100))

        starIcon = pygame.image.load('icons/StarIcon.png')
        trophyPanel = starIcon.get_rect(center=(480, 20))
        window.blit(starIcon, trophyPanel)

        highestScore = Utils.get_font(15).render(str(Utils.getHighestScore()), False, 'White')
        highestScorePanel = menuText.get_rect(center=(677, 55))
        window.blit(highestScore, highestScorePanel)

        playButton = Button(image=None, pos=(250, 200), text_input='PLAY', font=Utils.get_font(45), base_color='Grey', hovering_color='White')
        leaderboardButton = Button(image=None, pos=(250, 300), text_input='LEADERBOARD', font=Utils.get_font(42), base_color='Grey', hovering_color='White')
        quitButton = Button(image=None, pos=(250, 400), text_input='QUIT', font=Utils.get_font(45), base_color='Grey', hovering_color='White')

        buttons = [playButton, leaderboardButton, quitButton]
        options = [game, showLeaderboard, quitGame]

        window.blit(menuText, menuPanel)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                cursor = (cursor + 1 ) % len(buttons)
            elif keys[pygame.K_UP]:
                if cursor == 0: cursor = len(buttons) - 1
                else: cursor -= 1
            elif keys[pygame.K_RETURN]:
                options[cursor](window)


        for i, button in list(enumerate(buttons)):
            if i == cursor: button.changeColor(True)
            else: button.changeColor(False)
            button.update(window)
        
        pygame.display.update()


def game(window) -> None:
    pygame.display.set_caption('Score: 0')

    clock = pygame.time.Clock()

    snake = Snake((10, 10), (255, 0, 0), window)

    snack = Cube(Utils.randomSnack(ROWS, snake), color=(0,255,0))

    quit = False
    lost = False

    while not quit and not lost:
        pygame.time.delay(50)
        clock.tick(10)
        
        quit = snake.move() 
        if snake.head.pos == snack.pos:
            snake.addCube()
            pygame.display.set_caption('Score: ' + str(len(snake.body) - 1))
            snack = Cube(Utils.randomSnack(ROWS, snake), color=(0,255,0))

        lost = snake.hasEatenItself()

        Utils.update(window, snake, snack)
    if quit:
        quitGame(window)
    Utils.actualizeHighestScore(len(snake.body) - 1)

def showLeaderboard(window) -> None:
    window.fill((0, 0, 0))

    text = Utils.get_font(45).render('COMING SOON', True, 'White')
    textPanel = text.get_rect(center=(255, 255))
    window.blit(text, textPanel)
    pygame.display.update()
    pygame.time.delay(1000)
    window.fill((0, 0, 0))


def quitGame(window) -> None:
    pygame.quit()
    sys.exit() 



def main():
    # TODO: intentar usar Singleton para controlar el número de ventanas
    pygame.init()
    win = Utils.initWindow()
    menu(win)


        

if __name__ == '__main__':
    main()

