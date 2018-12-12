from enum import Enum


class Mod(Enum):
    AND = 1
    OR = 2

class Rule:
    def calcCF(self):
        return 1


#  combine function comb(CF1, CF2):
#               CF1 + CF2 - CF1CF2 if CF1 > 0 and CF2 > 0 else
#               CF1 + CF2 + CF1CF2 if CF1 < 0 and CF2 < 0 else
#               (CF1 + CF2)/(1 - min(abs(CF1), abs(CF2)))

# MB(H, E) = 1 if P(H) == 1 else (max(P(H|E), P(H)) - P(H)) / (1 - P(H))
# MD(H, E) = 0 if P(H) == 0 else (min(P(H|E), P(H)) - P(H)) / (- P(H))
# CF = (MB - MD) / (1 - min(MB, MD))

class StartRule:
    def __init__(self, name, condition, consequence):
        self.name = name
        self.condition = condition
        self.consequence = consequence
        # self.probability = probability
        # self.type = type

    # probabilities - dictionary from fact name to truly of fact
    def calc(self, probabilities):
        for par in self.condition:
            par.calc_CF()
            # TODO: to think what do with P(H)
            P_H = 1
            p_H_E = probabilities[self.name]
            MB = 1 if P_H == 1 else (max(p_H_E, P_H) - P_H) / (1 - P_H)
            MD = 0 if P_H == 0 else (min(p_H_E, P_H) - P_H) / (1 - P_H)
            CF = (MB - MD) / (1 - min(MB, MD))
            self.consequence.add_CF(CF)

class MidRule:
    def __init__(self, name, condition, consequence, probability=1):
        self.name = name
        self.condition = condition
        self.consequence = consequence
        self.probability = probability
        # self.type = type