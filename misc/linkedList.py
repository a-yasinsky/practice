# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def initLList(head,pos):
    headNode = None
    currNode = None
    cycleNode = None
    for key,node in enumerate(head):
        newNode = ListNode(node)
        if not headNode:
            headNode = newNode
            currNode = headNode
        else:
            currNode.next = newNode
            currNode = newNode
        if pos >= 0 and pos == key:
            cycleNode = newNode
    if cycleNode:
        currNode.next = cycleNode
    return headNode

def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    nodeMap = [head]
    curNode = head.next
    while curNode:
        if curNode in nodeMap:
            return curNode
        if not curNode:
            return None
        nodeMap.append(curNode)
        curNode = curNode.next
def detectCycle2(head):
    fastRunner = head
    slowRunner = head
    while fastRunner and fastRunner.next:
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next.next
        if slowRunner == fastRunner:
            break

    if not fastRunner or not fastRunner.next:
        return None

    slowRunner = head
    while slowRunner != fastRunner:
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next

    return fastRunner


head = initLList([-1,-7,7,-4,19,6,-9,-5,-2,-5],6)
print(detectCycle(head).val)
print(detectCycle2(head).val)
