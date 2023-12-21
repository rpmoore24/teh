'''
Getting users in a league

This endpoint retrieves all users in a league.

This also includes each user's display_name, avatar, and their metadata which sometimes includes a nickname they gave their team.

HTTP Request
GET https://api.sleeper.app/v1/league/<league_id>/users

URL Parameters
Parameter   Description
league_id   The ID of the league to retrieve rosters from
'''

import os
from common.Sleeper import Sleeper

## Class representing users
class Users(Sleeper):
   
   ## Constructor
   # @param leagueId   The int for user ID
   def __init__(self, leagueId):
      self.users = []
      file = os.path.join(__file__, '..', '..', 'data', 'users.json')
      request = 'https://api.sleeper.app/v1/league/{}/users'.format(leagueId)
      self.download(file, request)

   ## Gets user given ID
   # @param ownerId   The int for user ID
   # @return          The dict with user data
   def getUser(self, userId):
      for user in self.data:
         if user['user_id'] == userId:
            return user