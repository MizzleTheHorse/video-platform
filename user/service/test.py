import unittest
from unittest.mock import patch
from sqlalchemy.orm import Session
from your_module import DatabaseInterface

class DatabaseInterfaceTest(unittest.TestCase):
    @patch('your_module.Session')
    def test_get_user_existing_user(self, mock_session):
        # Create a mock user object
        mock_user = User(user_id=1, name='John Doe', email='john@example.com', hashed_password='hashed_password')
        
        # Configure the mock session to return the mock user object
        mock_session.return_value.query.return_value.filter.return_value.first.return_value = mock_user
        
        # Create an instance of DatabaseInterface
        db_interface = DatabaseInterface()
        
        # Call the method being tested
        user = db_interface.get_user('john@example.com')
        
        # Assert that the method returns the expected user object
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.hashed_password, 'hashed_password')
        
    @patch('your_module.Session')
    def test_get_user_nonexistent_user(self, mock_session):
        # Configure the mock session to return None (user does not exist)
        mock_session.return_value.query.return_value.filter.return_value.first.return_value = None
        
        # Create an instance of DatabaseInterface
        db_interface = DatabaseInterface()
        
        # Call the method being tested
        user = db_interface.get_user('nonexistent@example.com')
        
        # Assert that the method returns None
        self.assertIsNone(user)
        
    @patch('your_module.Session')
    def test_get_user_by_id_existing_user(self, mock_session):
        # Create a mock user object
        mock_user = User(user_id=1, name='John Doe', email='john@example.com', hashed_password='hashed_password')
        
        # Configure the mock session to return the mock user object
        mock_session.return_value.query.return_value.filter.return_value.first.return_value = mock_user
        
        # Create an instance of DatabaseInterface
        db_interface = DatabaseInterface()
        
        # Call the method being tested
        user = db_interface.get_user_by_id(1)
        
        # Assert that the method returns the expected user object
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.hashed_password, 'hashed_password')
        
    @patch('your_module.Session')
    def test_get_user_by_id_nonexistent_user(self, mock_session):
        # Configure the mock session to return None (user does not exist)
        mock_session.return_value.query.return_value.filter.return_value.first.return_value = None
        
        # Create an instance of DatabaseInterface
        db_interface = DatabaseInterface()
        
        # Call the method being tested
        user = db_interface.get_user_by_id(2)
        
        # Assert that the method returns None
        self.assertIsNone(user)
        
    @patch('your_module.Session')
    def test_post_user_new_user(self, mock_session):
        # Configure the mock session to return None (user does not exist)
        mock_session.return_value.query.return_value.filter.return_value.first.return_value = None
        
        # Create a mock user object
        mock_user = User(user_id=1, name='John Doe', email='john@example.com', hashed_password='hashed_password')
        
        # Configure the mock session to return the mock user object
        mock_session.return_value.add.return_value.commit.return_value = None
        mock_session.return_value.query.return_value.filter.return_value.first.return_value = mock_user
        
        # Create an instance of DatabaseInterface
        db_interface = DatabaseInterface()
        
        # Call the method being tested
        user = db_interface.post_user('John Doe', 'john@example.com', 'hashed_password')
        
        # Assert that the method returns the expected user object
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.hashed_password, 'hashed_password')
        
    @patch('your_module.Session')
    def test_post_user_existing_user(self, mock_session):
        # Create a mock user object
        mock_user = User(user_id=1, name='John Doe', email='john@example.com', hashed_password='hashed_password')
        
        # Configure the mock session to return the mock user object
        mock_session.return_value.query.return_value.filter.return_value.first.return_value = mock_user
        
        # Create an instance of DatabaseInterface
        db_interface = DatabaseInterface()
        
        # Call the method being tested
        user = db_interface.post_user('John Doe', 'john@example.com', 'hashed_password')
        
        # Assert that the method returns None (user already exists)
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
