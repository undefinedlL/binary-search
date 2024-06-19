def binary_search(list, target_element, low_index, high_index): 
    if low_index <= high_index:
        
        mid = low_index + (high_index - low_index) // 2
        
        item = list[mid]
        
        if item == target_element:
            return mid
        
        if item < target_element:
            return binary_search(list, target_element, mid + 1, high_index)
        else:
            return binary_search(list, target_element, low_index, mid - 1)
    else:
        return None