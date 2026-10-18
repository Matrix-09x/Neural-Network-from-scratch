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

car_x , car_y = 180 , 360

rotate = 0


speed = 2

sensor_length  = 150 

sensor_angles = [0,-90,-60,-30,30,60,90]


def sensor_length_cal(car_x,car_y,rotate,sensorlength,surface) :

    distance = 0 
    while distance < sensorlength :
        x_end = car_x - (distance * math.sin(math.radians(rotate)))
        y_end = car_y - (distance * math.cos(math.radians(rotate)))
        x_end = int(x_end)
        y_end = int(y_end)

        color = surface.get_at((x_end,y_end))

        if color != (0,0,0,255) :
            print(color)
            break


        distance += 1


    return distance , x_end , y_end

        




while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 



  
    
    window.fill('green')

    pygame.draw.ellipse(window,'black',outer_ellipse_rect)
    pygame.draw.ellipse(window,'green',ellipse_rect)

    color = window.get_at((car_x,car_y))
    print(color)

    


    

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

    distances = []
    x_ends = []
    y_ends = []
    
    for i in  sensor_angles :

        distance, x_end , y_end = sensor_length_cal(car_x,car_y,rotate+i,sensor_length,window)

        distances.append(distance)
        x_ends.append(x_end)
        y_ends.append(y_end)

    print(distances[0])

    for x_e,y_e in zip(x_ends,y_ends) :

        pygame.draw.line(window,'yellow',[car_x,car_y],[x_e,y_e],width=1)


    window.blit(rotated_image ,rotated_rect)




    
    


    correct_position = False 

    if  ((car_x- 640)**2/500**2) + ((car_y - 360 )**2/300**2) < 1 and ((car_x - 640)**2/400**2) + ((car_y-  360)**2/200**2) > 1  :
        correct_position = True
 
    if not correct_position :
        car_x , car_y = 180 , 360
        rotate = 0
    
      

    pygame.display.flip()

    clock.tick(60)


 
        
pygame.quit()
 
    



            











    

