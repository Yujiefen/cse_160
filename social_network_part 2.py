# Name: Yujie Feng
# CSE 160
# Homework 5


import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

###
#  Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
# (Your code for Problem 1a goes here.)
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_practice_graph(practice_graph)


###
#  Problem 1b
###

rj = nx.Graph()
# (Your code for Problem 1b goes here.)
rj.add_edge("Nurse", "Juliet")
rj.add_edge("Juliet", "Capulet")
rj.add_edge("Juliet", "Tybalt")
rj.add_edge("Capulet", "Tybalt")
rj.add_edge("Juliet", "Friar Laurence")
rj.add_edge("Juliet", "Romeo")
rj.add_edge("Romeo", "Friar Laurence")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Benvolio", "Montague")
rj.add_edge("Escalus", "Montague")
rj.add_edge("Romeo", "Mercutio")
rj.add_edge("Escalus", "Mercutio")
rj.add_edge("Escalus", "Paris")
rj.add_edge("Paris", "Mercutio")
rj.add_edge("Capulet", "Escalus")
rj.add_edge("Capulet", "Paris")


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
# draw_rj(rj)


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    name_set = set()
    friends_set = friends(graph, user)
    for name in friends_set:
        name_set = name_set | friends(graph, name)
    name_set = name_set - friends_set - {user}
    return set(sorted(name_set))


def common_friends(graph, user1, user2):
    """Finds and returns the set of friends that user1 and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    return friends(graph, user1) & friends(graph, user2)


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    common_friends_dict = {}
    for element in sorted(friends_of_friends(graph, user)):
        common_friends_dict[element] = len(common_friends(graph,
                                           user, element))
    return common_friends_dict


def number_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    key_val_list = []
    for (key, val) in map_with_number_vals.items():
        key_val_list.append((key, val))
    sorted_key_list = sorted(key_val_list, key=itemgetter(0))
    sorted_val_list = sorted(sorted_key_list, key=itemgetter(1), reverse=True)
    key_list = []
    for element in sorted_val_list:
        key_list.append(itemgetter(0)(element))
    return key_list


def recommend_by_number_of_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    common_friends_dict = number_of_common_friends_map(graph, user)
    return number_map_to_sorted_list(common_friends_dict)


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    influence_map_dict = {}
    influence_score = 0
    for element in recommend_by_number_of_common_friends(graph, user):
        for name in common_friends(graph, user, element):
            influence_score += 1/len(friends(graph, name))
        influence_map_dict[element] = influence_score
        influence_score = 0
    return influence_map_dict


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    influence_map_list = []
    for (key, val) in influence_map(graph, user).items():
        influence_map_list.append((key, val))
    sorted_influence_map_key_list = sorted(influence_map_list,
                                           key=itemgetter(0))
    sorted_influence_map_val_list = sorted(sorted_influence_map_key_list,
                                           key=itemgetter(1), reverse=True)
    influence_list = []
    for element in sorted_influence_map_val_list:
        influence_list.append(itemgetter(0)(element))
    return influence_list


###
#  Problem 4
###

print("Problem 4:")
print()

unchanged_list = []
changed_list = []
for element in list(rj.nodes()):
    if recommend_by_number_of_common_friends(rj, element) == \
       recommend_by_influence(rj, element):
        unchanged_list.append(element)
    else:
        changed_list.append(element)
print("Unchanged Recommendations: " + str(sorted(unchanged_list)))
print("Changed Recommendations: " + str(sorted(changed_list)))


###
#  Problem 5
###

facebook = nx.Graph()
facebook_file = open("facebook-links.txt")
line = facebook_file.readlines()
for element in line:
    ids = element.split()
    facebook.add_edge(int(ids[0]), int(ids[1]))

assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090

###
#  Problem 6
###
print()
print("Problem 6:")
print()

users_list = sorted(list(facebook.nodes))
for element in users_list:
    if element % 1000 == 0:
        print(str(element) + " (by number_of_common_friends): " + str(recommend_by_number_of_common_friends(facebook, element)[0:10]))

###
#  Problem 7
###
print()
print("Problem 7:")
print()

# (Your Problem 7 code goes here.)
users_list = sorted(list(facebook.nodes))
for element in users_list:
    if element % 1000 == 0:
        print(str(element) + " (by influence): " + str(recommend_by_influence(facebook, element)[0:10]))

###
#  Problem 8
###
print()
print("Problem 8:")
print()

# (Your Problem 8 code goes here.)
same = 0
different = 0
users_list = sorted(list(facebook.nodes))
for element in users_list:
    if element % 1000 == 0:
        common = recommend_by_number_of_common_friends(facebook, element)[0:10]
        influence = recommend_by_influence(facebook, element)[0:10]
        if common == influence:
            same += 1
        else:
            different += 1
print("Same: " + str(same))
print("Different: " + str(different))

###
#  Collaboration: Yuhui Xiang
###

# ... Write your answer here, as a comment (on lines starting with "#").
