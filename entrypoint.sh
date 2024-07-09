#!/bin/sh

# Run database.py
python database/database.py

# Start the Flask application
flask run --host=0.0.0.0 --port=5000
