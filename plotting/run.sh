#! /bin/bash

export PLOTTING=$(pwd)
export CPLUS_INCLUDE_PATH=$PLOTTING

root -l -x -q macros/flux.C+
root -l -x -q macros/xsec.C+
root -l -x -q macros/events.C+
root -l -x -q macros/profiles.C+
root -l -x -q macros/digi.C+