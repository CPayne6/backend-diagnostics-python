FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app

ARG PORT
ENV HOST "0.0.0.0:$PORT"

ENV UPPER_LIMIT $UPPER_LIMIT
ENV LOWER_LIMIT $LOWER_LIMIT
ENV DEFAULT_UPPER_LIMIT $DEFAULT_UPPER_LIMIT

# Copy in app files
COPY Pipfile Pipfile.lock *.py .

# Install dependencies
RUN pip install pipenv
RUN pipenv install --system --deploy



# Run app
CMD gunicorn --graceful-timeout 5 --chdir /app app:app -w 4 -b $HOST
