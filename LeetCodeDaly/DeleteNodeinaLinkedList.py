'''
    delet the given node in a linkList where head is not given 
    ===> delet the first node by shifting all  values
    shift the node value to last like a buble
    delet the last Node
    :) 
'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = None
    
def createList(lst:list[int]) -> ListNode:
    head = ListNode()
    copy = head
    for x in lst:
        copy.next = ListNode(x)
        copy = copy.next
    return head.next


def printList(head:ListNode):
    while head:
        print(head.val, end = ' ')
        head = head.next

def deletNode(node1):
    node = node1
    if node is None: return 
    while node and node.next:
        node.val,node.next.val = node.next.val,node.val
        node = node.next
    back = None
    curr = node1
    while curr.next:
        back = curr
        curr = curr.next
    back.next = None
    
    printList(node1)
    
deletNode(createList([1,2,3,4,5]))
#printList(deletLast(createList([1,2,3])))