class Solution:
    def reverse(self, head):
        if not head:
            return None
        
        current = head
        
        while current:
            current.next, current.prev = current.prev, current.next
            
            if current.prev is None:
                return current
                
            current = current.prev
        
        return head
