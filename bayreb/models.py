"""
This file is part of the BAYREB library
"""
from typing import List

import numpy as np
from scipy.linalg import expm
from numpy.linalg import inv

def dot3(A, B, C):
    """ Returns the matrix multiplication of A*B*C"""
    return np.dot(A, np.dot(B, C))


def stack4(A, B, C, D):
    return np.vstack((np.hstack((A, B)), np.hstack((C, D))))


class RC_model(object):
    def __init__(self):
        self.type = 'RC'

    def information(self):
        pass

    def get_parameters(self):
        return 0

    def print_parameters(self):
        print('Print parameters')

    def onestep_prediction(self):
        pass

    def onestep_update(self):
        pass

    def onestep_filtering(self):
        pass



class model_2R2C(RC_model):

    def __init__(self):
        self.parameters_list = ['R1', 'R2', 'C1', 'C2', 'A1', 'A2']

    def _set_parameters(self):
        pass





