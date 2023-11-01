import itertools
import networkx as nx
def is_dom_set(G, D):
    """
    Returns a boolean whether the subset of G is a dominant set or not.
    """
    edges = G.edges
    V = G.nodes
    is_dom = False
    for d in D:
        for v in V:
            if v not in D: #and len(D) != 1: # verifies if node is in subset D, if not, verifies if its adjacent to any another node in the set
                for d2 in D:
                    if (d2,v) in edges or (v,d2) in edges: # checks if nodes are adjacent
                        is_dom = True
                        break
                    else:
                        is_dom = False
                if is_dom == True:
                    continue
                else: 
                    return False          
    return True

def find_dom_sets(G):
    """
    Finds all possible dominating sets in a given graph G. 
    """
    nodes_arr = G.nodes
    subsets = [list(S) for l in range(0, len(nodes_arr)) for S in itertools.combinations(nodes_arr, l+1)] 
    dom_sets = []

    for D in subsets: 
        if len(D) == len(G):
            dom_sets.append(tuple(D))
            continue

        if nx.is_dominating_set(G, tuple(D)):
            dom_sets.append(tuple(D)) 
    return dom_sets

def find_minimum_dom_sets(G):
    """
    Finds all the minimum dominant sets in a given graph G.
    """
    dom_sets = find_dom_sets(G)
    min_len = min([len(x) for x in dom_sets])
    for x in dom_sets:
        if len(x) == min_len:
            min_sets = x
            break
    # min_sets = [x for x in dom_sets if len(x) == min_len]
    # return min_sets[1]
    return min_sets