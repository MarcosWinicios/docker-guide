FROM python:3.6
LABEL mantainer="Marcs Winicios <pmarcoswinicios@gmail.com>"

ENV PYTHONUNBUFFERED 1 # Definne que o buffer do python não deve ser usado para a saída padrão dos prints

RUN pip install redis==2.10.5

ENTRYPOINT ["/usr/local/bin/python"]