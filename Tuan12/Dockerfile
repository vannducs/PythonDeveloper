from python:3.12-slim

workdir /app
copy requirements.txt
run pip install --no-cache-dir -r requirements.txt
copy . .
expose 8000
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker",
 "app.main:app", "--bind", "0.0.0.0:8000"]

# lệnh production: gunicorn -k uvicorn.workers.UvicornWorker app.main:app