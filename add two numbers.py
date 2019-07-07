class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2,carry=0):
        val =l1.val+l2.val+carry
        carry=val // 10
        ret = ListNode(val%10)

        if (l1.next!=None) or (l2.next!=None) or (carry!=0):
            if l1.next==None:
                l1.next=ListNode(0)
            if l2.next==None:
                l2.next=ListNode(0)
            
            ret.next=self.addTwoNumbers(l1.next,l2.next,carry)
        
        return ret

        


'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

listNode_one = ListNode(2)
listNode_two = ListNode(4)
listNode_three = ListNode(3)
listNode_one.next = listNode_two
listNode_two.next = listNode_three

listNode_four = ListNode(5)
listNode_five = ListNode(6)
listNode_six = ListNode(4)
listNode_four.next = listNode_five
listNode_five.next = listNode_six


solution = Solution()
listnode = solution.addTwoNumbers(listNode_one, listNode_four)

while listnode != None:
    print(listnode.val)
    listnode=listnode.next
