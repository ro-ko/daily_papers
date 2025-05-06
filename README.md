# 🤖 Hugging Face Daily Papers 요약 자동화

이 레포는 Hugging Face의 [Daily Papers](https://huggingface.co/papers)에 매일 올라오는 최신 인공지능 논문들을 자동으로 크롤링하고, OpenAI GPT API를 활용해 요약하는 시스템입니다. 요약 결과는 매일 마크다운 형식으로 저장되며, GitHub Actions를 통해 자동화됩니다.

---

## ✅ 기능 개요

- 매일 오전 9시(KST), Hugging Face Daily Papers 페이지에서 논문 목록 수집
- 각 논문의 링크를 GPT에게 전달하여 자동 요약 생성
- 요약 내용을 `output/summaries/YYYY-MM-DD.md`로 저장
- GitHub Actions를 통해 자동 실행 및 커밋

---

## 🛠️ 사용 기술

- Python 3.10+
- Playwright (동적 크롤링)
- OpenAI GPT-4 API
- GitHub Actions (CI 자동화)
- BeautifulSoup (HTML 파싱)
- Markdown 파일 저장 및 관리

---

## 📂 프로젝트 구조
```
.
├── .github/workflows/daily.yml # 자동 실행 워크플로
├── scraper.py # 논문 링크 수집 (Playwright)
├── summarizer.py # GPT 요약 모듈
├── daily_runner.py # 전체 실행 파이프라인
├── output/
│ └── summaries/ # 날짜별 요약 결과 저장
├── .env.example # API 키 예시 템플릿
└── requirements.txt # 의존성 목록
```


---

## 🔐 환경 설정

`.env` 파일을 생성해 OpenAI API 키를 등록하세요:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
이 키는 절대로 커밋하지 마세요!

## 🚀 수동 실행
- GitHub Actions > "Run workflow" 버튼을 눌러 수동 실행이 가능합니다.
- 자동 실행은 매일 UTC 3시 (한국 시간 정오 12시)에 수행됩니다.

## 📖 예시 출력
- output/summaries/2025-05-06.md

- GPT가 요약한 논문 목록을 날짜별로 확인할 수 있습니다.

## 🧪 향후 계획
- Notion 자동 업로드 연동

- Slack 알림 연동

- 요약 평가 지표(Factuality, Relevance 등) 자동화

##  개발자
- @ro-ko
- Hugging Face Papers 자동 정리 프로젝트
