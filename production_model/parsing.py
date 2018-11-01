from production import IF, OR, AND, THEN

def make_fact(row):
    # F1: 'opus is a penguin'
    mark, fact = row.split(':')
    return mark.strip(), fact.strip()

def make_rule(row, facts):
    mark, rule = row.split(':')
    conditions, consequence = rule.split('=>')
    conditions = [c.strip() for c in conditions.split(',')]
    conditions = [facts[cond] for cond in conditions]
    consequence = facts[consequence.strip()]
    return IF(AND(*conditions), THEN(consequence))

def get_facts(rows):
    return {mark: fact for mark, fact in [make_fact(row) for row in rows]}

def get_rules(rows, facts):
    return [make_rule(row, facts) for row in rows]


def parse_file(filename):
    """
    :param filename:
    :return: pair (list of facts, list of rules)
    """
    facts, rules = None, None
    rows = open(filename, "r").read().splitlines()
    rows = list(filter(None, rows))
    for i in range(len(rows)):
        if rows[i].strip() == 'end':
            facts = get_facts(rows[0:i])
            rules = get_rules(rows[i+1:], facts)
            break

    return facts, rules

