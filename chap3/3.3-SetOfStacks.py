class SetOfStacks:
    def __init__(self, threshold=1):
        self.stacks = [[]]
        self.threshold = threshold

    def peekStack(self):
        return self.stacks[len(self.stacks) - 1]

    def push(self, value):
        cStack = self.peekStack()
        if(len(cStack) < self.threshold):
            cStack.append(value)
        else:
            self.stacks.append([value])

    def pop(self):
        cStack = self.peekStack()
        if(len(cStack) > 1):
            return cStack.pop()
        elif(len(cStack) == 1):
            element = cStack.pop()
            self.stacks.pop()
            return element

    def print(self):
        for stack in self.stacks:
            print([el for el in stack])

stack = SetOfStacks(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.pop()
stack.print()
