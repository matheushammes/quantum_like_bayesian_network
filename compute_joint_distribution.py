from factor_product import getting_joint_val

""""
Returns the Full Joint Probability Distribution of a list of Node Objects scrapped form the provided network
Objects can be accessed by their indexes. 
* call Node.node_info for a list of all indexes."""


def JPD_creator(all_nodes): # takes Node objects as arguments

    for i in all_nodes:
        if all_nodes.index(i) == 0:
            comb, indices = getting_joint_val(i, all_nodes[all_nodes.index(i) + 1])
        elif all_nodes.index(i) == 1:
            continue
        else:
            comb, indices = getting_joint_val(comb, i)

    return comb, indices