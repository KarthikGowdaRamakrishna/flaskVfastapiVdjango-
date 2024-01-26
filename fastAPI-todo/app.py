from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

import models 
from database import SessionLocal, engine


#create all database tables
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")
app = FastAPI()

# helper function to access the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
#"get_db" passed to home function has a dependence(so if the db can't be accessed the request to this route will throw a error: this handled by FastAPI)
def home(request: Request, db: Session = Depends(get_db)): 
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "todo_list": todos})

@app.post("/add")
# here is the typing!! we get the title argument from the 'form' tag and type it to be a string type 
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)): 
    new_todo = models.Todo(title=title)                                              
    db.add(new_todo)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)



@app.get("/update/{todo_id}")
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get("/delete/{todo_id}")
def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)