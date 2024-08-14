# Project IT3150

Đây là project lập trình của học phần đồ án Project I (IT3150) (kỳ 20223) dưới sự hướng dẫn của cô Nguyễn Thị Thu Hương, được thực hiện bởi cá nhân, đạt điểm 9.0/10. Project này yêu cầu lập trình xây dựng chương trình chuyển đổi giữa các biểu thức tiền tố (prefix expr), trung tố (infix expr) và hậu tố (postfix expr).

## Mô tả

**1. Biểu thức Trung tố (Infix Expression)**
   - Trong ký hiệu trung tố, toán tử được đặt giữa các toán hạng. Đây là ký hiệu mà ta vẫn sử dụng.
   - **Ví dụ:** biểu thức `3 + 4` (kết quả là `7`), `4 + 5 * 9` (kết quả là `49`).

**2. Biểu thức Tiền tố (Prefix Expression)**
   - Trong ký hiệu tiền tố, toán tử đứng trước toán hạng. Dạng này không cần dấu ngoặc để xác định thứ tự thực hiện phép toán, vì vị trí của toán tử đã quyết định điều đó.
   - **Ví dụ:** biểu thức trung tố `3 + 4` có dạng tiền tố `+ 3 4`, `4 + 5 * 9` có dạng tiền tố `+ 4 * 5 9`.

**3. Biểu thức Hậu tố (Postfix Expression)**
   - Trong ký hiệu hậu tố, toán tử đứng sau toán hạng. Giống như ký hiệu tiền tố, dạng này không cần dấu ngoặc để xác định thứ tự thực hiện phép toán.
   - **Ví dụ:** biểu thức trung tố `3 + 4` có dạng hậu tố `3 4 +`, `4 + 5 * 9` có dạng hậu tố `4 5 9 * +`.

Một số ưu điểm của việc sử dụng biểu thức hậu tố và tiền tố để thay thế biểu thức trung tố, có thể kể đến như sau:

* **Biểu thức tiền tố và hậu tố** không cần dấu ngoặc để chỉ định thứ tự các phép toán. Trong **biểu thức trung tố**, thứ tự thực hiện các phép toán có thể không rõ ràng nếu không có dấu ngoặc, đặc biệt là với các toán tử có độ ưu tiên khác nhau;
* **Biểu thức hậu tố** hiệu quả trong việc đánh giá dựa trên ngăn xếp (stack), vì vậy nó thường được sử dụng trong trình biên dịch và máy tính cầm tay. Mỗi toán tử trong một biểu thức hậu tố có thể được đánh giá ngay khi nó xuất hiện, sử dụng ngăn xếp để giữ các toán hạng.

## Nội dung lập trình
Chương trình cần thực hiện được những yêu cầu sau:
* Chuyển đổi giữa các biểu thức tiền tố, trung tố, hậu tố (chẳng hạn, chuyển từ `3 + 4` về `3 4 +` hoặc `+ 3 4` và ngược lại);
* Có khả năng phát hiện lỗi cú pháp ở bất cứ dạng biểu thức nào (chẳng hạn, `3 +` là một lỗi cú pháp với biểu thức trung tố);
* Tính giá trị của một biểu thức số học cho trước.

## Thuật toán
Cấu trúc ngăn xếp (stack) được sử dụng để chuyển đổi từ biểu thức **trung tố** sang **tiền tố, hậu tố** và sử dụng cây cú pháp trừu tượng **(AST)** để tìm lỗi cú pháp của biểu thức **trung tố**.

## Một số kết quả khi thực hiện

![image](https://github.com/user-attachments/assets/b7957ede-a47d-410a-bda3-cf785773f07c)

## Lỗi chương trình
Chương trình có thể cho kết quả không mong muốn trong một số trường hợp. Chẳng hạn trong chế độ chuyển đổi từ biểu thức **trung tố** sang **tiền tố - hậu tố**, biểu thức nhập vào có chứa khoảng trắng hoặc số có từ hai chữ số trở lên (Ở chế độ này nên nhập vào một biểu thức đại số (chẳng hạn `a+b` thay vì `1+2`) không chứa khoảng trắng (`a+b` thay vì `a + b`)).
