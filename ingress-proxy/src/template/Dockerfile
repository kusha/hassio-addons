ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache socat

COPY run.sh /
RUN chmod a+x /run.sh

EXPOSE 8099
ENTRYPOINT [ "socat", "tcp-listen:8099,reuseaddr,fork", "tcp:192.168.0.10:80" ]
# CMD [ "/run.sh" ]
