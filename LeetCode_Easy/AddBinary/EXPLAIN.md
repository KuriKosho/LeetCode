# Bài Toán: Cộng Hai Chuỗi Nhị Phân

Cho hai chuỗi nhị phân `a` và `b`, trả về tổng của chúng dưới dạng một chuỗi nhị phân.

### Ví Dụ

1. **Ví dụ 1:**
   - **Input**: `a = "11"`, `b = "1"`
   - **Output**: `"100"`
   - **Giải Thích**: 11 (3 trong hệ thập phân) + 1 = 100 (4 trong hệ nhị phân).

2. **Ví dụ 2:**
   - **Input**: `a = "1010"`, `b = "1011"`
   - **Output**: `"10101"`
   - **Giải Thích**: 1010 (10 trong hệ thập phân) + 1011 (11 trong hệ thập phân) = 10101 (21 trong hệ nhị phân).

### Ràng Buộc

- \(1 \leq \text{len}(a), \text{len}(b) \leq 10^4\)
- `a` và `b` chỉ chứa các ký tự `'0'` hoặc `'1'`.
- Không có số 0 ở đầu mỗi chuỗi trừ khi chuỗi là `"0"`.

## Hướng Giải Quyết

1. **Sử Dụng Hai Con Trỏ**:
   - Khởi tạo hai con trỏ `i` và `j` để duyệt từ cuối của `a` và `b`.
   - Tạo biến `carry` để lưu trữ số dư khi tính tổng.
   - Duyệt từ cuối đến đầu, cộng các chữ số tương ứng của `a` và `b`, cùng với `carry` hiện tại, và tính giá trị kết quả.

2. **Xử Lý Từng Bước**:
   - Cộng chữ số ở vị trí hiện tại của `a` và `b` với `carry`.
   - Tính chữ số hiện tại trong kết quả bằng cách lấy phần dư khi chia cho 2.
   - Cập nhật `carry` bằng cách lấy phần nguyên khi chia cho 2.
   - Di chuyển hai con trỏ `i` và `j` sang trái và lặp lại cho đến khi không còn ký tự nào.

3. **Xử Lý Trường Hợp Còn `carry` Sau Cùng**:
   - Nếu sau khi duyệt hết các ký tự mà vẫn còn `carry`, thêm `carry` vào đầu của kết quả.

### Mã Python

```python
def addBinary(a, b):
    # Khởi tạo các biến
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    
    # Lặp lại cho đến khi duyệt hết cả hai chuỗi
    while i >= 0 or j >= 0 or carry:
        # Lấy giá trị chữ số hiện tại của a và b, nếu có
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        # Tính tổng và cập nhật carry
        total = digit_a + digit_b + carry
        result.append(str(total % 2))  # Lưu chữ số vào kết quả
        carry = total // 2  # Cập nhật carry
        
        # Di chuyển con trỏ sang trái
        i -= 1
        j -= 1
    
    # Kết quả phải được đảo ngược vì chúng ta thêm vào từ cuối
    return ''.join(result[::-1])
