from db import DB

db_path = 'login.db'
db = DB(db_path)

class App:
    def __init__(self):
        self.active_user = None
        self.logged_in = False

    def get_active_user(self):
        return self.active_user
    
    def get_is_logged_in(self):
        return self.logged_in
    
    def register(self):
        username = input("Select your username:")
        password = input("Select your password:")
        db.add(username, password)
        self.main_menu()
        return
    
    def login(self):
        username = input("Username:")
        password = input("Password:")
        match = db.compare(username, password)
        if match == True:
            print("Succes!")
            self.logged_in = True
            self.active_user = username
            self.main_menu()
        else:
            try_again = input("Login unsuccesful. Want to try again?")
            if try_again == "yes":
                self.login()
            else:
                self.main_menu()
        
        return
    
    def rename(self):
        print('Rename not implemented yet.')
        return
    
    def logout(self):
        self.active_user = None
        self.logged_in = False
        self.main_menu()
        return

    def main_menu(self):
        # We print all the options for the user
        print('Welcome to our application. What do you want to do?')
        if self.logged_in:
            print('Currently logged in as ' + self.active_user)
            print('(C)hange username')
            print('Log(O)ut')
        print('(R)egister')
        print('(L)ogin')
        print('(Q)uit')

        # We ask what the user wants to do
        user_input = input('>>> ').lower()
        
        # We check the input and decide what to do
        if user_input == 'r':
            self.register()
        elif user_input == 'l':
            self.login()
        elif user_input == 'c':
            self.rename()
        elif user_input == 'o':
            self.logout()
        elif user_input == 'q':
            return

    def run(self):
        self.main_menu()

app = App()
app.run()