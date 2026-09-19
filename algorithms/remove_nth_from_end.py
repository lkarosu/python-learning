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


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


assert linked_list_to_list(
    remove_nth_from_end(build_linked_list([1, 2, 3, 4, 5]), 2)
) == [1, 2, 3, 5]

assert linked_list_to_list(
    remove_nth_from_end(build_linked_list([1, 2]), 2)
) == [2]

assert remove_nth_from_end(build_linked_list([1]), 1) is None

print("所有测试通过")