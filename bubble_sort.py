import time


def bubble_sort(data_list):

    # Sorts a list using the Bubble Sort algorithm and returns the list along with performance metrics.

    n = len(data_list)
    loop_count = 0
    actions = 0  # Represents the number of swaps
    start_time = time.time()

    # Outer loop: controls the passes
    for i in range(n - 1):
        swapped = False

        # Inner loop: compares and swaps adjacent elements
        for j in range(0, n - i - 1):
            loop_count += 1  # Comparison counts as an inner loop execution

            if data_list[j] > data_list[j + 1]:
                # Swap
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                actions += 1
                swapped = True

        # Optimization: If no two elements were swapped, the list is sorted
        if not swapped:
            break

    end_time = time.time()
    time_taken = end_time - start_time

    return data_list, loop_count, actions, time_taken
