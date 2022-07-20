# Insertion sort algorithm by ruzen
# 2022-07-19T20:00
# 2022-07-20T14:48

# `input_list` example = [3, 2, 1, 0]
# This algorithm sees the list as "sorted partial list" + "unsorted partial list"

def insertionSort(input_list):
    """Perform insertion sort in ascending order."""
    # In the first step, assume that index 0 is already sorted.
    # So the outer for-loop's range is [0, len(input_list) - 1), because the last index is sorted in the last loop step.
    # The variable `sorted_bound_index` notates the last index of "sorted partial list".
    for sorted_bound_index in range(0, len(input_list) - 1):
        # One index after the `sorted_bound_index`, unsorted partial list starts. 
        # The variable `unsorted_head_index` notates the first index of "unsorted partial list".
        # `input_list[unsorted_head_index]` will be inserted in the "sorted partial list".
        unsorted_head_index = sorted_bound_index + 1
        # Inner for-loop is for finding the place(index) where `input_list[unsorted_head_index]` should be inserted.
        # So inner for-loop's range is the entire "sorted partial list". This is notated as [0, sorted_bound_index] (variable name implies the boundary of parial sorted list)
        for compare_index in range(0, unsorted_head_index):
            # This function sorts elements in ascending order. 
            # So, if the value of `input_list[unsorted_head_index]` is not less(>=) than `input_list[compare_index]`, do nothing.
            if input_list[unsorted_head_index] >= input_list[compare_index]:
                pass
            # Else if the value of `input_list[unsorted_head_list]` is less(<) than `input_list[compare_index]` the "insertion process" needed.
            elif input_list[unsorted_head_index] < input_list[compare_index]:
                # The "insertion process" starts in here.
                # The `holder` variable holds the value of `input_list[unsroted_head_index]`, because this element will be replaced by the preceding element.
                holder = input_list[unsorted_head_index]
                # All the elements' index in range [unsorted_head_index, compare_index](reverse order) must be incremented by one.
                for i in range(unsorted_head_index, compare_index, -1):
                    input_list[i] = input_list[i - 1]
                # `holder` goes to the index `compare_index`
                input_list[compare_index] = holder