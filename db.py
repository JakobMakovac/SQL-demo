from cs50 import SQL

class DB:
    def __init__(self, path_to_db):
        self.db = SQL('sqlite:///' + path_to_db)

    def read(self):
        '''Example method for db interaction'''
        rows = self.db.execute('SELECT * FROM users')
        return rows