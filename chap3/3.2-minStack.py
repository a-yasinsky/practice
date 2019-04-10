class Stack:
     def __init__(self):
         self.items = []
         self.minvals = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)
         if(len(self.minvals) > 0):
             self.minvals.append( min(item, self.minvals[len(self.minvals) -1]) )
         else:
             self.minvals.append(item)

     def pop(self):
         self.minvals.pop()
         return self.items.pop()

     def min(self):
        return self.minvals[len(self.minvals) -1]

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

stack = Stack()
stack.push(5)
print(stack.min())
stack.push(7)
print(stack.min())
stack.push(3)
print(stack.min())
stack.push(9)
print(stack.min())
stack.push(2)
print(stack.min())
stack.push(8)
print(stack.min())

print(stack.pop())
print(stack.pop())
print(stack.min())
