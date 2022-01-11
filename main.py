import pygame

pygame.init()

screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('deez nuts')

walkRight = [pygame.image.load('postava/R1.png'), pygame.image.load('postava/R2.png'), pygame.image.load('postava/R3.png'), pygame.image.load('postava/R4.png'), pygame.image.load('postava/R5.png'), pygame.image.load('postava/R6.png'), pygame.image.load('postava/R7.png'), pygame.image.load('postava/R8.png'), pygame.image.load('postava/R9.png')]
walkLeft = [pygame.image.load('postava/L1.png'), pygame.image.load('postava/L2.png'), pygame.image.load('postava/L3.png'), pygame.image.load('postava/L4.png'), pygame.image.load('postava/L5.png'), pygame.image.load('postava/L6.png'), pygame.image.load('postava/L7.png'), pygame.image.load('postava/L8.png'), pygame.image.load('postava/L9.png')]
bg = pygame.image.load('img/bg.jpg')
char = pygame.image.load('postava/standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            screen.blit(char, (self.x,self.y))


def redrawGameWindow():
    screen.blit(bg, (0,-75))
    man.draw(screen)
    pygame.display.update()


man = player(300, 410, 64, 64)
running = True
while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x+=man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount <0:
                neg = -1
            man.y -= (man.jumpCount**2)/2 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()


pygame.quit()
