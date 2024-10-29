# Tìm Tiền Tố Chung Dài Nhất Trong Mảng Chuỗi

## Bài Toán
Chúng ta cần viết một hàm để tìm tiền tố chung dài nhất trong một mảng các chuỗi. Nếu không có tiền tố chung, hàm sẽ trả về một chuỗi rỗng.

### Ví dụ
**Ví dụ 1:**
- **Input**: `strs = ["flower", "flow", "flight"]`
- **Output**: `"fl"`

**Ví dụ 2:**
- **Input**: `strs = ["dog", "racecar", "car"]`
- **Output**: `""`
- **Giải thích**: Không có tiền tố chung giữa các chuỗi đầu vào.

## Giải Pháp
Để tìm tiền tố chung dài nhất, chúng ta có thể sử dụng phương pháp sau:

1. **Khởi tạo**: Bắt đầu với tiền tố là chuỗi đầu tiên trong mảng.
2. **So sánh**: Duyệt qua từng chuỗi trong mảng và so sánh với tiền tố hiện tại:
   - Nếu chuỗi nào không bắt đầu bằng tiền tố hiện tại, chúng ta sẽ cắt ngắn tiền tố đến khi tìm thấy một tiền tố chung.
3. **Kết thúc**: Nếu tiền tố trở thành một chuỗi rỗng, có nghĩa là không có tiền tố chung.

### Mã Python
```python
def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Khởi tạo tiền tố là chuỗi đầu tiên
    prefix = strs[0]

    # Duyệt qua từng chuỗi trong mảng
    for s in strs[1:]:
        # Cắt ngắn tiền tố nếu không khớp với chuỗi hiện tại
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
