import pygame

pygame.init()

screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('deez nuts')

#promenne tykajici se hrace
x = 50
y = 425
width = 50
height = 50
vel = 15

#promenne pro skoky
isJump = False
jumpCount = 10



running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -=vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x+=vel
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y-=vel
        if keys[pygame.K_DOWN] and y <screenHeight - height:
            y+=vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount <0:
                neg = -1
            y -= (jumpCount**2)/2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10



    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0),(x,y,width,height))
    pygame.display.update()

pygame.quit()
