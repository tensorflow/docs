FROM python:3.7.3-alpine3.9

# install java etc
RUN apk update
RUN apk --no-cache add tar wget openjdk8 gcc pkgconfig zeromq zeromq-dev musl-dev

# install python package
RUN pip install jupyter

# download redpen
# RUN wget https://github.com/redpen-cc/redpen/archive/redpen-1.10.2.tar.gz
RUN wget https://github.com/redpen-cc/redpen/releases/download/redpen-1.10.1/redpen-1.10.1.tar.gz
RUN tar xvf redpen-1.10.1.tar.gz
RUN mkdir -p /user/local/redpen
RUN mv redpen-distribution-1.10.1 /usr/local/redpen
# RUN mv redpen-redpen-1.10.2 /usr/local/redpen


# add redpen to PATH
ENV PATH="/usr/local/redpen/bin:${PATH}"

WORKDIR /usr/local/documents

# set "redpen" command for entory point
CMD [ "redpen", "--help" ]
