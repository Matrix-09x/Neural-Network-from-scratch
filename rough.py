
import numpy as np 

inputs  = np.array([2.4,5,6,3.4])

weights = np.array([[2,3,4,4.5],
                    [3.4,5,1.8,1.1],
                    [6,6.1,5.2,2]
                    ])

bias = [2,3,4]


layer_output = []

for index,neruon_weight in enumerate(weights) :
    output = inputs @ neruon_weight + bias[index]
    layer_output.append(output)

matrix = np.array([
          [4,5],
          [4,3],
          [2,5]
          ])

d3_matrix = np.array([
    [[1,4,5],
    [13,4,5]],
    [[2,3,6],
     [3,4,5]],
     [[7,8,3],
     [3,4,5]],
     [[3,8,5],
      [5,4,2]],
      [[2,6,7],
       [3,8,7]]
])



weights = np.random.rand(7,8)

for i in weights :
    print(i)