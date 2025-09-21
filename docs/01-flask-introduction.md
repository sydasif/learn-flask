# Flask Hello World Application

## Overview

A simple Flask web application that displays "Hello, World!" when accessed.

## Code Breakdown

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
```

## Components

- **Flask Import**: Imports the Flask class
- **App Instance**: Creates a Flask application instance
- **Route Decorator**: `@app.route('/')` maps the root URL to the index function
- **Index Function**: Returns the "Hello, World!" message
- **Main Block**: Runs the application with:
    - Host: `127.0.0.1` (localhost)
    - Port: `5000`
    - Debug: `True` (enables auto-reload and debug mode)

## Usage

1. Save the code in a file (e.g., `app.py`)
2. Run with: `python app.py`
3. Visit `http://127.0.0.1:5000` in your browser
4. You should see "Hello, World!" displayed

## Requirements

- Python 3.x
- Flask (`pip install flask`)

## Note

The application runs in debug mode, which should be disabled in production environments.
