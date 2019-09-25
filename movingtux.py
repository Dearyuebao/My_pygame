import sys, pygame
size=(500,220)


pygame.init()

tux=pygame.image.load("tux.png")
surface = pygame.display.set_mode(size)
surface.fill(pygame.Color(255,255,255))
rect=tux.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    
    surface.blit(tux,(200,200))
    surface.blit(tux,rect)
    pygame.display.update()

    rect.x=rect.x+1

