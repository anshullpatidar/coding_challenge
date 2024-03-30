# Use the official Python image with the version as close as possible to 3.12.2
FROM python:3.12

# Set the working directory inside the container
WORKDIR /usr/src/app

COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Make your script executable
RUN chmod +x run_pytest.sh

# Command to run the pytest script
CMD ["./run_pytest.sh"]

