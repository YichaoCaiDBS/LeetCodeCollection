# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        print("|{},{}|".format(self.val, self.next))


# My original construtor funciton which has bug
def fromListToLinkedNodeMine(l):
    n = ListNode(l[0])
    for number in l[1:]:
        # print('Adding {}'.format(number))
        n.next = ListNode(number)
        n = n.next
    return n


# Constructor funciton from LeetCode
# dummyNode is the final object to be returned.
# n is the intemediate node
# When we swap n and n.next and assign new value,
# the linkedList would be recorded by dummyNode
def fromListToLinkedNodeDetail(l):
    dummyNode = ListNode('Head')
    n = dummyNode
    print(printLinkedList(dummyNode))
    print(printLinkedList(n))
    for number in l:
        print("===========")
        print("Consider number: {}".format(number))
        print(printLinkedList(dummyNode))
        print(printLinkedList(n))
        n.next = ListNode(number)
        print("After assign next value")
        print(printLinkedList(dummyNode))
        print(printLinkedList(n))
        n = n.next
        print("After swap value")
        print(printLinkedList(dummyNode))
        print(printLinkedList(n))
    n = dummyNode.next
    return n


# Constructor funciton from LeetCode
def fromListToLinkedNode(l):
    dummyNode = ListNode('Head')
    n = dummyNode
    for number in l:
        n.next = ListNode(number)
        n = n.next
    n = dummyNode.next
    return n


def printLinkedList(l):
    if(l.next is None):
        return "{} -> {{None}}".format(l.val)
    return "{} -> {}".format(l.val, printLinkedList(l.next))


# Similar to how we construct a linked list.
# carry is for recording overflow where sum is greater than 10.
# The condition where judging whether p/q is None is to deal with situation
# where we have integer arrays with different lengths. When a arrat reaches its end,
# it would always be 0 when calculating the sum of trailling digits.
def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode('Head')
        current = dummyHead
        carry = 0
        p = l1
        q = l2
        while(p is not None or q is not None):
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if(p is not None):
                p = p.next
            if(q is not None):
                q = q.next
        if(carry > 0):
            current.next = ListNode(carry)
        return dummyHead.next


# Other's code
# This one used function recursion
# Faster than the function above.
def addTwoNumbers2(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        val = l1.val + l2.val
        if val < 10:
            ret = ListNode(val)
            ret.next = addTwoNumbers(l1.next, l2.next)
            return ret
        else:
            val = val - 10
            ret = ListNode(val)
            ret.next = addTwoNumbers(ListNode(1),
                                     addTwoNumbers(l1.next, l2.next))
            return ret


l1 = fromListToLinkedNode([3, 4, 2])
l2 = fromListToLinkedNode([9, 9])
l3 = addTwoNumbers(l1, l2)
print(printLinkedList(l3))
