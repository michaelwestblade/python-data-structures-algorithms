class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list.keys() or vertex2 not in self.adj_list.keys():
            return False
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
        return True

    def remove_edge(self,vertex1, vertex2):
        if vertex1 not in self.adj_list.keys() or vertex2 not in self.adj_list.keys():
            return False

        try:
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)
        except ValueError as e:
            print(e)
            pass
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            return False

        for other_vertex in self.adj_list[vertex]:
            self.adj_list[other_vertex].remove(vertex)

        del self.adj_list[vertex]
        return True

    def print_graph(self):
        for vertex in self.adj_list.keys():
            print(vertex, ":", self.adj_list[vertex])

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "A")

my_graph.print_graph()

my_graph.remove_edge("A", "B")
my_graph.remove_edge("A", "D")
my_graph.print_graph()

print("BEFORE D REMOVED")
my_graph.remove_edge("B", "C")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "D")

my_graph.print_graph()

print("D REMOVED")
my_graph.remove_vertex("D")
my_graph.print_graph()