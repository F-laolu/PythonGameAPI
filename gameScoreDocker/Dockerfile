FROM python:3.9.0

RUN pip install flask
RUN pip install azure-cosmos
RUN pip install opencensus-ext-azure
RUN pip install opencensus-ext-flask

#WORKDIR /PycharmProjects/gamescoresAPI 
#for the container
COPY gameScoreDocker/gameScore.py . 
EXPOSE 5000
CMD [ "python3", "./gameScore.py"]
