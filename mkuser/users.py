import os
import bcrypt
import getpass


class UserOps:    
    def __init__(self):
        '''
        Prompts the user for a username and password.
        '''
        self.salt = bcrypt.gensalt(log_rounds = 15)
        self.username = input("Please enter a username: ")
        self.password = bcrypt.hashpw(getpass.getpass(prompt='Please enter a password: '), self.salt)

        
    def make_user(self):
        '''
        Authenticates the user to the session username and password, then
        adds the users username and password to data_file via a call to make_data_file().
        '''
                
        # Verification of credentials
        while input("Please enter your username: ") == self.username:
            while bcrypt.checkpw(getpass.getpass(prompt="Please enter your password: "), self.password):
                print("Accepted")
                self.make_data_file()
                return True
            else:
                print("Error, password does not match user")
        else:
            print("Error, username not found")
            self.make_user()

    def pwd_hash(self, password):
        # Simple helper function for make_data_file
        return bcrypt.hashpw(password, self.salt)
            
    def make_data_file(self):
        '''
        Creates a new text file for the user data or modifies an existing data file.
        '''
        
        # Sets the data file path and the folder it is in.
        data_path = os.getcwd() + "/data/"
        data_file = data_path + "data.txt"
    
        # Checks if file exists or higher level folder and makes/appends user data.
        # Else just makes new file and corresponding folder.
        if os.path.isfile(data_file):
            open_filemode = 'a'
        else:
            open_filemode = 'w'
            if not os.path.isdir(data_path):
                os.mkdir(data_path)

        with open(data_file, open_filemode) as output:
            output.write(self.username + ' : ' + self.password + '\n')


def initiate():
    '''
    This starts the whole process
    '''
    while True:
        try:
            if int(input('Welcome to my piece of junk! \nIf you want to make a new user account, press 1. \nPress any other key to exit: ')) == 1:
                UserOps().make_user()
                break
            else:
                quit()
        except ValueError:
            quit()


# So initiate() is not called when the test file is run
if __name__ == '__main__':
    initiate()
