# ⚡ FeedFlash: Scheduled News Summarizer

## 📌 Summary

**FeedFlash** is a scheduled news summarization system that pulls 60 English-language news articles daily and generates concise ~60-word summaries using a fine-tuned transformer model. The summaries are displayed through a Gradio UI that updates throughout the day and resets every night at 2:00 AM to minimize storage and stay free-tier compatible.

Built for students, readers, and anyone who wants to scan the day’s news quickly without losing key information.

---

## ✅ What It Does

- Pulls live headlines from **NewsAPI** (free tier)
- Extracts full article text using `newspaper3k`
- Uses a **fine-tuned transformer model** (based on `bart-base`)
- Summarizes articles into ~60-word abstracts
- Displays title, summary, and link in a clean **Gradio** interface
- Logs user feedback (👍/👎) and purges data daily to save memory

---

## ⚙️ How It’s Built

### 🧠 Model
- Base: `facebook/bart-base`
- Fine-tuned on news-style data (e.g. CNN/DailyMail)
- Hosted on Hugging Face Hub under contributor’s ID

### 📅 Scheduled Runs
- Summarizes **15 articles every 4 hours**
  - 8 AM, 2 PM, 6 PM, 10 PM (IST)
- Purges all summaries and feedback logs daily at **2:00 AM**

### 🧰 Tech Stack

| Component       | Tool/Library               |
|----------------|-----------------------------|
| Data Fetching   | `NewsAPI`, `newspaper3k`    |
| Summarization   | Hugging Face Transformers (`bart-base`) |
| Scheduling      | `apscheduler`               |
| UI              | `Gradio`                    |
| Hosting         | Hugging Face Spaces (CPU)   |
| Logging         | JSON (`summaries.json`, `logs.json`) |

---

## 🗃️ Folder Structure

```text
feedflash/
├── app.py              # Gradio UI
├── news_fetcher.py     # NewsAPI + newspaper3k
├── summarizer.py       # Loads fine-tuned model
├── scheduler.py        # Scheduled runs + data reset
├── summaries.json      # Stores current day's summaries
├── logs.json           # Stores user feedback
├── requirements.txt
├── README.md
└── spaces.yaml         # Hugging Face Spaces config
```

---

## 🧪 Development Plan

| Phase | Task                                                    |
|-------|---------------------------------------------------------|
| 1     | Fine-tune summarization model and push to Hugging Face |
| 2     | Build article ingestion + summarizer pipeline           |
| 3     | Create Gradio UI and test manually                      |
| 4     | Add scheduled runs + daily purge                        |
| 5     | Deploy to Hugging Face Spaces and test full stack       |

---

## 🌍 Use Cases

- Quickly get an overview of major headlines
- Save time by reading compact summaries
- Ideal for students, researchers, and readers on the go
- Easily extendable for multi-language or regional sources

---

## 🧾 Highlight

**Project:** Built an automated news summarization system using a fine-tuned `bart-base` model, article ingestion pipeline, Gradio UI, and free-tier deployment on Hugging Face Spaces with scheduled daily runs.  
**Skills:** Transformers, NLP, JSON pipelines, `Gradio`, `apscheduler`, `newspaper3k`, Hugging Face deployment

---

## 📚 References & Resources

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Gradio Docs](https://gradio.app)
- [NewsAPI](https://newsapi.org/)
- [newspaper3k](https://newspaper.readthedocs.io/en/latest/)
- [apscheduler](https://apscheduler.readthedocs.io/en/latest/)
