from compute_joint_distribution import JPD_creator
import numpy as np
import convert_network
from Nodes_ import Node
import os
from pprint import pprint
from observe_evidence import observe_evidence
from compute_marginal import compute_marginal

# TODO: normalize all values when changed to 0

""" 

    Creates the Node object, which is a factor, containing the following information:
    Cardinality
    Name
    Probabilities
    Variables -  the first variable is the node itself, the ones after it are their parents

    use read_network(path) to open your network. path is a string

    the quantum aspect of the networks is currently being trialed, but it is not added in this release.


"""


def read_network(path, isquantum):
    network = open(path, "r").read()
    variable_each, node_dict, values, node_names = convert_network.file_scrapper(network)
    nodes_list = []

    print("variable_each", variable_each)

    for name, variables in zip(node_names, variable_each):

        variables.reverse()
        variables.insert(0, variables[len(variables) - 1])
        variables = variables[0:(len(variables) - 1)]
        # if isquantum:
        #     probabilities = [np.sqrt(float(i)) for i in values.get(name)["val"]]
        # else:
        probabilities = [float(i) for i in values.get(name)["val"]]
        cardinality = []
        cardinality.append(values.get(name)["card"])
        for var in variables[1:len(variables)]:
            name_par = node_dict.get(var)
            cardinality.append(values.get(name_par)["card"])

        nodes = Node(name, probabilities, cardinality, variables)
        nodes_list.append(nodes)

    return nodes_list

def check_input():
    path_ask = input("please input path and set True or False for the quantum aspect of the analysis")
    path_ask = path_ask.split(",")
    path_ask = tuple(path_ask)

    if len(path_ask) != 2:
        check_input()
    else:
        if os.path.exists(path_ask[0]) and path_ask[1] == "True" or "False":
            scrape = read_network(path_ask[0], path_ask[1])
            return scrape


def show_factor(factor):
    for i in factor:
        print(Node.node_info(i))
    return None


if __name__ == "__main__":

    nodes_list = check_input()
    # print(nodes_list)
    show_factor(nodes_list)
    print("reminder")
    [print("node name:", Node.get_names(i), "node index:", nodes_list.index(i), "states:", i.cardinality[0], "\n probs:", Node.get_probabilities(i)) for i in
     nodes_list]

    node = input("Would you like to set any node to a certain state? Input node index here\n press enter if you dont want it")

    if node != "":
        state = input("Now input the state")
        marginal = input("Compute Marginal?\n press enter if you dont want it")
        if marginal != "":
            new_node = compute_marginal([int(marginal)], nodes_list, [[int(node), int(state)]])
            print(new_node.node_info())
        else:
            nodes_list = observe_evidence(nodes_list, [[int(node), int(state)]])
            jpd, assignments_list = JPD_creator(nodes_list)
            np.set_printoptions(precision=7, suppress=True)
            print("JOINT PROBABILITIES, {}".format(jpd.get_names()))
            norm = np.sum(jpd.probabilities)
            jpd.probabilities = np.divide(jpd.probabilities, norm)
            pprint(jpd.probabilities)

    else:
        show_factor(nodes_list)
        jpd, assignments_list = JPD_creator(nodes_list)
        np.set_printoptions(precision=4, suppress=True)
        print("JOINT PROBABILITIES, {}".format(jpd.get_names()))
        norm = np.sum(jpd.probabilities)
        jpd.probabilities = np.divide(jpd.probabilities, norm)
        pprint(jpd.probabilities)
