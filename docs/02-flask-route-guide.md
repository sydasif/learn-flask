# Flask URL Routing Documentation

## Overview

This Flask application demonstrates various URL routing techniques including static routes, dynamic
routes, and query parameter handling.

```python
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1> "


@app.route('/about')
def about():
    return "<h2>About Page</h2>"


@app.route('/user/<username>')
def user(username):
    return f"<h2>User: {username}</h2>"


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"<h2>{num1} + {num2} = {num1 + num2}</h2>"


@app.route('/handle_url')
def handle_params():
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    return f"<h2>{greeting}, {name}!</h2>"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
```

## URL Routes

### 1. Home Route

- **URL**: `http://127.0.0.1:5000/`
- **Function**: `index()`
- **Response**: Displays "Hello, World!" in H1 heading

### 2. Static Route

- **URL**: `http://127.0.0.1:5000/about`
- **Function**: `about()`
- **Response**: Displays "About Page" in H2 heading

### 3. Dynamic Route with String Parameter

- **URL**: `http://127.0.0.1:5000/user/<username>`
- **Function**: `user(username)`
- **Example**: `http://127.0.0.1:5000/user/John`
- **Response**: Displays "User: John" in H2 heading

### 4. Dynamic Route with Integer Parameters

- **URL**: `http://127.0.0.1:5000/add/<int:num1>/<int:num2>`
- **Function**: `add(num1, num2)`
- **Example**: `http://127.0.0.1:5000/add/5/3`
- **Response**: Displays "5 + 3 = 8" in H2 heading

### 5. Query Parameter Handling

- **URL**: `http://127.0.0.1:5000/handle_url?name=Mike&greeting=Hello`
- **Function**: `handle_params()`
- **Parameters**:
    - `name`: User's name
    - `greeting`: Greeting message
- **Response**: Displays "Hello, Mike!" in H2 heading

## URL Components

### Route Types

- **Static Routes**: Fixed URLs (`/`, `/about`)
- **Dynamic Routes**: URLs with variable parts (`/user/<username>`)
- **Typed Routes**: Variables with specific types (`/add/<int:num1>/<int:num2>`)

### Query Parameters

- Accessed via `request.args.get()`
- Format: `?key1=value1&key2=value2`
- Example: `?name=Mike&greeting=Hello`
