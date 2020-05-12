#! /bin/bash

CURRENTDIR=$(pwd)
export THESIS="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $THESIS/plotting

if [[ -d "./env" ]]; then
    source ./env/bin/activate
    conda activate thesis
else
    # Download the latest version of miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh --no-check-certificate

    # Install miniconda3 in the current directory
    bash miniconda.sh -b -p $THESIS/plotting/env
    rm miniconda.sh

    # Activate miniconda and create the thesis environment
    source ./env/bin/activate
    conda update -n base -c defaults conda -y
    conda config --add envs_dirs $THESIS/plotting/env/envs
    conda config --add envs_dirs $THESIS/plotting/env/envs
    conda env create -f $THESIS/environment.yaml

    # Clean the miniconda install
    conda clean --all -y

    # Make sure the base environement is not enabled by default
    conda config --set auto_activate_base false

    conda activate thesis
fi

# Go back to the user directory
cd $CURRENTDIR
return
