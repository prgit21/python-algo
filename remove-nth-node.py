#remove nth node from end of linked list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right =head
        while n>0 and right:
            right=right.next
            n-=1
        while right:            #this step idk why
            left=left.next
            right=right.next
        
        #del
        left.next=left.next.next
        return dummy.next
