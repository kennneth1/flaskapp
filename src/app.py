from flask import flask

app = Flask(__name__)

@app.route('/home')
def home_page():
    return "rendered on browser"

if __name__ == "__main__":
    app.run(debug=True)