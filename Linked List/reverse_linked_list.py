# https://leetcode.com/problems/reverse-linked-list/description/
# 206. Reverse Linked List
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
        
    if head == None:
        return

    prev = None
    current = head
    front = ListNode()

    while current != None:

        front = current.next
        current.next = prev
        prev = current
        current = front

    return prev


head = [1,2,3,4,5]
v1 = reverseList(head)
# we can iterate through v1 using loop to print the linked list.
