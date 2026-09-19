class MinStack:
    def __init__(self):
        self.values = []
        self.minimums = []

    def push(self, value: int) -> None:
        self.values.append(value)

        if not self.minimums:
            self.minimums.append(value)
        else:
            self.minimums.append(min(value, self.minimums[-1]))

    def pop(self) -> int:
        self.minimums.pop()
        return self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def get_min(self) -> int:
        return self.minimums[-1]


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)

assert stack.get_min() == -3
assert stack.pop() == -3
assert stack.top() == 0
assert stack.get_min() == -2

stack.push(-2)
assert stack.get_min() == -2
stack.pop()
assert stack.get_min() == -2

print("所有测试通过")