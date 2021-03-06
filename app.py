import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URI')
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('TESTING_DATABASE_URI')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_test.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    try:
        title = request.json['title']
        done = request.json['done']

        new_todo = Todo(title=title, done=done)
        db.session.add(new_todo)
        db.session.commit()
        todo = Todo.query.get(new_todo.id)

        return todo_schema.jsonify(todo)
    except KeyError as keyName:
        return jsonify(message=f'KeyError: I was looking for {keyName}')


@app.route('/api/v1/get-all-todos', methods=['GET'])
def get_all_todos():
    all_todos = Todo.query.all()
    result = todos_schema.dump(all_todos)
    return jsonify(result)


@app.route('/api/v1/mark-complete', methods=["PUT"])
def mark_complete():
    try:
        todo = Todo.query.get(request.json['id'])
        if todo:
            todo.done = request.json['done']
            db.session.commit()
            return todo_schema.jsonify(todo)
        else:
            return jsonify(message=f'Sorry, no todo with that id exists')
    except KeyError as keyName:
        return jsonify(message=f'KeyError: I was looking for {keyName}')

    # OR

    # try:
    #     todo = Todo.query.get(request.json['id'])
    #     todo.done = request.json['done']
    #     db.session.commit()
    #     return todo_schema.jsonify(todo)
    # except KeyError as error:
    #     return jsonify(message=f'KeyError: I was looking for {error}')
    # except AttributeError:
    #     return jsonify(message=f'Sorry, no todo with that id exists')


@app.route('/api/v1/delete-todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify(message=f'Deleted Todo with id of {todo_id}')
    else:
        return jsonify(message=f'Sorry, no todo with that id exists')


@app.route('/api/v1/delete-all-todos-marked-complete', methods=["DELETE"])
def delete_all_todos_marked_complete():
    completed_todos_list = Todo.query.filter_by(done=True).all()
    if completed_todos_list:
        for todo in completed_todos_list:
            db.session.delete(todo)
        db.session.commit()
        return jsonify(message="Todos Deleted")
    else:
        return jsonify(message="No todos are marked complete")


if __name__ == "__main__":
    app.debug = True
    app.run()
