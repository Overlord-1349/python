from enum import IntEnum, auto
from random import randint
from uuid import uuid4
class edge_direction(IntEnum):
    left = auto()
    right = auto()
    up = auto()
    down = auto()
    undirected = auto()
class edge(object):
    def __init__(self, first_node, second_node, direction=edge_direction.undirected, weight=0):
        self.__uuid = uuid4()
        self.weight=weight
        self.direction=direction
        self.first_node = first_node
        self.second_node = second_node
        if(direction in ( edge_direction.up , edge_direction.left, edge_direction.undirected) ):
            first_node.node_edges.add(self)
        if(direction in ( edge_direction.down , edge_direction.right, edge_direction.undirected) ):
            
            second_node.node_edges.add(self)
    def __str__(self):
        #return "direction: {}, weight: {}".format(str(self.direction), str(self.weight))
        return "first_node: {}, second_node: {}, direction: {}, weight: {}".format(str(self.first_node.value), str(self.second_node.value), str(self.direction), str(self.weight))
    def __del__(self):
        self = None
    def __eq__(self, other_edge):
        if(not isinstance(other_edge, edge)):
            return False
        if(self.first_node == other_edge.first_node and self.second_node == other_edge.second_node and self.weight== other_edge.weight and self.direction == other_edge.direction):
            return True
        return False
    def __ne__(self, other_edge):
        if(not isinstance(other_edge, edge)):
            return True
        if(self.first_node != other_edge.first_node or self.second_node != other_edge.second_node or self.weight != other_edge.weight or self.direction != other_edge.direction):
            return True
        return False

    @property
    def weight(self):
        return self._weight 
    @weight.setter
    def weight(self, value):
        if(not isinstance(value, int) or value not in range(0, 100)):
            raise ValueError('value between 0 and 100 expected')
        self._weight = value

    @property
    def direction(self):
        return self._direction 
    @direction.setter
    def direction(self, value):
        self._direction = edge_direction( value )
    @property
    def first_node(self):
        return self._first_node
    @first_node.setter
    def first_node(self, value):
        self._first_node=value
    @property
    def second_node(self):
        return self._second_node
    @second_node.setter
    def second_node(self, value):
        self._second_node=value
class edges(object):
    def __init__(self):
        self._edges = []
    def __eq__(self, other_edges):
        if (len(self) != len(other_edges)):
            return False
        for i in range(0, len(self)):
            if( self[i] != other_edges[i] ):
                return False
        return True
    def __len__(self):
        return len(self._edges)
    def __getitem__(self, key):
        return self._edges[key]

    def __iter__(self):
        self._index=-1
        return self

    def __next__(self):
        self._index += 1
        if(self._index >= len(self)):
            raise StopIteration
        return self[self._index]
    
    def __str__(self):
        str_rep = ""
        for edg in self:
           str_rep += "{}\n".format(str(edg)) 
        return str_rep
    def add(self, new_edge):
        if(not isinstance(new_edge, edge)):
            TypeError('edge is expected')
        self._edges.append(new_edge)
class node(object):
    def __init__(self, value):
        self.__uuid = uuid4()
        self.value = value
        self._edges = edges()
    def __eq__(self, other_node):
        if(not isinstance(other_node, node)):
            return False
        if(self.value == other_node.value ):#and self.node_edges == other_node.node_edges):
            return True
        return False
    def __str__(self):
        #return "value: {}".format( str(self.value) )
        return "value: {}, edges: [{}]".format( str(self.value), str(self.node_edges) )
    @property
    def node_edges(self):
        return self._edges
    @node_edges.setter
    def node_edges(self, value):
        raise Exception()
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value
 
class nodes(object):
    def __init__(self):
        self._nodes = []
        self._index = -1
    
    def __len__(self):
        return len(self._nodes)
    def __getitem__(self, key):
        return self._nodes[key]

    def __iter__(self):
        self._index = -1
        return self
    def __next__(self):
        self._index += 1
        if(self._index >= len(self)):
            raise StopIteration
        return self[self._index]
    def add(self, new_node):
        self._nodes.append(new_node)
    def __str__(self):
        str_rep = ""
        for nde in self:
            str_rep += "{}\n".format(str(nde))
        return str_rep
class graph(object):
    def __init__(self):
        self._nodes = nodes()
    def add(self, node_value):
        if(not isinstance(node_value, node)):
            node_value = node(node_value)
        self._nodes.add(node_value)
    def find(self, value):
        """finds nodes within """
        if(not isinstance(value, node)):
            value = node(value)
        for nde in self.graph_nodes:
            if(nde == value):
                return nde
        return False
    def exists(self, value):
        return True if (self.find(value)) else False
    @property
    def graph_nodes(self):
        return self._nodes
    @graph_nodes.setter
    def graph_nodes(self, value):
        raise Exception()

gr = graph()
for i in range(5):
    gr.add(node(randint(1,100)))

for i in range(15):
    edge(gr.graph_nodes[randint(0, (len(gr.graph_nodes) -1))], gr.graph_nodes[randint(0, (len(gr.graph_nodes) -1))], edge_direction(randint(1,5)), randint(1, 100) )
print (gr.graph_nodes)

for i in range(30):
    a = randint(0, (len(gr.graph_nodes)-1 ) )
    b = randint(0, (len(gr.graph_nodes)-1 ) )
    print(a, b, (gr.graph_nodes[a] == gr.graph_nodes[b]))

