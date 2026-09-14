class Database:
    def __init__(self):
        self._store={}

    def set(self,key,value):
        self._store[key]=value
        return True

    def get(self,key):
        return self._store.get(key)

    def delete(self,key):
        if key in self._store:
            del self._store[key]
            return 1
        return 0
    def exists(self,key):
        if key in self._store :
            return 1
        else :0