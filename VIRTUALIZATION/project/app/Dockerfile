FROM ubuntu:20.04

RUN apt-get update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update
RUN apt-get update && \
  apt-get -y install python3.11 python3-pip && \
  update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

RUN update-alternatives --set python /usr/bin/python3.11 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN apt update && apt install curl -y && \
  curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && \
  apt-get -y install nodejs && \
  npm install -g pnpm && \
  rm -rf /var/lib/apt/lists/*
RUN npm install -g npm@latest

WORKDIR /app
COPY . /app

RUN cd frontend && \
  pnpm install && \
  pnpm run build && \
  cd ..

RUN pip install --upgrade --user setuptools==58.3.0
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry add requests
RUN poetry install

EXPOSE 80

CMD ["poetry", "run", "python3", "app.py"]
