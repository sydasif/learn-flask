# Flask HTTP Methods and Routes Documentation

## Overview

This Flask application demonstrates handling different HTTP methods (GET, POST) for various routes
with appropriate response codes.

```python
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"


@app.route('/about', methods=['POST'])
def about():
    return "About Page", 202


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Contact Page - POST Request\n"
    return "Contact Page\n"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
```

## Route Details

### 1. Home Route - GET Only

- **URL**: `http://127.0.0.1:5000/`
- **Methods**: `GET`
- **Function**: `index()`
- **Response**:
    - HTML: `Hello, World!`
    - Status: 200 (default)
- **Test**: `curl http://127.0.0.1:5000/`

### 2. About Route - POST Only

- **URL**: `http://127.0.0.1:5000/about`
- **Methods**: `POST`
- **Function**: `about()`
- **Response**:
    - HTML: `About Page`
    - Status: 202 (Accepted)
- **Test**: `curl -X POST http://127.0.0.1:5000/about`
- **Header Check**: `curl -I -X POST http://127.0.0.1:5000/about`

### 3. Contact Route - Multiple Methods

- **URL**: `http://127.0.0.1:5000/contact`
- **Methods**: `GET, POST`
- **Function**: `contact()`
- **Logic**:
    - **GET Request**: Returns "Contact Page"
    - **POST Request**: Returns "Contact Page - POST Request"
- **Tests**:
    - GET: `curl http://127.0.0.1:5000/contact`
    - POST: `curl -X POST http://127.0.0.1:5000/contact`

## Key Features

### HTTP Method Specification

- `methods=['GET']` - Restricts route to GET requests only
- `methods=['POST']` - Restricts route to POST requests only
- `methods=['GET', 'POST']` - Allows both GET and POST requests

### Response Customization

- **Default Status Code**: 200 OK
- **Custom Status Code**: 202 Accepted (in about route)
- **Method Detection**: `request.method` to handle different HTTP methods

## Testing Commands

```bash
# Test GET request on home route
curl http://127.0.0.1:5000/

# Test POST request on about route
curl -X POST http://127.0.0.1:5000/about

# Check headers for POST request
curl -I -X POST http://127.0.0.1:5000/about

# Test GET and POST on contact route
curl http://127.0.0.1:5000/contact
curl -X POST http://127.0.0.1:5000/contact
```

## Error Handling

- Attempting POST on GET-only routes will return 405 Method Not Allowed
- Attempting GET on POST-only routes will return 405 Method Not Allowed
