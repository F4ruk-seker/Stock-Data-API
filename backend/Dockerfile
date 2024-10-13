FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    useradd -ms /bin/bash django-user


COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

USER django-user