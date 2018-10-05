FROM python:3.7.0

RUN pip install pipenv
COPY . .
RUN pipenv install --system
EXPOSE 5000
CMD gunicorn gunicornentry:app --workers ${WORKERS:-8} --bind 0.0.0.0:5000 --access-logfile -