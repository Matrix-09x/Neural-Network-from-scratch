import numpy as np 
import random as rd
import string 
Target_string = 'iqra pagal khane jayegi'


population_szie = 150
 
def random_character(length) :
    characters = string.ascii_lowercase + " "
    
    word_generated = ""
    for i in range(1,length+1) :
        starter =  rd.choice(characters) + word_generated
        word_generated = starter

    return word_generated


def population_func(number,length) :
   population = []

   for i in range(1,number+1) :
       word = random_character(length) 
       population.append(word)

   return population 







def fitness_func(word) :
    correct = 0 
    for index, ltr in enumerate(word) :
        if ltr ==  Target_string[index] :
            correct+= 1


    fitness_Score = correct/len(Target_string)

    return fitness_Score 



population = population_func(population_szie,len(Target_string))

generation = 0
n = False

while n == False:

    generation += 1

    
    fitness_list = []
    for  i  in population :
        fitness_score = fitness_func(i)
        fitness_list.append(fitness_score)




    mating_pool = []


    for index,score in enumerate(fitness_list) :
        chances = score * 100 

        for i in range(int(chances+1)) :
            mating_pool.append(population[index])



    def offspring(parent_a , parent_b) :

        split = rd.randint(1,len(Target_string)) 

        child = parent_a[:split] + parent_b[split:]

        return child


    new_pop = []
    characters = string.ascii_lowercase + " "
    for i in range(population_szie+1) :

        parent_a = rd.choice(mating_pool)
        parent_b = rd.choice(mating_pool)

        child = offspring(parent_a,parent_b)

        mutation_rate = 0.01

        mutation_list = []
        for index,Chr in enumerate(child) :
            random_no = rd.uniform(0,1)
            if random_no < mutation_rate :
                new_chr = rd.choice(characters)
                mutation_list.append((index,new_chr))


        if mutation_list :
            for index,Chr  in mutation_list :
            
                child = child[:index] +  Chr + child[index+1:]

        new_pop.append(child)
        

        population = new_pop

    
    for i in population :
        
        print(i)
        if i == Target_string :
            n = True
            print(i)
            print(f'No of generations | {generation}')
            break



       


    

 

            



    





         
        
    


       






