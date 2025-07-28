#!/bin/bash

# Activate the virtual environment
source ./venv/bin/activate

# Run the tests
pytest

# Check the exit code from pytest
if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed."
    exit 1
fi