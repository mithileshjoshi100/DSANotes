'''
    Delet the middle element for list
    count the length count the index of middle elemnet 
    go to the middle - 1 index 
    do curr.next = curr.next.next
    if length is 1 the return None
'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def deletMiddle(head:ListNode):
    length = 0
    run = head
    while run:
        length += 1
        run = run.next
    if length ==1 : retun None
    i = length//2
    count = 0
    curr = head
    while count < i-1:
        count += 1
        curr = curr.next
    curr.next = curr.next.next

    return head

'''
Not tested no local Machine
'''
