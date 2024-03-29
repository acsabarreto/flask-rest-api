from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()
        return {'message': 'Store not found!'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'mesage': "A store with the name '{}' already exists!"
                    .format(name)}, 400

        store = StoreModel(name)

        store.save_to_db()

        return store.json(), 201

    def delete(self, name):

        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
            return {'message': 'Store deleted successfully!'}

        return {'message': 'Store not found!'}, 404


class StoreList(Resource):

    def get(self):

        stores = [store.json() for store in StoreModel.query.all()]

        return {'stores': stores}
