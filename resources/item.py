from flask import Flask
from flask_restful import Resource,  reqparse
from flask_jwt import JWT, jwt_required
import sqlite3

from models.item import ItemModel

class Item(Resource): # only work with indiviual item
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
        type = float,
        required= True,
        help='this field cannot be left blank'
    )
    parser.add_argument('store_id', 
        type = int,
        required= True,
        help='every items need store_id '
    )
    # @jwt_required() # auth
    def get(self,name): 
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not Found'}, 404
    
    def post(self, name): # post a new item, if exist cancel the request
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        new_item = ItemModel(name, **data)
        if item is None:  
            try: 
                new_item.save_to_db()
                return new_item.json()
            except:
                return {'message': "An error occur when inserting the item"}, 500
        else:
            return {'message': 'item already exist'}, 400
            
    def delete(self, name):
        item = ItemModel.find_by_name(name) # return an object
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}, 200
        else:
            return {'message': 'Item NOT found'}, 400

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:  
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.save_to_db()
        return item.json()

    
class ItemList(Resource): # work with items list
    def get(self):
        # return {'items': [item.json() for item in ItemModel.query.all()]}
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}





