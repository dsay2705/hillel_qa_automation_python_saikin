FROM python:3.11-slim

WORKDIR /workspace/lesson_31

# Install Chromium and dependencies
RUN apt-get update && \
	apt-get install -y chromium chromium-driver && \
	rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PATH="/usr/lib/chromium:/usr/lib/chromium-browser:$PATH"
ENV CHROME_BIN="/usr/bin/chromium"
ENV CHROMEDRIVER_BIN="/usr/bin/chromedriver"

CMD ["pytest", "tests/"]