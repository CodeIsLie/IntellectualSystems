from rules import *


def get_graph_facts():
    facts = [
        "Сдал лабы",
        "Сдал опросы",
        "Зачёт",
            ]
    return facts

def get_graph_key_facts():
    key_facts = [
            "Зачёт"
                ]
    return key_facts

def get_graphs_rules():
    rules = []
    rules.append(
        Rule("Сдача", ["Сдал лабы", "Сдал опросы"], "Зачёт", 0.99))
    return rules
