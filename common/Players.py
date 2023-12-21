import os
from common.Sleeper import Sleeper

## Class representing players
class Players(Sleeper):
   
   ## Constructor
   def __init__(self):
      self.players = []
      
      file = os.path.join(__file__, '..', '..', 'data', 'players.json')
      request = 'https://api.sleeper.app/v1/players/nfl'
      self.download(file, request)