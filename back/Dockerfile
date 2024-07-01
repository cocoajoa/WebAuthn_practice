# 장고
FROM python:3.9-slim

# 장고는 back 아래에 있다.
WORKDIR /app

# 루트 다이렉토리의 requirements 사용
COPY requirements.txt /app/

#
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일을 추가
COPY . /back/

# 장고 설정
ENV DJANGO_SETTINGS_MODULE=mypjt.settings

# 장고 관리 명령 실행 (예: 마이그레이션)
RUN python manage.py migrate

# 포트 노출
EXPOSE 8000

# 장고 개발 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
