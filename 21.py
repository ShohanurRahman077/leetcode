class ListNode:
    def __init__(self, val = 0, next =None):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)
    def swapNodesInPair(head):
        dummy = ListNode(self,0,head)
        print(dummy.val,dummy.next)



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next =node3
node3.next = node4
ListNode.swapNodesInPair(node1)