
def func1(rules, updates):
    orderingRules = {}
    correctUpdates = []

    for index, rule in enumerate(rules):

        if orderingRules.get(rule[0], None) is None:
            orderingRules[rule[0]] = []
        else:
            orderingRules[rule[0]].append(rule[1])

    for update in updates:
        for index in range(len(update)):
            if orderingRules.get(update[index], None) is None:
                continue
            else:





