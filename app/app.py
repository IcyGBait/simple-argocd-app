from flask import Flask, jsonify
import os
import time
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "Hello from simpleapp",
        "host": socket.gethostname(),
        "timestamp": int(time.time())
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
