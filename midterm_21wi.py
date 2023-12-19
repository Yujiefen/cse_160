# Name: Yujie Feng
# CSE 160
# Winter 2021
# Midterm Exam


# Problem 1
def check_oddeven(num_list):
    '''
    Check if a list of integer lists contain strictly positive, alternating odd
    and even values for the format: [odd, even, odd, even, ...]. The empty list
    is considered in the correct oddeven format. 0 should be treated as even.

    Arguments:
        num_list: a list of zero or more lists. Each list holds zero or more
          integers

    Returns: a boolean value indicating if the input is formatted correctly
    '''
    # your solution code should start here
    if len(num_list) > 0:
        for i in range(len(num_list)):
            for j in range(len(num_list[i])):
                if j % 2 == 0 and num_list[i][j] % 2 == 0:
                    return False
                elif j % 2 == 1 and num_list[i][j] % 2 == 1:
                    return False
        return True
    else:
        return True


assert check_oddeven([[1, 2, 3]]) is True
assert check_oddeven([[2]]) is False
assert check_oddeven([[1, 0, 1], [1, 2, 4, 0]]) is False

# Problem 2


def student_grades(name, grades):
    '''
    Takes a student's name as a string and a list of grades as floats, and
    writes the name and the average of the grades (as a float) to the first and
    second lines (respectively) of a file called grades.txt. grades.txt should
    be in the same location as this code file. An empty list of grades can be
    assumed to have an average of 0.0 . Your solution cannot use the mean()
    function.

    Arguments:
        name: string representing student's name
        grades: a list of zero or more numbers representing grades

    Returns: None, but the function should create a file
    called "grades.txt" with the desired output as a side-effect.
    '''
    # your solution code should start here
    file = open('grades.txt', 'w')
    sum = 0
    if len(grades) > 0:
        for grade in grades:
            sum = sum + grade
        average = sum / (len(grades))
    else:
        average = 0.0
    file.write(name + '\n')
    file.write(str(average) + '\n')
    file.close()


student_grades("Rex Lapis", [1.0, 2.0, 3.0, 4.0, 5.0])
file = open("grades.txt")
assert file.read() == "Rex Lapis\n3.0\n"
student_grades("AB", [5.4, 3.5, 6.7, 9.2, 3.4])
file = open("grades.txt")
assert file.read() == "AB\n5.64\n"
file.close()

# Problem 3


def counts_of_char(words, character):
    '''
    Counts the number of occurrences of a character within each of a list of
    strings. The count for an empty string specifically should be -1. Your
    solution cannot use the count() function.

    Arguments:
        words: a list of zero or more strings
        character: a string of length 1

    Returns: A list of zero or more integers where the value at index i is the
    number of occurrences of the given character in the string at words[i].
    '''
    # your solution code should start here
    counts_of_char = 0
    list_of_counts = []
    for word in words:
        if len(word) == 0:
            counts_of_char = -1
        else:
            for letter in word:
                if letter == character:
                    counts_of_char = counts_of_char + 1
        list_of_counts.append(counts_of_char)
        counts_of_char = 0
    return list_of_counts


assert counts_of_char([], '0') == []
assert counts_of_char(["0000", "0111", "0", "000", "00", "0"], '0') == [4, 1, 1, 3, 2, 1]
assert counts_of_char(["0000", "0111", "0", "000", "00", "0"], 'a') == [0, 0, 0, 0, 0, 0]
assert counts_of_char(['', '000', '0001'], '0') == [-1, 3, 3]


# Problem 4
def get_initials(name_list):
    '''
    Takes a list of names and returns a list of initialized versions of those
    names. An initial is just the first character of a word and then a period.
    Names are made up of one or two words only. For names with two words,
    separate the initials with a single space.

    Arguments:
        name_list: a list of zero or more strings.
            Each string contains only letters and spaces, and is comprised of
            one or two words. Words are separated by a single space.

    Returns: A list of strings representing the initialized versions of
    name_list.
    '''
    # your solution code should start here
    res = []
    for name in name_list:
        sp = name.split()
        lst = []
        for s in sp:
            lst.append(s[0] + '.')
        res.append(' '.join(lst))
    return res


assert get_initials([]) == []
assert get_initials(["sherry"]) == ["s."]
assert get_initials(["Paris Hilton", "paris hilton", "jin"]) == ["P. H.", "p. h.", "j."]


# Problem 5
def replacer(lst, value, replacement):
    '''
    Replaces all instances of a value in the provided lst with an alternate
    list of values (replacement). The value is not guaranteed to occurr inside
    of lst, nor is replacement guaranteed to be of any particular length.

    Arguments:
        lst: a list of zero or more immutable values
        value: a single immutable value
        replacement: a list of zero or more immutable values

    Returns: a list of zero or more immutable values
    '''
    # your solution code should start here
    res = []
    for num in lst:
        if num == value:
            res.extend(replacement)
        else:
            res.append(num)
    return res


assert replacer([1, 2, 3], 0, ["never"]) == [1, 2, 3]
assert replacer([1, 2], 1, [4, 5, 6]) == [4, 5, 6, 2]
assert replacer([1, 1, 1], 1, []) == []
assert replacer([1, 0, 1, 0, 1, 0], 0, [2, 3]) == [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ANSWER the following questions as COMMENTS

# (1 pt) Did you work on this quiz alone or collaborate with others?
# Collaboration
# If you collaborated with others, list full names and UWNetIDs
# of everyone you collaborated with.
# Yuhui Xiang， 1762441
