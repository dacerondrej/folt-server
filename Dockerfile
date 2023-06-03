FROM python:3.8
RUN mkdir /folt
WORKDIR /folt
ADD . /folt
RUN pip3 install -r requirements.txt
ENV NAME folt
CMD ["python3", "app.py"]
