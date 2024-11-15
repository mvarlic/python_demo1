import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

try:
    APP_PORT = int(os.getenv("APP_PORT", 80))
except ValueError:
    raise ValueError("El puerto especificado en APP_PORT no es un número válido.")

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World 3!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)

    