class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head, left, right):
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    for _ in range(left - 1):
        prev = prev.next
    
    curr = prev.next
    
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
left, right = 2, 4
new_head = reverse_between(head, left, right)
print_list(new_head)
