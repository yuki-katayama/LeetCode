class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listCreator(nodeValues):
    temp = dummyHead = ListNode(0)
    for value in nodeValues:
        temp.next = ListNode(value)
        temp = temp.next
    return dummyHead.next


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = temp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            tempSum = temp1 + temp2 + carry
            print(tempSum, temp1, temp2, carry)

            temp.next = ListNode(tempSum % 10)
            temp = temp.next
            carry = tempSum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next


func = Solution()
l1 = listCreator([2, 5, 23])
l2 = listCreator([5, 6, 4])
print(func.addTwoNumbers(l1, l2).val)

# 個人的なテスト
# head = listCreator([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(head.next.val)

# l1 = ListNode(0)
# l1.next = ListNode(1)
# l1.next.next = ListNode(2)

# l2 = ListNode(3)
# l2.next = ListNode(4)
# l2.next.next = ListNode(5)
# print(l1.val, l2.val)
