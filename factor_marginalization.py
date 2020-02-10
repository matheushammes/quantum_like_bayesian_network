import numpy as np
from index_to_assignment import index_to_assignment
from assignment_to_index import assignment_to_index
import Nodes_

""""Takes a Factor and returns each of its probabilities normalized in a new Factor B"""

def  factor_marginalization(a,v): # A is a factor with var, card and val; V is a set of one or more variables

    # starts placeholder Node B to be populated later with corrected values
    b = Nodes_.Node([], [], [], [])

    b.variables = np.setdiff1d(a.variables, v)

    if b.variables == []:
        print("error: resultant factor has empty scope")

    map_b = []
    for i in a.variables:
        if np.isin(i, b.variables):
            map_b.append(np.where(b.variables == i)[0][0])

    b.cardinality = np.take(a.cardinality, map_b)
    b.probabilities = np.zeros(np.prod(b.cardinality), dtype = int)
    b.cardinality = [int(i) for i in list(b.cardinality)]

    assignments = []
    prob_range = list(range(len(a.probabilities)))
    prob_range = [i + 1 for i in prob_range]

    for i in prob_range:
        assignments.append(index_to_assignment(i, a.cardinality))

    assignments = np.array(assignments)

    juntosb = np.zeros(shape=(np.size(assignments, 0), len(map_b)))
    index = 0
    for mapping in map_b:
        each_column = assignments[:, mapping]
        juntosb[:, index] = each_column
        index += 1

    index_b = assignment_to_index(juntosb, b.cardinality)
    b.probabilities = list(b.probabilities)
    for i in range(len(index_b)):
        b.probabilities[index_b[i]] = float(b.probabilities[index_b[i]]) + float(a.probabilities[i])

    print("we got here and this is b", b)
    return b
