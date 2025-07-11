# Hugging Face Daily Papers 알리미

Hugging Face에 매일 새로 올라오는 논문 정보를 스크래핑하여 지정된 Discord 웹훅으로 알림을 보내는 자동화 스크립트입니다.

## ✨ 주요 기능

- **일일 논문 스크래핑**: Hugging Face의 'Papers' 섹션에서 최신 논문 목록을 가져옵니다.
- **Discord 알림**: 스크래핑한 논문 목록을 Discord 임베드 메시지 형식으로 전송합니다.
- **자동화**: Cron을 사용하여 매일 정해진 시간에 스크립트를 실행합니다.
- **Docker 지원**: Docker를 통해 간편하게 배포하고 실행 환경을 관리할 수 있습니다.

## 📂 파일 구조

```
.
├── .dockerignore
├── .gitignore
├── crontab           # Cron 스케줄 설정 파일
├── Dockerfile        # Docker 이미지 빌드를 위한 설정 파일
├── entrypoint.sh     # Docker 컨테이너 시작 시 실행될 스크립트
├── main.py           # 메인 실행 파일 (스크래핑 및 Discord 전송)
├── README.md         # 프로젝트 설명 파일
├── requirements.txt  # Python 의존성 목록
└── scraper.py        # Hugging Face 스크���핑 로직
```

## 🚀 배포 방법

이 프로젝트는 두 가지 방법으로 배포할 수 있습니다: **Python 직접 실행** 또는 **Docker 사용**.

### 1. Python으로 직접 실행하기

이 방법은 로컬 환경이나 서버에서 직접 Python 스크립트를 실행할 때 사용합니다.

#### 사전 준비

- Python 3.10 이상
- `pip` 및 `venv`

#### 단계

1.  **저장소 복제**
    ```bash
    git clone https://github.com/your-username/huggingface-daily-papers.git
    cd huggingface-daily-papers
    ```

2.  **가상 환경 생성 및 활성화**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate   # Windows
    ```

3.  **의존성 설치**
    ```bash
    pip install -r requirements.txt
    ```

4.  **환경 변수 설정**
    `.env` 파일을 생성하고 Discord 웹훅 URL을 추가합니다.
    ```
    # .env
    DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/your/webhook_url"
    ```

5.  **스크립트 실행**
    수동으로 스크립트를 실행하여 정상적으로 동작하는지 확인합니다.
    ```bash
    python main.py
    ```

6.  **(선택 사항) Cron으로 자동 실행 등록**
    매일 정해진 시간에 스크립트를 실행하려면 시스템의 `crontab`에 작업을 등록합니다.
    ```bash
    # crontab -e
    # 매일 새벽 1시에 실행
    0 1 * * * /path/to/your/project/venv/bin/python /path/to/your/project/main.py
    ```

### 2. Docker로 실행하기

Docker를 사용하면 의존성이나 실행 환경에 대한 걱정 없이 간편하게 배포할 수 있습니다.

#### 사전 준비

- Docker

#### 단계

1.  **저장소 복제**
    ```bash
    git clone https://github.com/your-username/huggingface-daily-papers.git
    cd huggingface-daily-papers
    ```

2.  **환경 변수 설정**
    Docker 컨테이너에 환경 변수를 전달하기 위해 `.env` 파일을 생성합니다.
    ```
    # .env
    DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/your/webhook_url"
    ```

3.  **Docker 이미지 빌드**
    ```bash
    docker build -t hf-daily-papers .
    ```

4.  **Docker 컨테이너 실행**
    `--env-file` 옵션을 사용하여 `.env` 파일의 환경 변수를 컨테이너에 전달합니다.
    ```bash
    docker run -d --name hf-papers-notifier --env-file .env hf-daily-papers
    ```
    - `-d`: 컨테이너를 백그라운드에서 실행합니다.
    - `--name`: 컨테이너에 이름을 부여합니다.

    컨테이너는 `entrypoint.sh` 스크립트에 의해 시작 시 한 번, 그리고 `crontab` 설정에 따라 매일 새벽 1시에 주기적으로 `main.py`를 실행합니다.

#### 로그 확인

컨테이너의 실행 로그는 다음 명령어로 확인할 수 있습니다.
```bash
docker logs hf-papers-notifier
```
