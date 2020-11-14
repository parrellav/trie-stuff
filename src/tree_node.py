class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if None is root:
        return False
    sum -= root.val
    if 0 == sum:
        return True
    return has_path(root.left, sum) or has_path(root.right, sum)
