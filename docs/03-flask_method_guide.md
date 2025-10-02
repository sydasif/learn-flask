# Flask HTTP Methods and Routes Documentation

## Overview

This document provides a general guide to handling HTTP methods in Flask. The current application (`app.py`) primarily uses the GET method for its routes.

## HTTP Methods in Flask

HTTP methods (or verbs) indicate the desired action to be performed for a given resource. Common methods include GET, POST, PUT, DELETE.

### GET Method

- **Purpose**: Used to request data from a specified resource.
- **Characteristics**: Idempotent (multiple identical requests have the same effect as a single one) and safe (does not alter the state of the server).
- **Usage in Flask**: By default, all routes handle GET requests if no `methods` argument is specified in the `@app.route()` decorator.
  - **Example**:

    ```python
    @app.route('/')
    def index():
        return "This is a GET request."
    ```

### POST Method

- **Purpose**: Used to submit data to be processed to a specified resource.
- **Characteristics**: Not idempotent and not safe (can alter the state of the server).
- **Usage in Flask**: You must explicitly specify `methods=['POST']` in the `@app.route()` decorator.
  - **Example**:

    ```python
    from flask import request

    @app.route('/submit', methods=['POST'])
    def submit_form():
        data = request.form['item']
        return f"Submitted: {data}"
    ```

### Handling Multiple Methods

A single route can handle multiple HTTP methods by listing them in the `methods` argument.

- **Example**:

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f"Logged in as {username}"
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
```

### Response Status Codes

Flask allows you to return a custom HTTP status code along with the response.

- **Example**: `return "Resource Created", 201`

## Current Application HTTP Methods

The `app.py` in this project currently uses the `GET` method for its `/` and `/about` routes, which is the default behavior for Flask routes.
