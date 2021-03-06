# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def hasCycle(self, head) -> bool:
        if head is None:
            return False
        slowPointer = head
        fastPointer = head.next
        while fastPointer is not None:
            if fastPointer == slowPointer:
                return True
            if fastPointer.next is None:
                return False
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        return False

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        current = head
        nodes = []
        while current is not None:
            nodes.append(current.val)
            current = current.next
        i = 0
        j = len(nodes) - 1
        #print(nodes)
        while i < j:
            # print(nodes[i])
            # print(nodes[j])
            if nodes[i] != nodes[j]:
                return False
            i += 1
            j -= 1
        return True

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        currentA = headA
        currentB = headB
        lengthA = lengthB = 0
        while currentA is not None:
            lengthA += 1
            currentA = currentA.next
        while currentB is not None:
            lengthB += 1
            currentB = currentB.next
        if lengthA > lengthB:
            longerList = headA
            shorterList = headB
        else:
            longerList = headB
            shorterList = headA
        lengthDif = abs(lengthA - lengthB)
        while lengthDif > 0:
            longerList = longerList.next
            lengthDif -= 1
        print("longer list starts at %s" % longerList.val)
        while longerList is not None:
            if longerList == shorterList:
                return longerList
            longerList = longerList.next
            shorterList = shorterList.next
        return None

    def removeElements(self, head, val):
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return head
        prev = head
        current = (head.next if head.next is not None else None)
        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return head

