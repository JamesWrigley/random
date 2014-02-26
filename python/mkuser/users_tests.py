# Test file for users script
import unittest
from unittest.mock import patch
import shutil
import users
import os


data_path = os.getcwd() + "/data/"
data_file = data_path + "data.txt"


class MakeUserFilesTests(unittest.TestCase):
    '''
    This case tests make_data_file. I think I should get rid of it since I want make_data_file
    to be a private method.
    '''

    def tearDown(self):
        shutil.rmtree(data_path)
        if os.path.isdir(os.getcwd() + '/__pycache__'): shutil.rmtree(os.getcwd() + '/__pycache__')
        
    def test_make_data_for_james(self):
        '''
        Tests whether the script can create a new data file and write the user info to it.
        This case focuses on writing to a new file, not appending to an existing one.
        '''
        
        self.username = 'james'
        self.password = 'blah'

        users.UserOps.make_data_file(self)        
        self.assertTrue(os.path.isfile(data_file))
        with open(data_file) as data:
            self.open_data_file = data.read()
        self.assertIn((self.username + ' : ' + self.password), self.open_data_file)

        
    def test_make_data_for_hurr(self):
        '''
        Tests whether the script can append user data to an existing data file.
        '''
        def env_setup(self):
            '''
            Sets up an environment for test_make_data_for_hurr by calling make_data_file
            '''
            self.username = 'hurr_setup'
            self.password = 'durr_setup'
            users.UserOps.make_data_file(self)
            
        self.username = 'Hurrr'
        self.password = 'Durrr'
        env_setup(self)
        
        with open(data_file) as data:
            self.open_data_file = data.read()

        users.UserOps.make_data_file(self)
        self.assertIn((self.username + ' : ' + self.password), self.open_data_file)

        
## class InteractiveTests(unittest.TestCase):
##     '''
##     Tests make_user, and thereby make_data_file. Must try and integrate these steps in the future.
##     '''
    
##     def test_straighforward_james(self):
##         self.username = 'james'
##         self.password = 'obfuscate'
##         users.UserOps.make_user(self).input = lambda: 'james'
##         self.assertTrue('james : blah' in data_file)


if __name__ == '__main__':
    unittest.main()
