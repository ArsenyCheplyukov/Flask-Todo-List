from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('main_template.html')

if __name__ == "__main__":
    app.run(debug=True)