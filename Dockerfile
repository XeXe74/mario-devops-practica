FROM ubuntu:latest
LABEL authors="mariotg"

ENTRYPOINT ["top", "-b"]