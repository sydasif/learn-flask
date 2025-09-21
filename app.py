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
