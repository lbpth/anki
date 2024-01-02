import re

def create_anki_cards(word_list):
    HANG_SO_01 = "ch"
    HANG_SO_02 = "tr"
    
    anki_cards = []
    
    for word in word_list:
        # Tìm vị trí của "ch" hoặc "tr" trong từ
        match = re.search(rf"({HANG_SO_01}|{HANG_SO_02})", word)
        
        if match:
            # Tạo câu hỏi
            #question = f"{HANG_SO_01.capitalize()} hay {HANG_SO_02.upper()}?"
            question = f"{HANG_SO_01.upper()} hay {HANG_SO_02.upper()}?"
            
            # Tạo từ với cloze deletion
            cloze_word = re.sub(rf"({HANG_SO_01}|{HANG_SO_02})", r"{{c1::\1}}", word)
            
            # Tạo câu trả lời
            answer = f"{cloze_word};"
            
            # Kết hợp câu hỏi và câu trả lời
            anki_card = f"{question} <br>{answer}"
            
            # Thêm vào danh sách các card Anki
            anki_cards.append(anki_card)
    
    return anki_cards

def export_to_anki_file(anki_cards, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for card in anki_cards:
            file.write(f"{card}\n")

# Danh sách từ tiếng Việt
vietnamese_words = ["tra tấn",
"tra cứu",
"tra khảo",
"cha mẹ",
"tra tay vào cùm",
"cha xứ",
"cha ông",
"ông cha",
"cha chung không ai khóc",
"tra tay vào cùm",
"tra cán cuốc",
"chà xát",
"ái chà",
"hoa trà mi",
"trà trộn",
"trà tam rượu tử",
"chả cá ",
"chả chìa ",
"chả bù ",
"chả hạn ",
"chả là ",
"chả mấy khi",
"trả nợ",
"trả tiền",
"trả lại",
"trả hàng",
"trả đũa",
"trả thù",
"trả lời",
"trả giá",
"trả miếng",
"ăn miếng trả miếng",
"nước mắt rơi lã chã",
"trã kho cá",
"dối trá",
"trá hình",
"chung chạ",
"lang chạ",
"chiếng chạ",
"ăn chung ở chạ",
"bán chác ",
"đồi chác",
"trác tuyệt",
"trác việt",
"điêu trác",
"trác táng",
"chạc buộc",
"chạc cây",
"chạc hươu nai",
"chững chạc",
"trạc tuổi đôi mươi ",
"anh ấy trạc tuổi tôi",
"trách mắng",
"trách cứ",
"trách móc",
"chê trách",
"khiển trách",
"trách nhiệm",
"tắc trách",]

# Tạo danh sách câu hỏi Anki
anki_cards = create_anki_cards(vietnamese_words)

# Xuất danh sách câu hỏi Anki ra file
anki_file_path = "anki_cards.txt"
export_to_anki_file(anki_cards, anki_file_path)

print(f"Danh sách câu hỏi Anki đã được xuất ra file: {anki_file_path}")
