import LinkedList

head = LinkedList.creare_list([1,2,3])

def reverse_list(head):
    prev,curr = None,head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def reverse_list_r(head):
    


LinkedList.print_list(reverse_list(LinkedList.creare_list([1,2,3,4])))