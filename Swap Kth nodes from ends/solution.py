class Solution:
    def swapKth(self, head, k):
        if not head:
            return head
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        if k > length:
            return head
        
        if 2 * k - 1 == length:
            return head
        
        first = head
        for i in range(k - 1):
            first = first.next
        
        second = head
        for i in range(length - k):
            second = second.next
        
        first.data, second.data = second.data, first.data
        
        return head
