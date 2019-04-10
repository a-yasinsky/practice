class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinckedList(object):
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
