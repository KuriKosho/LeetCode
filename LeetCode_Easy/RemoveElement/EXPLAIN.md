# Bài Toán: Loại Bỏ Tất Cả Các Phần Tử Có Giá Trị Xác Định trong Mảng

Cho một mảng số nguyên `nums` và một số nguyên `val`, loại bỏ tất cả các phần tử có giá trị `val` trong `nums` trực tiếp trên mảng. Thứ tự của các phần tử có thể thay đổi và hàm nên trả về số phần tử trong `nums` không bằng `val`.

### Yêu Cầu

- Thay đổi mảng `nums` sao cho `k` phần tử đầu tiên chứa các phần tử không bằng `val`.
- Hàm cần trả về `k`, là số phần tử không bằng `val` trong mảng.

### Ví Dụ

1. **Input**: `nums = [3,2,2,3]`, `val = 3`  
   **Output**: `2`, `nums = [2,2,_,_]`
   
2. **Input**: `nums = [0,1,2,2,3,0,4,2]`, `val = 2`  
   **Output**: `5`, `nums = [0,1,4,0,3,_,_,_]`


## Hướng Giải Quyết

Để giải bài toán này, chúng ta có thể sử dụng kỹ thuật hai con trỏ:

1. **Kỹ Thuật Hai Con Trỏ**:
   - Khởi tạo hai con trỏ:
     - `i` để duyệt qua mảng.
     - `n` chỉ đến vị trí cuối cùng hợp lệ trong mảng (`n = len(nums) - 1`).
   - Khi duyệt qua `nums` với `i`, thực hiện:
     - Nếu `nums[i]` bằng `val`, thay `nums[i]` bằng `nums[n]` (phần tử ở cuối) và giảm `n` đi 1.
     - Nếu `nums[i]` không bằng `val`, tăng `i` để tiếp tục.
   - Phương pháp này "hoán đổi" các phần tử `val` bằng cách chuyển chúng về cuối mảng, trong khi các phần tử hợp lệ sẽ giữ ở đầu mảng.

2. **Trả Về Kết Quả**:
   - Sau khi hoàn thành vòng lặp, `n + 1` sẽ là số phần tử không bằng `val`.

## Mã Python

```python
def removeElement(nums, val):
    n = len(nums) - 1  # Khởi tạo con trỏ cho phần tử cuối

    i = 0
    while i <= n:
        if nums[i] == val:
            nums[i] = nums[n]  # Thay thế phần tử tại i bằng phần tử tại n
            n -= 1  # Giảm kích thước của mảng hợp lệ
        else:
            i += 1  # Chuyển sang phần tử tiếp theo nếu nums[i] không bằng val
    
    return n + 1  # Số phần tử không bằng val
