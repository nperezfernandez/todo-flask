# While I personalized the todolist, I follwoed the tutorial susgested in the homework enterily and so most of the code was obtained from there
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# These are an example of what is needed for the Rendering Templetes Concept
from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

# This is an example of the concpet of Simplified SQL/Data Base Interaction
# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
#This is an example of a Post request
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

#This is an example of a HTTP request
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

#This is an example of the Routing Concept
@app.route("/")
def home():
    todo_list = Todo.query.all()
    #this is an example of the concept of rendering a Template
    return render_template("base.html", todo_list=todo_list)

    # Aika Aldayarova gave me these two lines of code to help Flask know where to pull informaiton from to avoid having issues creating the app
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
