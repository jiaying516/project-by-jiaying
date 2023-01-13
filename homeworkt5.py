import graphviz

# Initialize the graph
g = graphviz.Digraph(format='png')

# Add nodes for each element in the heap
for i in range(heap.size):
    node = heap.get_node(i)
    g.add_node(str(node.key))

# Add edges between nodes
for i in range(heap.size):
    node = heap.get_node(i)
    # Add an edge to the parent
    parent_index = heap.get_parent(i)
    if parent_index >= 0:
        parent_node = heap.get_node(parent_index)
        g.add_edge(str(node.key), str(parent_node.key))
    # Add an edge to the left child
    left_child_index = heap.get_left_child(i)
    if left_child_index < heap.size:
        left_child_node = heap.get_node(left_child_index)
        g.add_edge(str(node.key), str(left_child_node.key))
    # Add an edge to the right child
    right_child_index = heap.get_right_child(i)
    if right_child_index < heap.size:
        right_child_node = heap.get_node(right_child_index)
        g.add_edge(str(node.key), str(right_child_node.key))

# Render the graph to a file
g.render('heap.png')