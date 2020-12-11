# EPIC
Create a todo app with Flask.
1. Create the app as a monolithic flask app
2. Refactor the app to be a microservice via Flask and React

All with the mindset of testing first.

## Acceptance Criteria

* Show users a list of current todos
* Users can Add a todo
* Users can Mark a todo complete
* Users can delete a todo
* Users can delete all todos marked complete
* Data to show for each todo
  1. Title
  2. Complete

## Technical Design

TodoModel:
```
{
  "_id": String,
  "title": String,
  "done": Boolean
}
```