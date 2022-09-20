#!/bin/bash
if [[ -x "$(command -v python)" ]]
then
    python_version="$python -V 2>&1)"
    if [[ $python_version == "Python 3"* ]]
    then 
        python main.py
    else
        echo "This program runs best on Python 3. Recommend to upgrade" >&2
    fi
else
    echo "To run this program please install python" >&2
    exit 1
fi