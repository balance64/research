def merge(number_list):
    # Check if the list is longer than 1 element
    if len(number_list) > 1:
        # Find the middle of the list
        half_idx = int(len(number_list) / 2)
        # Create a list with front half of the list
        list_a = number_list[:half_idx]
        # Create a list with the back half
        list_b = number_list[half_idx:]
        # Recursively call this merge function
        # Sort the first half
        sorted_a = merge(list_a)
        # Sort the second half
        sorted_b = merge(list_b)
        # Init an empty list
        sorted_list = []
        # Set a flag to indicate both lists are inserted
        done = False
        while not done:
            # Iterate on the lists until done
            # Compare the first item of each list
            if sorted_a[0] < sorted_b[0]:
                # If first list item is smaller insert it into the sorted list
                sorted_list.append(sorted_a.pop(0))
            else:
                # Do the other one
                sorted_list.append(sorted_b.pop(0))
            if len(sorted_a) == 0:
                # Add the remainder of the second list to the sorted list
                sorted_list = sorted_list + sorted_b
                # Change the done flag to end the loop
                done = True
            elif len(sorted_b) == 0:
                # Add the remainder of the other list to the sorted list
                sorted_list = sorted_list + sorted_a
                # Change the done flag
                done = True
        print(sorted_list)
    else:  # If the list is only 1 element it is already sorted
        sorted_list = number_list

    return (sorted_list)


x = [12, 23, 123, 432, 456, 132, 567, 432,
     65, 8, 6, 34, 245, 56, 6, 7, 45, 345]


print(f'Unsorted list is: {x}')
print('Sorted list is: ', merge(x))
