# Tài liệu hướng dẫn Vision Assistant Pro

**Vision Assistant Pro** là một trợ lý AI đa phương thức, nâng cao dành cho NVDA. Nó tận dụng các mô hình Gemini của Google để cung cấp khả năng đọc màn hình thông minh, dịch thuật, đọc chính tả bằng giọng nói và phân tích tài liệu.

*Add-on này được phát hành cho cộng đồng nhằm tôn vinh Ngày Quốc tế Người khuyết tật.*

## 1. Thiết lập & Cấu hình

Đi tới **Menu NVDA > Tùy chọn > Cài đặt > Vision Assistant Pro**.

* **Khóa API (API Key):** Bắt buộc. Bạn có thể nhập nhiều khóa (phân tách bằng dấu phẩy hoặc xuống dòng). Trợ lý sẽ tự động luân phiên giữa các khóa nếu đạt đến giới hạn hạn ngạch.
* **Mô hình AI:** Chọn giữa các mô hình **Flash** (Nhanh nhất/Miễn phí), **Lite**, hoặc **Pro** (Trí thông minh cao).
* **URL Proxy:** Tùy chọn. Sử dụng thiết lập này nếu Google bị chặn ở khu vực của bạn. Đây phải là một địa chỉ web hoạt động như một cầu nối với Gemini API.
* **Công cụ OCR:** Chọn giữa **Chrome (Fast)** để có kết quả nhanh hoặc **Gemini (Formatted)** để giữ nguyên bố cục và nhận dạng bảng tốt hơn.
* **Giọng nói TTS:** Chọn kiểu giọng nói ưa thích để tạo tệp âm thanh từ các trang tài liệu.
* **Chuyển đổi thông minh (Smart Swap):** Tự động chuyển đổi ngôn ngữ nếu văn bản nguồn khớp với ngôn ngữ đích.
* **Đầu ra trực tiếp (Direct Output):** Bỏ qua cửa sổ trò chuyện và đọc thẳng phản hồi của AI qua giọng nói. **Lưu ý:** Ngay cả trong chế độ này, bạn có thể nhấn **Space** trong lớp lệnh để mở lại kết quả cuối cùng trong một hộp thoại trò chuyện.
* **Tích hợp Clipboard:** Tự động sao chép phản hồi của AI vào clipboard.

## 2. Lớp lệnh & Phím tắt

Để ngăn ngừa xung đột bàn phím, add-on này sử dụng một **Lớp lệnh (Command Layer)**.

1. Nhấn **NVDA + Shift + V** (Phím chính) để kích hoạt lớp lệnh (bạn sẽ nghe thấy tiếng bíp).
2. Nhả các phím, sau đó nhấn một trong các phím đơn sau:

| Phím | Chức năng | Mô tả |
| --- | --- | --- |
| **T** | Dịch thông minh | Dịch văn bản dưới con trỏ navigator hoặc vùng đang chọn. |
| **Shift + T** | Dịch Clipboard | Dịch nội dung hiện có trong clipboard. |
| **R** | Tinh chỉnh văn bản | Tóm tắt, Sửa ngữ pháp, Giải thích hoặc chạy các **Prompt tùy chỉnh**. |
| **V** | Thị giác đối tượng | Mô tả đối tượng navigator hiện tại. |
| **O** | Thị giác toàn màn hình | Phân tích toàn bộ bố cục và nội dung màn hình. |
| **Shift + V** | Phân tích Video trực tuyến | Phân tích video trên **YouTube**, **Instagram**, **TikTok**, hoặc **Twitter (X)**. |
| **D** | Trình đọc tài liệu | Trình đọc nâng cao cho PDF và hình ảnh với tùy chọn chọn phạm vi trang. |
| **F** | OCR Tệp | Nhận dạng văn bản trực tiếp từ các tệp hình ảnh, PDF hoặc TIFF được chọn. |
| **A** | Chuyển biên âm thanh | Chuyển biên các tệp MP3, WAV hoặc OGG thành văn bản. |
| **C** | Giải CAPTCHA | Chụp và giải mã CAPTCHA trên màn hình hoặc đối tượng navigator. |
| **S** | Đọc chính tả thông minh | Chuyển đổi giọng nói thành văn bản. Nhấn để bắt đầu ghi âm, nhấn lần nữa để dừng/gõ văn bản. |
| **L** | Thông báo trạng thái | Thông báo tiến trình hiện tại (ví dụ: "Đang quét...", "Nhàn rỗi"). |
| **U** | Kiểm tra cập nhật | Kiểm tra thủ công trên GitHub để tìm phiên bản mới nhất của add-on. |
| **Space** | Gọi lại kết quả cuối | Hiển thị phản hồi cuối cùng của AI trong hộp thoại trò chuyện để xem lại hoặc hỏi tiếp. |
| **H** | Trợ giúp lệnh | Hiển thị danh sách tất cả các phím tắt có sẵn trong lớp lệnh. |

### 2.1 Phím tắt Trình đọc tài liệu (Bên trong Trình xem)

Khi một tài liệu được mở qua lệnh **D**:

* **Ctrl + PageDown:** Chuyển đến trang tiếp theo (thông báo số trang).
* **Ctrl + PageUp:** Chuyển đến trang trước đó (thông báo số trang).
* **Alt + A:** Mở hộp thoại trò chuyện để đặt câu hỏi về tài liệu.
* **Alt + R:** Buộc quét lại trang hiện tại hoặc tất cả các trang bằng công cụ Gemini.
* **Alt + G:** Tạo và lưu tệp âm thanh chất lượng cao (WAV) từ nội dung.
* **Alt + S / Ctrl + S:** Lưu văn bản được trích xuất dưới dạng tệp TXT hoặc HTML.

## 3. Prompt tùy chỉnh & Biến

Mở **Cài đặt > Prompts > Manage Prompts...** để cấu hình các prompt hệ thống và tùy chỉnh.

* **Thẻ Default Prompts:** chỉnh sửa các prompt có sẵn. Bạn có thể đặt lại một prompt duy nhất hoặc đặt lại tất cả về mặc định.
* **Thẻ Custom Prompts:** thêm, sửa, xóa và sắp xếp lại các prompt tùy chỉnh.
* **Nút Variables Guide:** mở cửa sổ trợ giúp với tất cả các biến và loại đầu vào được hỗ trợ.

### Các biến có sẵn

| Biến | Mô tả | Loại đầu vào |
| --- | --- | --- |
| `[selection]` | Văn bản hiện đang được chọn | Text |
| `[clipboard]` | Nội dung clipboard | Text |
| `[screen_obj]` | Ảnh chụp màn hình của đối tượng navigator | Image |
| `[screen_full]` | Ảnh chụp toàn bộ màn hình | Image |
| `[file_ocr]` | Chọn tệp hình ảnh/PDF để trích xuất văn bản | Image, PDF, TIFF |
| `[file_read]` | Chọn tài liệu để đọc | TXT, Code, PDF |
| `[file_audio]` | Chọn tệp âm thanh để phân tích | MP3, WAV, OGG |

### Ví dụ về Prompt tùy chỉnh

* **OCR Nhanh:** `My OCR:[file_ocr]`
* **Dịch hình ảnh:** `Translate Img:Extract text from this image and translate to English. [file_ocr]`
* **Phân tích âm thanh:** `Summarize Audio:Listen to this recording and summarize the main points. [file_audio]`
* **Tìm lỗi mã nguồn (Code Debugger):** `Debug:Find bugs in this code and explain them: [selection]`

---

**Lưu ý:** Cần có kết nối internet đang hoạt động cho tất cả các tính năng AI. Tài liệu nhiều trang và tệp TIFF được xử lý tự động.

## 4. Hỗ trợ & Cộng đồng

Cập nhật những tin tức, tính năng và bản phát hành mới nhất:

* **Kênh Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
* **GitHub Issues:** Dành cho báo cáo lỗi và yêu cầu tính năng.

## Những thay đổi trong phiên bản 4.6

* **Gọi lại kết quả tương tác:** Đã thêm phím **Space** vào lớp lệnh, cho phép người dùng mở lại ngay lập tức phản hồi cuối cùng của AI trong cửa sổ trò chuyện để đặt câu hỏi tiếp theo, ngay cả khi chế độ "Direct Output" đang hoạt động.
* **Cộng đồng Telegram:** Đã thêm liên kết "Official Telegram Channel" vào menu Tools của NVDA, cung cấp một cách nhanh chóng để cập nhật những tin tức, tính năng và bản phát hành mới nhất.
* **Tăng cường độ ổn định của phản hồi:** Tối ưu hóa logic cốt lõi cho các tính năng Dịch thuật, OCR và Thị giác để đảm bảo hiệu suất đáng tin cậy hơn và trải nghiệm mượt mà hơn khi sử dụng đầu ra giọng nói trực tiếp.
* **Cải thiện hướng dẫn giao diện:** Đã cập nhật các mô tả cài đặt và tài liệu hướng dẫn để giải thích rõ hơn về hệ thống gọi lại mới và cách thức hoạt động của nó cùng với các cài đặt đầu ra trực tiếp.

## Những thay đổi trong phiên bản 4.5

* **Trình quản lý Prompt nâng cao:** Giới thiệu một hộp thoại quản lý chuyên dụng trong cài đặt để tùy chỉnh các prompt hệ thống mặc định và quản lý các prompt do người dùng xác định với hỗ trợ đầy đủ cho việc thêm, sửa, sắp xếp lại và xem trước.
* **Hỗ trợ Proxy toàn diện:** Đã giải quyết các sự cố kết nối mạng bằng cách đảm bảo rằng các cài đặt proxy do người dùng định cấu hình được áp dụng nghiêm ngặt cho tất cả các yêu cầu API, bao gồm dịch thuật, OCR và tạo giọng nói.
* **Di chuyển dữ liệu tự động:** Tích hợp hệ thống di chuyển thông minh để tự động nâng cấp các cấu hình prompt cũ sang định dạng v2 JSON mạnh mẽ trong lần chạy đầu tiên mà không làm mất dữ liệu.
* **Cập nhật khả năng tương thích (2025.1):** Đặt phiên bản NVDA yêu cầu tối thiểu thành 2025.1 do sự phụ thuộc thư viện trong các tính năng nâng cao như Trình đọc tài liệu để đảm bảo hiệu suất ổn định.
* **Tối ưu hóa giao diện cài đặt:** Sắp xếp hợp lý giao diện cài đặt bằng cách tổ chức lại việc quản lý prompt thành một hộp thoại riêng biệt, mang lại trải nghiệm người dùng rõ ràng và dễ tiếp cận hơn.
* **Hướng dẫn về biến Prompt:** Đã thêm hướng dẫn tích hợp trong các hộp thoại prompt để giúp người dùng dễ dàng xác định và sử dụng các biến động như `[selection]`, `[clipboard]`, và `[screen_obj]`.

## Những thay đổi trong phiên bản 4.0.3

* **Tăng cường độ ổn định mạng:** Đã thêm cơ chế thử lại tự động để xử lý tốt hơn các kết nối internet không ổn định và lỗi máy chủ tạm thời, đảm bảo phản hồi AI đáng tin cậy hơn.
* **Hộp thoại dịch trực quan:** Giới thiệu một cửa sổ dành riêng cho kết quả dịch. Người dùng giờ đây có thể dễ dàng điều hướng và đọc các bản dịch dài theo từng dòng, tương tự như kết quả OCR.
* **Chế độ xem định dạng tổng hợp:** Tính năng "View Formatted" trong Trình đọc tài liệu hiện hiển thị tất cả các trang đã xử lý trong một cửa sổ duy nhất, được tổ chức với các tiêu đề trang rõ ràng.
* **Tối ưu hóa quy trình OCR:** Tự động bỏ qua việc chọn phạm vi trang đối với các tài liệu chỉ có một trang, giúp quá trình nhận dạng diễn ra nhanh chóng và liền mạch hơn.
* **Cải thiện độ ổn định API:** Chuyển sang phương thức xác thực dựa trên header mạnh mẽ hơn, giải quyết các lỗi "All API Keys failed" tiềm ẩn do xung đột khi luân phiên khóa.
* **Sửa lỗi:** Đã giải quyết một số sự cố treo có thể xảy ra, bao gồm sự cố trong quá trình tắt add-on và lỗi tiêu điểm trong hộp thoại trò chuyện.

## Những thay đổi trong phiên bản 4.0.1

* **Trình đọc tài liệu nâng cao:** Một trình xem mới, mạnh mẽ dành cho PDF và hình ảnh với khả năng chọn phạm vi trang, xử lý nền và điều hướng liền mạch bằng `Ctrl+PageUp/Down`.
* **Menu con Tools mới:** Đã thêm một menu con "Vision Assistant" chuyên dụng bên dưới menu Tools của NVDA để truy cập nhanh hơn vào các tính năng cốt lõi, cài đặt và tài liệu hướng dẫn.
* **Tùy chỉnh linh hoạt:** Giờ đây, bạn có thể chọn công cụ OCR và giọng nói TTS ưa thích trực tiếp từ bảng cài đặt.
* **Hỗ trợ nhiều khóa API:** Đã thêm hỗ trợ cho nhiều khóa API Gemini. Bạn có thể nhập một khóa trên mỗi dòng hoặc phân tách chúng bằng dấu phẩy trong cài đặt.
* **Công cụ OCR thay thế:** Giới thiệu một công cụ OCR mới để đảm bảo nhận dạng văn bản đáng tin cậy ngay cả khi đạt đến giới hạn hạn ngạch của Gemini API.
* **Luân phiên Khóa API thông minh:** Tự động chuyển sang và ghi nhớ khóa API hoạt động nhanh nhất để vượt qua giới hạn hạn ngạch.
* **Tài liệu sang MP3/WAV:** Tích hợp khả năng tạo và lưu các tệp âm thanh chất lượng cao ở cả định dạng MP3 (128kbps) và WAV trực tiếp trong trình đọc.
* **Hỗ trợ Instagram Stories:** Đã thêm khả năng mô tả và phân tích Instagram Stories bằng URL của chúng.
* **Hỗ trợ TikTok:** Giới thiệu hỗ trợ cho các video TikTok, cho phép mô tả hình ảnh đầy đủ và chuyển biên âm thanh của các đoạn clip.
* **Hộp thoại cập nhật được thiết kế lại:** Cung cấp một giao diện mới, dễ tiếp cận với hộp văn bản có thể cuộn để đọc rõ các thay đổi của phiên bản trước khi cài đặt.
* **Trạng thái & UX thống nhất:** Chuẩn hóa các hộp thoại tệp trên toàn bộ add-on và cải tiến lệnh 'L' để báo cáo tiến trình theo thời gian thực.

## Những thay đổi trong phiên bản 3.6.0

* **Hệ thống trợ giúp:** Đã thêm lệnh trợ giúp (`H`) trong Lớp lệnh để cung cấp một danh sách dễ truy cập gồm tất cả các phím tắt và chức năng của chúng.
* **Phân tích Video trực tuyến:** Mở rộng hỗ trợ để bao gồm các video trên **Twitter (X)**. Đồng thời cải thiện khả năng phát hiện URL và độ ổn định để có trải nghiệm đáng tin cậy hơn.
* **Đóng góp cho dự án:** Đã thêm hộp thoại quyên góp tùy chọn cho những người dùng muốn ủng hộ các bản cập nhật trong tương lai và sự phát triển liên tục của dự án.

## Những thay đổi trong phiên bản 3.5.0

* **Lớp lệnh:** Giới thiệu hệ thống Lớp lệnh (mặc định: `NVDA+Shift+V`) để nhóm các phím tắt dưới một phím chính duy nhất. Ví dụ: thay vì nhấn `NVDA+Control+Shift+T` để dịch, giờ đây bạn nhấn `NVDA+Shift+V` theo sau là `T`.
* **Phân tích Video trực tuyến:** Đã thêm tính năng mới để phân tích trực tiếp các video trên YouTube và Instagram bằng cách cung cấp URL.

## Những thay đổi trong phiên bản 3.1.0

* **Chế độ Đầu ra trực tiếp:** Đã thêm tùy chọn để bỏ qua hộp thoại trò chuyện và nghe thẳng các phản hồi của AI qua giọng nói để có trải nghiệm nhanh chóng và liền mạch hơn.
* **Tích hợp Clipboard:** Đã thêm một cài đặt mới để tự động sao chép các phản hồi của AI vào clipboard.

## Những thay đổi trong phiên bản 3.0

* **Ngôn ngữ mới:** Đã thêm bản dịch tiếng **Ba Tư** và tiếng **Việt**.
* **Mở rộng mô hình AI:** Tổ chức lại danh sách chọn mô hình với các tiền tố rõ ràng (`[Free]`, `[Pro]`, `[Auto]`) để giúp người dùng phân biệt giữa các mô hình miễn phí và giới hạn tốc độ (trả phí). Đã thêm hỗ trợ cho **Gemini 3.0 Pro** và **Gemini 2.0 Flash Lite**.
* **Độ ổn định khi Đọc chính tả:** Cải thiện đáng kể độ ổn định của tính năng Đọc chính tả thông minh. Đã thêm kiểm tra an toàn để bỏ qua các đoạn âm thanh ngắn hơn 1 giây, ngăn chặn hiện tượng AI "ảo giác" và các lỗi trống.
* **Xử lý tệp:** Đã sửa lỗi tải lên các tệp có tên không phải tiếng Anh bị thất bại.
* **Tối ưu hóa Prompt:** Cải thiện logic Dịch thuật và cấu trúc lại kết quả của Thị giác.

## Những thay đổi trong phiên bản 2.9

* **Đã thêm bản dịch tiếng Pháp và tiếng Thổ Nhĩ Kỳ.**
* **Chế độ xem định dạng:** Đã thêm nút "View Formatted" trong các hộp thoại trò chuyện để xem cuộc hội thoại với định dạng chuẩn (Tiêu đề, In đậm, Code) trong một cửa sổ có thể duyệt qua tiêu chuẩn.
* **Cài đặt Markdown:** Đã thêm tùy chọn mới "Clean Markdown in Chat" trong phần Cài đặt. Bỏ chọn tùy chọn này cho phép người dùng xem cú pháp Markdown gốc (ví dụ: `**`, `#`) trong cửa sổ trò chuyện.
* **Quản lý hộp thoại:** Đã sửa sự cố trong đó cửa sổ "Refine Text" hoặc cửa sổ trò chuyện sẽ mở nhiều lần hoặc không lấy được tiêu điểm chính xác.
* **Cải tiến UX:** Chuẩn hóa các tiêu đề hộp thoại tệp thành "Open" và loại bỏ các thông báo giọng nói dư thừa (ví dụ: "Opening menu...") để có trải nghiệm mượt mà hơn.

## Những thay đổi trong phiên bản 2.8

* Đã thêm bản dịch tiếng Ý.
* **Thông báo trạng thái:** Đã thêm một lệnh mới (NVDA+Control+Shift+I) để thông báo trạng thái hiện tại của add-on (ví dụ: "Uploading...", "Analyzing...").
* **Xuất HTML:** Nút "Save Content" trong các hộp thoại kết quả hiện lưu đầu ra dưới dạng tệp HTML được định dạng, giữ nguyên các kiểu như tiêu đề và chữ in đậm.
* **Giao diện Cài đặt:** Cải thiện bố cục bảng Cài đặt với các nhóm dễ tiếp cận hơn.
* **Các mô hình mới:** Đã thêm hỗ trợ cho gemini-flash-latest và gemini-flash-lite-latest.
* **Ngôn ngữ:** Đã thêm tiếng Nepal vào các ngôn ngữ được hỗ trợ.
* **Logic menu Refine:** Đã sửa một lỗi nghiêm trọng khiến các lệnh "Refine Text" bị lỗi nếu ngôn ngữ giao diện NVDA không phải là tiếng Anh.
* **Đọc chính tả:** Cải thiện tính năng phát hiện khoảng lặng để ngăn chặn đầu ra văn bản không chính xác khi không có giọng nói được nhập vào.
* **Cài đặt cập nhật:** Tính năng "Check for updates on startup" hiện bị tắt theo mặc định để tuân thủ các chính sách của Add-on Store.
* Dọn dẹp mã nguồn.

## Những thay đổi trong phiên bản 2.7

* Chuyển đổi cấu trúc dự án sang Mẫu Add-on chính thức của NV Access để tuân thủ các tiêu chuẩn tốt hơn.
* Đã triển khai logic thử lại tự động cho các lỗi HTTP 429 (Rate Limit) để đảm bảo độ tin cậy trong thời gian lưu lượng truy cập cao.
* Tối ưu hóa các prompt dịch thuật để có độ chính xác cao hơn và xử lý logic "Smart Swap" tốt hơn.
* Đã cập nhật bản dịch tiếng Nga.

## Những thay đổi trong phiên bản 2.6

* Đã thêm hỗ trợ bản dịch tiếng Nga (Cảm ơn nvda-ru).
* Cập nhật các thông báo lỗi để cung cấp phản hồi mang tính mô tả cao hơn về vấn đề kết nối.
* Thay đổi ngôn ngữ đích mặc định thành tiếng Anh.

## Những thay đổi trong phiên bản 2.5

* Đã thêm lệnh Native File OCR (NVDA+Control+Shift+F).
* Đã thêm nút "Save Chat" vào các hộp thoại kết quả.
* Đã triển khai hỗ trợ bản địa hóa đầy đủ (i18n).
* Đã chuyển các phản hồi âm thanh sang mô-đun tones gốc của NVDA.
* Chuyển sang sử dụng Gemini File API để xử lý tốt hơn các tệp PDF và âm thanh.
* Đã sửa lỗi treo khi dịch văn bản có chứa dấu ngoặc nhọn.

## Những thay đổi trong phiên bản 2.1.1

* Đã sửa sự cố trong đó biến `[file_ocr]` không hoạt động bình thường trong Custom Prompts.

## Những thay đổi trong phiên bản 2.1

* Chuẩn hóa tất cả các phím tắt để sử dụng NVDA+Control+Shift nhằm loại bỏ xung đột với bố cục Bàn phím Laptop của NVDA và các phím nóng hệ thống.

## Những thay đổi trong phiên bản 2.0

* Đã triển khai hệ thống Tự động cập nhật tích hợp sẵn.
* Đã thêm Bộ nhớ đệm Dịch thông minh để truy xuất tức thì các văn bản đã dịch trước đó.
* Đã thêm Bộ nhớ hội thoại để tinh chỉnh kết quả theo ngữ cảnh trong các hộp thoại trò chuyện.
* Đã thêm Lệnh dịch Clipboard chuyên dụng (NVDA+Control+Shift+Y).
* Tối ưu hóa các prompt AI để thực thi nghiêm ngặt đầu ra ngôn ngữ đích.
* Đã sửa lỗi treo do các ký tự đặc biệt trong văn bản đầu vào.

## Những thay đổi trong phiên bản 1.5

* Đã thêm hỗ trợ cho hơn 20 ngôn ngữ mới.
* Đã triển khai Hộp thoại Tinh chỉnh Tương tác cho các câu hỏi tiếp theo.
* Đã thêm tính năng Đọc chính tả thông minh gốc.
* Đã thêm danh mục "Vision Assistant" vào hộp thoại Input Gestures của NVDA.
* Đã sửa các lỗi treo COMError trong một số ứng dụng cụ thể như Firefox và Word.
* Đã thêm cơ chế tự động thử lại đối với các lỗi máy chủ.

## Những thay đổi trong phiên bản 1.0

* Phát hành lần đầu.
