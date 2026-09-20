class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


root = TreeNode(
    1,
    left=TreeNode(
        2,
        left=TreeNode(4),
    ),
    right=TreeNode(3),
)

assert max_depth(root) == 3
assert max_depth(None) == 0
assert max_depth(TreeNode(42)) == 1

print("所有测试通过")