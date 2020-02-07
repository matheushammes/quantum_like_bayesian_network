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

    if np.any(np.array(np.shape(A)) == 1):

        final = []
        A = np.array(A)

        for i in A:
            i = i.astype(int)
            result = sum(np.cumprod(D) * (i.transpose()))
            final.append(result)

        return final

    else:
        result = np.sum((np.dot(npm.repmat(np.cumprod(D), int(np.shape(A[0])[0]), 1), A.transpose()), 1)) - 1
        result = list(result)
        idx = 0
        for i in result:
            converted = list(i)
            int_conv = [int(s) for s in converted]
            result[idx] = int_conv
            idx += 1

        return result[0]
