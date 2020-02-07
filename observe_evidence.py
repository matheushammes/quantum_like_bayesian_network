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

    print("this is the evidence value entered")
    print(evidence)
    print("dis F")
    print(F)
    for each in evidence:
        variable = each[0]
        value = each[1]
        print("we checking for this one here", variable)
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
                print(assignments)
                index = 0
                for comb in assignments:
                    print("dis comb", comb)

                    # print("var_index", var_index)
                    # # you got to iterate thru alll the values here
                    # indices_tbc = np.argwhere(int(comb[var_index]) != value)
                    # print("value type", type(value))
                    # print("each in comb", type(comb[var_index]))
                    # print("tbc",indices_tbc)
                    # print("here the vals:", node.probabilities)
                    # # the problem be here and only here.
                    # # we might need to add some checking before we wnter thi loop.
                    # new_node = [print("here we go",node.probabilities[i]) for i[0] in indices_tbc]
                    if comb[var_index] != value:
                        # print("here is return of npwhere", np.where(assignments == np.array(np.array(comb))))
                        node.probabilities[index] = 0
                        index += 1
                    else:
                        index += 1
                        continue
                    print(node.probabilities)

    return F


"""heres what we b doin:
                    
        
        
    
                    
                    checking every single combination for certain index. if index matches, we will get its index
                    this comb's index will get its probability value set to 0 node.probabilities[assignmens.index(comb)]"""


"""for comb in comb_list:
    print(comb)
    if comb[1] == 1:
        comb = "im the coathanger in your mans vagina"
    else:
        continue
    print(comb_list)     """





'''for node in F:
            print(node.node_info())
            node_var = node.variables
            if variable in node_var[1:len(node_var)]:
                node_var = node_var.index(variable)
                if value >= 0:
                    if value > node.cardinality[node_var] - 1 or value < 0:
                        print("invalid value, the options are the following {}".format(range(F[variable].card)))
                    else:
                        range_of_node = list(range(int(np.prod(node.cardinality))))
                        range_of_node = [i + 1 for i in range_of_node]
                        assignments = []
                        for i in range_of_node:
                            i_assignment = index_to_assignment(i, node.cardinality)
                            assignments.append(i_assignment)
                        assignments = np.array(assignments)
                        idx_ass = assignments[:, node_var]
                        final_idx = np.where(idx_ass != value)
                        for i in final_idx[0]:
                            node.probabilities[i] = 0
                        return F
                else:
                    print("invalid value, chosen variable is not in {}".format(node.probabilities))
            else:
                print("invalid variable, check the list here {}".format(node.variables))'''
