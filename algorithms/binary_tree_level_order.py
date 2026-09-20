from collections import deque


class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        result.append(level)

    return result


root = TreeNode(
    1,
    left=TreeNode(
        2,
        left=TreeNode(4),
        right=TreeNode(5),
    ),
    right=TreeNode(3),
)

assert level_order(root) == [[1], [2, 3], [4, 5]]
assert level_order(None) == []
assert level_order(TreeNode(42)) == [[42]]

print("所有测试通过")