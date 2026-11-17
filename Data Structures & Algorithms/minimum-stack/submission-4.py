class MinStack:

    def __init__(self):
        self.stack = []
        self.minSatck = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minSatck or val<=self.minSatck[-1]:
            self.minSatck.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minSatck[-1]:
            self.minSatck.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minSatck[-1]
        
