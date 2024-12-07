from typing import List
from typing import List
from collections import defaultdict
from typing import Optional

class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def list_to_linked_list(items):
    """Convert a Python list to a linked list."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

class Solution(object):
    # 2. Add two numbers
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = current = ListNode(0)

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, val = divmod(v1 + v2 + carry, 10)

            current.next = ListNode(val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

    def reverse(self, x: int) -> int:
        mod = 2**31  # Modulo for overflow checking
        sign = -1 if x < 0 else 1
        x *= sign
        
        reversed_number = int(str(x)[::-1])
        
        # Check for overflow
        if reversed_number > mod - 1:
            return 0
        return sign * reversed_number
    
def linked_list_to_list(head):
    """Convert a linked list back to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result



# Input lists
list1 = [2, 4, 3]
list2 = [5, 6, 4]

# Convert input lists to linked lists
l1 = list_to_linked_list(list1)
l2 = list_to_linked_list(list2)

solution = Solution() 
result = solution.addTwoNumbers(l1, l2)

output = linked_list_to_list(result)
print(output)

print(solution.reverse(123))

