FROM continuumio/miniconda3:latest

WORKDIR /app

RUN apt-get update && \
  apt-get install build-essential -y && \
  apt-get -q clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create the environment:
COPY muda_env.yml .
RUN conda info && \
  conda env create -f muda_env.yml

RUN mkdir -p /app/home && \
  chmod o=rwx /app/home

# COPY relevant codes and data
COPY convert_docid.py .
COPY muda /app/MuDA/muda

ENV PYTHONPATH=.:./MuDA:
ENV HOME=/app/home

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "muda4", "python"]
