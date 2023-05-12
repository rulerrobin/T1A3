#!/bin/bash

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Please install Python 3"
    exit 1
fi

if [ -f "requirements.txt" ]
then
    pip3 install -r requirements.txt
fi

# Run main.py
python3 main.py