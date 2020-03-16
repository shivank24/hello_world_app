import unittest
import app


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World !')

    def test_hello_hello(self):
        rv = self.app.get('/hello')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World !')

    def test_hello_user(self):
        name = 'User'
        rv = self.app.get('/hello/%s' % name)
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, bytearray('Hello {} !'.format(name), 'utf-8'))


if __name__ == '__main__':
    unittest.main()

