import numpy as np
import numpy.matlib as npm

""""
    IndexToAssignment Convert index to variable assignment.

   A = IndexToAssignment(I, D) converts an index, I, into the .val vector
   into an assignment over variables with cardinality D. If I is a vector, 
   then the function produces a matrix of assignments, one assignment 
    per row """

def index_to_assignment(I,D): # i is an integer and D is a python list eg [2, 2, 2]

    # print(D)
    g = list(D[0:len(D) - 1])
    g.insert(0, 1)
    # print("Cardinality fixed inside index_to_assignment\n", g)
    # print("index same\n", I)

    result = np.float32(np.mod(np.floor(np.divide(npm.repmat(I - 1, 1, len(D)), npm.repmat(np.cumproduct(g), 1, 1))), npm.repmat(D, 1, 1)))
    # print("this is full result inside index to assignment\n",result)
    return result[0]






