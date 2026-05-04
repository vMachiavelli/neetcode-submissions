# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        if head == None:
            return False

        while head != None:
            print(visited)
            if head in visited:
                return True
            else:
                visited.append(head)
                if head.next == None:
                    return False
                head = head.next