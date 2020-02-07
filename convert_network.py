"""
    convert_network returns a list of dictionaries  with all the nodes information found in a Huggin .net file
    dictionaries_list contain the information for individual nodes. The keys included are:
       var(parent names, if any);
       card(cardinality),
       and values(holds probability values).
    the order of dictionaries and keys is the same as in the .net file converted"""
import re  # imported to match regex
import pprint

# create base dictionary and empty dictionary to store each node in it
factors = {"var": [],
            "states": [],
            "val": [],
            "card": []}

dictionaries_list = {}
# create function that will scrape the file and store information
var_dict = {}
rev_dict = {}

def file_scrapper(file):
    # find variable names
    variable_names = re.findall("potential \( (.*?) \|", file)
    # iterate through variable_names and create dictionaries for each one of them

    pairs = []
    for node in variable_names:
        dictionaries_list[node] = factors.copy()
        var_dict[node] = variable_names.index(node)
        rev_dict[variable_names.index(node)] = node



    # get the name of the parents
    parent_names = re.findall("\|(.*?) \)", file)  # gotta keep the space or some variables will disappear
    # tokenizing
    for parents in parent_names:
        parent_names[parent_names.index(parents)] = parents.strip()

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

    # remove the "" from the states (tokenize), separate and store accordingly in cardinality list
    cardinality = []
    for states in state_names:
        states = states.replace("\"", "").rstrip()
        states = states.split(" ")

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
        values = values.translate(str.maketrans({'(': '', ')': '', "\n": "", "\t": " "})).strip()
        values = values.strip().split("    ")
        probabilities.append(values)

    for each_list in probabilities:
        index = probabilities.index(each_list)
        mini_list = []

        for probability in each_list:
            individual_probability = re.findall("\d+\.\d+", probability)

            for i in individual_probability:
                mini_list.append(i)
                probabilities[index] = mini_list

        # iterate through all lists and add information to dictionaries
        for dicts, name, prob, state, var, node in zip(dictionaries_list.copy(), variable_names, probabilities, cardinality,
                                                 parent_names, variables_list):
            dictionaries_list.get(dicts)["names"] = name
            dictionaries_list.get(dicts)["val"] = prob
            dictionaries_list.get(dicts)["states"] = state
            dictionaries_list.get(dicts)["var"] = node
            dictionaries_list.get(dicts)["card"] = len(state)

    return variables_list, rev_dict, dictionaries_list, variable_names
