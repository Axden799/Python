import math

def isValidBST(self, root):
    if root is None:
        return True
    
    s = []
    s.append((root, -math.inf, math.inf))
    
    while s:
        node, lower ,upper = s.pop()
        if not node:
            continue
        if node.val <= lower or node.val >= upper:
            return False
        s.append((node.right, node.val, upper))
        s.append((node.left, lower, node.val))
    return True

def inOrderBST(self, root):
    s, prev = [], -math.inf
    
    while s or root:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        
        if root.val <= prev:
            return False
        prev = root.val
        root = root.right
    return True