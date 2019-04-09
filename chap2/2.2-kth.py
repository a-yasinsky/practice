class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def getHead(self):
        return self.head

    def append(self,new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def printList(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def findKth(self, k):
        current = kth = self.head
        for i in range(k):
            if not kth:
                return -1
            kth = kth.next
        while kth:
            current = current.next
            kth = kth.next
        return current.value

def findRecursivly(head, k, iList):
    if head is None:
        return head
    node = findRecursivly(head.next, k, iList)
    iList[0] += 1
    if iList[0] == k:
        return head.value
    return node

ll = LinkedList(Element(2))
ll.append(Element(5))
ll.append(Element(6))
ll.append(Element(2))
ll.append(Element(4))
print(ll.findKth(3))
print(findRecursivly(ll.getHead(),3, [0]))
