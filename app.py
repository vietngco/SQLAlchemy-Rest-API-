from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
import sqlite3

from resources.user import UserRegister, USERS
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # shutdown the flask sqlalchemy tracker, but not sqlachemy tracker
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db' # tell the server where our database is
app.secret_key = 'viet'
api = Api(app)

@app.before_first_request
def create():
    db.create_all() # create the tables first if none table exists, skip the module create_table.py
    
jwt = JWT(app, authenticate, identity) # /aut+h



####
api.add_resource(Item,'/item/<string:name>') # add a para
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(USERS, '/users')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# /auth
if (__name__) == '__main__':
    from db import db
    db.init_app(app) # register the app with alchemy database
    app.run(port=5000)

