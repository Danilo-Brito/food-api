#!/bin/sh

# Run database.py
python database/database.py

# Start the Flask application
flask run --host=172.25.0.2 --port=5000
