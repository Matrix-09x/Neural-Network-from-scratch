import pygame

import numpy as np

import math 


import random


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
           
            break
            
            


        distance += 1


    return distance , x_end , y_end

        

def normalization(distance,sensor_length) :
    output = []
    for i in distance :
        no = i/sensor_length
        output.append(no)

    output = np.array(output)

    return output



def activation(output) :
    if output > 0 :
        number = output 

    else :
        number = 0

    return number


def population_func(number) :
    population_parameter_list = []
    for i in range(1,number+1) :
        weights = np.random.rand(8,7)
        biases = np.random.rand(8)
        output_weight = np.random.rand(3,8)
        output_bias = np.random.rand(3)
        population_parameter_list.append([weights,biases,output_weight,output_bias])

    return population_parameter_list


def selection(fitness_scores) :
    selected_candidates = []

    fitness_scores = np.array(fitness_scores)
    sorted_fitness = np.argsort(fitness_scores)[::-1]
    top1 , top2 = sorted_fitness[0] , sorted_fitness[1]
    selected_candidates.extend([top1,top2])

    for i in range(1,49):
        random_three = random.sample(range(0,len(fitness_scores)),k=3)
        best_candidate = max(random_three,key=lambda index :fitness_scores[index])
        selected_candidates.append(best_candidate)
            
    return selected_candidates


def mutation(paramerters) :
    for metrics in paramerters :
        for i in np.ndindex(metrics.shape) :
            per_parameter = random.uniform(0,1)
            if per_parameter <= 0.05 :
                replaced_number = random.uniform(-1,1)
                metrics[i] = replaced_number

    return paramerters

        



def cross0ver(selected_candidate,population) :

    new_generation = [] 
    elite_candiadate_1 , elite_candidate_2 =  population[selected_candidate[0]] , population[selected_candidate[1]]
    new_generation.extend((elite_candiadate_1 , elite_candidate_2))
    new_selected_candidate = selected_candidate[2:]
    random.shuffle(new_selected_candidate)

    

    for index,candidate in enumerate(new_selected_candidate) :
        if index % 2 ==  0 :
            parent_a = new_selected_candidate[index]
            parent_b = new_selected_candidate[index+1]
            metrices_a = population[parent_a]
            metrices_b = population[parent_b]

            weights_a , bias_a , output_weights_a , output_bias_a  =  metrices_a[0], metrices_a[1] , metrices_a[2] , metrices_a[3]
            weights_b , bias_b , output_weights_b , output_bias_b = metrices_b[0] , metrices_b[1] ,  metrices_b[2] , metrices_b[3]

            child_weight = []
            second_child_weight = []
            for a , b  in zip(weights_a,weights_b) :
                random_point = random.randint(1,6)
                partition_a = a[random_point:]
                partition_b = b[:random_point]
                second_partion_a = a[:random_point]
                second_partion_b = b[random_point:]

                child = np.concatenate((partition_a,partition_b))
                second_child = np.concatenate((second_partion_a,second_partion_b))
                child_weight.append(child)
                second_child_weight.append(second_child)

            child_weight = np.array(child_weight)
            second_child_weight = np.array(second_child_weight)


            random_point = random.randint(1,7)
            partition_a = bias_a[random_point:]
            second_partion_a = bias_a[:random_point]
            partition_b = bias_b[:random_point]
            second_partion_b = bias_b[random_point:]
            child_bias = np.concatenate((partition_a,partition_b))
            second_child_bias = np.concatenate((second_partion_a,second_partion_b))

            second_child_output_weight = []
            child_output_weights = []
            for a,b in zip(output_weights_a,output_weights_b) :
                random_point = random.randint(1,7)
                partition_a = a[random_point:]
                second_partion_a = a[:random_point]
                partition_b = b[:random_point]
                second_partion_b = b[random_point:]
                child = np.concatenate((partition_a,partition_b))
                second_child = np.concatenate((second_partion_a,second_partion_b))
                child_output_weights.append(child)
                second_child_output_weight.append(second_child)

            child_output_weights = np.array((child_output_weights))
            second_child_output_weight = np.array((second_child_output_weight))

            random_point = random.randint(1,2) 
            partition_a = output_bias_a[random_point:]
            second_partion_a = output_bias_a[:random_point]
            partition_b = output_bias_b[:random_point]
            second_partion_b = output_bias_b[random_point:]
            child_output_bias = np.concatenate((partition_a,partition_b))
            second_child_output_bias = np.concatenate((second_partion_a,second_partion_b))
            child_parameters = [child_weight,child_bias,child_output_weights,child_output_bias]
            second_child_parameters =  [second_child_weight,second_child_bias,second_child_output_weight,second_child_output_bias]

            for i in range(1,3) :
                mutation_prob = random.uniform(0,1)
                if mutation_prob <= 0.01 :
                    if i == 1 :
                        child_parameters = mutation(child_parameters)
                    else :
                        second_child_parameters = mutation(second_child_parameters)
                    


            new_generation.append(child_parameters)
            new_generation.append(second_child_parameters)
            


    return new_generation


def lap_completion(current_car_x ,current_car_y , car_y) :
    if car_y > 360 and current_car_y <= 360 and current_car_x >= 140 and current_car_x <= 240 :
        return True
    else :
        return False


        

        


def fitness_function(frame_survived) :

    return frame_survived
    


population = population_func(50)

frame_survived = 0

fitness_scores = []

parameters_list = []

g = 0



for i in range(1,2):

    g += 1 
    print(f'generation no : {g}')
    car_distance_list = []
    for popu in population:



        weights = popu[0]
        biases = popu[1]
        output_weight = popu[2]
        output_bias = popu[3]
        
        total_distance = 0
        lap_counter = 0
        while running :

            if frame_survived == 3000 :
                car_distance_list.append(total_distance)
                car_x,car_y = 180 , 360
                rotate = 0
                fitness = fitness_function(frame_survived)
                fitness_scores.append(fitness)
                frame_survived = 0
                break

            frame_survived += 1

            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    running = False

        


        
            
            window.fill('green')

            pygame.draw.ellipse(window,'black',outer_ellipse_rect)
            pygame.draw.ellipse(window,'green',ellipse_rect)
            # pygame.draw.line(window,'white',(190,260),(190,460),width=4)
            pygame.draw.line(window,'white',(140,360),(240,360),width=16)

            color = window.get_at((car_x,car_y))

            

            keys = pygame.key.get_pressed()

            # if keys[pygame.K_a] :
            #     rotate += 1

            # if keys[pygame.K_d] :
            #     rotate -= 1 

        
            current_car_x = car_x
            current_car_y = car_y

            car_x -=  speed * math.sin(math.radians(rotate))
            car_y -= speed * math.cos(math.radians(rotate))

            
            lap_checker = lap_completion(current_car_x,current_car_y,car_x)

            if lap_checker :
                lap_counter += 1

            

            


            distance_travelled = math.sqrt((car_x-current_car_x)**2 + (car_y - current_car_y)**2)

            total_distance += distance_travelled

                
            # if keys[pygame.K_s] :
            #     car_x  += speed * math.sin(math.radians(rotate))
            #     car_y += speed  * math.cos(math.radians(rotate))
            

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

            normalized_distance = normalization(distances,sensor_length)


            layer_output = np.dot(weights,normalized_distance) + biases
        

            activated_values = []

            for i in layer_output :
                value = activation(i)
                activated_values.append(value)

            activated_values = np.array(activated_values)

            output_layer = np.dot(output_weight,activated_values) + output_bias
        

            
            
            action = np.argmax(output_layer)

            if action == 0 :
                rotate += 1
        
            elif action == 1 :
                rotate -=1


            for x_e,y_e in zip(x_ends,y_ends) :

                pygame.draw.line(window,'yellow',[car_x,car_y],[x_e,y_e],width=1)
            


            window.blit(rotated_image ,rotated_rect)

        
            
            


            correct_position = False 

            if  ((car_x- 640)**2/500**2) + ((car_y - 360 )**2/300**2) < 1 and ((car_x - 640)**2/400**2) + ((car_y-  360)**2/200**2) > 1  :
                correct_position = True
        
            if not correct_position :
                car_x , car_y = 180 , 360
                rotate = 0
                fitness = fitness_function(frame_survived)
                fitness_scores.append(fitness)
                car_distance_list .append(total_distance)
                total_distance = 0
                
                frame_survived = 0
                break
            
                
            
            

            pygame.display.flip()

            clock.tick(60)

        if running == False :
            break 

    
    print(f'Length of distance list | {len(car_distance_list)}')
    print(f'largest distance list |  {max(car_distance_list)}')
    print(f'average distance list  {sum(car_distance_list)/len(car_distance_list)}')



    selected_candidate = selection(fitness_scores)
     
    new_generation = cross0ver(selected_candidate,population)
    population  = new_generation
    print(f'new population size : {len(population)}')
    print(f'largest fitness | {max(fitness_scores)}')
    print(f'average fitness | {sum(fitness_scores)/len(fitness_scores)}')
    fitness_scores = []
    


pygame.quit()

            



    
# print(fitness_scores)


            

"""
i cant undestand


"""








    

