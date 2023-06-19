from collections import deque

class TwoStacks:
    def __init__(self, n):
        self.size = n  # Size of the array
        self.arr = [None] * n  # Array to store elements
        self.top1 = -1  # Top index of the first stack
        self.top2 = self.size  # Top index of the second stack (initialized at the end)
    
    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x  # Push the element into the first stack
            return True
        return False
    
    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x  # Push the element into the second stack
            return True
        return False
    
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]  # Get the top element from the first stack
            self.top1 = self.top1 - 1
            return x
        return None
    
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]  # Get the top element from the second stack
            self.top2 = self.top2 + 1
            return x
        return None
    
    def size1(self):
        return self.top1 + 1  # Size of the first stack
    
    def size2(self):
        return self.size - self.top2  # Size of the second stack

# Create an instance of TwoStacks with size 5
ts = TwoStacks(5)

# Push elements into the stacks
ts.push1(10)
ts.push2(70)

# Pop an element from the first stack and print it
print(ts.pop1())

