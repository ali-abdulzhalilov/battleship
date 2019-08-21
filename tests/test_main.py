import unittest

from app import create_app

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client(self)

    def tearDown(self):
        with self.app.app_context():
            pass

    def test_helloworld(self):
        res = self.client.get('/', content_type='html/text')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, b'Hello, World!')

if __name__=='__main__':
    unittest.main()
