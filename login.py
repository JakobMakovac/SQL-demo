from db import DB

db_path = 'shows.db'
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
        print('Register not implemented yet.')
        return
    
    def login(self):
        print('Login not implemented yet.')
        return
    
    def rename(self):
        print('Rename not implemented yet.')
        return
    
    def logout(self):
        print('Logout not implemented yet.')
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