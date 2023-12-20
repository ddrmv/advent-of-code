import copy

class Rng():
    def __init__(self):
        self.x_gt = 0
        self.x_lt = 4001
        self.m_gt = 0
        self.m_lt = 4001
        self.a_gt = 0
        self.a_lt = 4001
        self.s_gt = 0
        self.s_lt = 4001

    def update_passing_range(self, category, lt_gt, new_val):
        if lt_gt == '<':
            old_val = getattr(self, f'{category}_lt')
            setattr(self, f'{category}_lt', min(new_val, old_val))
        else:
            old_val = getattr(self, f'{category}_gt')
            setattr(self, f'{category}_gt', max(new_val, old_val))

    def update_failing_range(self, category, lt_gt, new_val):
        if lt_gt == '>': # less than x + 1
            old_val = getattr(self, f'{category}_lt')
            setattr(self, f'{category}_lt', min(old_val, new_val + 1))
        else:
            old_val = getattr(self, f'{category}_gt')
            setattr(self, f'{category}_gt', max(old_val, new_val - 1))

    def get_combinations(self):
        product = 1
        for c in ['x', 'm', 'a', 's']:
            product *= getattr(self, f'{c}_lt') - getattr(self, f'{c}_gt') - 1
        return product


def process_input(input: str):
    workflows_part = input.rstrip().split('\n\n')[0]

    workflows = dict()
    for wf in workflows_part.split('\n'):
        wf_name, rules_part = wf.split('{')
        wf_rules = []
        for rule in rules_part[:-1].split(','):
            if ':'in rule:
                i = rule.index(':')
                wf_rules.append((rule[0], rule[1], int(rule[2:i]), rule[i+1:]))
            else:
                wf_rules.append(rule)
        workflows[wf_name] = wf_rules

    return workflows

def traverse_paths(wfs: list, wf: str, rng: Rng):
    '''Traverse and add all subranges that reach A'''
    if wf == 'R':
        return 0
    elif wf == 'A':
        return rng.get_combinations()
    else:
        in_branch = 0
        for rule in wfs[wf]:
            if type(rule) == tuple:
                # this is non-last rule in a workflow
                category, lt_gt, value, wf_key = rule
                new_rng = copy.deepcopy(rng)
                # pass branch, go to new workflow
                new_rng.update_passing_range(category, lt_gt, value)
                in_branch += traverse_paths(wfs, wf_key, new_rng)
                # fail branch, continue in current wf
                rng.update_failing_range(category, lt_gt, value)
                continue
            else:
                # last rule of a workflow
                in_branch += traverse_paths(wfs, rule, rng)
        return in_branch


def part2(input):
    workflows = process_input(input)
    return traverse_paths(workflows, 'in', Rng())