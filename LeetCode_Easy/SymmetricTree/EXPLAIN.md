# Kiểm tra xem cây nhị phân có đối xứng hay không

Để xác định xem một cây nhị phân có đối xứng (tức là, nó là hình chiếu của chính nó xung quanh tâm) hay không, chúng ta có thể sử dụng cả hai phương pháp đệ quy và lặp. Dưới đây, tôi sẽ cung cấp các triển khai cho cả hai phương pháp.

## Giải pháp Đệ quy

Trong phương pháp đệ quy, chúng ta có thể định nghĩa một hàm trợ giúp kiểm tra xem hai cây con có phải là hình chiếu của nhau hay không. Hai cây được coi là hình chiếu nếu:
1. Gốc của chúng bằng nhau.
2. Cây con bên trái của một cây là hình chiếu của cây con bên phải của cây kia, và ngược lại.

### Mã

```python
# Định nghĩa cho một nút của cây nhị phân.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)
