class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Edge case: if the list is empty
        if not head:
            return head

        current = head  # Initialize the current pointer

        while current and current.next:  # Traverse the list
            if current.val == current.next.val:  # Check for duplicates
                current.next = current.next.next  # Skip the duplicate
            else:
                current = current.next  # Move to the next node

        return head  # Return the head of the modified list
# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example 1
head = create_linked_list([1, 1, 2])
solution = Solution()
new_head = solution.deleteDuplicates(head)
print(linked_list_to_list(new_head))  # Output: [1, 2]

# Example 2
head = create_linked_list([1, 1, 2, 3, 3])
new_head = solution.deleteDuplicates(head)
print(linked_list_to_list(new_head))  # Output: [1, 2, 3]


