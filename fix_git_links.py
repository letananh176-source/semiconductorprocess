import os
import re
import urllib.parse

def fix_obsidian_links(directory):
    # Lặp qua tất cả file .md trong thư mục
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Hàm xử lý match: bắt tên file ảnh, encode khoảng trắng và gắn path
            def repl(match):
                img_name = match.group(1)
                safe_name = urllib.parse.quote(img_name)
                return f'![{img_name}](images/{safe_name})'
            
            # Thay thế toàn bộ ![[tên_ảnh]] thành ![tên_ảnh](images/tên_ảnh_đã_encode)
            new_content = re.sub(r'!\[\[(.*?)\]\]', repl, content)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
                
            print(f"Đã fix xong file: {filename}")

# Chạy script tại thư mục hiện tại
if __name__ == "__main__":
    fix_obsidian_links(".")
    print("Xong task, sếp check lại git nhé!")
