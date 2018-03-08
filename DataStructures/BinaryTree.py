from random import randint
class Node(object):
    """
    Node class
    """
    def __init__(self, value, left_node=None, right_node=None):
        self.value=value
        self.left_node=left_node
        self.right_node=right_node
    def add_left_node(self, left_node):
        self.left_node=left_node
    def add_right_node(self, right_node):
        self.right_node=right_node
    
    def __str__(self):
        return "{0} -[ L: {1}, R: {2} ]".format(self.value, 'None' if (not self.left_node) else self.left_node.value, 'None' if (not self.right_node) else self.right_node.value )
        
class binary_tree(object):
    """Binary Tree"""
    def add(self, value):
        newNode = Node(value)
        if(not self.root):
            self.root = newNode
        else:
            self._add(self.root, newNode) 
    def merge(self, new_tree):
        self.add(new_tree.value)
        if(new_tree.left_node):
            self.merge(new_tree.left_node)
        if(new_tree.right_node):
            self.merge(new_tree.right_node)  
    def search(self, value):
        """ Recursevely search an element in the tree.
            Returns:
                None if value doesn't exist else the node
        """
        return self._search(self.root, value)
    def delete(self, value):
        self._search(self.root, value, delete=True, parent=None)
    def is_balanced(self):
        return True if (self._len_left_side() == self._len_right_side()) else False
#protected methods 
    def _add(self, parent, newNode):
        if(parent.value == newNode.value):
            pass
        elif(not parent.left_node and parent.value>newNode.value):
            parent.add_left_node(newNode)
        elif(not parent.right_node and parent.value<newNode.value):
            parent.add_right_node(newNode)
        elif(parent.left_node and newNode.value<parent.value ):
            self._add(parent.left_node, newNode)
        elif(parent.right_node and  newNode.value >  parent.value ):
            self._add(parent.right_node, newNode)
        else:
            raise Exception('{0} | {1}'.format(parent, newNode))
    def _search(self, node, searchValue, delete=False, parent=None):
        if(node and node.value==searchValue):
            if(delete):
                self._delete(node, parent)
            return node
        elif(node and searchValue < node.value):
            return self._search(node.left_node, searchValue, delete=delete, parent=node)
        elif (node and searchValue > node.value):
            return self._search(node.right_node, searchValue, delete=delete, parent=node)
        else:
            return None
    def _delete(self, node, parent):
        #simple node deletion.. simple deletion
        delete = False
        if( not parent ):
            self.root = None
            delete=True
        elif(parent.left_node and parent.left_node.value == node.value):
            parent.left_node = None
            delete = True
        elif(parent.right_node and parent.right_node.value == node.value):
            parent.right_node = None
            delete=True 
        if(delete and node.left_node):
            self.merge(node.left_node)
        if(delete and node.right_node):
            self.merge(node.right_node)

    def _len_left_side(self):
        return 0 if (not self.root.left_node ) else self._len(self.root.left_node)         
    def _len_right_side(self):
        return 0 if (not self.root.right_node ) else self._len(self.root.right_node)         
    def _len(self, node):
        count = 1
        if(node and node.left_node):
            count += self._len(node.left_node)
        if(node and node.right_node):
            count += self._len(node.right_node) 
        return count
    def _stringify(self, parent):
        strrep=str(parent)+"\n"
        if(parent.left_node):
            strrep += self._stringify(parent.left_node)
        if(parent.right_node):
            strrep += self._stringify(parent.right_node)
        return strrep
#protected methods
#dunders
    def __init__(self):
        self.root=None
    def __str__(self):
        return str(self._stringify(self.root))
    def __len__(self):
        return self._len(self.root)
#dunders
if __name__=='__main__':
    bt =binary_tree()
    for i in range(10):
        next = chr(randint(33,126))
        print('inserting', next)
        bt.add(next)
    print(bt)
    for i in range(30):
        number = chr(randint(33,126))
        print ("searching {}....".format(number))
        node = bt.search(number)
        if(node):
            print("Bingo! {0} was found".format(node) )
            bt.delete(number)
    print(bt)
    print(len(bt), bt._len_left_side(), bt._len_right_side(), bt.is_balanced())

