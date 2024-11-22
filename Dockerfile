FROM centos:latest
RUN yum clean all
RUN yum update -y
RUN yum install  -y python3.10
RUN yum install  -y python3-pip

ADD hello.py /
CMD ["python3", "/hello.py"]




