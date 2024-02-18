FROM alpine

RUN apk add --no-cache python3

ADD /Limerick-1.txt /home/data/Limerick-1.txt
ADD /IF.txt /home/data/IF.txt
ADD /main_docker.py /home/main_docker.py
 RUN mkdir -p /home/output/
CMD ["/home/main_docker.py"]
ENTRYPOINT ["python3"]