FROM python:3.7.0

RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system
COPY library.py .
EXPOSE 5000
CMD gunicorn library:app --workers ${WORKERS:-8} --bind 0.0.0.0:5000 --access-logfile -