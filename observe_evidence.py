import numpy as np
from index_to_assignment import index_to_assignment
from Nodes_ import Node


"""" ObserveEvidence Modify a vector of factors given some evidence.
   F = ObserveEvidence(F, E) sets all entries in the vector of factors, F,
   that are not consistent with the evidence, E, to zero. F is a vector of
   factors, each a data structure with the following fields:
     .var    Vector of variables in the factor, e.g. [1 2 3]
     .card   Vector of cardinalities corresponding to .var, e.g. [2 2 2]
     .val    Value table of size prod(.card)
   E is an N-by-2 matrix, where each row consists of a variable/value pair. 
   Variables are in the first column and values are in the second column
    Evidence example [[A, True], [B, False]} """



def observe_evidence(F, evidence): # F is the list of factors and evidence says what is true and what is not

    # print("this is the evidence value entered")
    # print(evidence)
    # print("dis F")
    # print(F)
    for each in evidence:
        variable = each[0]
        value = each[1]
        # print("we checking for this one here", variable)
        # open Factor to see if it contains said node

        for node in F:
            if variable in node.variables:
                var_index = node.variables.index(variable)
                card_prod_range = list(range(int(np.prod(node.cardinality))))
                card_prod_range = [i + 1 for i in card_prod_range]
                assignments = []
                for i in card_prod_range:
                    assignments.append(index_to_assignment(i, node.cardinality))
                assignments = np.array(assignments)
                # print(assignments)
                index = 0
                for comb in assignments:
                    # print("dis comb", comb)

                    if comb[var_index] != value:
                        node.probabilities[index] = 0
                        index += 1
                    else:
                        index += 1

    return F


