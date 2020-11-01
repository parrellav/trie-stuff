import copy  # For deep copy if needed

class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        """
        Constructor
        :param data : vertex
        """
        self.vertex = data
        self.next = None


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, vertices):
        """
        Constructor
        :param vertices : Total vertices in a graph
        """
        self.V = vertices
        self.graph = [None] * self.V

        # Function to add an edge in an undirected graph

    def add_edge(self, source, destination):
        """
        add edge
        :param source: Source Vertex
        :param destination: Destination Vertex
        """

        # Adding the node to the source node
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        # Adding the source node to the destination if undirected graph

        # Intentionally commented the lines
        #node = AdjNode(source)
        #node.next = self.graph[destination]
        #self.graph[destination] = node

    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def bfs(my_graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a queue for BFS
    queue = []

    # Result string
    result = ""

    # Mark the source node as
    # visited and enqueue it
    queue.append(source)
    visited[source] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        source = queue.pop(0)
        result += str(source)

        # Get all adjacent vertices of the
        # dequeued vertex source. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                queue.append(data)
                visited[data] = True
            my_graph.graph[source] = my_graph.graph[source].next

    return result


def their_dfs(my_graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a string
    """

    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a stack for DFS
    stack = []

    # Result string
    result = ""

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            my_graph.graph[source] = my_graph.graph[source].next

    return result

def dfs(graph, source):
    result = str(source)
    for i in graph.graph:
        current = i
        while current:
            if current.vertex:
                result += str(current.vertex)
            current = current.next

    return result


def their_transpose(my_graph):
    """
    Transpose the given graph
    :param graph: The graph
    :return: a new transposed graph of the given graph
    """

    new_graph = Graph(my_graph.V)  # Creating a new graph

    for source in range(my_graph.V):

        while my_graph.graph[source] is not None:

            destination = my_graph.graph[source].vertex
            # Now the source is destination and vice versa
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph

def transpose(graph):
    """
    Transpose the given graph
    :param graph: The graph
    :return: a new transposed graph of the given graph
    """

    new_graph = Graph(graph.V)  # Creating a new graph

    for source in range(graph.V):
        node = graph.graph[source]
        while node is not None:
            new_graph.add_edge(node.vertex, source)
            node = node.next

    return new_graph


def find_all_paths_recursive(graph, source, destination, path, paths, visited):
    path.append(source)
    visited[source] = True

    if source == destination:
        paths.append(copy.deepcopy(path))
    else:
        while graph.graph[source] is not None:
            i = graph.graph[source].vertex
            if not visited[i]:
                find_all_paths_recursive(graph, i, destination, path, paths, visited)
            graph.graph[source] = graph.graph[source].next
    path.pop()
    visited[source] = False

def find_all_paths(graph, source, destination):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """
    paths = []
    single_path = []
    visited = [False] * graph.V


    find_all_paths_recursive(graph, source, destination, single_path, paths, visited)

    return paths

def number_of_nodes(graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """

    # Write your code here!
    pass
# Main program
if __name__ == "__main__":

    V = 5  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()
