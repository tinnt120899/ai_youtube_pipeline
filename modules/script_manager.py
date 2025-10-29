import sys
from pathlib import Path
from logger import log
from config import SCRIPTS_DIR

def select_script():
    files = list(SCRIPTS_DIR.glob("*.txt"))
    if not files:
        log(f"⚠️ Không tìm thấy file .txt trong {SCRIPTS_DIR}/")
        sys.exit(1)
    print("\n📝 Danh sách script:")
    for i, f in enumerate(files):
        print(f"  [{i+1}] {f.name}")

    while True:
        try:
            choice = int(input("\n👉 Chọn số file: ")) - 1
            if 0 <= choice < len(files):
                selected = files[choice]
                log(f"✅ [SCRIPT] Chọn: {selected.name}")
                return selected
        except ValueError:
            print("⚠️ Nhập số hợp lệ.")

def read_script_from_file(filepath: Path):
    text = filepath.read_text(encoding="utf-8").strip()
    log(f"✅ [SCRIPT] Đọc từ: {filepath}")
    return text
