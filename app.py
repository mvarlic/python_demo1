import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

APP_PORT = os.getenv("APP_PORT")
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World 3!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)

    