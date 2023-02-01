FROM python:3-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT flask --app app --debug run --host=0.0.0.0
EXPOSE 5000/tcp

