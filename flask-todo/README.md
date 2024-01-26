```console
python3 -m venv venv
. venv/bin/activate

pip install Flask
pip install Flask-SQLAlchemy

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
## About Flask

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself.

## Flask Features 

###  Routing

Flask makes it easy to connect URL paths to Python functions, which is essential for defining the endpoints for creating, updating, deleting, and viewing to-do tasks.

```python
@app.route('/')
def index():
    #show all todo
    todo_list =Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    #add new item
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))
```

### Templates

Flask's integration with Jinja2 templates allows for dynamic content generation, making it straightforward to display tasks, input forms, and other UI components.

```html
    {% for todo in todo_list %}
    <div class="ui segment">
        <p class="ui big header">{{todo.id }} | {{ todo.title }}</p>

        {% if todo.complete == False %}
        <span class="ui gray label">Not Complete</span>
        {% else %}
        <span class="ui green label">Completed</span>
        {% endif %}

        <a class="ui blue button" href="/update/{{ todo.id }}">Update</a>
        <a class="ui red button" href="/delete/{{ todo.id }}">Delete</a>
    </div>
    {% endfor %}
```

### Forms and Validation

Using Flask-WTF, Flask's integration with WTForms, simplifies form handling and validation, ensuring data integrity modules.

###  Database Integration

Flask's flexibility allows for easy integration with various database solutions, from simple SQLite databases to more robust solutions like PostgreSQL.

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
db = SQLAlchemy(app)
```

###  RESTful API Development

Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs. It encourages best practices with minimal setup.

For more detailed information about Flask and its features, visit the [official Flask documentation](https://flask.palletsprojects.com/).
