# Bài Toán: Tìm Chỉ Mục hoặc Vị Trí Chèn của Giá Trị Mục Tiêu trong Mảng Đã Sắp Xếp

Cho một mảng `nums` đã sắp xếp theo thứ tự tăng dần và chứa các phần tử duy nhất. Cho trước một giá trị mục tiêu `target`, hãy tìm chỉ mục của `target` nếu nó tồn tại trong `nums`. Nếu không tồn tại, trả về chỉ mục nơi `target` sẽ được chèn để giữ nguyên thứ tự của mảng.

**Yêu cầu:** Viết một thuật toán có độ phức tạp thời gian là \(O(\log n)\).

### Ví Dụ

1. **Input**: `nums = [1,3,5,6]`, `target = 5`  
   **Output**: `2`  
   **Giải Thích**: `5` nằm ở chỉ mục `2` trong mảng.

2. **Input**: `nums = [1,3,5,6]`, `target = 2`  
   **Output**: `1`  
   **Giải Thích**: `2` không có trong `nums`. Nếu được chèn vào để giữ thứ tự, `2` sẽ nằm ở chỉ mục `1`.

3. **Input**: `nums = [1,3,5,6]`, `target = 7`  
   **Output**: `4`  
   **Giải Thích**: `7` không có trong `nums`. Nếu được chèn vào để giữ thứ tự, `7` sẽ nằm ở cuối mảng.

### Ràng Buộc

- `nums` chứa các giá trị duy nhất và được sắp xếp tăng dần.

## Hướng Giải Quyết

1. **Tìm Kiếm Nhị Phân**:
   - Sử dụng tìm kiếm nhị phân để đạt được độ phức tạp thời gian \(O(\log n)\).
   - Khởi tạo hai con trỏ `left` và `right` chỉ vào đầu và cuối của mảng.
   - Trong vòng lặp:
     - Tính `mid` là vị trí giữa `left` và `right`.
     - Nếu `nums[mid] == target`, trả về `mid`.
     - Nếu `nums[mid] < target`, di chuyển `left` sang `mid + 1`.
     - Nếu `nums[mid] > target`, di chuyển `right` sang `mid - 1`.
   - Kết thúc vòng lặp: nếu không tìm thấy `target`, `left` sẽ là vị trí mà `target` cần được chèn vào để giữ thứ tự.

### Mã Python

```python
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid  # Tìm thấy target tại chỉ mục mid
        elif nums[mid] < target:
            left = mid + 1  # Tìm kiếm phía phải
        else:
            right = mid - 1  # Tìm kiếm phía trái
    
    return left  # left là vị trí cần chèn target nếu không tìm thấy

# Kiểm Tra Kết Quả
print(searchInsert([1,3,5,6], 5))  # 2
# Step 1: left = 0, right = 3, mid = 1
# Step 2: left = 2, right = 3, mid = 2
# Step 3: left = 2, right = 2, mid = 2
# Output: 2