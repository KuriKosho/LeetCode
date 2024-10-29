# Giải Thích và Hướng Dẫn Giải Quyết Bài Toán Xóa Phần Tử Trùng Lặp trong Mảng

## Đề Bài
Cho một mảng số nguyên `nums` đã được sắp xếp theo thứ tự không giảm, nhiệm vụ của chúng ta là loại bỏ các phần tử trùng lặp trong mảng này sao cho mỗi phần tử duy nhất chỉ xuất hiện một lần. Sắp xếp tương đối của các phần tử phải được giữ nguyên. Cuối cùng, trả về số lượng phần tử duy nhất trong `nums`.

## Cách Giải Quyết Bài Toán

### Bước 1: Khởi Tạo
- **Kiểm Tra Mảng Rỗng**: Nếu mảng `nums` rỗng, trả về `0` ngay lập tức.
- **Khởi Tạo Chỉ Số**: Tạo một biến `i` và khởi tạo nó bằng `0`. `i` sẽ dùng để theo dõi vị trí của phần tử duy nhất cuối cùng trong mảng.

### Bước 2: Duyệt Qua Mảng
- **Sử Dụng Hai Con Trỏ**: Duyệt qua mảng bằng cách sử dụng một vòng lặp `for` với biến `j`, bắt đầu từ chỉ số `1` (phần tử thứ hai của mảng) đến hết mảng.
- **So Sánh Phần Tử**: Tại mỗi bước, so sánh `nums[j]` với `nums[i]`:
  - Nếu chúng khác nhau (có nghĩa là `nums[j]` là phần tử duy nhất), thì:
    - Tăng giá trị của `i` lên `1` để di chuyển đến vị trí tiếp theo.
    - Cập nhật `nums[i]` bằng `nums[j]`, tức là gán phần tử duy nhất vào mảng.

### Bước 3: Cập Nhật Mảng
- **Đặt Giá Trị Sau k**: Sau khi hoàn thành vòng lặp, tất cả các phần tử duy nhất sẽ nằm trong `nums` từ chỉ số `0` đến `i`. Những phần tử sau chỉ số `i` không quan trọng và có thể được giữ nguyên hoặc thay bằng một ký tự khác (ví dụ: `_`).

### Bước 4: Trả Kết Quả
- **Trả Về Số Lượng Phần Tử Duy Nhất**: Trả về giá trị `i + 1`, đây là số lượng phần tử duy nhất trong mảng.

## Code

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    
    i = 0  # Pointer for the last unique element found
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    # Fill the remaining elements with underscores (optional, only for display purposes)
    for k in range(i + 1, len(nums)):
        nums[k] = '_'
    
    return i + 1
