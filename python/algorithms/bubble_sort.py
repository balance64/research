def bubble(NUMBER_LIST):
    print(NUMBER_LIST)  # Display the unsorted list
    swap_counter = 0  # Set a counter for the number of swaps
    for idx in range(0, len(NUMBER_LIST)):  # Loop through list
        pos = idx  # Set the item to compare
        swap_pos = pos - 1  # Set the item to swap if needed
        # Loop through the items to compare
        while swap_pos >= 0:  # Loop through the unsorted list
            # Check to see if you need to swap
            if NUMBER_LIST[swap_pos] > NUMBER_LIST[pos]:
                # Swap positions
                NUMBER_LIST[pos], NUMBER_LIST[swap_pos] = NUMBER_LIST[swap_pos], NUMBER_LIST[pos]
                # Increment the swap counter to show the work
                swap_counter = swap_counter + 1
            print(NUMBER_LIST)  # Display the current list
            # Move to the next swap item
            swap_pos = swap_pos - 1
            # Move to the next item to compare
            pos = pos - 1

    # Display the number of swaps
    print("SWAPS:", swap_counter)


numbers = [90, 87, 82, 43, 3, 5]
bubble(numbers)
