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

    def addCF(self, CF):
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
    def __init__(self, rules, nodes, key_facts):
        self.rules = rules
        # dictionary maybe
        self.nodes = nodes
        # ["notPass", "passInTime", "passOnRetake", "passOnCommission"]
        self.key_facts = key_facts
        self.likilihoods = {
            "rule1": 0.99,
            "rule2": 0.95
        }

    def mainloop(self):
        for rule in self.rules:
            fact_name = str(rule.consequence)
            if fact_name not in self.nodes:
                self.nodes[fact_name] = GraphNode(fact_name)
            rule.calc()

    def get_result(self):
        return [x for x in self.nodes if str(x) in self.key_facts]

    @staticmethod
    def get_instance(facts):
        fact_names = get_graph_facts()
        existing_fact_names = [str(f) for f in facts]
        for f in fact_names:
            if f not in existing_fact_names:
                facts.append(GraphNode(f))
        key_facts = get_graph_key_facts()
        rules = get_graphs_rules()

        return ProductionSystem(rules, facts, key_facts)