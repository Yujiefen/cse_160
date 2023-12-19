# Name: Sophie Feng
# Collaboration: Yuhui Xiang
# CSE 160
# Homework 4


import os
import math
from utils import converged, plot_2d, plot_centroids, read_data, \
    load_centroids, write_centroids_tofile
import matplotlib.pyplot as plt
import numpy as np


# problem for students
def euclidean_distance(dp1, dp2):
    """Calculate the Euclidean distance between two data points.

    Arguments:
        dp1: a non-empty list of floats representing a data point
        dp2: a non-empty list of floats representing a data point

    Returns: the Euclidean distance between two data points
    """
    distance = 0
    for i in range(len(dp1)):
        distance += (dp1[i] - dp2[i]) ** 2
    real_distance = math.sqrt(distance)
    return real_distance


# problem for students
def assign_data(data_point, centroids):
    """Assign a single data point to the closest centroid. You should use
    the euclidean_distance function (that you previously implemented)
    Arguments:
        data_point: a list of floats representing a data point
        centroids: a dictionary representing the centroids where the keys are
                   strings (centroid names) and the values are lists of
                   centroid locations

    Returns: a string as the key name of the closest centroid to the data point
    """
    min_dis = float('inf')
    for key in centroids.keys():
        temp = euclidean_distance(data_point, centroids[key])
        if temp < min_dis:
            min_dis = temp
            string = key
        else:
            continue
    return string


# problem for students
def update_assignment(data, centroids):
    """Assign all data points to the closest centroids. You should use
    the assign_data function (that you previously implemented).

    Arguments:
        data: a list of lists representing all data points
        centroids: a dictionary representing the centroids where the keys are
                   strings (centroid names) and the values are lists of
                   centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are lists of points that belong to the centroid. If a
             given centroid does not have any data points closest to it,
             do not include the centroid in the returned dictionary.
    """
    string_data = dict()
    for key in centroids.keys():
        string_data[key] = []
    for i in data:
        string = assign_data(i, centroids)
        string_data[string].append(i)
    for key in list(string_data.keys()):
        if string_data[key] == []:
            string_data.pop(key)
    return string_data


# problem for students
def mean_of_points(data):
    """Calculate the mean of a given group of data points. You should NOT
    hard-code the dimensionality of the data points).

    Arguments:
        data: a list of lists representing a group of data points

    Returns: a list of floats as the mean of the given data points
    """
    count = 0.0
    sum = 0.0
    average = 0.0
    newlst = []
    for i in range(len(data[0])):
        for j in range(len(data)):
            sum += data[j][i]
            count += 1.0
        average = sum / count
        newlst.append(average)
        sum = 0
        count = 0
        average = 0
    return newlst


# problem for students
def update_centroids(assignment_dict):
    """Update centroid locations as the mean of all data points that belong
    to the cluster. You should use the mean_of_points function (that you
    previously implemented).

    Arguments:
        assignment_dict: the dictionary returned by update_assignment function

    Returns: A new dictionary representing the updated centroids
    """
    new_centoids = {}
    for key in assignment_dict:
        new_centoids[key] = mean_of_points(assignment_dict[key])
    return new_centoids


# helper functions
def assert_dict_eq(dict1, dict2):
    """Verifies two dictionaries are equal. Throws an error if not.

    Arguments:
        dict1: a dictionary
        dict2: a second dictionary
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    assert type(dict1) is dict
    assert type(dict2) is dict
    # keys
    assert dict1.keys() == dict2.keys()
    # values
    for k, v in dict2.items():
        matrix2 = np.array(v)
        matrix1 = np.array(dict1[k])
        assert np.allclose(np.sort(matrix1, axis=0), np.sort(matrix2, axis=0))


def setup_data_centroids():
    """Creates are returns data for testing k-means methods.

    Returns: data, a list of data points
             random_centroids, two 4D centroids
             bad_centroids, two non-random 4D centroids
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    data = [
            [-1.01714716,  0.95954521,  1.20493919,  0.34804443],
            [-1.36639346, -0.38664658, -1.02232584, -1.05902604],
            [1.13659605, -2.47109085, -0.83996912, -0.24579457],
            [-1.48090019, -1.47491857, -0.6221167,  1.79055006],
            [-0.31237952,  0.73762417,  0.39042814, -1.1308523],
            [-0.83095884, -1.73002213, -0.01361636, -0.32652741],
            [-0.78645408,  1.98342914,  0.31944446, -0.41656898],
            [-1.06190687,  0.34481172, -0.70359847, -0.27828666],
            [-2.01157677,  2.93965872,  0.32334723, -0.1659333],
            [-0.56669023, -0.06943413,  1.46053764,  0.01723844]
        ]
    random_centroids = {
            "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
            "centroid2": [-0.71767545, 1.2309971, -1.00348728, -0.38204247],
        }
    bad_centroids = {
            "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
            "centroid2": [10, 10, 10, 10],
        }
    return data, random_centroids, bad_centroids


# tests begin
def test_eucliean_distance():
    """Function for verifying if euclidean_distance is correctly implemented.
    Will throw an error if it isn't.
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # int
    data1 = [0, 0, 0, 0]
    data2 = [1, 1, 1, 1]
    assert euclidean_distance(data1, data2) == 2

    # negative
    data1 = [-1, -1, -1, -1]
    data2 = [-5, -3, -1, -1]
    assert np.allclose(np.array(euclidean_distance(data1,
                       data2)),
                       np.linalg.norm(np.array(data1) -
                       np.array(data2)).tolist())

    # floats
    data1 = [1.1, 1, 1, 0.5]
    data2 = [4, 3.14, 2, 1]
    assert np.allclose(np.array(euclidean_distance(data1,
                       data2)),
                       np.linalg.norm(np.array(data1) -
                       np.array(data2)).tolist())

    # random
    data1 = np.random.randn(100)
    data2 = np.random.randn(100)
    assert np.allclose(np.array(euclidean_distance(data1.tolist(),
                       data2.tolist())),
                       np.linalg.norm(data1 - data2).tolist())
    print("test_eucliean_distance passed.")


def test_assign_data():
    """Function for verifying if assign_data is correctly implemented.
    Will throw an error if it isn't.
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    data_empty = [0, 0, 0, 0]
    data_random = [1.1, 5.3, 55, -12.1]
    centroids = {"centroid1": [1, 1, 1, 1],
                 "centroid2": [-10.1, 1, 23.2, 5.099]}
    assert assign_data(data_empty, centroids) == "centroid1"
    assert assign_data(data_random, centroids) == "centroid2"

    data = [10.1, 1, 23.2, 5.099]
    centroids = {"centroid1": [1, 1, 1, 1],
                 "centroid2": [10, 1, 23, 5],
                 "centroid3": [-100, 20.2, 52.9, -37.088]}
    assert assign_data(data, centroids) == "centroid2"
    print("test_assign_data passed.")


def test_update_assignment():
    """Function for verifying if update_assignment is correctly implemented.
    Will throw an error if it isn't.
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    data, random_centroids, bad_centroids = setup_data_centroids()

    # random
    rtn = update_assignment(data, random_centroids)
    answer = {
        "centroid1": [[-1.36639346, -0.38664658, -1.02232584, -1.05902604],
                      [1.13659605, -2.47109085, -0.83996912, -0.24579457],
                      [-0.83095884, -1.73002213, -0.01361636, -0.3265274]],
        "centroid2": [[-1.01714716, 0.95954521, 1.20493919, 0.34804443],
                      [-1.48090019, -1.47491857, -0.6221167, 1.79055006],
                      [-0.31237952, 0.73762417, 0.39042814, -1.1308523],
                      [-0.78645408, 1.98342914, 0.31944446, -0.41656898],
                      [-1.06190687, 0.34481172, -0.70359847, -0.27828666],
                      [-2.01157677, 2.93965872, 0.32334723, -0.1659333],
                      [-0.56669023, -0.06943413, 1.46053764, 0.01723844]]
    }
    assert_dict_eq(rtn, answer)

    # bad
    rtn = update_assignment(data, bad_centroids)
    answer = {
        "centroid1": [[-1.36639346, -0.38664658, -1.02232584, -1.05902604],
                      [1.13659605, -2.47109085, -0.83996912, -0.24579457],
                      [-0.83095884, -1.73002213, -0.01361636, -0.3265274],
                      [-1.01714716, 0.95954521, 1.20493919, 0.34804443],
                      [-1.48090019, -1.47491857, -0.6221167, 1.79055006],
                      [-0.31237952, 0.73762417, 0.39042814, -1.1308523],
                      [-0.78645408, 1.98342914, 0.31944446, -0.41656898],
                      [-1.06190687, 0.34481172, -0.70359847, -0.27828666],
                      [-2.01157677, 2.93965872, 0.32334723, -0.1659333],
                      [-0.56669023, -0.06943413, 1.46053764, 0.01723844]]
    }
    assert_dict_eq(rtn, answer)
    print("test_update_assignment passed.")


def test_mean_of_points():
    """Function for verifying if mean_of_points is correctly implemented.
    Will throw an error if it isn't.
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # empty
    data = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    assert mean_of_points(data) == [0, 0, 0, 0]

    # random
    data = np.random.randn(10, 4)
    assert np.allclose(np.array(mean_of_points(data.tolist())),
                       data.mean(axis=0))

    # negative
    data = [
            [-1, -10, -70, -89],
            [2, 3, 55, 7],
        ]
    assert np.allclose(np.array(mean_of_points(data)),
                       np.array(data).mean(axis=0))
    print("test_mean_of_points passed.")


def test_update_centroids():
    """Function for verifying if update_centroids is correctly implemented.
    Will throw an error if it isn't.
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    data, random_centroids, bad_centroids = setup_data_centroids()

    # random
    assignment_dict = update_assignment(data, random_centroids)
    answer = {
        'centroid2': [-1.03386497, 0.774388037, 0.33899735, 0.023455955],
        'centroid1': [-0.35358541, -1.529253186, -0.62530377, -0.543782673]
    }
    rtn = update_centroids(assignment_dict)
    assert_dict_eq(rtn, answer)

    # bad
    assignment_dict = update_assignment(data, bad_centroids)
    answer = {
        'centroid1': [-0.82978110, 0.08329567, 0.04970701, -0.146715632]
    }
    rtn = update_centroids(assignment_dict)
    assert_dict_eq(rtn, answer)
    print("test_update_centroids passed.")


# main functions
def main_test():
    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    test_eucliean_distance()
    test_assign_data()
    test_update_assignment()
    test_mean_of_points()
    test_update_centroids()
    print("all tests passed.")


def main_2d(data, init_centroids):
    #######################################################
    # You do not need to change anything in this function #
    #######################################################
    centroids = init_centroids
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = update_assignment(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        # plot centroid
        fig = plot_2d(assignment_dict, centroids)
        plt.title(f"step{step}")
        fig.savefig(os.path.join("results", "2D", f"step{step}.png"))
        plt.clf()
        step += 1
    print(f"K-means converged after {step} steps.")
    return centroids


def main_mnist(data, init_centroids):
    #######################################################
    # You do not need to change anything in this function #
    #######################################################
    centroids = init_centroids
    # plot initial centroids
    plot_centroids(centroids, "init")
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = update_assignment(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        step += 1
    print(f"K-means converged after {step} steps.")
    # plot final centroids
    plot_centroids(centroids, "final")
    return centroids


if __name__ == "__main__":
    # main_test()

    data, label = read_data("data/data_2d.csv")
    init_c = load_centroids("data/2d_init_centroids.csv")
    final_c = main_2d(data, init_c)
    write_centroids_tofile("2d_final_centroids.csv", final_c)
