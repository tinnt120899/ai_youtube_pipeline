#!/usr/bin/env bash
# ==============================================
# AI YouTube Pipeline - Auto Environment Setup
# ==============================================
# Compatible: macOS / Linux
# Author: ChatGPT (GPT-5)
# ==============================================

echo "🚀 Bắt đầu setup môi trường AI YouTube Pipeline..."

# --- B1: Xác định Python ---
if command -v python3.11 &> /dev/null; then
  PYTHON=python3.11
elif command -v python3.10 &> /dev/null; then
  PYTHON=python3.10
elif command -v python3.9 &> /dev/null; then
  PYTHON=python3.9
else
  echo "❌ Không tìm thấy Python 3.9+ (>=3.9). Cài đặt Python trước!"
  exit 1
fi

echo "✅ Dùng Python: $($PYTHON --version)"

# --- B2: Tạo venv ---
if [ -d "venv" ]; then
  echo "⚠️  Đã có môi trường ảo (venv), bỏ qua tạo mới."
else
  echo "🧩 Tạo môi trường ảo..."
  $PYTHON -m venv venv
fi

# --- B3: Kích hoạt venv ---
source venv/bin/activate
echo "✅ Đã kích hoạt môi trường ảo."

# --- B4: Cập nhật pip ---
echo "📦 Cập nhật pip..."
pip install --upgrade pip setuptools wheel > /dev/null

# --- B5: Ghi requirements.txt nếu chưa có ---
REQ=requirements.txt
if [ ! -f "$REQ" ]; then
  echo "🧾 Tạo file requirements.txt mặc định..."
  cat << 'EOF' > requirements.txt
openai>=1.44.0
python-dotenv>=1.0.1
requests>=2.32.3
elevenlabs>=1.3.0
moviepy==2.0.0
imageio[ffmpeg]>=2.37.0
pillow>=10.2.0,<11.0
numpy>=2.0.0
decorator>=5.2.1
proglog>=0.1.12
google-auth>=2.34.0
google-auth-oauthlib>=1.2.1
google-api-python-client>=2.151.0
tqdm>=4.66.5
colorama>=0.4.6
urllib3==1.26.20
importlib_metadata==6.8.0
EOF
fi

# --- B6: Cài package ---
echo "📥 Cài đặt dependencies..."
pip install -r requirements.txt

# --- B7: Kiểm tra ---
echo "🧠 Kiểm tra thư viện chính..."
python - << 'PYCODE'
try:
    import moviepy, openai, googleapiclient, elevenlabs
    print("✅ Tất cả thư viện đã sẵn sàng!")
except Exception as e:
    print(f"❌ Có lỗi khi import: {e}")
PYCODE

echo "🎉 Setup hoàn tất! Bắt đầu với:"
echo "👉 source venv/bin/activate"
echo "👉 python main.py --help"
