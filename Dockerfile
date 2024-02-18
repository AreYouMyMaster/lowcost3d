FROM --platform=linux/x86_64 ubuntu:22.04

RUN apt-get -y clean && apt-get -y update && apt-get -y upgrade \
    && apt-get install --yes --no-install-recommends libegl1 libgl1 libgomp1 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install python packages
WORKDIR /workspace
COPY requirements.txt ./

RUN pip3 install --timeout 1000 -r requirements.txt
ENV EGL_PLATFORM=surfaceless

# copy files
COPY . /workspace
