class ListNode:
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node


def has_cycle(head: ListNode | None) -> bool:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


no_cycle = ListNode(1, ListNode(2, ListNode(3)))
assert has_cycle(no_cycle) is False

first = ListNode(1)
second = ListNode(2)
third = ListNode(3)

first.next = second
second.next = third
third.next = second

assert has_cycle(first) is True

print("所有测试通过")