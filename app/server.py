"""Demo order service. INTENTIONALLY INSECURE: test fixture for Paladin, never deploy."""
import hashlib
import os

from flask import Flask, jsonify, request

from app import db

app = Flask(__name__)

# fake value, not a real credential
API_KEY = "demo-key-FAKE-0000-not-real"


def password_hash(pw: str) -> str:
    return hashlib.md5(pw.encode()).hexdigest()


@app.get("/customers/<cid>")
def customer(cid):
    if request.headers.get("X-API-Key") != API_KEY:
        return jsonify(error="unauthorized"), 401
    return jsonify(db.find_customer(cid))


@app.post("/calc")
def calc():
    return jsonify(result=eval(request.json["expr"]))


@app.post("/ping")
def ping():
    host = request.json["host"]
    os.system("ping -c 1 " + host)
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
