# scraper.py
import requests
from playwright.sync_api import sync_playwright

def fetch_paper_links(date="2025-05-05"):
    url = f"https://huggingface.co/papers/date/{date}"
    paper_links = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"🔗 페이지 열기: {url}")
        page.goto(url, timeout=60000)

        try:
            # 논문 링크가 들어 있는 h3 > a[href^="/papers/"] 요소가 나타날 때까지 대기
            page.wait_for_selector('h3 > a[href^="/papers/"]', timeout=15000)
            links = page.query_selector_all('h3 > a[href^="/papers/"]')
            paper_links = ["https://huggingface.co" + link.get_attribute("href") for link in links]
        except Exception as e:
            print(f"❗ 논문 링크를 찾는 데 실패했습니다: {e}")
            print(page.content()[:1000])  # 렌더링된 HTML 일부 출력

        browser.close()

    return paper_links
