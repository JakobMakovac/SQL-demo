from cs50 import SQL

class DB:
    def __init__(self, path_to_db):
        self.db = SQL('sqlite:///' + path_to_db)

    def read(self):
        '''Example method for db interaction'''
        rows = self.db.execute('SELECT * FROM users')
        return rows
    
    def add(self, username, password):
        self.db.execute("INSERT INTO users (username, password) VALUES (?,?)", username, password)

    def compare(self, username, password):
        try:
            users = self.db.execute("SELECT username, password FROM users WHERE username = ?", username)
            slovar = users[0]
            if password == slovar["password"]:
                return True
        except:
            return False    
        
        