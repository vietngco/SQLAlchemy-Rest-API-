from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create():
    db.create_all() #create the database