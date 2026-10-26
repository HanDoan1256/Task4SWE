# Use an official image that includes Python 3.12
FROM python:3.12-slim
# Set the working directory inside the container
WORKDIR /app
# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application source code
COPY app.py .
# Document the port used by the app
EXPOSE 5000
# Start the web server when the container launches
CMD ["python", "app.py"]
