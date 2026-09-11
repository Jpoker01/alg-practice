from collections import deque

class MyStack:

    def __init__(self):
        self.deque = deque()

    def push(self, x: int) -> None:
        self.deque.appendleft(x)

    def pop(self) -> int:
        return self.deque.popleft()

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        if len(self.deque) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()