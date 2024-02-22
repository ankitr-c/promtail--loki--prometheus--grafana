FROM python:3.7-slim
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY flask_app.log log-app.py /app/
EXPOSE 8000
CMD [ "python", "log-app.py" ]