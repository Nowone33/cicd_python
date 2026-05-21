# Dockerfile

FROM python:3.12-alpine3.23 AS builder

COPY . /opt/app

WORKDIR /opt/app

RUN apk add make binutils

RUN make dependency && make build

FROM alpine:3.23

RUN apk add --no-cache zlib

COPY --from=builder /opt/app/dist/calculs-snapshot /calculs

CMD ["/calculs"]