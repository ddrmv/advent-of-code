import graphviz
import heapq

def process_input(input):
    graph = dict()
    for line in input.rstrip().split('\n'):
        l = line.split(' ')
        graph[l[0][:-1]] = list(node for node in l[1:])
    return graph

def undirected_to_linked_list(graph: dict[str, list[str]]):
    extra_nodes: dict[str, list[str]]
    extra_nodes = dict()
    for key, links in graph.items():
        for link in links:
            if link not in graph.keys():
                if link not in extra_nodes.keys():
                    extra_nodes[link] = []
                    extra_nodes[link].append(key)
                else:
                    if key not in extra_nodes[link]:
                        extra_nodes[link].append(key)
            else:
                if key not in graph[link]:
                    graph[link].append(key)
    for key, links in extra_nodes.items():
        graph[key] = links


def unplug_connection(g: dict[str, list[str]], a: str, b: str):
    if a in g.keys() and b in g[a]:
        if len(g[a]) > 1:
            g[a].remove(b)
        else:
            g.pop(a, None)
    if b in g.keys() and a in g[b]:
        if len(g[b]) > 1:
            g[b].remove(a)
        else:
            g.pop(b, None)


def count_nodes(g, node):
    counter = 0
    q = [node]
    seen = {node}
    heapq.heapify(q)
    while q:
        node = heapq.heappop(q)
        counter += 1
        for link in g[node]:
            if link in seen:
                continue
            else:
                heapq.heappush(q, link)
                seen.add(link)
    return counter


def part1(input):
    g = process_input(input)
    undirected_to_linked_list(g)

    # gv = graphviz.Digraph('ForSanta', filename='for_santa.gv')
    # gv.attr(overlap='true')
    # gv.attr(ratio='0.7')
    # for key in g:
    #     gv.node(key)
    # for key, links in g.items():
    #     for link in links:
    #         gv.edge(key, link)
    # gv.view()
    # use_eyes()
    # links to unplug: jff zns, qmr kzx, fts nvb

    unplug_connection(g, 'jff', 'zns')
    unplug_connection(g, 'qmr', 'kzx')
    unplug_connection(g, 'fts', 'nvb')
    a = count_nodes(g, 'jff')
    b = count_nodes(g, 'zns')
    return a * b