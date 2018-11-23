# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = ""
        while True:
            x = x + str(l1.val)
            if not l1.next:
                break
            l1 = l1.next
        x = "".join(reversed(x))
        y = ""
        while True:
            y = y + str(l2.val)
            if not l2.next:
                break
            l2 = l2.next
        y = "".join(reversed(y))
        rtn = str(int(x) + int(y))
        pp = []
        for xx1 in rtn:
            pp.append(ListNode(int(xx1)))
        prev = None
        for item in pp:
            item.next = prev
            prev = item
        return pp[-1]


if __name__ == '__main__':
    s = Solution()
    lx1 = ListNode(2)
    lx2 = ListNode(4)
    lx3 = ListNode(3)
    lx1.next = lx2
    lx2.next = lx3

    ly1 = ListNode(5)
    ly2 = ListNode(6)
    ly3 = ListNode(4)
    ly1.next = ly2
    ly2.next = ly3
    x1 = s.addTwoNumbers(lx1, ly1)
    print(x1)
