# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0 #Carry over
        head=ListNode() #Creating a new Linked List for the result
        curr=head
        while l1 and l2: #Traversing both linked lists until one ends
            res=l1.val+l2.val+carry 
            carry=res//10 #Carry over = (l1.val+l2.val+prev carry over)//10
            curr.next=ListNode(res%10) #Next linked list node = (l1.val+l2.val+carry) mod 10
            curr=curr.next
            l1=l1.next
            l2=l2.next
        #Checking the remaining nodes of both linked lists
        while l1:
            res=l1.val+carry
            carry=res//10
            curr.next=ListNode(res%10)
            curr=curr.next
            l1=l1.next
        while l2:
            res=l2.val+carry
            carry=res//10
            curr.next=ListNode(res%10)
            curr=curr.next
            l2=l2.next
        if carry>0: #If carry>0 => We need to add a new linked list node at the end
            curr.next=ListNode(carry)
        return head.next 


        
