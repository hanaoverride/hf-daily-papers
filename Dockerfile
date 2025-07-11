# Dockerfile

# 1. 베이스 이미지 설정
FROM python:3.10-slim

# 1-1. GitHub 저장소 연결용 LABEL 추가
LABEL org.opencontainers.image.source=https://github.com/hanaoverride/huggingface-daily-papers

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 시스템 패키지 업데이트 및 cron, tzdata 설치
ENV TZ=Asia/Seoul
RUN apt-get update && apt-get install -y cron tzdata && rm -rf /var/lib/apt/lists/*

# 4. 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 코드 및 스케줄링 파일 복사
COPY . .

# 6. entrypoint.sh 실행 권한 부여
RUN chmod +x /app/entrypoint.sh

# 7. 컨테이너 시작 시 entrypoint.sh 실행
ENTRYPOINT ["/app/entrypoint.sh"]