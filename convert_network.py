"""
    convert_network returns a list of dictionaries  with all the nodes information found in a Huggin .net file
    dictionaries_list contain the information for individual nodes. The keys included are:
       var(parent names, if any);
       card(cardinality),
       and values(holds probability values).
    the order of dictionaries and keys is the same as in the .net file converted"""
import re  # imported to match regex
import numpy as np
from Nodes_ import Node

# create base dictionary and empty dictionary to store each node in it
factors = {"var": [],
            "states": [],
           "state_names": [],
            "val": [],
            "card": []}

dictionaries_list = {}
# create function that will scrape the file and store information
var_dict = {}
rev_dict = {}

def file_scrapper(file):
    # find variable names
    scraped = re.findall("potential \( (.*?) \)", file)
    variable_names = []
    parent_names = []
    for node in scraped:
        if "|" in node:
            temp_list = node.split("|")
            variable_names.append(temp_list[0].strip())
            stripped_parents = temp_list[1].strip()
            parent_names.append(stripped_parents)

        else:

            node = node.strip()
            variable_names.append(node)
            parent_names.append("")






    # iterate through variable_names and create dictionaries for each one of them

    for node in variable_names:
        dictionaries_list[node] = factors.copy()
        var_dict[node] = variable_names.index(node)
        rev_dict[variable_names.index(node)] = node

    # store node name on index 0 and parents on the following indexes

    variables_list = []

    for node, parents in zip(variable_names, parent_names): # change the order of parents and node so nodes are last
        join = node + " " + parents
        join = join.strip().split(" ")
        for var_name in join:
            join[join.index(var_name)] = var_dict[var_name]

        variables_list.append(join)



    # get states names, to find cardinality
    state_names = re.findall("states = \((.*?)\);", file)
    states_copy = []

    # remove the "" from the states (tokenize), separate and store accordingly in cardinality list
    cardinality = []

    for states in state_names:

        states = states.replace("\"", "").strip()
        split = states.split(" ")
        states = states.split(" ")
        states_copy.append(split)


    # change the names for numbers 0 for first state, 1 for the second, so on and so forth
        for each in states:
            states[states.index(each)] = states.index(each)
        cardinality.append(states)




    # re.compile used to add flag DOTALL that will enable to match multiple lines
    # as it is the case of dependent nodes
    regex_data = re.compile("data = (.*?);", re.DOTALL)

    # gets the values of each probability and stores in get_data
    get_data = re.findall(regex_data, file)

    # create probabilities list to store the values that are going to be cleaned in the next loop
    probabilities = []

    for values in get_data:
        values = values.replace(")(", " ")
        values = values.translate(str.maketrans({'(': '', ')': '', "\n": "", "\t": " "})).strip()
        values = values.strip().split("    ")
        probabilities.append(values)


    for each_list in probabilities:
        index = probabilities.index(each_list)
        mini_list = []

        for probability in each_list:
            individual_probability = re.findall("\d+\.\d+", probability)

            for i in individual_probability:
                i = np.float32(i)
                mini_list.append(i)
                probabilities[index] = mini_list

        # iterate through all lists and add information to dictionaries
        for dicts, name, prob, state, states_list, var, node in zip(dictionaries_list.copy(), variable_names, probabilities, cardinality, states_copy, parent_names, variables_list):
            dictionaries_list.get(dicts)["names"] = name
            dictionaries_list.get(dicts)["val"] = prob
            dictionaries_list.get(dicts)["states"] = state
            dictionaries_list.get(dicts)["state_names"] = states_list
            dictionaries_list.get(dicts)["var"] = node
            dictionaries_list.get(dicts)["card"] = len(state)

    nodes_list = []

    for name, variables in zip(variable_names, variables_list):

        variables.reverse()
        variables.insert(0, variables[len(variables) - 1])
        variables = variables[0:(len(variables) - 1)]
        state_names = dictionaries_list.get(name)["state_names"]
        probabilities = [float(i) for i in dictionaries_list.get(name)["val"]]
        cardinality = []
        cardinality.append(dictionaries_list.get(name)["card"])
        for var in variables[1:len(variables)]:
            name_par = rev_dict.get(var)
            cardinality.append(dictionaries_list.get(name_par)["card"])
        nodes = Node(name, probabilities, state_names, cardinality, variables)
        nodes_list.append(nodes)

    return nodes_list, variable_names
