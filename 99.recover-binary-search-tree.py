class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recover_tree(root):
    def inorder(node):
        return inorder(node.left) + [node] + inorder(node.right) if node else []
    
    nodes = inorder(root)
    sorted_nodes = sorted(nodes, key=lambda x: x.val)
    swap = [n for n, s in zip(nodes, sorted_nodes) if n.val != s.val]
    swap[0].val, swap[1].val = swap[1].val, swap[0].val

root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
recover_tree(root)

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

print(serialize(root))
