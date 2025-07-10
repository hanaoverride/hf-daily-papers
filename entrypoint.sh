#!/bin/bash

# 1. 컨테이너 시작 시 스크립트 즉시 실행
echo "Running script on container start..."
python /app/main.py

# 2. crontab 파일로부터 cron 데몬 설정
# crontab 파일의 소유권을 root로 변경하고, 읽기 전용 권한을 부여합니다.
chown root:root /app/crontab
chmod 0644 /app/crontab
crontab /app/crontab

# 3. cron 데몬을 포그라운드에서 실행
# 이렇게 하면 컨테이너가 종료되지 않고 계속 실행 상태를 유지합니다.
echo "Starting cron daemon..."
cron -f
