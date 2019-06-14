class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.x_to_node = {}


    def _preorder_traverse(self, root, x_coor, y_coor):
        if root is None:
            return None
        
        if self.x_to_node.get(x_coor):
            if self.x_to_node.get(x_coor).get(y_coor):
                self.x_to_node.get(x_coor).get(y_coor).append(root.val)
            else:
                self.x_to_node[x_coor][y_coor] = [root.val]
        else:
            self.x_to_node[x_coor] = {y_coor: [root.val]}

        self._preorder_traverse(root.left, x_coor - 1, y_coor - 1)
        self._preorder_traverse(root.right, x_coor + 1, y_coor - 1)
    
    
    def _given_x_return_node_values(self, x):
        ys = self.x_to_node[x].keys()
        ys = sorted(ys, reverse=True)
        nodes = []
        for y in ys:
            nodes.extend(sorted(self.x_to_node[x][y]))

        return nodes


    def verticalTraversal(self, root):
        self._preorder_traverse(root, 0, 0)
        vertical_traversal = list(map(self._given_x_return_node_values, sorted(self.x_to_node.keys())))

        return vertical_traversal

        