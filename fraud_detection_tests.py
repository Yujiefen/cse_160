
import fraud_detection


def test_problem1():
    lst = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    assert fraud_detection.extract_election_vote_counts(
        "election-iran-2009.csv", lst)[:4] == \
        [1131111, 16920, 7246, 837858]


def test_problem2():
    assert fraud_detection.ones_and_tens_digit_histogram(
        [127, 426, 28, 9, 90]) == \
        [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]


def test_problem3():
    assert fraud_detection.mean_squared_error([1, 4, 9], [6, 5, 4]) == 17.0


def test_problem6():
    lst = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    lst = fraud_detection.extract_election_vote_counts(
        "election-iran-2009.csv", lst)
    histogram = fraud_detection.ones_and_tens_digit_histogram(lst)
    assert abs(fraud_detection.calculate_mse_with_uniform(histogram)
               - 0.000739583333333) < 0.0000001
