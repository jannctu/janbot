FROM python:3.11

WORKDIR /janbot

ENV PIP_CACHE_DIR=/cache

RUN mkdir -p ${PIP_CACHE_DIR}

COPY . .

RUN pip install --cache-dir ${PIP_CACHE_DIR} --upgrade -r /janbot/requirements.txt

ENV PYTHONPATH="/janbot:${PYTHONPATH}"

CMD ["python", "app/__main__.py"]