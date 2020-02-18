from index_to_assignment import index_to_assignment
from assignment_to_index import assignment_to_index
import numpy as np
from Nodes_ import Node


""""Takes two Factors at a time and returns the resusltant joint probability distribution for the two of them.
    This function does not need to be called multiple times if you want to create a a JPD for
     a larger network. Use factorJointDistribution to do it automatically."""

def getting_joint_val(node_a, node_b): # we are returning proper nodes on this one now, so no need to all the workarounds to enter the factor

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

    # print("this is inside factor_product, here is all the info about the newly created node:")
    # print("new name", comb.name)
    # print("variables", comb.variables)
    # print("cardinality", comb.cardinality)
    assignments = []
    for i in card_prod_range:
        assignments.append(index_to_assignment(i, comb.cardinality))
    assignments = np.array(assignments)


    juntosA = np.zeros(shape = (np.size(assignments, 0), len(map_a)))
    juntosB = np.zeros(shape = (np.size(assignments, 0), len(map_b)))
    index = 0

    # for mapping in map_a:
    #
    #     each_column = assignments[:, mapping]
    #     juntosA[:, index] = each_column
    #     index += 1

    index_a = assignment_to_index(assignments[:, map_a], node_a.cardinality)

    index = 0

    # for mapping in map_b:
    #
    #     each_column = assignments[:, mapping]
    #     juntosB[:, index] = each_column
    #     index += 1

    index_b = assignment_to_index(assignments[:, map_b], node_b.cardinality)
    # print("inside factor_product, these are the values for the first node, a.")
    # print(node_a.probabilities)
    # print("indexes of A")
    # print(index_a)
    # print("map_a")
    # print(map_a)
    # print("now, node b")
    # print(node_b.probabilities)
    # print("indexes of B")
    # print(index_b)
    # print("map_b")
    # print(map_b)


    # change the for loop for a idx_a's length
    for i in range(len(index_a)):

        # TODO fix indexing here, it seems like its giving all the same values no matter what
        # print("i", i)
        # print("index used for a",index_a[i])
        prob_a = float(node_a.probabilities[index_a[i]])
        # print("prob_a", prob_a)
        prob_b = float(node_b.probabilities[index_b[i]])
        # print("index used for b", index_b[i])
        # print("prob_b", prob_b)
        comb.probabilities[i] = prob_a * prob_b

    return comb, assignments
