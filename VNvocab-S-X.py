import re

def create_anki_cards(word_list):
    HANG_SO_01 = "s"
    HANG_SO_02 = "x"
    
    anki_cards = []
    
    for word in word_list:
        # Tìm vị trí của "ch" hoặc "tr" trong từ
        match = re.search(rf"({HANG_SO_01}|{HANG_SO_02})", word)
        
        if match:
            # Tạo câu hỏi
            question = f"{HANG_SO_01.capitalize()} hay {HANG_SO_02.upper()}?"
            
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
vietnamese_words = ["sản xuất",
"xổ số",
"sặc sỡ",
"xúc xắc",
"xem xét",
"xét nghiệm",
"soi mói"]

# Tạo danh sách câu hỏi Anki
anki_cards = create_anki_cards(vietnamese_words)

# Xuất danh sách câu hỏi Anki ra file
anki_file_path = "anki_cards.txt"
export_to_anki_file(anki_cards, anki_file_path)

print(f"Danh sách câu hỏi Anki đã được xuất ra file: {anki_file_path}")
