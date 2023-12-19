# Name: ...
# CSE 160
# Homework 5

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

###
#  Problem 1a
####

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("D", "C")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")
# (Your code for Problem 1a goes here.)


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

# rj = nx.Graph()
# (Your code for Problem 1b goes here.)


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
rj = nx.Graph()
rj.add_edge("Nurse", "Juliet")
rj.add_edge("Tybalt", "Juliet")
rj.add_edge("Capulet", "Juliet")
rj.add_edge("Friar Laurence", "Juliet")
rj.add_edge("Romeo", "Juliet")
rj.add_edge("Tybalt", "Capulet")
rj.add_edge("Friar Laurence", "Romeo")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Romeo", "Mercutio")
rj.add_edge("Benvolio", "Montague")
rj.add_edge("Montague", "Escalus")
rj.add_edge("Escalus", "Mercutio")
rj.add_edge("Escalus", "Paris")
rj.add_edge("Escalus", "Capulet")
rj.add_edge("Paris", "Capulet")
rj.add_edge("Paris", "Mercutio")
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

    friends_1 = friends(graph, user) | set([user])
    friends_2 = set()
    for i in friends_1:
        friends(graph, i)
        friends_2 |= friends(graph, i)
    fridens_3 = friends_2 - friends_1
    return fridens_3


def common_friends(graph, user1, user2):
    """Finds and returns the set of friends that user1 and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    common_1 = friends(graph, user1)
    common_2 = friends(graph, user2)
    return common_1 & common_2


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
    friends_2 = friends_of_friends(graph, user)
    d = {}
    for i in friends_2:
        d[i] = len(common_friends(graph, user, i))
    return d


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
    lt = list(map_with_number_vals)
    for i in range(len(lt)):
        for j in range(i + 1, len(lt)):
            if map_with_number_vals[lt[i]] < map_with_number_vals[lt[j]]:
                lt[i], lt[j] = lt[j], lt[i]
            elif map_with_number_vals[lt[i]] == map_with_number_vals[lt[j]]:
                if lt[i] > lt[j]:
                    lt[i], lt[j] = lt[j], lt[i]
            else:
                pass
    return lt


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
    d = number_of_common_friends_map(graph, user)
    return number_map_to_sorted_list(d)

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
    available = friends_of_friends(graph, user)
    d = {}
    for i in available:
        common = common_friends(graph, user, i)
        n = 0
        for j in common:
            n += 1/len(friends(graph, j))
        d[i] = n

        # common_friends(graph,user,i)
    return d


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    d = influence_map(graph, user)
    return number_map_to_sorted_list(d)


###
#  Problem 4
###

print("Problem 4:")
print()

# (Your Problem 4 code goes here.)
nodes_rj = list(rj.nodes)
similar = []
difference = []
for idx in nodes_rj:
    one = recommend_by_number_of_common_friends(rj, idx)
    two = recommend_by_influence(rj, idx)
    # print(idx)
    # print("one: ",one)
    # print("two: ", two)

    if one == two:
        similar.append(idx)
    else:
        difference.append(idx)
print("Unchanged Recommendations: ", similar)
print("Changed Recommendations: ", difference)

###
#  Problem 5
###

# (Your Problem 5 code goes here.)

# assert len(facebook.nodes()) == 63731
# assert len(facebook.edges()) == 817090

###
#  Problem 6
###
print()
print("Problem 6:")
print()

# (Your Problem 6 code goes here.)

###
#  Problem 7
###
print()
print("Problem 7:")
print()

# (Your Problem 7 code goes here.)

###
#  Problem 8
###
print()
print("Problem 8:")
print()

# (Your Problem 8 code goes here.)

###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
