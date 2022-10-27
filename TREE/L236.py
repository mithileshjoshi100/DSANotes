'''

'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

## ccreate Tree 
n1 = TreeNode(1,TreeNode(0),TreeNode(8))
n2 = TreeNode(2,TreeNode(7),TreeNode(4))
n5 = TreeNode(5,TreeNode(6),n2)
r = TreeNode(3,n5,n1)

def travel(r):
    if r is None: return 
    travel(r.left)
    print(r.val , end = " ")
    travel(r.right)

def search(r,v):
    if r is None: return False
    if r.val == v: return True
    return search(r.left,v) or search(r.right,v)
    

def lca(root,p,q):
    print(root.val,p,q)
    if search(root.left,p) and search(root.left,q):
        return lca(root.left,p,q)
    if search(root.right,p) and search(root.right,q):
        return lca(root.right,p,q)
    return root.val

        # exist in left 
    

#print(search(r,50))
print(lca(r,4,5))