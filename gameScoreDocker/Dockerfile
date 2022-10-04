FROM python:3.9.0

RUN pip install flask
RUN pip install azure-cosmos

#WORKDIR /PycharmProjects/gamescoresAPI 
#for the container
COPY gameScore.py . 
EXPOSE 5000
CMD [ "python3", "./gameScore.py"]
