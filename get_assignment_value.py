from index_to_assignment import index_to_assignment
from assignment_to_index import assignment_to_index
import numpy as np
from Nodes_ import Node


""""Takes two Factors at a time and returns the resultant joint probability distribution for the two of them.
    This function does not need to be called multiple times if you want to create a a JPD for
     a larger network. Use factorJointDistribution to do it automatically."""

def get_assignment_value(node_a, node_b): # we are returning proper nodes on this one now, so no need to all the workarounds to enter the factor

    union = np.union1d(node_a.variables, node_b.variables)
    union = list(union)

    map_a = [union.index(i) for i in node_a.variables]
    map_b = [union.index(i) for i in node_b.variables]

    card_a = node_a.cardinality
    card_b = node_b.cardinality

    comb = Node([], [], [], [])
    comb.name = 'new_node'
    comb.variables = union
    comb.cardinality = np.zeros(len(comb.variables))
    np.put(comb.cardinality, map_a, card_a)
    np.put(comb.cardinality, map_b, card_b)
    comb.cardinality = [int(i) for i in list(comb.cardinality)]
    comb.probabilities = np.zeros((np.prod(comb.cardinality)), dtype=int)
    comb.probabilities = list(comb.probabilities)
    card_prod_range = list(range(int(np.prod(comb.cardinality))))
    card_prod_range = [i+1 for i in card_prod_range]


    assignments = []
    for i in card_prod_range:
        assignments.append(index_to_assignment(i, comb.cardinality))
    assignments = np.array(assignments)


    juntosA = np.zeros(shape = (np.size(assignments, 0), len(map_a)))
    juntosB = np.zeros(shape = (np.size(assignments, 0), len(map_b)))
    index = 0

    for mapping in map_a:

        each_column = assignments[:, mapping]
        juntosA[:, index] = each_column
        index += 1

    index_a = assignment_to_index(juntosA, node_a.cardinality)

    index = 0

    for mapping in map_b:

        each_column = assignments[:, mapping]
        juntosB[:, index] = each_column
        index += 1

    index_b = assignment_to_index(juntosB, node_b.cardinality)

    for i in comb.probabilities:

        idx = comb.probabilities.index(i)
        prob_a = float(node_a.probabilities[index_a[idx]])
        prob_b = float(node_b.probabilities[index_b[idx]])
        comb.probabilities[idx] = prob_a * prob_b

    return comb, assignments
