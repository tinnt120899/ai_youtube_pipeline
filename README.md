# 🎬 AI YouTube Pipeline – Tạo video YouTube tự động bằng AI (Miễn phí & Mã nguồn mở)

Dự án này giúp bạn **tạo video YouTube hoàn chỉnh tự động** bằng công nghệ AI – từ viết kịch bản, tạo giọng đọc, sinh ảnh minh họa, đến dựng video hoàn thiện.  
Toàn bộ sử dụng **các công cụ miễn phí hoặc có gói dùng thử**, có thể chạy **ngay trên máy cá nhân**, không cần GPU mạnh.

---

## 🧠 Tính năng chính

✅ Sinh kịch bản tự động bằng AI (OpenAI / Gemini / Claude / v.v.)  
🎙️ Tạo giọng nói tự nhiên (ElevenLabs / gTTS / OpenVoice)  
🖼️ Sinh ảnh minh họa (Stable Diffusion / Leonardo / OpenAI Images)  
🎞️ Dựng video tự động bằng MoviePy  
💾 Xuất file MP4 sẵn sàng upload lên YouTube  

---

## 🗂️ Cấu trúc thư mục

```
ai_youtube_pipeline/
│
├── main.py                 # File chính chạy pipeline
├── src/
│   ├── script_generator.py # Sinh kịch bản AI
│   ├── tts_engine.py       # Sinh giọng nói
│   ├── image_maker.py      # Tạo ảnh minh họa
│   ├── video_maker.py      # Dựng video
│   └── utils.py            # Hàm tiện ích chung
├── requirements.txt
└── README.md
```

---

## ⚙️ Cài đặt

### 1️⃣ Clone project:
```bash
git clone https://github.com/tinnt120899/ai-youtube-pipeline.git
cd ai-youtube-pipeline
```

### 2️⃣ Tạo môi trường ảo:
```bash
python3 -m venv venv
source venv/bin/activate  # Trên macOS/Linux
# hoặc:
venv\Scripts\activate     # Trên Windows
```

### 3️⃣ Cài dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Cách chạy

Chạy pipeline chính:
```bash
python main.py
```

Hoặc test từng module riêng:
```bash
python -m src.script_generator
python -m src.tts_engine
python -m src.video_maker
```

---

## 💡 Demo (tùy chọn)

📺 [YouTube Demo](https://youtube.com/) *(đang cập nhật)*  
📸 ![Demo Screenshot](assets/demo.png)

---

## ❤️ Ủng hộ & Donate

Nếu bạn thấy dự án này hữu ích, hãy ủng hộ để Tín có thêm động lực phát triển nhé 🙏  

| Hình thức | Thông tin |
|------------|------------|
| ☕ **Buy Me a Coffee** | [https://www.buymeacoffee.com/tinnt120899](https://www.buymeacoffee.com/tinnt120899) *(tùy chọn)* |
| 💰 **MoMo** | `0983 987 605` |
| 🏦 **TPBank** | Số tài khoản: `26712888888` — Chủ tài khoản: **Nguyễn Trung Tín** |
| 📧 **Liên hệ** | [tinnt120899@gmail.com](mailto:tinnt120899@gmail.com) |
| 🐙 **GitHub** | [github.com/tinnt120899](https://github.com/tinnt120899) |

📱 *(Nếu có QR code MoMo hoặc TPBank, thêm vào thư mục `assets/` và chèn ảnh như sau:)*

```markdown
![Donate QR](assets/donate_qr.png)
```

---

## 🧑‍💻 Đóng góp

Pull requests luôn được chào đón!  
Nếu bạn muốn đóng góp, hãy:

1. Fork repo này.  
2. Tạo branch mới (`feature/your-feature`).  
3. Commit thay đổi.  
4. Gửi Pull Request.

---

## 📜 License

MIT License © 2025 [Nguyễn Trung Tín](https://github.com/tinnt120899)

---

## 🚀 Ghi chú thêm

- Dự án này hướng tới giúp người sáng tạo nội dung nhỏ có thể tự động hóa toàn bộ quy trình làm video YouTube mà không cần đầu tư lớn.  
- Mọi người có thể dùng, sửa, hoặc mở rộng pipeline để làm kênh riêng.  
- Nếu thấy hữu ích — hãy ⭐ **star repo này** trên GitHub để ủng hộ nhé!

---

## 💖 Donate

Nếu bạn thấy project hữu ích, hãy ủng hộ mình để phát triển thêm tính năng nhé!

- 📱 **Zalo:** 0983987605 — Nguyễn Trung Tín  
- 📱 **MoMo:** 0708687169 — Nguyễn Trung Tín  
- 🏦 **TPBank:** 26712888888 — Nguyễn Trung Tín  
- 📧 **Liên hệ:** [tinnt120899@gmail.com](mailto:tinnt120899@gmail.com)
