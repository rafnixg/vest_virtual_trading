FROM tiangolo/uvicorn-gunicorn:python3.8-slim

# Install requirements dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose the application in port 8000
EXPOSE 8000

# Copy the application
COPY . /app

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]