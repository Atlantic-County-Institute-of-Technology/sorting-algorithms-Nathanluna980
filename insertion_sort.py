import time


def insertion_sort(data_list):

    # Sorts a list using the Insertion Sort algorithm and returns the sorted list along with performance metrics.

    n = len(data_list)
    loop_count = 0
    actions = 0  # Represents shifts/insertions
    start_time = time.time()

    # Outer loop: iterates from the second element (index 1) to the end
    for i in range(1, n):
        key = data_list[i]
        j = i - 1

        # Inner loop: shifts elements greater than 'key' one position ahead
        while j >= 0 and key < data_list[j]:
            loop_count += 1  # Comparison counts as an inner loop execution
            data_list[j + 1] = data_list[j]  # Shift action
            actions += 1
            j -= 1

        # Count the comparison that terminates the while loop (if j >= 0)
        if j >= 0:
            loop_count += 1

            # Place the key (current element) in its correct position
        if j + 1 != i:
            data_list[j + 1] = key
            actions += 1  # Final insertion action (only counts if a shift occurred)

    end_time = time.time()
    time_taken = end_time - start_time

    return data_list, loop_count, actions, time_taken
