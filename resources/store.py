from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    
    def get(self, name):
        store =StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'store not foound'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store: 
            return {'message': f'Store {name} already exist'}
        else:
            store = StoreModel(name)
            store.save_to_db()
            return store.json(), 201 # created

    def delete(self, name):
        store =StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'store deleted'}, 200
        else: 
            return {'message': 'store not found'}

class StoreList(Resource):
    def get(self):
        return {'Stores': list(map(lambda x: x.json(), StoreModel.query.all()))}

    
