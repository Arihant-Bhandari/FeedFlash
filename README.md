# LexiRead: Personalized News Summarizer

## 📌 Summary
Smart News Summarizer is an AI-powered tool that condenses lengthy news articles into concise, human-readable summaries. Using state-of-the-art transformer models like **T5** and **BART**, the system offers rapid comprehension of complex news content, tailored for students, professionals, and researchers who need TL;DRs without losing context.

## ✅ What It Does
- Accepts raw news article text and generates a concise summary.
- Leverages **T5/BART** models via Hugging Face pipelines.
- Built and executed in a Kaggle notebook using free-tier GPUs.

## ⚙️ How It Will Be Built

### Dataset
- [CNN/DailyMail](https://www.kaggle.com/datasets/saipavansarin/news-summary)
- BBC News Summary
- Inshorts News Data

### Model
- Pretrained transformer models: `t5-small`, `bart-base` (Hugging Face).

### Development Plan
| Week | Tasks |
|------|-------|
| 1 | Learn Hugging Face, load summarization pipeline |
| 2 | Load dataset, build basic summarizer |
| 3 | Add polish, output formatting, documentation |

## 🧠 Techniques Used
- Hugging Face Pipelines
- Transformer models for summarization
- Transfer Learning

## 🧰 Tech Stack
- Python 3.x, Hugging Face, Pandas, NumPy
- Kaggle Notebooks (Free GPU)
- Jupyter Notebook

## 🌍 Societal Use Case
- Help readers and students consume news faster.
- Useful for content summarization in journalism and academia.
- Potential use in browser extensions and learning platforms.

## 🧾 Resume Outlook
**Summary:** Built a summarizer using Hugging Face’s `t5-small` and `bart-base`, executed in Kaggle Notebook on CNN/DailyMail dataset.  
**Skills:** Transformers, Hugging Face, Jupyter, summarization pipelines.

## 📚 Learning Resources
- [Hugging Face Course](https://huggingface.co/learn/nlp-course)
- [T5 vs BART Blog](https://towardsdatascience.com/t5-vs-bart-which-summarizer-should-you-use-2d2f6cdbf04e)
- [Kaggle Notebooks Guide](https://www.kaggle.com/docs/notebooks)
