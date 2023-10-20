class Database:
    def __init__(self):
        self.data = {}
        self.transactions = []

    def set(self, name, value):
        self.data[name] = value

    def get(self, name):
        return self.data.get(name, "NULL")

    def unset(self, name):
        if name in self.data:
            del self.data[name]

    def count(self, value):
        count = list(self.data.values()).count(value)
        return count

    def find(self, value):
        found_vars = [key for key, val in self.data.items() if val == value]
        return " ".join(found_vars)

    def begin(self):
        self.transactions.append(self.data.copy())

    def rollback(self):
        if self.transactions:
            self.data = self.transactions.pop()

    def commit(self):
        self.transactions = []
