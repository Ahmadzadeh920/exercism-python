'''Use recursion:

If the current element is a list → recursively flatten it.

If it is not None → append it to the result.

Iteratively, you could use a stack, but recursion is simpler and elegant.'''



def flatten_array(nested_list):
    """
    Flatten a nested list of any depth and remove None values.
    """
    # Result list to store flattened elements


    results = []

    for i in range(len(nested_list)):
        if isinstance(nested_list[i], list):
            results.extend(flatten_array(nested_list[i]))
        elif nested_list[i] is not None:
            results.append(nested_list[i])

    return results

# Example Usage

if __name__ =="__main__":
    nested = [1, [2, 6, None], [[None, [4]], 5]]
    print(flatten_array(nested))  # -> [1, 2, 6, 4, 5]

    nested2 = [1, [None, [2, [3, None]]], 4]
    print(flatten_array(nested2))  # -> [1, 2, 3, 4]

    nested3 = [[[None]], None, 7, [8, [9]]]
    print(flatten_array(nested3))  # -> [7, 8, 9]