import os
import random
import time

# Import all sorting functions
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

# Default list parameters
list_size = 100
min_range = 1
max_range = 1000
data_list = []

# Map menu choices to functions and names
SORT_CHOICES = {
    '1': (bubble_sort, "Bubble Sort"),
    '2': (insertion_sort, "Insertion Sort"),
    '3': (selection_sort, "Selection Sort"),
}

# Utility Functions

def clear_screen():
    # Clears the terminal screen / Works for Windows ('cls') and Unix/Linux/Mac ('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_list():
    # Generates a new list based on current parameters.
    global data_list
    data_list = [random.randint(min_range, max_range) for _ in range(list_size)]
    print(f"\n New list")
    print(f"Size: {list_size:,}, Range: [{min_range}, {max_range}]")
    time.sleep(1.5)

def display_metrics(algorithm_name, original_list, sorted_list, loops, actions, time_taken):
    # Displays the performance metrics.
    clear_screen()
    print("\n" + "=" * 50)
    print(f" {algorithm_name} Stats ")
    print("=" * 50)
    # Display up to 10 elements of the list
    display_original = original_list[:100] + ['...'] if len(original_list) > 100 else original_list
    display_sorted = sorted_list[:100] + ['...'] if len(sorted_list) > 100 else sorted_list
    print(f"List Size: {len(original_list):,}")
    print(f"Original List (start): {display_original}")
    print(f"Sorted List (end): {display_sorted}")
    print("-" * 50)
    print(f"Time Taken (seconds): {time_taken:.6f} s")
    print(f"Loop Executed: {loops:,}")
    print(f"Sorting Actions (Swaps/Shifts): {actions:,}")
    print("=" * 50 + "\n")
    input("Press Enter to return to the main menu...")

# Input Validation and Configuration

def get_positive_int_input(prompt, current_value, validation_func=None):
    while True:
        try:
            user_input = input(f"{prompt} (Current: {current_value:,}): ")
            # Use current value if input is empty
            value = int(user_input) if user_input else current_value

            if validation_func and not validation_func(value):
                continue

            return value
        except ValueError:
            print(" Invalid input. Please enter a positive number.")
        except Exception:
            print(" Unexpected error occurred.")

def validate_list_size(val):
    # List size must be positive.
    if val > 0:
        return True
    print(" List size must be a positive number.")
    return False

def validate_max_range(max_val):
    # Max range must be >= Min range.
    if max_val >= min_range:
        return True
    print(f" Max range ({max_val}) must be greater than or equal to Min range ({min_range}).")
    return False

def change_list_parameters():
    # Allows the user to change the list size and value range.
    global list_size, min_range, max_range
    clear_screen()
    print("--- Configure List Parameters ---")
    # 1. Get List Size
    list_size = get_positive_int_input(
        "Enter List Size",
        list_size,
        validate_list_size
    )
    # 2. Get Min Range
    min_range = get_positive_int_input(
        "Enter Minimum Value ",
        min_range
    )
    # 3. Get Max Range (must be validated against the new min_range)
    max_range = get_positive_int_input(
        "Enter Maximum Value",
        max_range,
        validate_max_range
    )
    # Regenerate the list
    generate_list()

# Sort Execution

def run_sort_algorithm(algorithm_func, name):
    # Executes a sorting displays.
    if not data_list:
        clear_screen()
        print("\n Please generate a list first (Option 4).")
        time.sleep(2)
        return

    print(f"\n--- Running {name}... ---")

    # Create a copy of the list to sort
    list_to_sort = data_list.copy()

    try:
        # Execute the sort
        sorted_list, loops, actions, time_taken = algorithm_func(list_to_sort)
        # Display the results
        display_metrics(name, data_list, sorted_list, loops, actions, time_taken)

    except Exception as e:
        clear_screen()
        print(f"\n Error occurred during {name}: {e}")
        time.sleep(3)

# Main Menu Loop

def main_menu():
    # Displays the main menu
    while True:
        clear_screen()
        print("=" * 50)
        print(" Sorting Tool ")
        print("=" * 50)
        list_status = 'Generated' if data_list else 'NOT Generated'
        print(f"List: {list_status} (Size: {list_size:,}, Range: [{min_range}, {max_range}])")
        print("-" * 50)
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Selection Sort")
        print("4. Change Numbers")
        print("5. Exit")
        print("-" * 50)
        choice = input("Enter number (1-5): ").strip()
        # 1. Handle sorting
        if choice in SORT_CHOICES:
            func, name = SORT_CHOICES[choice]
            run_sort_algorithm(func, name)
        # 2. Handle configuration
        elif choice == '4':
            change_list_parameters()
        # 3. Handle exit
        elif choice == '5':
            clear_screen()
            print(" Thank you for using the Sorting Tool. Goodbye")
            break
        # 4. Handle invalid input gracefully
        else:
            print("\n Invalid selection. Please choose a number between 1 and 5.")
            time.sleep(1.5)


# Execution

if __name__ == "__main__":
    generate_list()
    main_menu()
