class ListNode:
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node


def build_linked_list(values: list[int]) -> ListNode | None:
    head = None

    for value in reversed(values):
        head = ListNode(value, head)

    return head


def linked_list_to_list(head: ListNode | None) -> list[int]:
    values = []

    while head is not None:
        values.append(head.value)
        head = head.next

    return values


def reverse_list(head: ListNode | None) -> ListNode | None:
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


assert linked_list_to_list(reverse_list(build_linked_list([1, 2, 3]))) == [3, 2, 1]
assert reverse_list(None) is None
assert linked_list_to_list(reverse_list(build_linked_list([42]))) == [42]

print("所有测试通过")