// insertion.cpp
// made by Ruzen in 2022-07-29

void insertionSort (int * input_array_ptr, const int input_array_size) {

    int insertion_target_index = 0;

    for (int sorted_tail_index = 0; sorted_tail_index < input_array_size; sorted_tail_index++) {
        int unsorted_head_index = sorted_tail_index + 1;
        for (int compare_index = 0; compare_index < unsorted_head_index; compare_index++) {
            insertion_target_index = compare_index;
            if (input_array_ptr[unsorted_head_index] < input_array_ptr[compare_index]) {
                break;
            }
        }
        for (int i = unsorted_head_index; i > insertion_target_index; i--) {
            int temp = input_array_ptr[i - 1];
            input_array_ptr[i - 1] = input_array_ptr[i];
            input_array_ptr[i] = temp; 
        }
    }

    return;
}