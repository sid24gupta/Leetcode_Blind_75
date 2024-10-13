# https://leetcode.com/problems/linked-list-cycle/description/
# 141. Linked List Cycle
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

def hasCycle(head) -> bool:
        
    if head == None:
        return 0

    first = head
    second = head


    while second.next != None and second.next.next != None:

        first = first.next
        second = second.next.next

        if first == second:
            return 1
    
    return 0

    # for getting the position of intersection.
    # first , second = head, head

    # has_cycle = 0

    # while second and second.next:

    #     first = first.next
    #     second = second.next.next

    #     if first == second:
    #         has_cycle =  1
    #         break

    # if not has_cycle:
    #     return None

    # first = head

    # while first != second:

    #     first = first.next
    #     second = second.next

    # return first


head = [3,2,0,-4]
v1 = hasCycle(head)
print(v1)