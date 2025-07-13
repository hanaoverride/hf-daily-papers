import os
import time
import schedule
import requests
from dotenv import load_dotenv
from scraper import scrape_papers

# .env 파일에서 환경 변수 로드
load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def send_to_discord_webhook(papers):
    """스크래핑한 논문 목록을 Discord 웹훅으로 전송합니다."""
    if not DISCORD_WEBHOOK_URL:
        print("Error: DISCORD_WEBHOOK_URL not set in .env file.")
        return

    if not papers:
        print("No papers found to send.")
        # 논문이 없을 때도 알림을 보낼 수 있습니다.
        payload = {
            "content": "😥 오늘의 새로운 Hugging Face 논문을 찾지 못했어요."
        }
        try:
            requests.post(DISCORD_WEBHOOK_URL, json=payload)
        except requests.exceptions.RequestException as e:
            print(f"Error sending webhook message: {e}")
        return

    # Discord Embed 형식에 맞춰 데이터 구성
    embed = {
        "title": "📜 Hugging Face Daily Papers",
        "description": f"오늘 업데이트된 {len(papers)}개의 새로운 논문입니다!",
        "color": 7506394,  # Discord Blue
        "fields": []
    }

    for paper in papers[:10]:  # 너무 길지 않게 최대 10개만 표시
        embed["fields"].append({
            "name": paper['title'],
            "value": f"[논문 링크]({paper['url']})",
            "inline": False
        })

    # 웹훅으로 보낼 최종 데이터
    payload = {
        "embeds": [embed]
    }

    # 웹훅 URL로 POST 요청 전송
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        print(f"Successfully sent {len(papers)} papers to Discord.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending to Discord webhook: {e}")

def job():
    """스케줄링될 작업을 정의합니다."""
    print("Scraping daily papers for webhook...")
    latest_papers = scrape_papers()
    send_to_discord_webhook(latest_papers)

if __name__ == '__main__':
    # 스크립트 시작 시 한 번 즉시 실행
    job()
    
    # 매일 01:00에 작업 예약
    schedule.every().day.at("01:00").do(job)
    
    print("Scheduler started... Waiting for the scheduled time.")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
