FROM python:3.11.4
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install --upgrade pip
ADD requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python", "/app/password_manager_api/manage.py", "runserver", "0.0.0.0:80"]