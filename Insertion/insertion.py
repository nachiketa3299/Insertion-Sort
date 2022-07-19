# insertion sort algorithm by ruzen
# 2022-07-19T20:00

# list = [25, 34, 2, 1, 234, 123]

def _moveRight(start_index, end_index, input_list):
    i = end_index
    while (i >= start_index):
        input_list[i + 1] = input_list[i]
        i -= 1
        
def insertionSort(input_list):
    sorted_bound_index = 0
    while (sorted_bound_index < len(input_list) - 1):
        unsorted_head_index = sorted_bound_index + 1
        compare_index = 0
        while(compare_index <= sorted_bound_index):
            if input_list[unsorted_head_index] < input_list[compare_index]:
                holder = input_list[unsorted_head_index]
                # [compare_index, unsorted_head_index]
                _moveRight(compare_index, unsorted_head_index, input_list)
                list[compare_index] = holder
            else:
                compare_index += 1

                
                
            


            

        
        
        

    