from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

assert level_order(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == [[1], [2, 3], [4, 5]]
assert level_order(None) == []
assert level_order(TreeNode(42)) == [[42]]
print("二叉树层序遍历闭卷复做通过")