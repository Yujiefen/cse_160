# Name: ...
# CSE 160 21wi Final Exam - Part 1
# Be sure you also complete Part 2, found in Gradescope!


# Problem 1
def get_student_info(courses):
    '''
    Takes a list of dictionaries containing student grades and creates a
    dictionary with a key for each student that maps to a list containing two
    values: the total number of grades that student received, and the average
    of those grade values.

    Arguments:
      courses: a list of dictionaries mapping student names to float grades

    Returns: a dictionary mapping student names to a list containing the total
    number of grades that student received and their grade average
    '''
    d = {}
    for course in courses:
        for name in course:
            if name not in d:
                d[name] = [0, 0]
            d[name][0] += 1
            d[name][1] += course[name]
    for key in d:
        d[key][1] = d[key][1] / d[key][0]
    return d


def test_get_student_info():
    assert get_student_info([{"Zoe": 3.6}]) == {"Zoe": [1, 3.6]}
    assert get_student_info([]) == {}
    input1 = [{"Zoe": 3.0, "Jack": 3.8, "Amanda": 3.0},
              {"Zoe": 3.5, "David": 2.8},
              {"Zoe": 4.0, "David": 4.0, "Amanda": 3.4, "Joely": 3.1}]
    output1 = {'Zoe': [3, 3.5], 'Jack': [1, 3.8], 'Amanda': [2, 3.2],
               'David': [2, 3.4], 'Joely': [1, 3.1]}
    assert get_student_info(input1) == output1


# Problem 2
def sorted_zoos(given_zoo, zoo_dict):
    '''
    Takes a zoo name and a zoo dictionary mapping zoo names to the set of
    animals that zoo contains. Calculates and returns the list of other zoo
    names sorted by the number of animals those zoos have in common with the
    given zoo, in order from largest to smallest. In the case of a tie, the
    zoos are sorted alphabetically by name instead. The output should not
    include the given_zoo. You can assume given_zoo will be a valid key of
    zoo_dict.

    Arguments:
      given_zoo: a zoo name
      zoo_dict: a dictionary mapping zoo names to sets of animals they contain

    Returns: a list of zoo names
    '''
    lst = []
    for zooname in zoo_dict:
        cnt = 0
        if zooname == given_zoo:
            continue
        for animal in zoo_dict[zooname]:
            if animal in zoo_dict[given_zoo]:
                cnt += 1
        lst.append([zooname, cnt])
    lst.sort(key=lambda x: (-x[1], x[0]))
    res = [x[0] for x in lst]
    return res



def test_sorted_zoos():
    zoo_dict1 = {"Woodland Park": {"bear"},
                 "zooB": {"bear"},
                 "zooA": {"squirrel"}}
    zoo_dict2 = {"Woodland Park": {"bear", "squirrel", "cheetah", "frog"},
                 "zooB": {"bear", "squirrel", "cheetah", "frog"},
                 "zooA": {"bear", "squirrel"}}
    assert sorted_zoos("Woodland Park", zoo_dict1) == ["zooB", "zooA"]
    assert sorted_zoos("zooA", zoo_dict1) == ["Woodland Park", "zooB"]
    assert sorted_zoos("Woodland Park", zoo_dict2) == ["zooB", "zooA"]


# Problem 3
def office_hour_queue(student_dict, time_began):
    '''
    Takes a dictionary mapping student names to their arrival time and an
    office hour starting time. The function returns a list of student names
    sorted by their arrival time. If students have the same arrival time,
    ties should be broken by alphabetical order. Students that arrived
    60 minutes or more after office hours started should not be included in
    the output.

    Arguments:
      student_dict: a dictionary mapping string student names to 24-hour
                    arrival time strings
      time_began: a string representing the starting time of office hours

    Returns: a list of student names
    '''
    lst = []
    time_began = 60 * int(time_began.split(':')[0]) + int(time_began.split(':')[1])
    for name in student_dict:
        t = student_dict[name]
        t = 60 * int(t.split(':')[0]) + int(t.split(':')[1])
        if t < time_began + 60:
            lst.append([name, t])
    lst.sort(key=lambda x: (x[1], x[0]))
    res = [x[0] for x in lst]
    return res




def test_office_hour_queue():
    assert office_hour_queue({'Mia': '15:00', 'Maya': '15:00'}, '15:00') ==\
        ['Maya', 'Mia']
    assert office_hour_queue({'Emma': '16:00', 'George': '15:00'}, '15:00') ==\
        ['George']
    times1 = {'Elizabeth': '9:45', 'Jane': '9:30', 'Caroline': '10:30',
              'Lydia': '10:20', 'Kitty': '10:20', 'Mary': '9:35'}
    assert office_hour_queue(times1, '9:30') == ['Jane', 'Mary', 'Elizabeth',
                                                 'Kitty', 'Lydia']


def main():
    test_get_student_info()
    test_sorted_zoos()
    test_office_hour_queue()


if __name__ == "__main__":
    main()
