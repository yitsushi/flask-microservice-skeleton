import os
import unittest
from example_service import app


class TestMain(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        if 'BASEDIR' not in app.config:
            app.config['BASEDIR'] = os.path.dirname(__file__)
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        #                                         os.path.join(app.config['BASEDIR'], 'test.db')
        self.app = app.test_client()
        # db.drop_all()
        # db.create_all()

        # Disable sending emails during unit testing
        # mail.init_app(app)
        self.assertEqual(app.debug, False)

    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()