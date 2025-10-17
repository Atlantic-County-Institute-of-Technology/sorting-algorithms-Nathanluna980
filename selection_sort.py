import time


def selection_sort(data_list):

    # Sorts a list using the Selection Sort algorithm and returns the sorted list along with performance metrics.

    n = len(data_list)
    loop_count = 0
    actions = 0  # Represents the number of swaps
    start_time = time.time()

    # Outer loop: moves the boundary of the unsorted subarray
    for i in range(n):
        min_idx = i

        # Inner loop: finds the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            loop_count += 1  # Comparison counts as an inner loop execution
            if data_list[j] < data_list[min_idx]:
                min_idx = j

        # Swap the found minimum element with the element at the current position 'i'
        if min_idx != i:
            data_list[i], data_list[min_idx] = data_list[min_idx], data_list[i]
            actions += 1  # One swap counts as one sorting action

    end_time = time.time()
    time_taken = end_time - start_time

    return data_list, loop_count, actions, time_taken
