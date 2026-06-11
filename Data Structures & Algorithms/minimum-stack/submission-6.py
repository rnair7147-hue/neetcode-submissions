class MinStack: 

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,val):
        self.stack.append(val)
        if len(self.minStack) == 0 :
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1],val))

    def pop(self):
            self.stack.pop()
            self.minStack.pop()     

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]

        
