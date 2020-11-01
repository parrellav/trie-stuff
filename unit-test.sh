#!/bin/bash

virtualenv venv --python=python3

# activate the virtual environment
source venv/bin/activate

pip install -U -q pytest

# pull down all dependencies
pip -q install -r requirements.txt

python -m pytest
deactivate
