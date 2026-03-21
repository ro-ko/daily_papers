from datetime import datetime, timedelta
from scraper import fetch_paper_links
from summarizer import summarize_text
import os

def save_markdown(papers, date_str):
    os.makedirs("output/summaries", exist_ok=True)
    file_path = f"output/summaries/{date_str}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# 📰 Hugging Face Daily Papers – {date_str}\n\n")
        for paper in papers:
            f.write(f"## {paper['title']}\n")
            f.write(f"🔗 {paper['url']}\n\n")
            f.write(f"**Summary**:\n{paper['summary']}\n\n---\n\n")
    return file_path

def main():
    yesterday = datetime.now() - timedelta(days=1)
    date_str = yesterday.strftime("%Y-%m-%d")
    
    print(f"📅 Fetching papers for Yesterday: {date_str}...")

    urls = fetch_paper_links(date_str)
    papers = []

    for url in urls:
        print(f"\n🔍 Processing: {url}")
        summary = summarize_text(url)
        # URL 마지막 부분을 제목으로 변환 (예: some-paper-title -> Some Paper Title)
        title = url.split("/")[-1].replace("-", " ").title()
        papers.append({
            "url": url,
            "title": title,
            "summary": summary
        })

    save_markdown(papers, date_str)
    print(f"\n✅ Saved to: output/summaries/{date_str}.md")

if __name__ == "__main__":
    main()
