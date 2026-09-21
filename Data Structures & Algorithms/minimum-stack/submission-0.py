class MinStack:

    def __init__(self):
        self.arr = []
        self.mi = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        temp = min(self.mi[-1] if self.mi else val, val)
        self.mi.append(temp)

    def pop(self) -> None:
        self.arr.pop()
        self.mi.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mi[-1]
