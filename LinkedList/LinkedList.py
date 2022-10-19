class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
    
def creare_list(arr):
    ll = ListNode()
    save = ll
    for x in arr:
        node = ListNode(x)
        ll.next = node
        ll = ll.next
    return save.next

def print_list(head):
    if head is None: 
        print(head)
        return 
    print(head.val,end = '->')
    print_list(head.next)

