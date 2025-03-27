class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    
    for _ in range(n + 1):
        first = first.next
    
    while first:
        first, second = first.next, second.next
    
    second.next = second.next.next
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

head = list_to_linked_list([1,2,3,4,5])
n = 2
new_head = remove_nth_from_end(head, n)
print(linked_list_to_list(new_head))  
