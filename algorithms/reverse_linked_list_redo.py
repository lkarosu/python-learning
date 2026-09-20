class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head: ListNode) -> ListNode | None:
    if head is None:
        return None
    prev = None
    current = head

    while current:
        next_node = current.next  
        current.next = prev       
        prev = current            
        current = next_node       

    return prev


def list_to_linked_list(lst: list[int]) -> ListNode | None:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(head: ListNode) -> list[int] | None:
    if head is None:
        return None
    lst = []
    current = head
    while current:
        lst.append(current.value)
        current = current.next
    return lst

assert linked_list_to_list(reverse_list(list_to_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
assert linked_list_to_list(reverse_list(list_to_linked_list([1, 2, 3]))) == [3, 2, 1]
assert linked_list_to_list(reverse_list(list_to_linked_list([]))) == None
assert linked_list_to_list(reverse_list(list_to_linked_list([42]))) == [42]

print("反转链表闭卷复做通过")