from flask import Flask, render_template, request, redirect, url_for
from database import read, init_db, create, delete, update 

app = Flask(__name__)

@app.route("/")
def main():
     data = read()
     return render_template("main.html", todos = data)

@app.route("/add", methods=["POST"])
def add_todo():
    todo_title = request.form["todo_title"]
    todo_text = request.form["todo_text"]
    create(todo_title, todo_text)
    return redirect(url_for("main"))

@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    delete(todo_id)
    return redirect(url_for("main"))

def update_todo(todo_id):
    new_title = request.form["todo_title"]
    new_text = request.form["todo_text"]
    update(todo_id, new_title, new_text)
    return redirect(url_for("main"))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
