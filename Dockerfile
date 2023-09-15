
FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# This will skip the venv folder as it's in the .dockerignore file
COPY . .

# Specify the command to run when the container starts
CMD ["gunicorn", "server:app", "-b", "0.0.0.0:8000"]
