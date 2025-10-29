# 🎬 AI YouTube Pipeline – Fully Automated YouTube Video Creation with AI (Free & Open Source)

This project helps you **automatically generate complete YouTube videos** using AI — from scriptwriting, voice generation, image creation, to final video rendering.  
Everything runs **for free or with trial tools**, and works **locally on your computer** (no need for a powerful GPU).

---

## 🧠 Main Features

✅ Auto-generate video scripts using AI (OpenAI / Gemini / Claude / etc.)  
🎙️ Generate natural human-like voiceovers (ElevenLabs / gTTS / OpenVoice)  
🖼️ Create illustration images (Stable Diffusion / Leonardo / OpenAI Images)  
🎞️ Automatically edit and render videos with MoviePy  
💾 Export final MP4 files ready to upload to YouTube  

---

## 🗂️ Project Structure

```
ai_youtube_pipeline/
│
├── main.py                 # Main pipeline entry point
├── src/
│   ├── script_generator.py # AI script generator
│   ├── tts_engine.py       # Text-to-speech engine
│   ├── image_maker.py      # Image generation module
│   ├── video_maker.py      # Video editing module
│   └── utils.py            # Common helper utilities
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/tinnt120899/ai-youtube-pipeline.git
cd ai-youtube-pipeline
```

### 2️⃣ Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # on macOS/Linux
# or:
venv\Scripts\activate     # on Windows
```

### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

To run the full pipeline:
```bash
python main.py
```

Or test individual modules:
```bash
python -m src.script_generator
python -m src.tts_engine
python -m src.video_maker
```

---

## 💡 Demo (optional)

📺 [YouTube Demo](https://youtube.com/) *(coming soon)*  
📸 ![Demo Screenshot](assets/demo.png)

---

## ❤️ Support & Donate

If you find this project helpful, please consider supporting me so I can continue improving it 🙏  

| Method | Details |
|---------|----------|
| ☕ **Buy Me a Coffee** | [https://www.buymeacoffee.com/tinnt120899](https://www.buymeacoffee.com/tinnt120899) *(optional)* |
| 💰 **MoMo** | `0983 987 605` |
| 🏦 **TPBank** | Account No: `26712888888` — **Nguyễn Trung Tín** |
| 📧 **Email** | [tinnt120899@gmail.com](mailto:tinnt120899@gmail.com) |
| 🐙 **GitHub** | [github.com/tinnt120899](https://github.com/tinnt120899) |

📱 *(If you have a MoMo or TPBank QR code, add it to the `assets/` folder and include it like this:)*

```markdown
![Donate QR](assets/donate_qr.png)
```

---

## 🧑‍💻 Contributing

Pull requests are always welcome!  
To contribute:

1. Fork this repository  
2. Create a new branch (`feature/your-feature`)  
3. Commit your changes  
4. Submit a Pull Request

---

## 📜 License

MIT License © 2025 [Nguyễn Trung Tín](https://github.com/tinnt120899)

---

## 🚀 Notes

- This project aims to help small creators automate YouTube video production without heavy investment.  
- You’re free to modify, extend, or integrate this pipeline into your own projects.  
- If you like this, please ⭐ **star the repo** on GitHub — it really helps!

---

## 💖 Donate

If you’d like to support my work, you can donate via:

- 📱 **Zalo:** 0983987605 — Nguyễn Trung Tín  
- 📱 **MoMo:** 0708687169 — Nguyễn Trung Tín  
- 🏦 **TPBank:** 26712888888 — Nguyễn Trung Tín  
- 📧 **Email:** [tinnt120899@gmail.com](mailto:tinnt120899@gmail.com)
