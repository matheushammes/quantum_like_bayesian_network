import numpy as np
from observe_evidence import observe_evidence
from compute_joint_distribution import JDP_creator
from factor_marginalization import factor_marginalization

"""" ComputeMarginal Computes the marginal over a set of given variables
   ComputeMarginal(v,f,e) computes the marginal over variables V
   in the distribution induced by the set of factors F, given evidence E

   It returns a Factor containing the marginal over variables V
   V is a vector containing the variables in the marginal e.g. [1 2 3] for
     X_1, X_2 and X_3.
    F is a Node Object containing the factors defining the distribution
    E is an N-by-2 matrix, each row being a variable/value pair. 
     Variables are in the first column and values are in the second column.
     If there is no evidence, pass in the empty matrix [] for E """

def computeMarginal(v,f,e):

    f = observe_evidence(f, e)
    joint = JDP_creator(f)
    joint.probabilities = joint.probabilities/sum(joint.probabilities)
    m = factor_marginalization((joint, np.setdiff1d(joint.variables, v)))
    m.probabilities = m.probabilities/sum(m.probabilities)

    return m