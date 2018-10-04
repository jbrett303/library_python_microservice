FROM python:3.7.0

RUN pip install pipenv
COPY . .
RUN pipenv install --system
EXPOSE 3000
CMD gunicorn user:app --workers ${WORKERS:-8} --bind 0.0.0.0:3000 --access-logfile -