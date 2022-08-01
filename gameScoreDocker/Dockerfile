FROM python:3.9.0

RUN pip install flask

#WORKDIR /PycharmProjects/gamescoresAPI 
#for the container
COPY -f gameScoreDocker/gameScore.py . 
EXPOSE 5000
CMD [ "python3", "./gameScore.py"]
