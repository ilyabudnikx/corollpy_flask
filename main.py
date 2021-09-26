from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    a = str(100)
    return a

if __name__ == "__main__":
    app.run(debug=True)