class Part():
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def __str__(self) -> str:
        return f'x:{self.x},m:{self.m},a:{self.a},s:{self.s}'
    
    def get_category_rating(self, category):
        match category:
            case 'x': return self.x
            case 'm': return self.m
            case 'a': return self.a
            case 's': return self.s

    def get_total_rating(self):
        return self.x + self.m + self.a + self.s


def process_input(input: str):
    workflows_part, parts_part = input.rstrip().split('\n\n')

    workflows = dict()
    for w in workflows_part.split('\n'):
        workflow_name, rules_part = w.split('{')
        rules = rules_part[:-1].split(',')
        workflow_value = []
        for rule in rules:
            if ':'in rule:
                colon_i = rule.index(':')
                workflow_value.append((rule[0], rule[1], int(rule[2:colon_i]), rule[colon_i+1:]))
            else:
                workflow_value.append(rule)
        workflows[workflow_name] = workflow_value
        
    parts = set()
    for l in parts_part.split('\n'):
        l = l.replace('=', ',')[1:-1].split(',')
        parts.add(Part(int(l[1]), int(l[3]), int(l[5]), int(l[7])))

    return workflows, parts

def compare(part_value, comparison_symbol, comparison_value):
    assert comparison_symbol in '<>', 'invalid comparison symbol'
    if comparison_symbol == '>':
        return part_value > comparison_value
    else:
        return part_value < comparison_value

def process_workflow(workflow, part: Part) -> str:
    '''Return rules key'''
    for wf in workflow:
        print(wf, type(wf))
        if type(wf) == str:
            return wf
        else:
            category, lt_gt, comp_value, forward_rule = wf
            if compare(part.get_category_rating(category), lt_gt, comp_value):
                return forward_rule
            else:
                continue
    assert False, 'faulty workflow'


def part1(input):
    parts: set[Part]
    workflows, parts = process_input(input)
    total = 0
    for part in parts:
        workflow = process_workflow(workflows['in'], part)
        while workflow not in 'AR':
            workflow = process_workflow(workflows[workflow], part)
        if workflow == 'A':
            total += part.get_total_rating()
    return total