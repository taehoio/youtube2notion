FROM linuxserver/ffmpeg:4.3-cli-ls22

RUN apt-get update && \
    apt install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get install -y python3.9 python3.9-venv make && \
    rm -rf /var/lib/apt/lists/* /var/tmp/*

WORKDIR /youtube2notion
COPY . .

RUN make venv

ENTRYPOINT [ "./entrypoint.sh" ]
