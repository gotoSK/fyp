import unittest
from app import app, db  # Import Flask app and database
from models import User  # Import User model
from flask import url_for
from werkzeug.security import generate_password_hash


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client and database"""
        app.config['TESTING'] = True
        # Use in-memory database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        # Create a test user
        user = User(username="testuser", email="test@example.com",
                    password_hash=generate_password_hash("testpassword"))
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """Clean up after each test"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login_success(self):
        """Test login with correct credentials"""
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        # Check if "Welcome" is in response (or dashboard redirect)
        # Adjust if your route differs
        self.assertIn(b"dashboard", response.data)

    def test_login_failure(self):
        """Test login with incorrect credentials"""
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'wrongpassword'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invalid username or password",
                      response.data)  # Error message expected


if __name__ == '__main__':
    unittest.main()
