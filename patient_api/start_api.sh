#!/bin/bash

# Stop on any error
set -e

echo "🌱 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🚀 Starting Patients API server..."
export FLASK_APP=app.py:app
export FLASK_ENV=venv
flask db upgrade
flask run