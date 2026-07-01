class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack:
            self.minstack.append(value)
        else:
            current_min = self.minstack[-1]
            self.minstack.append(min(value, current_min))
        

    def pop(self) -> None:         
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        
