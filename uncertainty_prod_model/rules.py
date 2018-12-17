from enum import Enum


class Mod(Enum):
    AND = 1
    OR = 2
    NOT = 3

class Rule:
    def __init__(self, name, condition, consequence, likelihood=1.0, rule_type = Mod.AND):
        self.name = name
        self.condition = condition
        self.consequence = consequence
        self.likelihood = likelihood
        self.rule_type = rule_type

    def calc(self):
        if self.rule_type == Mod.NOT:
            CF = 1 - self.condition[0].CF
        else:
            if self.rule_type == Mod.AND:
                CF_parents = min([p.CF for p in self.condition])
            else:
                CF_parents = max([p.CF for p in self.condition])
            CF = self.likelihood * CF_parents

        self.consequence.add_CF(CF)

