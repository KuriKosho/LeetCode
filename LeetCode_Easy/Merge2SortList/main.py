# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # Create a dummy node to start the merged list
    dummy = ListNode()
    current = dummy

    # Traverse through both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining nodes in either list1 or list2
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Return the next node after dummy as the head of the merged list
    return dummy.next


# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list of values for easy output
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example test case
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
print(linked_list_to_list(mergeTwoLists(list1, list2)))  # [1, 1, 2, 3, 4, 4]