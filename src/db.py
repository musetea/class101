from http import client
from pymongo import MongoClient
from pymongo.cursor import CursorType

class DBHanlder:
    #client = None
    def __init__(self, host:str="localhost", port:str = 27017):
        self.host = host
        self.port = port
        self.client = MongoClient(host, int(port))
        print(self.client)
        print(self.client.list_database_names())


    # INSERT
    def insert_item_one(self, data, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].insert_one(data).inserted_id
        return result
    def insert_item_many(self, datas, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].insert_many(datas).inserted_ids
        return result

    # FIND 
    def find_item_one(self, condition=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].find_one(condition, {"_id": False})
        return result
    def find_item(self, condition=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].find(
            condition, {"_id": False}, 
            no_cursor_timeout=True, 
            cursor_type=CursorType.EXHAUST)
        return result

    # UPDATE 
    def update_item_one(self, condition=None, update_value=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].update_one(
            filter=condition, 
            update=update_value)
        return result
    def update_item_many(self, condition=None, update_value=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].update_many(
            filter=condition, 
            update=update_value)
        return result

    # DELETE 
    def delete_item_one(self, condition=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].delete_one(condition)
        return result
    def delete_item_many(self, condition=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].delete_many(condition)
        return result

    # TEXT SEARCH
    def text_search(self, text=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].find({"$text": {"$search": text}})
        return result
    


    def get_db(self, db:str):
        return self.client[db]

    def get_collection(self, db, collection:str):
        return db[collection]

    def get_collection2(self, db:str, collection:str):
        print(db, collection)
        return self.client[db][collection]

    def client(self):
        return self.client


mongo = DBHanlder()
