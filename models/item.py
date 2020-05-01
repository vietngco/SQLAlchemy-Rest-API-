from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key = True) # automately created
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, "store_id": self.store_id}

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