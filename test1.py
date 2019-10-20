class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Merge(object):
    def __init__(self):
        # 用于判断元素是否重复
        self.values = set([])
        self.curValues = set([])

    def mergeList(self, head1, head2):

        # 设置一个临时的节点，保存最初的节点
        newHead = ListNode(0)
        pre = newHead

        # 开始合并
        while (head1 and head2):
            # 判断元素大小，谁小就添加谁
            if head1.val > head2.val:
                # 判断待添加的元素是否会重复
                if self.checkValue(head2.val):
                    pre.next = head2
                    head2 = head2.next
                else:
                    # 如果元素重复，head2前进一格，跳过本次循环
                    head2 = head2.next
                    continue
            else:
                if self.checkValue(head1.val):
                    pre.next = head1
                    head1 = head1.next
                else:
                    head1 = head1.next
                    continue
            pre = pre.next

        # 合并剩余的节点
        if head1:
            self.mergeLeft(head1, pre)

        if head2:
            self.mergeLeft(head2, pre)

        return newHead.next

    # 检查待元素是否重复
    def checkValue(self, value):
        self.values.add(value)
        if len(self.values) > len(self.curValues):
            self.curValues.add(value)
            return True
        else:
            return False

    def mergeLeft(self, head, pre):
        if not head.next:
            pre.next = head
            return

        while head.next:
            if head.val == head.next.val:
                head = head.next

                if not head.next:
                    pre.next = head
                continue
            else:
                pre.next = head
                head = head.next
head1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(9)
head1.next = n1
n1.next = n2
n2.next = n3

head2 = ListNode(3)
m1 = ListNode(5)
m2 = ListNode(7)
m3 = ListNode(8)
head2.next = m1
m1.next = m2
m2.next = m3
c = Merge()
head3 = c.mergeList(head1, head2)
while head3:
    print(head3.val)
    head3 = head3.next
