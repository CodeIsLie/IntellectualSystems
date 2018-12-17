"""
stanford certainty factor production model
"""

from rules import *
from graphsData import *

class GraphNode:
    def __init__(self, name, CF = None):
        self.name = name
        self.CF = CF
        self.calculated = False

    def add_CF(self, CF):
        if self.calculated:
            CF1 = self.CF
            CF2 = CF
            self.CF = CF1 + CF2 - CF1*CF2 if CF1 > 0 and CF2 > 0 else\
                           CF1 + CF2 + CF1*CF2 if CF1 < 0 and CF2 < 0 else\
                           (CF1 + CF2)/(1 - min(abs(CF1), abs(CF2)))
        else:
            self.CF = CF

        self.calculated = True

    def __str__(self):
        return self.name


class ProductionSystem:
    def __init__(self, rules, facts, key_facts):
        self.rules = rules
        # dictionary maybe
        self.facts = facts
        self.key_facts = key_facts
        self.likelihoods = {
            "rule1": 0.99,
            "rule2": 0.95
        }

    def mainloop(self):
        for rule in self.rules:
            rule.calc()

    def get_result(self):
        return [y for x, y in self.facts.items() if str(x) in self.key_facts]

    @staticmethod
    def get_instance(facts):
        fact_names = get_graph_facts()
        facts = {str(f): f for f in facts}
        for f in fact_names:
            if f not in facts:
                facts[f] = (GraphNode(f))
        key_facts = get_graph_key_facts()
        rules = [Rule(r.name, [facts[c] for c in r.condition],
                      facts[r.consequence], r.likelihood) for r in get_graphs_rules()]

        return ProductionSystem(rules, facts, key_facts)