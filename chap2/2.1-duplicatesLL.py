class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

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

    def delete(self, previous, toDelete):
        if toDelete.next:
            previous.next = toDelete.next
        else:
            previous.next = None

    def removeDuplicates(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            nextElement = current.next
            if nextElement and nextElement.value in values:
                self.delete(current, nextElement)
            current = current.next

ll = LinkedList(Element(2))
ll.append(Element(5))
ll.append(Element(6))
ll.append(Element(2))
ll.append(Element(4))
ll.printList()
print("****")
ll.removeDuplicates()
ll.printList()
