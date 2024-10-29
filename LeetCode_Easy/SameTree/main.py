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