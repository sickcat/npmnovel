FROM ubuntu
MAINTAINER SICKCAT
RUN apt-get update && \
	apt-get install -y python python-pip python-dev build-essential && \
	apt-get install -y mysql-client && \
	apt-get install -y libmysqlclient-dev && \
	apt-get install -y abiword && \
	pip install --upgrade && \
	pip install tornado && \
	pip install torndb && \
	pip install requests && \
	pip install mysql-python \
	&& apt-get clean \
 	&& apt-get autoclean \
 	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD * /police
WORKDIR /police
CMD ["bash"]
