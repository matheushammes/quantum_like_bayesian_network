import numpy as np
import numpy.matlib as npm

""""Converts an assignment A (eg.: [1 0 1]), over variables with cardinality
    D (eg.:[2 3 2]) into an index of the probabilities factor of the factor that 
    is being evaluated
    example: D = [2 3 2] and you can assign each cardinality value to whatever suits your purpose:
             A = [1 0 1], returning the index created for this specific case"""


def assignment_to_index(A, D):  # A is the assignment and D is the cardinality

    D = D[0:len(D) - 1]
    D = list(D)
    D.insert(0, 1)
    D = np.array(D)
    D = np.atleast_2d(D)
    A = np.array(A)
    A = np.atleast_2d(A)
    A = A.T
    A = A.flatten()

    final = np.cumprod(D)@ A + 1
    return final



