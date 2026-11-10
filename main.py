from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        ###TODO
        node = frontier.pop()
        for value in graph[node]:
            if value not in result:
                result.add(value)
                frontier.add(value)
        #break
    return result

def connected(graph):
    ### TODO
    if not graph:
        return False
    start_node = next(iter(graph)) #iterator/pointer is at the beginning and next gives the first key in dict
    results = reachable(graph, start_node)
    return len(graph) == len(results)
    pass

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    if not graph:
        return None
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            component = reachable(graph, node)
            visited.update(component)
            count += 1    
    return count
    ### TODO
    pass
