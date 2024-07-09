#!/bin/sh

# Function to wait for MySQL to be ready
wait_for_db() {
    max_attempts=10
    attempt=0
    while [ ${attempt} -lt ${max_attempts} ]; do
        echo "Attempting to connect to MySQL (attempt ${attempt}/${max_attempts})"
        if nc -z db 3306 >/dev/null 2>&1; then
            echo "MySQL is up - continuing"
            return 0
        fi
        attempt=$((attempt + 1))
        sleep 10  # Increase sleep time to 10 seconds
    done
    echo "Failed to connect to MySQL after ${max_attempts} attempts"
    exit 1
}

# Wait for MySQL to be ready
wait_for_db

# Run database initialization script
python database/database.py

# Start the Flask application
flask run --host=0.0.0.0 --port=5000
