class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def _move_if_needed(self) -> None:
        if self.output_stack:
            return

        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

    def push(self, value: int) -> None:
        self.input_stack.append(value)

    def pop(self) -> int:
        self._move_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_if_needed()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


queue = MyQueue()
queue.push(1)
queue.push(2)

assert queue.peek() == 1
assert queue.pop() == 1

queue.push(3)

assert queue.pop() == 2
assert queue.peek() == 3
assert queue.pop() == 3
assert queue.empty() is True

print("所有测试通过")