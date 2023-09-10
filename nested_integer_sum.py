def nested_integer_sum(lst, depth=1):
    """
    This function takes in a nested list and a depth (default value is 1).
    For each element in the list, it checks if it's an integer or another list.
    If it's an integer, it adds the integer weighted by its depth to the total sum.
    If it's a list, it recursively calls itself with increased depth.
    """
    total = 0
    for item in lst:
        if isinstance(item, int):
            total += item * depth
        else:
            total += nested_integer_sum(item, depth+1)
    return total

lst = [[1,1],2,[1,1]]
print(nested_integer_sum(lst))  # Outputs: 10
