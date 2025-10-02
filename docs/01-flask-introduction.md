# Flask Application Overview

## Overview

A simple Flask web application with a homepage displaying a list of numbers and an about page.

## Code Breakdown

```python
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    nums = [10, 20, 30, 40, 50]
    return render_template('index.html', numbers=nums)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
```

## Components

- **Flask Import**: Imports the Flask class and render_template function.
- **App Instance**: Creates a Flask application instance, specifying the 'templates' folder.
- **Home Route**: `@app.route('/')` maps the root URL to the `index` function.
  - The `index` function creates a list of numbers and renders `index.html`, passing the numbers.
- **About Route**: `@app.route('/about')` maps the `/about` URL to the `about` function.
  - The `about` function renders `about.html`.
- **Main Block**: Runs the application with:
  - Host: `127.0.0.1` (localhost)
  - Port: `5000`
  - Debug: `True` (enables auto-reload and debug mode)

## Usage

1. Save the code in `app.py`.
2. Ensure `index.html`, `about.html`, and `base.html` are in the `templates` directory.
3. Run with: `python app.py`
4. Visit `http://127.0.0.1:5000` for the homepage and `http://127.0.0.1:5000/about` for the about page in your browser.

## Requirements

- Python 3.x
- Flask (`pip install flask`)

## Note

The application runs in debug mode, which should be disabled in production environments.
