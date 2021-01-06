class Graph(object):
    
    def __init__(self, graph_dict=None) -> None:
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def nodes(self):
        return list(self.__graph_dict.keys())
    
    def edges(self):
        return self.__generate_edges()
    
    def add_node(self, node):
        if not self.find_node(node):
            self.__graph_dict[node] = []
    
    def add_edge(self, edge):
        node1, node2 = edge            
        if self.find_node(node1) and self.find_node(node2):
            if node1 not in self.__graph_dict[node2]:
                self.__graph_dict[node2].append(node1)
            if node2 not in self.__graph_dict[node1]:
                self.__graph_dict[node1].append(node2)

    def find_node(self, node):
        return node in self.__graph_dict
    
    def self_pointing_nodes(self):
        self_pointing_nodes = []
        for node, neighbours in self.__graph_dict.items():
            if node in neighbours:
                self_pointing_nodes.append(node)
        return self_pointing_nodes
    
    def get_isolated_nodes(self):
        isolated_nodes = []
        for node in self.__graph_dict:
            if not graph[node]:
                isolated_nodes.append(node)
        return isolated_nodes
    
    def __generate_edges(self):
        edges = []
        for node, neighbours in self.__graph_dict.items():
            for neighbour in neighbours:
                edges.append((node, neighbour))
        return edges
    
    def __str__(self):
        res = "nodes: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
if __name__ == "__main__":
    
    graph = {
        'a': ['c'],
        'b': ['c', 'e'],
        "c" : ["a", "b", "d", "e"],
        "d" : ["c"],
        "e" : ["c", "b"],
        "f" : [],
        "h" : ["h"]
    }

    mygraph = Graph(graph)

    print('All Edges\n',mygraph.edges())
    print('Isolated nodes\n',mygraph.get_isolated_nodes())
    print('Self pointing nodes\n',mygraph.self_pointing_nodes())
    print(mygraph)







