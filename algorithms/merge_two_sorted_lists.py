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


def merge_two_lists(
    first: ListNode | None,
    second: ListNode | None,
) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy

    while first is not None and second is not None:
        if first.value <= second.value:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next

        tail = tail.next

    if first is not None:
        tail.next = first
    else:
        tail.next = second

    return dummy.next


assert linked_list_to_list(
    merge_two_lists(
        build_linked_list([1, 2, 4]),
        build_linked_list([1, 3, 4]),
    )
) == [1, 1, 2, 3, 4, 4]

assert linked_list_to_list(
    merge_two_lists(None, build_linked_list([0]))
) == [0]

assert linked_list_to_list(
    merge_two_lists(
        build_linked_list([1, 1]),
        build_linked_list([1, 1]),
    )
) == [1, 1, 1, 1]

print("所有测试通过")