"""the Node class itself, has all the attributes that are added to the Node Object"""

class Node:

    def __init__(self, name, probabilities, state_names,cardinality, variables):
        self.name = name
        self.state_names = state_names
        self.probabilities = probabilities
        self.cardinality = cardinality
        self.variables = variables

    def node_info(self):
        return self.name, self.probabilities, self.variables, self.state_names, self.cardinality

    def get_probabilities(self):
        return self.probabilities
    def get_names(self):
        return self.name