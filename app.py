from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    done = db.Column(db.Boolean, nullable=False)


class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'done')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/add-todo', methods=['POST'])
def add_todo():
    title = request.json['title']
    done = request.json['done']

    new_todo = Todo(title=title, done=done)
    db.session.add(new_todo)
    db.session.commit()
    todo = Todo.query.get(new_todo.id)

    return todo_schema.jsonify(todo)


if __name__ == "__main__":
    app.debug = True
    app.run()
