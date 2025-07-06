import os
import json
from datetime import datetime, timedelta
from newspaper import Article
from newsapi import NewsApiClient
from app.summarizer import summarize_text

API_KEY = os.getenv("NEWS_API")
if not API_KEY:
    raise ValueError("❌ NEWS_API is not set in environment variables")

client = NewsApiClient(api_key=API_KEY)

def fetch_news(q, from_date, to_date, page_size=50):
    """Fetch news articles for a given query and date range."""
    try:
        response = client.get_everything(
            q=q,
            from_param=from_date,
            to=to_date,
            language="en",
            sort_by="relevancy",
            page_size=page_size,
        )
        return response.get("articles", [])
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return []

def extract_full_article(url):
    """Extract full text content from a news article URL."""
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text.strip()
    except Exception as e:
        print(f"⚠️ Failed to extract article from {url}: {e}")
        return ""

def main():
    """Main function to fetch, process, and save news summaries."""
    print("🚀 Starting news fetching and summarization...")

    from_date = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
    to_date = datetime.utcnow().strftime("%Y-%m-%d")

    # Fetch 30 international and 20 India-focused articles
    target_counts = {"international": 30, "india": 20}
    queries = {
        "international": "technology OR politics OR world -India",
        "india": "India AND (technology OR politics OR world)"
    }
    results = []
    logs = []
    fallback_attempts = 0
    max_fallbacks = 10

    for category, count in target_counts.items():
        collected = 0
        attempts = 0
        while collected < count and attempts < (max_fallbacks + 1):
            articles = fetch_news(
                q=queries[category],
                from_date=from_date,
                to_date=to_date,
                page_size=50
            )
            print(f"📰 Fetched {len(articles)} {category} articles (attempt {attempts+1})")
            for art in articles:
                if collected >= count:
                    break
                url = art.get("url")
                if not url:
                    continue
                full_text = extract_full_article(url)
                word_count = len(full_text.split())
                # Enforce word count limits
                if not full_text or word_count < 150 or word_count > 2500:
                    continue
                # Add prompt prefix
                prompt_text = "Summarize the following news article: " + full_text
                try:
                    summary = summarize_text(prompt_text)
                except Exception as e:
                    print(f"⚠️ Failed to summarize article {url}: {e}")
                    continue
                results.append({
                    "title": art.get("title"),
                    "source": art.get("source", {}).get("name"),
                    "publishedAt": art.get("publishedAt"),
                    "url": url,
                    "summary": summary
                })
                logs.append({
                    "title": art.get("title"),
                    "url": url,
                    "word_count": word_count,
                    "summary_length": len(summary.split()),
                    "category": category
                })
                collected += 1
            attempts += 1
            if collected < count:
                fallback_attempts += 1
                if fallback_attempts > max_fallbacks:
                    print(f"⚠️ Max fallback attempts reached for {category}.")
                    break

    print(f"✅ Successfully processed {len(results)} articles")

    os.makedirs("app", exist_ok=True)
    os.makedirs("backend", exist_ok=True)

    with open("app/summaries.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    with open("backend/fetch_log.json", "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.utcnow().isoformat(),
            "article_count": len(results),
            "logs": logs
        }, f, indent=2)

    print("💾 Results saved to app/summaries.json and backend/fetch_log.json")

if __name__ == "__main__":
    main()
