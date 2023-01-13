def insert(self, key):
    #Inserts a new node with the given key into the priority queue
    # Create a new node with the given key
    new_node = Node(key)
    # If the queue is empty, set the new node as the root
    if self.root is None:
        self.root = new_node
        self.size = 1
        return
    # Find the next available spot in the last level of the tree
    i = 0
    while i < self.size:
        if self.get_left_child(i) >= self.size:
            # The left child is not in the list, so we can use this spot
            break
        elif self.get_right_child(i) >= self.size:
            # The left child is in the list, but the right child is not, so we can use this spot
            break
        # Both children are in the list, so we move to the next node in the last level
        i += 1
    # Set the new node as the left or right child of the found node, depending on which spot is available
    if self.get_left_child(i) >= self.size:
        self.set_left_child(i, new_node)
    else:
        self.set_right_child(i, new_node)
    self.size += 1
    # Fix the heap property by sifting the new node up
    self._sift_up(self.size - 1)

def delMin(self):
    #Removes and returns the node with the minimum key from the priority queue
    if self.root is None:
        # The queue is empty, so there is no minimum node
        return None
    # Store the root node for later
    min_node = self.root
    # Replace the root with the last node in the list
    last_node = self.get_node(self.size - 1)
    self.root = last_node
    # Remove the last node from the list
    self.set_left_child(0, None)
    self.size -= 1
    # Fix the heap property by sifting the new root down
    self._sift_down(0)
    return min_node