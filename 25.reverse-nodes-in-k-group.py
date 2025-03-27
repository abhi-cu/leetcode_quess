class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_linked_list(start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    
    while True:
        kth = prev_group_end
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        next_group_start = kth.next
        
        group_start = prev_group_end.next
        prev_group_end.next = reverse_linked_list(group_start, next_group_start)
        group_start.next = next_group_start
        prev_group_end = group_start
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
k = 2
new_head = reverse_k_group(head, k)
print(linked_list_to_list(new_head)) 
