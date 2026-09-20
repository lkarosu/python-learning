class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    return [root.value] + preorder(root.left) + preorder(root.right)


root = TreeNode(
    1,
    left=TreeNode(
        2,
        left=TreeNode(4),
        right=TreeNode(5),
    ),
    right=TreeNode(3),
)

assert preorder(root) == [1, 2, 4, 5, 3]
assert preorder(None) == []
assert preorder(TreeNode(42)) == [42]

print("所有测试通过")