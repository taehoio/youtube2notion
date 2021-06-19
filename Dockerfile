FROM python:3.9 AS builder

COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.9-slim AS runner

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/* /var/tmp/*

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local:$PATH

WORKDIR /youtube2notion
COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]
