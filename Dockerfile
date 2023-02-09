FROM python:3.8
WORKDIR .
COPY . .
RUN pip install -r requirements.py
CMD ["python", "QuizQuestions.py"]