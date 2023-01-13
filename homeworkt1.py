def get_parent(self, i): 
    #Returns the index of the parent node of the node at index i
    return (i - 1) // 2
def get_left_child(self, i):
    #Returns the index of the left child node of the node at index i
    return 2 * i + 1
def get_right_child(self, i): 
    #Returns the index of the right child node of the node at index i
    return 2 * i + 2