import falcon
import falcon.testing as testing
import mysql
import json

import things

class TestThings(testing.TestBase):
    def before(self):
        t = things.Things()
        self.api.add_route('/things', t)

    def test_ok(self):
        body = self.simulate_request('/things', decode='utf-8')
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        b = json.loads(body)
        self.assertEqual(b[0]['Name'], 'Aruba')
