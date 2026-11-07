import pygame 
import math
pygame.init()

window = pygame.display.set_mode((1280,720))


track = pygame.image.load('cutomtrack.png')
track = pygame.transform.scale(track,(1280,720))
display_tract = pygame.transform.smoothscale(track,(900,506))

car_image = pygame.image.load('car.png')
scaled_car_image = pygame.transform.scale(car_image,(60,41))
road_mask = pygame.mask.from_threshold(track,(40,40,40,255),(50,50,50,255))

car_x , car_y = 577,629
acceleration = 0
max_vel = 2
rotate = 90
speed = 2
clock = pygame.time.Clock()

running = True
while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        elif event.type == pygame.KEYDOWN :
            if  event.key == pygame.K_q :
                running = False 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] :
        rotate += 1

    if keys[pygame.K_d] :
        rotate -= 1

    if keys[pygame.K_w] :
        car_x -= speed * math.sin(math.radians(rotate))
        car_y -= speed * math.cos(math.radians(rotate))

    if keys[pygame.K_s] :
        car_x += speed * math.sin(math.radians(rotate))
        car_y += speed  * math.cos(math.radians(rotate))
 

    rotated_image = pygame.transform.rotate(scaled_car_image,rotate)
    rotated_rect = rotated_image.get_rect()

    rotated_rect.center = (car_x* 0.703125,car_y * 0.703125 + 107)
    
    window.blit(display_tract,(0,107))
    window.blit(rotated_image,rotated_rect)

    

    pygame.display.flip()
    clock.tick(60)
