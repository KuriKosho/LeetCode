## Đề Bài

Cho đầu của một danh sách liên kết đã được sắp xếp, xóa tất cả các phần tử trùng lặp sao cho mỗi phần tử chỉ xuất hiện một lần. Trả về danh sách liên kết đã được sắp xếp.

### Ví Dụ 1:

- **Đầu vào**: `head = [1,1,2]`
- **Đầu ra**: `[1,2]`

### Ví Dụ 2:

- **Đầu vào**: `head = [1,1,2,3,3]`
- **Đầu ra**: `[1,2,3]`

### Ràng Buộc:

- Số lượng nút trong danh sách nằm trong khoảng `[0, 300]`.
- `-100 <= Node.val <= 100`
- Danh sách được đảm bảo là đã được sắp xếp theo thứ tự tăng dần.

## Giải Pháp

Để giải quyết vấn đề xóa các phần tử trùng lặp từ một danh sách liên kết đã sắp xếp, bạn có thể làm theo các bước sau:

1. **Khởi Tạo Con Trỏ**: Sử dụng một con trỏ để duyệt qua danh sách liên kết, bắt đầu từ đầu.
2. **Duyệt Qua Danh Sách**: Khi bạn duyệt qua danh sách, so sánh giá trị của nút hiện tại với giá trị của nút tiếp theo.
3. **Xóa Các Phần Tử Trùng Lặp**: Nếu các giá trị giống nhau, hãy bỏ qua nút tiếp theo bằng cách điều chỉnh con trỏ `next` của nút hiện tại để trỏ đến nút sau nút tiếp theo. Nếu chúng khác nhau, chỉ cần di chuyển con trỏ hiện tại đến nút tiếp theo.
4. **Trả Về Đầu**: Sau khi duyệt qua danh sách, trả về đầu của danh sách liên kết đã được chỉnh sửa.

### Triển Khai Mã Python

Dưới đây là một ví dụ triển khai bằng Python:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Trường hợp đặc biệt: nếu danh sách rỗng
        if not head:
            return head
        
        current = head  # Khởi tạo con trỏ hiện tại
        
        while current and current.next:  # Duyệt qua danh sách
            if current.val == current.next.val:  # Kiểm tra phần tử trùng lặp
                current.next = current.next.next  # Bỏ qua phần tử trùng lặp
            else:
                current = current.next  # Di chuyển đến nút tiếp theo
        
        return head  # Trả về đầu của danh sách đã được chỉnh sửa
        
# Cách tối ưu nhất
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head    