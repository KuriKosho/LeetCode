# Bài toán: Tính Căn Bậc Hai Của Số Nguyên

Cho một số nguyên không âm `x`, trả về căn bậc hai của `x`, làm tròn xuống tới số nguyên gần nhất. Số nguyên trả về cũng phải không âm. Không được phép sử dụng các hàm lũy thừa tích hợp hoặc toán tử như `pow` hoặc `**`.

### Ví dụ

1. **Ví dụ 1:**
   - **Input**: `x = 4`
   - **Output**: `2`
   - **Giải thích**: Căn bậc hai của 4 là 2, nên chúng ta trả về 2.

2. **Ví dụ 2:**
   - **Input**: `x = 8`
   - **Output**: `2`
   - **Giải thích**: Căn bậc hai của 8 xấp xỉ 2.828, và khi làm tròn xuống số nguyên gần nhất, ta có 2.

### Ràng buộc

- \(0 \leq x \leq 2^{31} - 1\)

### Hướng giải quyết

Ta có thể giải quyết bài toán này bằng cách sử dụng phương pháp tìm kiếm nhị phân, cho phép tìm căn bậc hai nguyên một cách hiệu quả với độ phức tạp \(O(\log x)\).

#### Các bước thực hiện:
1. **Thiết lập Tìm kiếm Nhị phân**: 
   - Khởi tạo `left` là 0 và `right` là `x`.
   - Chúng ta sẽ tìm trong khoảng này để xác định căn bậc hai nguyên.

2. **Thực hiện Tìm kiếm Nhị phân**:
   - Tính `mid` là giá trị giữa `left` và `right`.
   - Nếu `mid * mid` bằng `x`, thì `mid` là căn bậc hai nguyên của `x`.
   - Nếu `mid * mid` nhỏ hơn `x`, nghĩa là kết quả lớn hơn `mid`, ta di chuyển `left` sang `mid + 1`.
   - Nếu `mid * mid` lớn hơn `x`, nghĩa là kết quả nhỏ hơn `mid`, ta di chuyển `right` về `mid - 1`.

3. **Trả về Kết quả**:
   - Vì chúng ta cần tìm phần nguyên, `right` sẽ ở vị trí của căn bậc hai nguyên gần nhất của `x` sau khi kết thúc tìm kiếm nhị phân.

### Mã Giải pháp

```python
def mySqrt(x):
    # Khởi tạo giới hạn tìm kiếm nhị phân
    left, right = 0, x
    
    # Vòng lặp tìm kiếm nhị phân
    while left <= right:
        mid = (left + right) // 2
        # Kiểm tra nếu mid là căn bậc hai của x
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    # Trả về số nguyên lớn nhất nhỏ hơn hoặc bằng căn bậc hai
    return right
