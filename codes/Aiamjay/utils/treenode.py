# encoding=utf-8


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree_from_list(array: list) -> TreeNode:
    # [3,9,20,null,null,15,7]
    root_val = array.pop(0)
    if not root_val:
        return None
    root = TreeNode(root_val)
    queue = [root]
    while array:
        top = queue.pop(0)
        cur = array.pop(0)
        top.left = TreeNode(cur) if cur else None
        cur = array.pop(0)
        top.right = TreeNode(cur) if cur else None
        if top.left:
            queue.append(top.left)
        if top.right:
            queue.append(top.right)
    return root


def print_tree(root: TreeNode):
    if not root:
        return
    queue = [root]
    while queue:
        top = queue.pop(0)
        print(top.val, end="  ")
        if len(queue) == 0:
            print("")
        if top.left:
            queue.append(top.left)
        if top.right:
            queue.append(top.right)
