
FROM python


WORKDIR /app


COPY . /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y ffmpeg


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "audio_processing.py"]