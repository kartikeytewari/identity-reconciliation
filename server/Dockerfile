FROM python:latest

# make and build folder
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN cat requirements.txt

RUN pip3 install -r requirements.txt 
COPY . . 

CMD ["python3", "app.py"]
EXPOSE 5002
