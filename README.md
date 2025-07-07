# ⚡ FeedFlash: Scheduled News Summarizer

## 📌 Summary

**FeedFlash** is a fully automated, scheduled news summarization system that fetches 30 English-language news articles per cycle (20 international, 10 Indian, no genre restriction) and generates concise ~90-word summaries using a custom fine-tuned transformer model. Summaries are displayed in a Gradio web UI, which updates throughout the day and resets every night to minimize storage and ensure free-tier compatibility. The system is optimized for students, readers, and anyone who wants to quickly scan the day's news without missing key information.

---

## ✅ What It Does

- Fetches live headlines from **NewsAPI** (free tier), every 4 hours from 10 AM to 10 PM.
- Extracts full article text using `newspaper3k`.
- Summarizes articles with a **fine-tuned Flan-T5-Base model** (PEFT/LoRA, quantized to 4-bit for efficient training, dequantized for CPU inference).
- Produces ~90-word summaries for each article (600 input tokens, 300 output tokens).
- Displays titles, summaries, and links in a clean **Gradio** interface, with mobile-friendly auto-scroll and robust error handling.
- Logs user feedback (planned: 👍/👎) and purges data daily to save memory and stay within free-tier limits.
- Stores all summaries and logs as JSON for transparency and easy integration.

---

## ⚙️ How It’s Built

### 🧠 Model

- **Base:** Flan-T5-Base (Google), fine-tuned using PEFT/LoRA on news-style data.
- **Quantization:** Trained with 4-bit quantization for resource efficiency; dequantized for fast CPU and ONNX inference.
- **Input/Output:** 600 input tokens (supports 400–800 word articles), 300 output tokens per summary (~90 words).
- **Hosted:** Model is available on Hugging Face Hub under the contributor’s ID.

### 📅 Scheduled Runs

- Fetches and summarizes **30 articles every 4 hours** (10 AM, 2 PM, 6 PM, 10 PM IST).
- Purges all summaries and logs daily at **2:00 AM** to minimize storage and maintain free-tier compatibility.
- Automated via GitHub Actions, syncing new summaries to the Hugging Face Space.

### 🧰 Tech Stack

| Component       | Tool/Library                                   |
|-----------------|------------------------------------------------|
| Data Fetching   | `NewsAPI`, `newspaper3k`                      |
| Summarization   | Hugging Face Transformers (Flan-T5-Base, LoRA/PEFT, 4-bit quantized/dequantized) |
| Scheduling      | GitHub Actions (custom cron scheduler)         |
| UI              | `Gradio`                                      |
| Hosting         | Hugging Face Spaces (CPU/ONNX)                |
| Logging         | JSON (`summaries.json`, `fetch_log.json`)      |

---

## 🖼️ Screenshots & Images

> _Add your screenshots or demo images below:_

- ![Placeholder Image 1](https://placehold.co/600x400?text=FeedFlash+UI+Screenshot)
- ![Placeholder Image 2](https://placehold.co/600x400?text=Summary+View)
- ![Placeholder Image 3](https://placehold.co/600x400?text=Mobile+UI)

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
| 1     | Fine-tune summarization model (Flan-T5-Base, LoRA/PEFT, 4-bit) and push to Hugging Face |
| 2     | Build article ingestion + summarizer pipeline           |
| 3     | Create Gradio UI and test manually                      |
| 4     | Add scheduled runs + daily purge with GitHub Actions    |
| 5     | Deploy to Hugging Face Spaces and test full stack       |

---

## 🌍 Use Cases

- Quickly get an overview of major headlines
- Save time by reading compact, AI-generated summaries
- Ideal for students, researchers, and readers on the go
- Easily extendable for multi-language or regional sources

---

## 🧾 Highlight

**Project:** Built an automated news summarization system using a PEFT/LoRA-finetuned, 4-bit quantized and dequantized Flan-T5-Base model, robust article ingestion pipeline, Gradio UI, and free-tier deployment on Hugging Face Spaces with scheduled daily runs.  
**Skills:** Transformers, NLP, quantization, JSON pipelines, `Gradio`, GitHub Actions scheduling, `newspaper3k`, Hugging Face deployment

---

## 📚 References & Resources

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Gradio Docs](https://gradio.app)
- [NewsAPI](https://newsapi.org/)
- [newspaper3k](https://newspaper.readthedocs.io/en/latest/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [PEFT & LoRA](https://huggingface.co/docs/peft/index)
