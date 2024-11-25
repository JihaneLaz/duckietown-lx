from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
     
    res[int(shape[0]/2):, 0:int(shape[1]/2)] = 1
    res[ 0:int(shape[0]/2):,int(shape[1]/4):int(shape[1]/2)] = 1
    res[int(shape[0]/2): , int(shape[1]/2):] = -1
    res[ 0:int(shape[0]/2):,int(shape[1]/2):int(3*shape[1]/4)] = -1

    res[ 0:int(shape[0]/2):,:int(shape[1]/4)] = -0.5
    res[ 0:int(shape[0]/2):,int(shape[1]/4)*3:] = 0.5
    #res[300:, 200:] = 1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[int(shape[0]/2):, 0:int(shape[1]/2)] = -1
    res[ 0:int(shape[0]/2):,int(shape[1]/4):int(shape[1]/2)] = -1
    res[int(shape[0]/2): , int(shape[1]/2):] = 1
    res[ 0:int(shape[0]/2):,int(shape[1]/2):int(3*shape[1]/4)] = 1

    res[ 0:int(shape[0]/2):,:int(shape[1]/4)] = 0.5
    res[ 0:int(shape[0]/2):,int(shape[1]/4)*3:] = -0.5
    return res

