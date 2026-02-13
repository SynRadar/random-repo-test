import os
import sqlite3
import subprocess
import hashlib
import pickle
from flask import Flask, request

app = Flask(__name__)

SECRET_KEY = "super_secret_password_123"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login successful"
    return "Invalid credentials"

@app.route("/ping")
def ping():
    ip = request.args.get("ip")
    result = subprocess.check_output(f"ping -c 1 {ip}", shell=True)
    return result

@app.route("/load", methods=["POST"])
def load_data():
    data = request.data
    obj = pickle.loads(data)  
    return str(obj)

@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open(f"./files/{filename}", "r") as f:
        return f.read()

@app.route("/calculate")
def calculate():
    expression = request.args.get("expr")
    return str(eval(expression))

print("sdfhhjklfghj")

if __name__ == "__main__":
    app.run(debug=True)
