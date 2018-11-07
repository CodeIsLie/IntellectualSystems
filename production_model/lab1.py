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


def apply_forward_chain(rules, facts):
    init_facts = facts
    final_facts = forward_chain(rules, facts)
    print("input facts: {}".format(init_facts))
    print("consequent facts: {}".format(set(final_facts) - set(init_facts)))


facts, rules = parse_file("data.txt")
# backward chain
pretty_goal_tree(backchain_to_goal_tree(rules, 'гость - Тралл'))
# pretty_goal_tree(backchain_to_goal_tree(rules, 'гость - Нелтарион'))
# pretty_goal_tree(backchain_to_goal_tree(rules, 'гость - Вол\'Джин'))
# forward chain
# apply_forward_chain(rules, [facts['F18'], facts['F25'], facts['F43']])
# apply_forward_chain(rules, [facts['F23'], facts['F24'], facts['F43']])
# apply_forward_chain(rules, [facts['F19'], facts['F33'], facts['F35'], facts['F49'], facts['F44']])
