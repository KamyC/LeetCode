# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
class MinStack(object):
    class MinStack(object):

        def __init__(self):
            self.stack = []

        def push(self, x):
            self.stack.append(x)

        def pop(self):
            if len(self.stack) != 0:
                self.stack.pop(-1)

        def top(self):
            if len(self.stack) != 0:
                return self.stack[-1]

        def getMin(self):
            if len(self.stack) != 0:
                min = self.stack[0]
                # print(min)
                for i in self.stack:
                    if min > i:
                        min = i
                return min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()