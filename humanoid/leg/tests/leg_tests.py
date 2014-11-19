from unittest import TestCase
from salvius import app


class AnkleLegsTests(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_leg(self):
        url = "/api/robot/body/legs/"
        response = self.app.get(url, follow_redirects=True)

        self.assertFalse("null" in response.data.decode())
        self.assertTrue("hip" in response.data.decode())
        self.assertTrue("knee" in response.data.decode())
        self.assertTrue("ankle" in response.data.decode())
        self.assertTrue("href" in response.data.decode())
        self.assertTrue("id" in response.data.decode())


class AnkleLegTests(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_leg(self):
        url = "/api/robot/body/legs/0/"
        response = self.app.get(url, follow_redirects=True)

        self.assertFalse("null" in response.data.decode())
        self.assertTrue("hip" in response.data.decode())
        self.assertTrue("knee" in response.data.decode())
        self.assertTrue("ankle" in response.data.decode())
        self.assertTrue("href" in response.data.decode())
        self.assertTrue("id" in response.data.decode())

    def test_cannot_get_leg_that_does_not_exits(self):
        url = "/api/robot/body/legs/4200/"
        response = self.app.get(url, follow_redirects=True)

        self.assertFalse("null" in response.data.decode())
        self.assertFalse("href" in response.data.decode())
        self.assertFalse("knee" in response.data.decode())
        self.assertTrue("message" in response.data.decode())