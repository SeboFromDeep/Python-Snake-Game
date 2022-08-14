import pygame


class Cube:
    def __init__(self, start, xVel=1, yVel=0, color=(255, 0, 0)) -> None:
        self.pos = start
        self.xVel = xVel
        self.yVel = yVel
        self.color = color
        pass

    def move(self, xVel, yVel) -> None:
        self.xVel = xVel
        self.yVel = yVel
        self.pos = (self.pos[0] + self.xVel, self.pos[1] + self.yVel)  # change our position  
 
    def draw(self, surface, eyes=False) -> None:
        dis = 500 // 20  # Width/Height of each cube
        i = self.pos[0] # Current row
        j = self.pos[1] # Current Column

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        # By multiplying the row and column value of our cube by the width and height of each cube we can determine where to draw it
        
        if eyes: # Draws the eyes
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
