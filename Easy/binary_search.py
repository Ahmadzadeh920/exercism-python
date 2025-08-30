def binary_search(sorted_list, target):
    """
    Perform binary search on a sorted list to find the target value.
    
    Args:
    sorted_list (list): A list of sorted elements.
    target (int/float/str): The value to search for.
    
    Returns:
    int: The index of the target in the sorted_list.
    
    Raises:
    ValueError: If the target is not found in the list.
    """


    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_list[mid]
        
        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    raise ValueError(f"{target} not found in the list")



#Example Usage
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    try:
        index = binary_search(sorted_list, target)
        print(f"Element {target} found at index {index}.")
    except ValueError as e:
        print(e)