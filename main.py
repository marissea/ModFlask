from flask import Flask, url_for, render_template
app = Flask(__name__)

anna = ""


@app.route('/')
def hello_world():
    return render_template("main.html")

with app.test_request_context():
    anna =  url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run()
