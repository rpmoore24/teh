'''
Getting rosters in a league

This endpoint retrieves all rosters in a league.

HTTP Request
GET https://api.sleeper.app/v1/league/<league_id>/rosters

URL Parameters
Parameter   Description
league_id   The ID of the league to retrieve rosters from
'''

import os
from common.Sleeper import Sleeper

## Class representing rosters
class Rosters(Sleeper):
   
   ## Constructor
   # @param leagueId   The int for league ID
   def __init__(self, leagueId):
      self.rosters = []
      
      file = os.path.join(__file__, '..', '..', 'data', 'rosters.json')
      request = 'https://api.sleeper.app/v1/league/{}/rosters'.format(leagueId)
      self.download(file, request)
            
   ## Gets roster given ID
   # @param rosterId   The int for roster ID
   # @return           The dict with roster data
   def getRoster(self, rosterId):
      for roster in self.data:
         if roster['roster_id'] == rosterId:
            return roster