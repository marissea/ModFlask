from flask import Flask, url_for, render_template, request
app = Flask(__name__)

addon_names = ['Wahaha', 'Addon2', 'Addon3']


@app.route('/')
def hello_world():
    return render_template("main.html" , addon_names=addon_names)

with app.test_request_context():
    anna =  url_for('static', filename='style.css')

@app.route('/ajax.html')
def popup():
    return request.args.get("name")

if __name__ == '__main__':
    app.run()
