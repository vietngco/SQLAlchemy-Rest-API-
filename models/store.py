import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores' # tell which table it should go to
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    # items = db.relationship('ItemModel', lazy = 'dynamic') # list of itemModel object
    items = db.relationship('ItemModel', ) # list of itemModel object

    def __init__(self, name):
        self.name = name

    def json(self): # will be slower because must look at the table every time we call json(), but make the store creation faster
        return {'name': self.name, 'items': list(map(lambda x : x.json(), self.items))}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first() # SELECT * from items where name = name -> return an object of the first row (auto and limit to 1)

    def save_to_db(self):
        # useful for both update and insert method
        db.session.add(self) # session is collection of row object in  db
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()