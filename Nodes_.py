"""the Node class itself, has all the attributes that are added to the Node Object"""

class Node:

    def __init__(self, name, probabilities, cardinality, variables):
        self.name = name
        self.probabilities = probabilities
        self.cardinality = cardinality
        self.variables = variables

    def node_info(self):
        return self.name, self.probabilities, self.variables, self.cardinality

    def get_probabilities(self):
        return self.probabilities
    def get_names(self):
        return self.name