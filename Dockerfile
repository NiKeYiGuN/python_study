FROM python:3.8
RUN mkdir -p /test/
WORKDIR /test

COPY . .

RUN python -m pip config --global set global.index-url https://mirrors.aliyun.com/pypi/simple
RUN pip install pytest
CMD ["pytest"]