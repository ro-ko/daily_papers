# summarizer.py
from openai import OpenAI
import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def summarize_text(text):
    prompt = f"""Please analyze and summarize the following paper from Hugging Face:

{text}

Assume the reader is a Korean PhD-level AI researcher specializing in computer vision and generative models.

Please write the summary in Korean, using clear and formal academic language.

Your summary should cover the following in order:
1. **핵심 동기와 문제 정의** (두 문장 이내)
2. **주요 기여 및 참신성** (목록 형태로 명확히 제시)
3. **모델 아키텍처 및 학습 설정** (구조적 요약)
4. **실험 설정**: 사용된 데이터셋, 마스킹 방식, 비교 대상(Baseline)
5. **정량적 결과**: 기존 방법들과의 성능 비교 포함
6. **한계점 및 잠재적 실패 요인**
7. **후속 연구 아이디어 또는 확장 방향**

결과는 Markdown 형식으로 정리해주세요.

    """
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            tools=[{"type": "web_search_preview"}],
        )
        return response.output_text
    except Exception as e:
        return f"Failed to summarize: {e}"
