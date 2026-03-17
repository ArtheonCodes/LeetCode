# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(node): #Length function for calculating length of linked lists
            temp=node
            length=0
            while temp:
                length+=1
                temp=temp.next
            return length
        l=length(head)
        l-=n
        dummy=ListNode() # Creating a dummy Node for managing head node, In case we need to delete head
        dummy.next=head
        curr=dummy
        itr=-1
        while curr: 
            itr+=1
            if itr==l:
                curr.next=curr.next.next #If X-->Y-->Z are three nodes, and Y needs to be deleted, We change X's next node to Y's next node, X-->Z
                return dummy.next
            curr=curr.next
        

        
