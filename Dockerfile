FROM python:3.9.5-alpine3.13 AS builder

RUN apk add --no-cache libc6-compat build-base

COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.9.5-alpine3.13 AS runner

RUN apk add --no-cache ffmpeg

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local:$PATH

WORKDIR /youtube2notion
COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]
