import pygame 
import math
pygame.init()

window = pygame.display.set_mode((1280,720))


track = pygame.image.load('cutomtrack.png')
track = pygame.transform.scale(track,(1280,720))
display_tract = pygame.transform.smoothscale(track,(900,506))




clock = pygame.time.Clock()




running = True
while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        elif event.type == pygame.KEYDOWN :
            if  event.key == pygame.K_q :
                running = False  


    x,y = pygame.mouse.get_pos()
    print(f'Cords | x : {x} , y : {y}')
    
    window.blit(display_tract,(0,107))
   

    

    pygame.display.flip()
    clock.tick(60)

# Checkpoints 

'''
1. x : 154 , y : 524-600
2. x : 127 , y : 324- 399
3. x : 515 , y : 157-230 
4. x : 747 , y : 545-599
5. x : 430 - 535 , y : 499
6. lap
x - 417 , y = 523 , 602


'''

