class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev, current = dummy, head
    
    while current and current.next:
        first = current
        second = current.next
        
        prev.next = second
        first.next = second.next
        second.next = first
        
        prev = first
        current = first.next
    
    return dummy.next
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
head = list_to_linked_list([1,2,3,4])
swapped_head = swap_pairs(head)
print(linked_list_to_list(swapped_head)) 
