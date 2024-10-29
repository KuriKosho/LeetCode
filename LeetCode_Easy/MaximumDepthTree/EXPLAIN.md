# Tìm độ sâu tối đa của cây nhị phân

Cho gốc của một cây nhị phân, chúng ta cần trả về độ sâu tối đa của cây. Độ sâu tối đa của một cây nhị phân là số lượng nút dọc theo đường đi dài nhất từ nút gốc xuống đến nút lá xa nhất.

## Ví dụ

### Ví dụ 1

- **Input**: `root = [3,9,20,null,null,15,7]`
- **Output**: `3`
- **Giải thích**: Độ sâu tối đa là 3 (đường đi từ nút 3 đến nút 15 hoặc 7).

### Ví dụ 2

- **Input**: `root = [1,null,2]`
- **Output**: `2`
- **Giải thích**: Độ sâu tối đa là 2 (đường đi từ nút 1 đến nút 2).

## Ràng buộc

- Số lượng nút trong cây nằm trong khoảng [0, 10^4].
- -100 <= Node.val <= 100.

## Giải pháp

Chúng ta có thể giải quyết bài toán này bằng cách sử dụng phương pháp đệ quy. Dưới đây là mã mẫu bằng Python:

### Mã Python

```python
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
