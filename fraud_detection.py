import csv
from random import randint
import matplotlib.pyplot as plt


def extract_election_vote_counts(filename, column_names):
    '''
    extract election votes by names
    :param filename:
    :param column_names:
    :return:
    '''
    people_csv = open(filename)
    input_file = csv.DictReader(people_csv)
    lst = []
    for row in input_file:
        for name in column_names:
            try:
                lst.append(int(row[name].replace(',', '')))
            except ValueError:
                lst.append(0)
    return lst


def ones_and_tens_digit_histogram(numbers):
    '''
    calculate a array of histogram statistics of ones and tens digit
    :param numbers:
    :return:
    '''
    lst = [0 for i in range(10)]
    for index in range(10):
        for number in numbers:
            one = number % 10
            ten = (number // 10) % 10
            if index == one:
                lst[index] += 1
            if index == ten:
                lst[index] += 1

    total = sum(lst)
    for i in range(10):
        lst[i] = lst[i] / total
    return lst


def plot_iranian_least_digits_histogram(histogram):
    '''
    plot the iranian digit of histogram
    :param histogram:
    :return:
    '''
    ideal = [0.1 for i in range(10)]
    plt.plot(ideal, label='ideal')
    plt.plot(histogram, color='orange', label='iran')
    plt.title('Distribution of last two digits in Iranian dataset')
    plt.legend(loc='upper left')
    plt.savefig('iran-digits.png')
    plt.show()


def plot_distribution_by_sample_size():
    '''
    plot distribution by the sample size
    :return:
    '''
    plt.clf()
    ideal = [0.1 for i in range(10)]
    plt.plot(ideal, label='ideal')
    sizes = [10, 50, 100, 1000, 10000]
    for size in sizes:
        lst = [randint(0, 99) for i in range(size)]
        histogram = ones_and_tens_digit_histogram(lst)
        plt.plot(histogram, label='size %d' % size)
    plt.legend(loc='upper right')
    plt.savefig('random-digits.png')
    plt.show()


def mean_squared_error(numbers1, numbers2):
    '''
    calculate the mean squared value
    :param numbers1:
    :param numbers2:
    :return:
    '''
    total = 0
    for i in range(len(numbers1)):
        total += (numbers1[i] - numbers2[i]) ** 2
    return total / len(numbers1)


def calculate_mse_with_uniform(histogram):
    '''
    calculate histogram with ideal mean error
    :param histogram:
    :return:
    '''
    ideal = [0.1 for i in range(10)]
    return mean_squared_error(ideal, histogram)


def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    '''
    compare irannian mse to random samples
    :param iranian_mse:
    :param number_of_iranian_samples:
    :return:
    '''
    larger = 0
    less = 0
    for groups in range(10000):
        values = [randint(0, 99) for i in range(number_of_iranian_samples)]
        histogram = ones_and_tens_digit_histogram(values)
        mse = mean_squared_error(histogram, [0.1 for i in range(10)])
        if mse >= iranian_mse:
            larger += 1
        else:
            less += 1
    print('2009 Iranian election MSE:', iranian_mse)
    print('Quantity of MSEs larger than or equal to the 2009'
          ' Iranian election MSE:', larger)
    print('Quantity of MSEs smaller than the 2009 '
          'Iranian election MSE:', less)
    print('2009 Iranian election null hypothesis rejection '
          'level p:', (larger / (larger + less)))


def compare_us_mse_to_samples(us_mse, number_of_us_samples):
    '''
    compare us mse to random samples
    :param us_mse:
    :param number_of_iranian_samples:
    :return:
    '''
    larger = 0
    less = 0
    for groups in range(10000):
        values = [randint(0, 99) for i in range(number_of_us_samples)]
        histogram = ones_and_tens_digit_histogram(values)
        mse = mean_squared_error(histogram, [0.1 for i in range(10)])
        if mse >= us_mse:
            larger += 1
        else:
            less += 1
    print('2008 United States election MSE:', us_mse)
    print('Quantity of MSEs larger than or equal to the 2008 '
          'United States election MSE:', larger)
    print('Quantity of MSEs smaller than the 2008 United States '
          'election MSE:', less)
    print('2008 United States election null hypothesis rejection '
          'level p:', (larger / (larger + less)))


# The code in this function is executed
# when this file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    lst = extract_election_vote_counts("election-iran-2009.csv",
                                       ["Ahmadinejad", "Rezai",
                                        "Karrubi", "Mousavi"])
    histogram = ones_and_tens_digit_histogram(lst)
    plot_iranian_least_digits_histogram(histogram)
    plot_distribution_by_sample_size()
    mse = calculate_mse_with_uniform(histogram)
    compare_iranian_mse_to_samples(mse, len(lst))

    print()
    lst = extract_election_vote_counts("election-us-2008.csv",
                                       ["Obama", "McCain", "Nader", "Barr",
                                        "Baldwin", "McKinney"])
    histogram = ones_and_tens_digit_histogram(lst)
    mse = calculate_mse_with_uniform(histogram)
    compare_us_mse_to_samples(mse, len(lst))


if __name__ == "__main__":
    main()
