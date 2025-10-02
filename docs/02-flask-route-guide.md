# Flask URL Routing Documentation

## Overview

This document provides a general guide to URL routing in Flask. The current application (`app.py`) utilizes basic static routes.

## URL Routes in Flask

Flask uses the `@app.route()` decorator to bind functions to URLs.

### Static Routes

Static routes are fixed URLs that do not change.

- **Example**: `@app.route('/about')`
- **Usage**: Ideal for pages like "Home", "About", "Contact".

### Dynamic Routes

Dynamic routes allow variable parts in the URL. These variables can be passed as arguments to the view function.

- **Example**: `@app.route('/user/<username>')`
- **Type Converters**: You can specify type converters for dynamic parts, such as `<int:id>`, `<string:name>`, `<float:value>`, `<path:filepath>`, `<uuid:id>`.
  - **Example**: `@app.route('/post/<int:post_id>')`

### Query Parameters

Query parameters are appended to the URL after a question mark (`?`) and are used to pass additional, optional data.

- **Example**: `http://127.0.0.1:5000/search?query=flask&page=1`
- **Accessing Parameters**: In Flask, query parameters are accessed via `request.args.get('parameter_name')`.
  - **Example**: `search_query = request.args.get('query')`

## Current Application Routes

The `app.py` in this project currently implements two static routes:

- `/`: The homepage.
- `/about`: The about page.
