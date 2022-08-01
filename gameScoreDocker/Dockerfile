FROM python:3.9.0

RUN pip install flask

#WORKDIR /PycharmProjects/gamescoresAPI 
#for the container
RUN cp gameScore.py  
EXPOSE 5000
CMD [ "python3", "./gameScore.py"]
