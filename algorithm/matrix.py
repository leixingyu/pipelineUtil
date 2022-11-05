import math
import numpy as np

from transforms3d import *


np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)


def compose_matrix(trans, rots, scales, order='sxyz'):
    """
    Compose a transformation matrix given translation, rotation and scale

    :param trans: list. translation values
    :param rots: list. rotation values in degree
    :param scales: list. scale values
    :param order: str. rotation order, 24 combinations in total, refer to
                  transform3d library
    :return: numpy.ndarray. transformation matrix
    """
    def degree_to_radian(angle):
        """
        Convert degree to radian
        :param angle: float. angle in degree
        :return: float. angle in radian
        """
        return angle / 360 * 2 * math.pi

    rots = [degree_to_radian(rot) for rot in rots]
    m_rot = euler.euler2mat(*rots, axes=order)

    return affines.compose(trans, m_rot, scales)


def decompose_matrix(matrix, order='sxyz'):
    """
    Decompose matrix to translation rotation and scale
    I don't care about shearing.

    :param matrix: numpy.ndarray. transformation matrix
    :param order: str. rotation order, 24 combinations in total, refer to
                  transform3d library
    :return: ([translations], [rotations], [scales]).
             translation values,
             rotation values in degree,
             scale values
    """
    def radian_to_degree(rad):
        """
        Convert radian value to degree
        :param rad: float. angle in radian
        :return: float. angle in degree
        """
        return rad * 360 / 2 / math.pi

    m_t, m_r, m_s, _ = affines.decompose44(matrix)
    rots = euler.mat2euler(m_r, axes=order)
    rots = [radian_to_degree(rot) for rot in rots]

    return list(m_t), rots, list(m_s)


def change_xform(source_xform, change_of_basis):
    """
    Change a transformation matrix from one coordinate to another

    https://youtu.be/P2LTAUO1TdA
    M_new = M_cob * M_source * inverse(M_cob)

    :param source_xform: numpy.ndarray. original transformation matrix
    :param change_of_basis: numpy.ndarray. change of basis matrix
    :return: converted transformation matrix in new coordinate system
    """
    inverse_change_of_basis = np.linalg.inv(change_of_basis)
    temp = np.matmul(change_of_basis, source_xform)

    return np.matmul(temp, inverse_change_of_basis)
