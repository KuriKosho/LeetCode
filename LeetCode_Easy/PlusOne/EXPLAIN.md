# Bài Toán: Tăng Giá Trị Số Nguyên Lớn Được Biểu Diễn Dưới Dạng Mảng

Cho một số nguyên lớn được biểu diễn dưới dạng mảng `digits`, trong đó `digits[i]` là chữ số thứ `i` của số nguyên. Các chữ số được sắp xếp từ có ý nghĩa cao nhất đến thấp nhất theo thứ tự từ trái sang phải. Không có chữ số 0 ở đầu mảng.

Nhiệm vụ của bạn là tăng số nguyên này lên 1 và trả về mảng kết quả.

### Ví Dụ

1. **Input**: `digits = [1,2,3]`  
   **Output**: `[1,2,4]`  
   **Giải Thích**: Mảng đại diện cho số 123. Tăng lên 1 được 124, nên kết quả là `[1,2,4]`.

2. **Input**: `digits = [4,3,2,1]`  
   **Output**: `[4,3,2,2]`  
   **Giải Thích**: Mảng đại diện cho số 4321. Tăng lên 1 được 4322, nên kết quả là `[4,3,2,2]`.

3. **Input**: `digits = [9]`  
   **Output**: `[1,0]`  
   **Giải Thích**: Mảng đại diện cho số 9. Tăng lên 1 được 10, nên kết quả là `[1,0]`.

### Ràng Buộc

- \(1 \leq \text{digits.length} \leq 100\)
- \(0 \leq \text{digits}[i] \leq 9\)
- `digits` không chứa chữ số 0 ở đầu.

## Hướng Giải Quyết

1. **Duyệt Ngược**:
   - Duyệt qua mảng `digits` từ phải sang trái.
   - Nếu chữ số hiện tại là 9, khi tăng lên 1 sẽ gây ra việc "nhớ" (carry) do 9 + 1 = 10, nên ta đặt chữ số đó thành 0 và tiếp tục duyệt sang trái.
   - Nếu chữ số hiện tại khác 9, chỉ cần tăng chữ số đó lên 1 và trả về mảng kết quả.

2. **Xử Lý Trường Hợp Đặc Biệt**:
   - Nếu toàn bộ các chữ số là 9 (ví dụ `[9,9,9]`), việc tăng lên 1 sẽ tạo ra một mảng mới với 1 ở đầu và tất cả các số còn lại là 0 (ví dụ `[1,0,0,0]`).

### Mã Python

```python
def plusOne(digits):
    # Duyệt ngược qua từng chữ số trong mảng
    for i in range(len(digits) - 1, -1, -1):
        # Nếu chữ số khác 9, tăng lên 1 và trả về mảng
        if digits[i] != 9:
            digits[i] += 1
            return digits
        # Nếu chữ số là 9, đặt thành 0 (carry)
        digits[i] = 0
    
    # Trường hợp tất cả các chữ số là 9, thêm 1 ở đầu mảng
    return [1] + digits
