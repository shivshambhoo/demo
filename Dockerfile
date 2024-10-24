FROM python:3.10-slim

WORKDIR /app

# Copy your code into the container
COPY . /app

# Install pytest and any other dependencies
RUN pip install pytest

# Command to run the tests using pytest

CMD ["sh", "-c", "python3 calculator.py && pytest calculatorTest.py"]