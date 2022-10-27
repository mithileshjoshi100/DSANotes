

def serialize(root):
    lst = []
    st = [root]
    while st:
        lst.append(st[0].val if st[0] else None)
        if st[0]:
            st.append(st[0].left)
            st.append(st[0].right)
        st.pop(0)
    return ','.joint(lst)

def deserialize(s):
    lst = s.split(',')

    root = TreeNode(lst[0])
    root.left = TreeNode(lst[1])
    root.right = TreeNode(lst[2])
    




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
serialize(r)