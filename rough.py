
import numpy as np 
import random

# experimeantation

inputs = np.array([
    [2,4,5,6],
    [4.5,6,7,8],
    [9.8,2.3,4.5,3],
    [9,5.5,6.7,8],
    [1.2,3,4.3,4],
    [1.1,3,4,5],
    [2.4,5.3,4.2,1]
])

weights = np.array([
    [4.4,5,3,4],
    [2.2,4,5,7.7],
    [8.3,4,5,6.2]
])

biases = [3,4,5,1.2]

layer1_output = np.dot(inputs , weights.T) 

weights_2 = np.array([
    [3.4,4.5,3,2.3],
    [2,3,4,7.1],
    [2.3,4,1,2]
])

biases_2 = [3.4,5,2,4]

weights_3 = []
for i in range(3) :
    w_l = []
    for j in range(4) :
        no = random.uniform(0,10)
        w_l.append(no)
    weights_3.append(w_l)


print(weights_3)



layer2_output = np.dot(layer1_output,weights_2.T) + biases_2

