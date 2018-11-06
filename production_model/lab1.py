from production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from data import *
import pprint
from production import PASS, FAIL, match, populate, simplify, variables
# from tester import test_offline

from parsing import parse_file

pp = pprint.PrettyPrinter(indent=1)
pprint = pp.pprint


def backchain_to_goal_tree(rules, hypothesis):
    """
    Takes a hypothesis (string) and a list of rules (list
    of IF objects), returning an AND/OR tree representing the
    backchain of possible statements we may need to test
    to determine if this hypothesis is reachable or not.

    This method should return an AND/OR tree, that is, an
    AND or OR object, whose constituents are the subgoals that
    need to be tested. The leaves of this tree should be strings
    (possibly with unbound variables), *not* AND or OR objects.
    Make sure to use simplify(...) to flatten trees where appropriate.
    """

    tree = OR(hypothesis)
    for rule in rules:
        match_res = match(rule.consequent(), hypothesis)
        if match_res is not None:
            or_node = OR()
            tree.append(or_node)
            nodes = populate(rule.antecedent(), match_res)
            if type(nodes) == str:
                nodes = [nodes]
            for i in range(len(nodes)):
                nodes[i] = backchain_to_goal_tree(rules, nodes[i])
            or_node.append(nodes)

    tree = simplify(tree)
    return tree

pretty_goal_tree(backchain_to_goal_tree(zookeeper_rules, 'opus is a penguin'))
# print(parse_file('data.txt')[0])
# print(parse_file('data.txt')[1])
