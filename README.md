# Flask DevOps Project - CI/CD with CircleCI

## Overview
A Dockerized Flask app with full CI/CD pipeline using CircleCI.
Changing `app/config.yaml` automatically triggers the pipeline.

## Tech Stack
- **Flask** - Python web framework
- **Docker** - Containerization
- **CircleCI** - CI/CD pipeline
- **Docker Hub** - Image registry
- **Render** - Cloud deployment

## Pipeline Flow
1. Edit `app/config.yaml`
2. Push to GitHub
3. CircleCI triggers automatically
4. Tests run → Docker image builds → Deploys to Render

## API Endpoints
| Endpoint  | Description        |
|-----------|--------------------|
| `/`       | App info from config |
| `/health` | Health check       |
| `/config` | Current config info |

## How to Run Locally
```bash
pip install -r requirements.txt
cd app && python app.py
```