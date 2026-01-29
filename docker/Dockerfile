# Gebruik een lichtgewicht Python image als basis
FROM python:3.9-slim

# Stel de werkmap in de container in
WORKDIR /app

# Kopieer de bestanden van je PC naar de container
COPY . .

# Installeer de benodigdheden (Flask)
RUN pip install -r requirements.txt

# Het commando dat start als de container start
CMD ["python", "app.py"]