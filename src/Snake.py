from operator import truediv
from xmlrpc.client import Boolean

import pygame

from Cube import Cube


class Snake:
    def __init__(self, pos, color, surface) -> None:
        self.body = []
        self.turns = {}
        self.head = Cube(pos)
        self.body.append(self.head)
        self.xVel = 1
        self.yVel = 0 
        self.color = color
        self.surface = surface

    def addCube(self) -> None:
        tail = self.body[-1]
        vX, vY = tail.xVel, tail.yVel

        if vX == 1 and vY == 0:
            self.body.append(Cube((tail.pos[0]-1,tail.pos[1])))
        elif vX == -1 and vY == 0:
            self.body.append(Cube((tail.pos[0]+1,tail.pos[1])))
        elif vX == 0 and vY == 1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]-1)))
        elif vX == 0 and vY == -1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]+1)))
        
        self.body[-1].xVel = vX
        self.body[-1].yVel = vY


    def move(self) -> Boolean:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                keys = pygame.key.get_pressed()
                for key in keys:  # Loop through all the keys
                    if keys[pygame.K_LEFT] and self.xVel != 1:
                        self.xVel = -1
                        self.yVel = 0
                        self.turns[self.head.pos] = [self.xVel, self.yVel]
                        
                    elif keys[pygame.K_RIGHT] and self.xVel != -1:
                        self.xVel = 1
                        self.yVel = 0
                        self.turns[self.head.pos] = [self.xVel, self.yVel]

                    elif keys[pygame.K_UP] and self.yVel != 1:
                        self.xVel = 0
                        self.yVel = -1
                        self.turns[self.head.pos] = [self.xVel, self.yVel]

                    elif keys[pygame.K_DOWN] and self.yVel != -1:
                        self.xVel = 0
                        self.yVel = 1
                        self.turns[self.head.pos] = [self.xVel, self.yVel]

        self.turn()
        return False

    def turn(self) -> None:
        for i, c in enumerate(self.body):  # Loop through every cube in our body
            p = c.pos  # This stores the cubes position on the grid
            if p in self.turns:  # If the cubes current position is one where we turned
                turn = self.turns[p]  # Get the direction we should turn
                c.move(turn[0], turn[1])  # Move our cube in that direction
                if i == len(self.body) - 1:  # If this is the last cube in our body remove the turn from the dict
                    self.turns.pop(p)
            else:  # If we are not turning the cube
                # If the cube reaches the edge of the screen we will make it appear on the opposite side
                if c.xVel == -1 and c.pos[0] <= 0: c.pos = (20 - 1, c.pos[1])
                elif c.xVel == 1 and c.pos[0] >= 20 -1: c.pos = (0, c.pos[1])
                elif c.yVel == 1 and c.pos[1] >= 20 -1: c.pos = (c.pos[0], 0)
                elif c.yVel == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], 20 - 1)
                else: c.move(c.xVel, c.yVel)  # If we haven't reached the edge just move in our current direction

    def hasEatenItself(self) -> Boolean:
        for x in range(len(self.body)):
            if self.body[x].pos in list(map(lambda z:z.pos, self.body[x+1:])): # This will check if any of the positions in our body list overlap
                return True
        return False


    def draw(self) -> None:
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(self.surface, eyes=True)
            else:
                c.draw(self.surface)  

