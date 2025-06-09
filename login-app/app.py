from flask import Flask, jsonify
import database

app = Flask(__name__)
users = []

@app.route("/register/<username>/<password>")
def register(username, password):
    user = database.insert_user(username, password)
    if user:
        return jsonify(user)
    return jsonify({"message": "Username already exists"})

@app.route("/login/<username>/<password>")
def login(username, password):
    if database.login_user(username, password):
        return "shexvedi"
    return "NOT FOUND"

@app.route("/users")
def get_users():
    return jsonify(database.get_all_users())

@app.route("/users/<int:id>")
def get_user(id):
    user = database.get_user_by_id(id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"})

@app.route("/delete/<int:id>")
def delete_user(id):
    if database.delete_user_by_id(id):
        return "success"
    return "Not found"

@app.route("/update/<int:id>/<username>")
def update_username(id, username):
    if database.update_username_by_id(id, username):
        return "Username updated"
    return "Not Found"

if __name__ == "__main__":
    app.run(debug=True)
