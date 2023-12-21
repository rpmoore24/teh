'''
Get a specific league

This endpoint retrieves a specific league.

HTTP Request
GET https://api.sleeper.app/v1/league/<league_id>

URL Parameters
Parameter   Description
league_id   The ID of the league to retrieve

'''

import os
from common.Sleeper import Sleeper

## Class representing league
class League(Sleeper):
   
   ## Constructor
   # @param leagueId   The int for league ID
   def __init__(self, leagueId):
      file = os.path.join(__file__, '..', '..', 'data', 'league.json')
      request = 'https://api.sleeper.app/v1/league/{}'.format(leagueId)
      self.download(file, request)
