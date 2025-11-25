FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Gunicorn inside the container
CMD ["gunicorn", "metro_system.wsgi:application", "--bind", "0.0.0.0:" + os.getenv("PORT", "8000")]

