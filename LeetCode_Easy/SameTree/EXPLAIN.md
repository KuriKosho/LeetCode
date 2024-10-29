## Đề bài

Cho hai cây nhị phân `p` và `q`, hãy viết một hàm để kiểm tra xem chúng có giống nhau hay không.

Hai cây nhị phân được coi là giống nhau nếu chúng có cấu trúc giống hệt nhau và các nút có cùng giá trị.

### Ví dụ 1:

- **Input**: `p = [1,2,3]`, `q = [1,2,3]`
- **Output**: `true`

### Ví dụ 2:

- **Input**: `p = [1,2]`, `q = [1,null,2]`
- **Output**: `false`

### Ví dụ 3:

- **Input**: `p = [1,2,1]`, `q = [1,1,2]`
- **Output**: `false`

### Ràng buộc:

- Số lượng nút trong cả hai cây nằm trong khoảng `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Phương pháp giải

Để xác định xem hai cây nhị phân có giống nhau hay không, chúng ta có thể sử dụng phương pháp đệ quy. Ý tưởng chính là so sánh giá trị của các nút ở mỗi vị trí tương ứng trong cả hai cây.

### Các bước giải:

1. **Trường hợp cơ sở**:
   - Nếu cả hai nút đều là `null`, trả về `true` (chúng giống nhau ở thời điểm này).
   - Nếu một trong hai nút là `null` và nút còn lại không phải là `null`, trả về `false` (chúng không thể giống nhau).
   - Nếu giá trị của hai nút khác nhau, trả về `false`.

2. **So sánh đệ quy**:
   - Đệ quy kiểm tra cây con bên trái và cây con bên phải của cả hai nút.
   - Nếu cả hai cây con đều giống nhau, trả về `true`.

### Cài đặt trong Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # Trường hợp cơ sở: cả hai nút đều là None
    if not p and not q:
        return True
    # Nếu một trong hai nút là None hoặc giá trị khác nhau
    if not p or not q or p.val != q.val:
        return False
    
    # Đệ quy kiểm tra cây con bên trái và bên phải
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Ví dụ sử dụng:
# Tạo hai cây nhị phân và kiểm tra xem chúng có giống nhau không
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p, q))  # Output: True
