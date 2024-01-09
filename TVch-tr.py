# Tạo một danh sách các từ tiếng Việt có 2 âm tiết có chứa "ch" hoặc "tr"
danh_sach_tu = ["tranh chấp", "chim muông", "trường giang", "chó cắn", "tròn vo", "chân dài", "trời mưa", "chè bưởi", "trái tim", "chảy máu"]

# Tạo một hàm để tạo một câu hỏi với cấu trúc cloze deletion
def tao_cau_hoi(tu):
  # Tìm vị trí của "ch" hoặc "tr" trong từ
  vi_tri = tu.find("ch") if "ch" in tu else tu.find("tr")
  # Tạo một chuỗi chứa câu hỏi với cấu trúc cloze deletion
  # Ví dụ: CH hay TR<br>{{c1::tr}}anh chấp
  cau_hoi = "CH hay TR<br>{{c1::" + tu[vi_tri:vi_tri+2] + "}}" + tu[vi_tri+2:]
  # Tạo một chuỗi chứa phần input để nhập đáp án
  # Ví dụ: Type: tranh chấp
  input = "Type: " + tu
  # Trả về câu hỏi và phần input
  return cau_hoi, input

# Tạo một hàm để tạo một danh sách n câu hỏi
def tao_danh_sach_cau_hoi(n):
  # Tạo một danh sách rỗng để lưu các câu hỏi
  danh_sach_cau_hoi = []
  # Lặp n lần
  for i in range(n):
    # Chọn ngẫu nhiên một từ trong danh sách từ
    tu = random.choice(danh_sach_tu)
    # Tạo một câu hỏi và phần input bằng hàm tao_cau_hoi
    cau_hoi, input = tao_cau_hoi(tu)
    # Thêm câu hỏi và phần input vào danh sách
    danh_sach_cau_hoi.append((cau_hoi, input))
  # Trả về danh sách câu hỏi
  return danh_sach_cau_hoi

# Tạo một hàm để ghi một danh sách câu hỏi vào một file .txt
def ghi_file(danh_sach_cau_hoi, ten_file):
  # Mở file .txt với chế độ ghi
  file = open(ten_file, "w")
  # Lặp qua các câu hỏi trong danh sách
  for cau_hoi, input in danh_sach_cau_hoi:
    # Ghi câu hỏi và phần input vào file, kèm theo dấu tab và dòng mới
    file.write(cau_hoi + "\t" + input + "\n")
  # Đóng file
  file.close()

# Sử dụng các hàm đã tạo để tạo và ghi một danh sách 10 câu hỏi vào file on_tap_tieng_viet.txt
danh_sach_cau_hoi = tao_danh_sach_cau_hoi(10)
ghi_file(danh_sach_cau_hoi, "on_tap_tieng_viet.txt")
