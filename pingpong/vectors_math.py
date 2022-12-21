import numpy as np


def inner(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def sum_tuple(v1, v2):
    a, b = v1
    A, B = v2

    return (a + A, b + B)


def multy_tuple(value, vector):
    a, b = vector
    a *= value
    b *= value
    return (a, b)


def theta_to_bubson(theta):
    # 세타로 단위법선벡터를 구한다
    return (np.sin(theta), np.cos(theta))


def theta_to_danwi(theta):
    # 세타로 단위벡터를 구한다
    return (np.cos(theta), np.sin(theta))


def angle_to_theta(angle):
    # 기울기를 세타로 바꿔준다
    return np.arctan(angle)
