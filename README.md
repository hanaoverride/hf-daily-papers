# Hugging Face Daily Papers

매일 Hugging Face에 올라오는 새로운 논문 정보를 수집하여 제공하는 자동화 프로젝트입니다.

## ✨ 주요 기능

-   매일 정해진 시간에 Hugging Face의 최신 논문 정보 스크래핑
-   Docker를 이용한 간편한 실행 환경 구성

## 🛠️ 기술 스택

-   Python
-   Docker

## 🚀 시작하기

### 사전 요구사항

-   [Docker](https://www.docker.com/get-started)가 설치되어 있어야 합니다.

### 설치 및 실행

1.  **프로젝트 클론**

    ```bash
    git clone https://github.com/your-username/huggingface-daily-papers.git
    cd huggingface-daily-papers
    ```

2.  **환경 변수 설정**

    프로젝트 루트 디렉터리에 `.env` 파일을 생성하고 필요한 환경 변수를 설정합니다.

    ```env
    # .env
    # 예: 알림을 위한 Webhook URL 등
    # SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
    ```

3.  **Docker 컨테이너 실행**

    Docker를 사용하여 프로젝트를 빌드하고 실행합니다.

    ```bash
    docker-compose up --build -d
    ```

## ⚙️ 설정

프로젝트에 필요한 주요 설정은 `.env` 파일을 통해 관리됩니다. 스크래핑 주기, 알림 채널 등 필요한 변수를 이 파일에 추가하여 사용할 수 있습니다.
