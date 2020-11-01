import copy

class Graph2:

    graph_dict = {}
    _vertexes = 0

    def add_edge(self, node, neighbor):
        # increment count for neighbor
        self._vertexes += 1
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbor]
            self._vertexes += 1
        else:
            self.graph_dict[node].append(neighbor)
        if neighbor not in self.graph_dict:
            self.graph_dict[neighbor] = []

    @property
    def vertexes(self):
        return self._vertexes


def bfs(graph, start):
    result = ''
    queue = []
    seen = [False] * graph.vertexes
    queue.append(start)
    seen[start] = True
    while queue:
        vertex = queue.pop(0)
        result += str(vertex)

        for node in graph.graph_dict[vertex]:
            if not seen[node]:
                queue.append(node)
                seen[node] = True

    return result


def dfs(graph, start):
    result = ''
    queue = []
    seen = [False] * graph.vertexes
    queue.append(start)
    while queue:
        vertex = queue.pop()
        if not seen[vertex]:
            result += str(vertex)
            seen[vertex] = True
        if vertex in graph.graph_dict:
            current = graph.graph_dict[vertex]
            for neighbor in current:
                queue.append(neighbor)
    return result


def _find_all_paths_recursive(graph, source, destination, this_path, accum):
    this_path.append(source)
    for node in graph.graph_dict[source]:
        if node == destination:
            my_copy = copy.deepcopy(this_path)
            my_copy.append(node)
            accum.append(my_copy)
        else:
            _find_all_paths_recursive(graph, node, destination, this_path, accum)
    this_path.pop()


def find_all_paths(graph, source, destination):
    paths = []
    this_path = []
    _find_all_paths_recursive(graph, source, destination, this_path, paths)
    return paths
