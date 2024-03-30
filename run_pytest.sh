#!/bin/bash

# Set the directory where your tests are located
TEST_DIR="tests"

# Name of the virtual environment directory
VENV_DIR="venv"

# Path to requirements.txt
REQUIREMENTS_FILE="requirements.txt"

# Specify the path where the geckodriver will be located
GECKODRIVER_PATH="/usr/local/bin/geckodriver"

# Check if geckodriver exists and is executable
if [ ! -x "$GECKODRIVER_PATH" ]; then
    echo "Geckodriver not found, downloading..."
    wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
        && tar -xzf geckodriver-v0.30.0-linux64.tar.gz -C /usr/local/bin \
        && chmod +x /usr/local/bin/geckodriver \
        && rm geckodriver-v0.30.0-linux64.tar.gz
else
    echo "Geckodriver already exists."
fi

# wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
#     && tar -xzf geckodriver-v0.30.0-linux64.tar.gz -C /usr/local/bin \
#     && chmod +x /usr/local/bin/geckodriver \
#     && rm geckodriver-v0.30.0-linux64.tar.gz

# Update package lists
apt-get update

# Install  Firefox ESR
apt-get install -y firefox-esr

# Install Firefox
apt-get install -y firefox

# Function to install pip if not installed
install_pip() {
    echo "Installing pip..."
    python3 -m ensurepip --upgrade --default-pip
}

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    install_pip
fi

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    # Create the virtual environment
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Check if requirements.txt exists and install dependencies
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing dependencies from $REQUIREMENTS_FILE..."
    pip install -r $REQUIREMENTS_FILE
else
    echo "No requirements.txt found. Skipping dependencies installation."
fi

# Run pytest
echo "Running pytest for test cases in $TEST_DIR..."
pytest $TEST_DIR

# Check if pytest ran successfully
if [ $? -eq 0 ]; then
    echo "Pytest finished successfully."
else
    echo "Pytest encountered errors."
fi

# Deactivate the virtual environment
deactivate