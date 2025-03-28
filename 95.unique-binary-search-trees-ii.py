class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_trees(n):
    if n == 0:
        return []
    
    def build_trees(start, end):
        if start > end:
            return [None]
        all_trees = []
        for i in range(start, end + 1):
            left_trees = build_trees(start, i - 1)
            right_trees = build_trees(i + 1, end)
            for l in left_trees:
                for r in right_trees:
                    all_trees.append(TreeNode(i, l, r))
        return all_trees
    
    return build_trees(1, n)

def serialize(root):
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

n = 3
trees = generate_trees(n)
output = [serialize(tree) for tree in trees]
print(output)
