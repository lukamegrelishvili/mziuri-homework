from flask import Flask, render_template, url_for, request, redirect
from user import User

app = Flask(__name__)

users = []

@app.route("/")
def main_page():

    user_data = [{"fullname": user.fullname, "email": user.email} for user in users]
    return render_template("main.html", users=user_data)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form["user_fullname"]
        email = request.form["user_email"]
        password = request.form["user_password"]
        user = User(fullname,email,password)
        users.append(user)
        return redirect(url_for("main_page"))
    return render_template("register.html")
        

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        for user in users:
            if email == user.email and password == user.password:
                return redirect(url_for('main_page'))

    return render_template("login.html")

if "__main__" == __name__:
    app.run(debug=True)



