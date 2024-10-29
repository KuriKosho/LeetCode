# Giải thích từng dòng của hàm `two_sum`

- **`hash_map = {}`**: Khởi tạo một bảng băm (hash map) rỗng, dùng để lưu trữ các phần tử đã duyệt qua cùng với chỉ số của chúng trong mảng `nums`.

- **`for i, num in enumerate(nums):`**: Dùng vòng lặp `for` để duyệt qua từng phần tử `num` của mảng `nums`, với `i` là chỉ số của phần tử đó. Vòng lặp sẽ kiểm tra từng phần tử của `nums` để tìm ra cặp số có tổng bằng `target`.

- **`diff = target - num`**: Tính giá trị `diff` là giá trị còn thiếu để tổng hai số đạt được giá trị `target`. Cụ thể, `diff` chính là số cần tìm để khi cộng với `num` sẽ ra `target`.

- **`if diff in hash_map:`**: Kiểm tra xem `diff` có trong bảng băm `hash_map` hay không:
  - Nếu có, điều này có nghĩa là đã tìm thấy một phần tử `num` trong `nums` sao cho `diff + num = target`.
  - Tức là đã tìm ra một cặp số `num` và `diff` có tổng bằng `target`. Do đó, hàm sẽ trả về `[hash_map[diff], i]`, là chỉ số của `diff` (được lưu trong `hash_map`) và chỉ số hiện tại `i` của `num`.

- **`hash_map[num] = i`**: Nếu `diff` không có trong `hash_map`, thêm `num` vào `hash_map` với khóa là `num` và giá trị là `i` (chỉ số của phần tử đó). Điều này lưu trữ `num` để có thể kiểm tra trong các lần lặp sau nếu phần tử cần tìm xuất hiện.

- **`return None`**: Nếu không tìm thấy cặp nào có tổng bằng `target`, hàm sẽ trả về `None`. Tuy nhiên, vì đề bài đảm bảo có một nghiệm duy nhất, dòng này ít khi được thực thi.

## Ví dụ minh họa
Với `nums = [3, 3]` và `target = 6`, ta có:

- **Bước 1**: `i = 0`, `num = 3`
  - `diff = target - num = 6 - 3 = 3`
  - `diff` chưa có trong `hash_map`, nên lưu `{3: 0}` vào `hash_map`.

- **Bước 2**: `i = 1`, `num = 3`
  - `diff = target - num = 6 - 3 = 3`
  - `diff` có trong `hash_map` với giá trị là `0`, nên trả về `[0, 1]`.

## Kết quả
Hàm sẽ trả về `[0, 1]`, là chỉ số của hai số `3` và `3` trong `nums` có tổng bằng `target`.
