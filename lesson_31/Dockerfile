
# Use a stable Debian base for Chrome compatibility

# Use Selenium's official Chrome image for reliable browser testing
FROM selenium/standalone-chrome:latest

# Install Python and pip
USER root
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace/lesson_31

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "tests/"]
