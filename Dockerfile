FROM SCRATCH

MAINTAINER Yesh

WORKDIR /app

Add . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME ITRAIN-BATMAN

CMD ["python", "txt.py"]
