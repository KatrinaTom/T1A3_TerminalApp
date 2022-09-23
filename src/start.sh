#!/bin/bash
clear

python3 main.py

if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python example.py
    else
        echo "Try Python version 3 for the best experience!" >&2
    fi 
else
    echo "To use this application, install python from https://www.python.org/ for more instructions." >&2
fi