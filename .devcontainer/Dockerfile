FROM continuumio/miniconda3

ARG USER_NAME=thesis
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Copy environment.yaml to a temp locaition so we can update the environment.
COPY .devcontainer/environment.yaml /tmp/conda-tmp/

# Configure apt and install packages
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    #
    # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
    && apt-get -y install git openssh-client less iproute2 procps iproute2 lsb-release \
    #
    # Install latex tools
    && apt-get install -y biber latexmk make texlive-full python-pygments gnuplot \
    #
    # Install pylint
    && /opt/conda/bin/pip install pylint \
    #
    # Update Python environment based on environment.yaml
    && if [ -f "/tmp/conda-tmp/environment.yaml" ]; then /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yaml; fi \
    && rm -rf /tmp/conda-tmp \
    #
    # Create a non-root user and give sudo access
    && groupadd --gid $USER_GID $USER_NAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USER_NAME \
    && apt-get install -y sudo \
    && echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME\
    && chmod 0440 /etc/sudoers.d/$USER_NAME \
    #
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
