import time

# Initialize the heap
heap = LinkedListHeap()

# Perform a series of insertions and deletions
num_operations = 10000
insertion_times = []
deletion_times = []
for i in range(num_operations):
    # Record the start time
    start_time = time.perf_counter()
    # Insert a new node into the heap
    heap.insert(i)
    # Record the end time and add it to the list
    end_time = time.perf_counter()
    insertion_times.append(end_time - start_time)
    # Record the start time
    start_time = time.perf_counter()
    # Delete the minimum node from the heap
    heap.delMin()
    # Record the end time and add it to the list
    end_time = time.perf_counter()
    deletion_times.append(end_time - start_time)

# Plot the results
import matplotlib.pyplot as plt
plt.plot(insertion_times, label="Insertion time")
plt.plot(deletion_times, label="Deletion time")
plt.legend()
plt.show()