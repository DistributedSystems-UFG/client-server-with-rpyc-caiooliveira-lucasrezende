import rpyc
from constRPYC import *

class Client:
    conn = rpyc.connect(SERVER, PORT)

    def append(self, data):
        return self.conn.root.exposed_append(data)

    def get_value(self):
        return self.conn.root.exposed_value()

    def search(self, value):
        return self.conn.root.exposed_search(value)

    def remove(self, value):
        return self.conn.root.exposed_remove(value)

    def insert(self, index, value):
        return self.conn.root.exposed_insert(index, value)

    def sort(self):
        return self.conn.root.exposed_sort()

if _name_ == "_main_":
    client = Client()
    client.append(5)
    client.append(3)
    client.append(8)
    print("Original value:", client.get_value())

    print("Search 5:", client.search(5))
    print("Search 7:", client.search(7))

    client.remove(3)
    print("After removal:", client.get_value())

    client.insert(1, 4)
    print("After insertion:", client.get_value())

    client.sort()
    print("After sorting:", client.get_value())
