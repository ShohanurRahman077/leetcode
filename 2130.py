# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverse(list):

        prev = None
        curr = list
        while curr:
            next_node = curr.next # first, make sure we don't lose the next node
            curr.next = prev      # reverse the direction of the pointer
            prev = curr           # set the current node to prev for the next node
            curr = next_node      # move on
            
        return prev




    def pairSum(self, head: ListNode) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        slow.next = Solution.reverse(slow)
        while slow:
            print(rev.val)
            rev = rev.next

        return head
node1 = ListNode(5)
node2 = ListNode(4)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4

Solution.pairSum("test", node1)
        