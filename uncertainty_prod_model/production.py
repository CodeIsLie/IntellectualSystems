"""
stanford certainty factor production model
"""

class GraphNode:
    def __init__(self, parents):
        self.parents = parents
        self.CF = None
        self.calculated = False



    def calcCF(self):
        self.calculated = True
        self.CF = max([p.CF for p in self.parents])
        for p in self.parents:
            p.calcCF()