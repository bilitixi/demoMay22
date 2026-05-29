# Readme
## Installation

```bash
pip install -r requirements.txt
```

## start

```bash
python app.py
```

## test

```bash
pytest
```

## Docker

```bash
docker build -t flask-app .
docker run -p 5001:5000 flask-app
docker exec -it flask-app pytest
```