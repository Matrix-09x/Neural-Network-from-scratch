import numpy as np
import random as rd
import matplotlib.pyplot as plt 


def activate(dot_product)  :

    if dot_product > 0 :
        return 1

    else :
        return -1


weighted_list = []
for i in range(1,4) :
    weight = rd.uniform(-1,1)
    weighted_list.append(weight)

weighted_list = np.array(weighted_list)

def perceptron(inputs,corrected,learning_constant) :
    
    dot_product = weighted_list @ inputs

    guess = activate(dot_product)

    error = corrected - inputs

    for i in range(len(weighted_list)) :
        weighted_list[i] =  error * i * learning_constant

  


print(weighted_list)
guess = perceptron([1,2.4,3])

print(guess)
    




