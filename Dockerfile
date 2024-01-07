FROM --platform=linux/x86_64 pytorch/pytorch:1.10.0-cuda11.3-cudnn8-devel

# Update all packages
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-get -y clean && apt-get -y update && apt-get -y upgrade

# Install Open3D system dependencies and pip
RUN apt-get install --no-install-recommends -y \
    libegl1 \
    libgl1 \
    libgomp1 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


# Install python packages
WORKDIR /workspace
COPY requirements.txt ./

RUN pip3 install --timeout 1000 -r requirements.txt

# copy files
COPY . /workspace
