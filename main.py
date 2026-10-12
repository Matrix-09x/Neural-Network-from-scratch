import pygame

import numpy 

import math 

pygame .init()

window = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()


car_image = pygame.image.load('car.png')
scaled_car_image = pygame.transform.scale(car_image,(100,75))


running = True 

ellipse_rect = pygame.Rect(0,0,800,400)
outer_ellipse_rect = pygame.Rect(0,0,1000,600)
outer_ellipse_rect.center = (640,360)
ellipse_rect.center = (640,360)

car_x , car_y = 300,300

rotate = 0

speed = 2

while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 



  
    
    window.fill('green')

    pygame.draw.ellipse(window,'black',outer_ellipse_rect)
    pygame.draw.ellipse(window,'green',ellipse_rect)


    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] :
        rotate += 1

    if keys[pygame.K_d] :
        rotate -= 1 

  
    if keys[pygame.K_w] :

        car_x -=  speed * math.sin(math.radians(rotate))
        car_y -= speed * math.cos(math.radians(rotate))
        
    if keys[pygame.K_s] :
        car_x  += speed * math.sin(math.radians(rotate))
        car_y += speed  * math.cos(math.radians(rotate))
    
        
    rotated_image = pygame.transform.rotate(scaled_car_image,rotate)

    rotated_rect = rotated_image.get_rect()

    rotated_rect.center =  (car_x , car_y)


    window.blit(rotated_image ,rotated_rect)
    


      

    pygame.display.flip()

    clock.tick(60)
 
        
 


pygame.quit()








    

