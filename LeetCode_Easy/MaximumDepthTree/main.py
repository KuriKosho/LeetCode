# Định nghĩa cho một nút của cây nhị phân.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        # Tính độ sâu tối đa cho cả hai nhánh trái và phải
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Độ sâu tối đa của cây là độ sâu lớn hơn giữa nhánh trái và phải cộng thêm 1
        return max(left_depth, right_depth) + 1

# Ví dụ sử dụng
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.maxDepth(root))  # Kết quả: 3
