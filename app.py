import falcon

import mysql
import things

api = application = falcon.API()

things = things.Things()
api.add_route('/things', things)
