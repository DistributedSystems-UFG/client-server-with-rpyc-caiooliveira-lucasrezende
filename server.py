import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value.append(data)
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_search(self, value):
        return value in self.value

    def exposed_remove(self, value):
        if value in self.value:
            self.value.remove(value)
        return self.value

    def exposed_insert(self, index, value):
        self.value.insert(index, value)
        return self.value

    def exposed_sort(self):
        self.value.sort()
        return self.value

if _name_ == "_main_":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()
