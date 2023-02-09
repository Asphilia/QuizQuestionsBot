FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.py
CMD ["python", "QuizQuestions.py"]