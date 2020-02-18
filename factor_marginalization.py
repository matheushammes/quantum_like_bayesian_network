import numpy as np
from index_to_assignment import index_to_assignment
from assignment_to_index import assignment_to_index
import Nodes_

""""Takes a Factor and returns each of its probabilities normalized in a new Factor B"""

def  factor_marginalization(a,v): # A is a factor with var, card and val; V is a set of one or more variables
    #TODO there is an indexing error around here somewhere, the probability values are correct
    # starts placeholder Node B to be populated later with corrected values
    b = Nodes_.Node([], [], [], [])

    b.variables = np.setdiff1d(a.variables, v)
    map_b = np.where(a.variables == b.variables)
    map_b = map_b[0][0]
    map_b = [map_b]
    print("these are all the variables in the new node: ", b.variables)
    print("avar", a.variables)

    if b.variables == []:
        print("error: resultant factor has empty scope")

    # THE ERROR IS FRICKING HERE
    # map_b = []
    # for i in a.variables:
    #     if np.isin(i, b.variables):
    #         map_b.append(np.where(b.variables == i)[0][0])

    print("this is map_b")
    print(map_b, type(map_b))

    print(a.cardinality, "card a")
    b.cardinality = np.take(a.cardinality, map_b)
    print("pre b card: ", b.cardinality)
    b.cardinality = [int(i) for i in list(b.cardinality)]

    print("cardi b")
    print(b.cardinality)
    assignments = []
    b.probabilities = np.zeros((np.prod(b.cardinality)), dtype=int)
    b.probabilities = list(b.probabilities)


    print("we creating the prob range here")
    print(b.probabilities)

    for i in range(len(a.probabilities)):
        assignments.append(index_to_assignment(i+1, a.cardinality))

    print(assignments)
    assignments = np.array(assignments)

    # all good til here

    # all_assignments = np.zeros(shape=(np.size(assignments, 0), len(map_b)))
    # index = 0
    # for mappings in map_b:
    #     each_column = assignments[:, mappings]
    #     all_assignments[:, index] = each_column
    #     index += 1

    index_b = assignment_to_index(assignments[:, map_b], b.cardinality)

    print("this is index b")
    print(index_b)
    print("and these are probabilities of b",b.probabilities)
    print("now a", a.probabilities)

    b.probabilities = list(b.probabilities)
    for i in range(len(index_b)):
        b.probabilities[index_b[i]] = float(b.probabilities[index_b[i]]) + float(a.probabilities[i])

        # print("bprob index b [i]")
        # print(b.probabilities[index_b[i]])
        #
        # print("aprob index i]")
        # print(a.probabilities[i])
        # print("final b")
        # print(b.probabilities)

    print("we got here and this is b", b.node_info())
    return b
