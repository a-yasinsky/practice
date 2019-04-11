from LinckedList import Element, LinckedList

def deleteMiddle(vertex):
    if(vertex and vertex.next):
        vertex.value = vertex.next.value
        vertex.next = vertex.next.next

ll = LinckedList(Element(2))
ll.append(Element(5))
middle = Element(6)
ll.append(middle)
ll.append(Element(2))
ll.append(Element(4))

deleteMiddle(middle);
ll.printList()
