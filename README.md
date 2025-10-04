
# 🌿 MindEase – AI Mental Wellness Companion  
Your AI-powered friend for stress relief, mood tracking, and daily wellness tips — making mental health support accessible to everyone.


> 🚀 Built for HackSocial – Empowering Well-being Through Technology  

---

## 💡 Inspiration  
Mental health is one of the most pressing issues in today’s fast-paced world. Many people hesitate to seek help due to stigma, cost, or lack of access. We wanted to create a **friendly AI companion** that helps users track their moods, get instant support, and receive personalized wellness tips — right from their devices.  

---

## 🎯 What it does  
MindEase is an **AI-powered mental wellness chatbot** that allows users to:  
- 🧠 **Chat with AI** for emotional support.  
- 🌈 **Track their mood** daily through quick inputs.  
- 📊 **Get insights** on their emotional patterns.  
- ✨ **Receive personalized tips** for stress relief, motivation, and mindfulness.  

---

## 🛠️ How we built it  
- **Frontend:** React.js (simple chatbot UI + mood tracker form)  
- **Backend:** Flask / Node.js API  
- **AI Model:** Hugging Face (DistilBERT for sentiment analysis)  
- **Database (optional for MVP):** SQLite / Firebase for saving mood history  

---

## 🚀 Demo  
👉 [Add your demo link or screenshots here once ready]  

---

## 🧩 Challenges we ran into  
- Integrating **real-time AI responses** with the frontend.  
- Making the UI feel **friendly and supportive** instead of robotic.  
- Handling **sentiment analysis efficiently** with a lightweight model.  

---

## 🌟 Accomplishments we’re proud of  
- Built a **working AI chatbot prototype** within hours.  
- Designed a **clean and engaging user interface.**  
- Laid the foundation for a **scalable mental health companion app.**  

---

## 📚 What we learned  
- Hands-on experience with **NLP (sentiment analysis).**  
- Frontend-backend integration for real-time communication.  
- Importance of **designing with empathy** for mental wellness apps.  

---

## 🔮 What’s next  
- ✅ Add **voice interaction** for accessibility.  
- ✅ Integrate **mood history visualization (charts).**  
- ✅ Provide **daily personalized exercises** (breathing, journaling, affirmations).  
- ✅ Ensure **data privacy & security.**  

---

## 🛠️ Tech Stack  
- **Frontend:** React.js / HTML, CSS, JS  
- **Backend:** Flask / Node.js  
- **AI/NLP:** Hugging Face (Transformers - DistilBERT)  
- **Database:** SQLite / Firebase  

---

## 🤝 Team  
Built with ❤️ by haritha macharla for **HackSocial 2025**.  

---

## 🧭 Run locally (Windows - PowerShell)

Start the backend (Flask + transformers). From repository root:

```powershell
cd .\backend
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Start the frontend (Vite):

```powershell
cd .\frontend
npm install
npm run dev
```

By default the frontend runs on http://localhost:5173 and the backend on http://127.0.0.1:5000. The Chatbot component calls `/api/analyze` on the backend.

