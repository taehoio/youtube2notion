FROM python:3.9.5-alpine3.13 AS builder

RUN apk add --no-cache libc6-compat build-base git

# Google CloudRun changes HOME to /home for CMD where RUN uses /root
# https://stackoverflow.com/questions/62276734/google-cloud-run-changes-home-to-home-for-cmd-where-run-uses-root
# So add a new user and copy /home directory explictly to be compatible with Google CloudRun.
RUN adduser -S youtube2notion
USER youtube2notion

COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.9.5-alpine3.13 AS runner

RUN apk add --no-cache ffmpeg

RUN adduser -S youtube2notion
USER youtube2notion

COPY --from=builder /home/youtube2notion/.local /home/youtube2notion/.local
ENV PATH=/home/youtube2notion/.local/bin:$PATH

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]
