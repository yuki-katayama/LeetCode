from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        process = output = ListNode()
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        while(1):
            if(l1.val <= l2.val):
                process.next = l1
                process = process.next
                l1 = l1.next
                if l1 == None:
                    process.next = l2
                    break
            else:
                process.next = l2
                process = process.next
                l2 = l2.next
                if l2 == None:
                    process.next = l1
                    break
        return output.next

def setData(node: ListNode, l: List[int]):
    for v in l:
        node.next = ListNode(v)
        node = node.next

node1 = ListNode()
setData(node1, [1, 5, 8, 11])
node2 = ListNode()
setData(node2, [1, 2, 3, 4])

solution = Solution()
node3 = solution.mergeTwoLists(node1, node2)
while(node3.next != None):
    print(node3.val)
    node3 = node3.next
print(node3.val)