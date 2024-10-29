## Đề bài

Bạn được cho hai mảng số nguyên `nums1` và `nums2`, được sắp xếp theo thứ tự không giảm, và hai số nguyên `m` và `n`, đại diện cho số lượng phần tử trong `nums1` và `nums2` tương ứng.

Hãy hợp nhất `nums1` và `nums2` thành một mảng duy nhất được sắp xếp theo thứ tự không giảm.

Mảng đã sắp xếp cuối cùng không nên được trả về bởi hàm, mà thay vào đó nên được lưu trữ bên trong mảng `nums1`. Để làm điều này, `nums1` có độ dài là `m + n`, trong đó `m` phần tử đầu tiên là các phần tử cần được hợp nhất, và `n` phần tử cuối cùng được đặt thành 0 và nên bị bỏ qua. `nums2` có độ dài là `n`.

### Ví dụ 1:

- **Đầu vào**: `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`
- **Đầu ra**: `[1,2,2,3,5,6]`
- **Giải thích**: Các mảng mà chúng ta đang hợp nhất là `[1,2,3]` và `[2,5,6]`. Kết quả của việc hợp nhất là `[1,2,2,3,5,6]` với các phần tử gạch dưới đến từ `nums1`.

### Ví dụ 2:

- **Đầu vào**: `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`
- **Đầu ra**: `[1]`
- **Giải thích**: Các mảng mà chúng ta đang hợp nhất là `[1]` và `[]`. Kết quả của việc hợp nhất là `[1]`.

### Ví dụ 3:

- **Đầu vào**: `nums1 = [0]`, `m = 0`, `nums2 = [1]`, `n = 1`
- **Đầu ra**: `[1]`
- **Giải thích**: Các mảng mà chúng ta đang hợp nhất là `[]` và `[1]`. Kết quả của việc hợp nhất là `[1]`. Lưu ý rằng vì `m = 0`, không có phần tử nào trong `nums1`. Số 0 chỉ có mặt để đảm bảo rằng kết quả hợp nhất có thể vừa vặn trong `nums1`.

### Ràng buộc:

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Theo dõi:

Bạn có thể nghĩ ra một thuật toán chạy trong thời gian O(m + n) không?

---

## Giải pháp

Để hợp nhất hai mảng đã sắp xếp một cách hiệu quả, bạn có thể sử dụng kỹ thuật hai con trỏ cho phép bạn duyệt qua cả hai mảng từ cuối về phía đầu. Bằng cách này, bạn có thể điền mảng `nums1` từ phía sau, đảm bảo rằng bạn không ghi đè lên bất kỳ phần tử nào vẫn cần được so sánh.

### Các bước thực hiện giải pháp:

1. **Khởi tạo các con trỏ**:
   - Đặt hai con trỏ: một cho phần tử cuối cùng của phần hợp nhất trong `nums1` (`m - 1`) và một cho phần tử cuối cùng của `nums2` (`n - 1`).
   - Đặt một con trỏ thứ ba cho vị trí cuối cùng trong `nums1` (`m + n - 1`).

2. **Hợp nhất từ cuối**:
   - Trong khi vẫn còn các phần tử cần được hợp nhất từ `nums2`:
     - So sánh các phần tử được chỉ định bởi cả hai con trỏ.
     - Đặt phần tử lớn hơn tại vị trí hiện tại của `nums1`.
     - Di chuyển con trỏ tương ứng và con trỏ thứ ba lùi lại một bước.

3. **Sao chép các phần tử còn lại**:
   - Nếu vẫn còn bất kỳ phần tử nào trong `nums2`, hãy sao chép chúng vào `nums1` (điều này cần thiết nếu `nums2` có các phần tử nhỏ hơn phần tử nhỏ nhất trong `nums1`).

### Mã Python triển khai:

```python
def merge(nums1, m, nums2, n):
    # Các con trỏ cho nums1, nums2 và cuối mảng đã hợp nhất
    i, j, k = m - 1, n - 1, m + n - 1
    
    # Hợp nhất theo thứ tự ngược
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # Nếu còn bất kỳ phần tử nào trong nums2, sao chép chúng
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Ví dụ sử dụng:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Đầu ra: [1, 2, 2, 3, 5, 6]
