import pygame
pygame.init()

class Player(object):
    def __init__(self, x,y, rectWidth, rectHeight):
        self.x = x
        self.y = y
        self.width = rectWidth
        self.height = rectHeight
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.jumpStart = 0
        self.standing = True
        self.hitbox = (self.x + 16, self.y + 10, 29, 52)

    def Draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.right:
                window.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

            elif self.left:
                window.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))

            elif self.left:
                window.blit(walkLeft[0], (self.x, self.y))
            else:
                window.blit(char, (self.x, self.y))
        self.hitbox = (self.x + 16, self.y + 10, 29, 52)

pygame.quit()