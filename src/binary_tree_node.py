from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_min_heap_recur(root: Node):
    if None is root:
        return False

    if root.left is None and root.right is None:
        return True
    if root.right.data < root.left.data or root.left.data < root.data:
        return False
    return is_min_heap_recur(root.left) and is_min_heap_recur(root.right)

def is_min_heap_iter(root: Node):
    if None is root:
        return True

    my_stack = deque()
    my_stack.append(root)

    is_min_heap = True

    while my_stack:
        current = my_stack.popleft()
        if current.left is None and current.right is None:
            continue

        if current.left.data < current.data or current.right.data < current.left.data:
            is_min_heap = False
            break
        my_stack.append(current.left)
        my_stack.append(current.right)

    return is_min_heap