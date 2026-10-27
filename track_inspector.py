import pygame 

pygame.init()

window = pygame.display.set_mode((1280,720))


track = pygame.image.load('cutomtrack.png')
track = pygame.transform.scale(track,(1280,720))

road_mask = pygame.mask.from_threshold(track,(40,40,40,255),(50,50,50,255))

clock = pygame.time.Clock()

running = True
while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        elif event.type == pygame.KEYDOWN :
            if  event.key == pygame.K_q :
                running = False 




    window.blit(track,(0,0))

    x ,y = pygame.mouse.get_pos()
    color = track.get_at((x,y))

    print(f'x : {x} | y : {y}')
    # print(track.get_at((x,y)))
    

    pygame.display.flip()
    clock.tick(60)