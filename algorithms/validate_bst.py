class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    def validate(node: TreeNode | None, lower: float, upper: float) -> bool:
        if node is None:
            return True

        if not lower < node.value < upper:
            return False

        return (
            validate(node.left, lower, node.value)
            and validate(node.right, node.value, upper)
        )

    return validate(root, float("-inf"), float("inf"))


valid_root = TreeNode(
    5,
    left=TreeNode(3, TreeNode(2), TreeNode(4)),
    right=TreeNode(7, TreeNode(6), TreeNode(8)),
)
assert is_valid_bst(valid_root) is True

invalid_root = TreeNode(
    5,
    left=TreeNode(1),
    right=TreeNode(
        7,
        left=TreeNode(4),
        right=TreeNode(8),
    ),
)
assert is_valid_bst(invalid_root) is False

assert is_valid_bst(None) is True

print("所有测试通过")