# Kiểm Tra Tính Hợp Lệ Của Chuỗi Dấu Ngoặc

## Bài Toán
Cho một chuỗi `s` chỉ chứa các ký tự `'('`, `')'`, `'{'`, `'}'`, `'['` và `']'`, hãy xác định xem chuỗi đầu vào có hợp lệ hay không.

### Điều Kiện Hợp Lệ
Một chuỗi được coi là hợp lệ nếu:
1. Các dấu ngoặc mở phải được đóng bởi cùng một loại dấu ngoặc.
2. Các dấu ngoặc mở phải được đóng theo đúng thứ tự.
3. Mỗi dấu ngoặc đóng phải có một dấu ngoặc mở tương ứng cùng loại.

### Ví dụ
- **Ví dụ 1**:
  - **Input**: `s = "()"` 
  - **Output**: `true`
  
- **Ví dụ 2**:
  - **Input**: `s = "()[]{}"`
  - **Output**: `true`
  
- **Ví dụ 3**:
  - **Input**: `s = "(]"`
  - **Output**: `false`
  
- **Ví dụ 4**:
  - **Input**: `s = "([])"`
  - **Output**: `true`

## Giải Pháp
Để kiểm tra tính hợp lệ của chuỗi dấu ngoặc, chúng ta có thể sử dụng cấu trúc dữ liệu ngăn xếp (stack). Ngăn xếp sẽ giúp chúng ta theo dõi các dấu ngoặc mở và đảm bảo rằng mỗi dấu ngoặc đóng phù hợp với dấu ngoặc mở gần nhất.

### Các Bước Thực Hiện

1. **Khởi Tạo Ngăn Xếp**: Tạo một ngăn xếp rỗng để lưu trữ các dấu ngoặc mở khi gặp chúng.

2. **Bản Đồ Tương Ứng Dấu Ngoặc**: Tạo một bản đồ để ánh xạ các dấu ngoặc đóng đến dấu ngoặc mở tương ứng. Điều này giúp dễ dàng tra cứu.

3. **Duyệt Qua Từng Ký Tự**:
   - Nếu ký tự là dấu ngoặc mở (`'('`, `'{'`, `'['`), đẩy nó vào ngăn xếp.
   - Nếu là dấu ngoặc đóng (`')'`, `'}'`, `']'`):
     - Kiểm tra xem ngăn xếp có rỗng không. Nếu có, trả về `false` (nghĩa là không có dấu ngoặc mở tương ứng).
     - Lấy phần tử trên cùng ra khỏi ngăn xếp và kiểm tra xem nó có phù hợp với dấu ngoặc mở tương ứng cho dấu ngoặc đóng hiện tại không. Nếu không, trả về `false`.

4. **Kiểm Tra Cuối Cùng**: Sau khi xử lý tất cả các ký tự, nếu ngăn xếp rỗng, trả về `true` (tất cả các dấu ngoặc đã được đóng). Nếu ngăn xếp không rỗng, trả về `false`.

### Mã Python

Dưới đây là cách cài đặt giải pháp trong Python:

```python
def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # Nếu là dấu ngoặc mở
            stack.append(char)
        elif char in bracket_map.keys():  # Nếu là dấu ngoặc đóng
            if not stack or stack[-1] != bracket_map[char]:  # Kiểm tra tính hợp lệ
                return False
            stack.pop()  # Khớp hợp lệ, bỏ dấu ngoặc mở

    return not stack  # Trả về True nếu ngăn xếp rỗng, ngược lại False
