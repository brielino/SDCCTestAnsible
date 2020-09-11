# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /SDCC
# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
# copy the content of the local  directories to the working directory
COPY . /SDCC
#COPY src /src
#COPY dbConnection /dbConnection
# set the pytonpath
ENV PYTHONPATH="$PYTHONPATH:/dbConnection/"
ENV PYTHONPATH="$PYTHONPATH:/src/"
# command to run on container start
CMD [ "python", "src/server.py" ]
