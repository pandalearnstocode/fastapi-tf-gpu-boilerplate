FROM tensorflow/tensorflow:2.2.0-gpu
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY ./app /app
WORKDIR /app/
ENV PYTHONPATH=/app
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py
COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh
EXPOSE 80
CMD ["/start.sh"]