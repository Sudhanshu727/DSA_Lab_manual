def insert_in_sorted_order(stack, element):
    """
    Insert an element into the stack in sorted order.
    """
    if not stack or element > stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_in_sorted_order(stack, element)
        stack.append(temp)

def sort_stack(stack):
    """
    Sort a stack using recursion.
    """
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert_in_sorted_order(stack, temp)

# Example usage
stack = [3, 1, 4, 2]
print("Original Stack:", stack)

sort_stack(stack)
print("Sorted Stack:", stack)