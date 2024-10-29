## Giải thích từng bước

### Bước 1: Khởi tạo nút giả (`dummy`)
- Để tạo đầu danh sách liên kết đã hợp nhất, ta sử dụng một **nút giả** (`dummy`). Điều này giúp việc quản lý danh sách dễ dàng hơn và tránh các kiểm tra đặc biệt.
- `dummy` sẽ là đầu của danh sách liên kết mới, nhưng sẽ **bỏ qua** nó khi trả về kết quả.

### Bước 2: Khởi tạo con trỏ `current`
- `current` là con trỏ sẽ di chuyển qua từng nút của danh sách đã hợp nhất, bắt đầu từ `dummy`.

### Bước 3: Duyệt qua cả hai danh sách (`while list1 and list2`)
- Trong khi cả `list1` và `list2` còn phần tử, chúng ta sẽ duyệt qua từng nút trong hai danh sách.
- **So sánh giá trị** của các nút ở `list1` và `list2`:
  - Nếu `list1.val < list2.val`: Gán `list1` cho `current.next`, sau đó di chuyển con trỏ `list1` sang nút tiếp theo (`list1 = list1.next`).
  - Ngược lại, gán `list2` cho `current.next` và di chuyển con trỏ `list2`.
- Cập nhật `current` trỏ tới nút tiếp theo (`current = current.next`) để tiếp tục xây dựng danh sách đã hợp nhất.

### Bước 4: Xử lý các nút còn lại
- Sau khi thoát khỏi vòng `while`, có thể còn lại các nút trong `list1` hoặc `list2`. Ta chỉ cần gắn chúng vào cuối của danh sách đã hợp nhất:
  - Nếu `list1` còn phần tử, gán `current.next = list1`.
  - Nếu `list2` còn phần tử, gán `current.next = list2`.

### Bước 5: Trả về danh sách đã hợp nhất
- Trả về `dummy.next`, đây là đầu của danh sách đã hợp nhất (bỏ qua nút `dummy`).
