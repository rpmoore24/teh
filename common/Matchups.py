'''
Getting matchups in a league

This endpoint retrieves all matchups in a league for a given week. Each object in the list represents one team. The two teams with the same matchup_id match up against each other.

The starters is in an ordered list of player_ids, and players is a list of all player_ids in this matchup.

The bench can be deduced by removing the starters from the players field.

HTTP Request
GET https://api.sleeper.app/v1/league/<league_id>/matchups/<week>

URL Parameters
Parameter   Description
league_id   The ID of the league to retrieve matchups from
week   The week these matchups take place
'''

import os
from common.Sleeper import Sleeper

## Class representing matchups for a given week
class Matchups(Sleeper):
   
   # Constructor
   # @param leagueId   The int for league ID
   # @param week       The int for week
   def __init__(self, leagueId, week):
      self.week     = week
      self.matchups = []
      
      file = os.path.join(__file__, '..', '..', 'data', 'matchups_week{}.json'.format(week))
      request = 'https://api.sleeper.app/v1/league/{}/matchups/{}'.format(leagueId, week)
      self.download(file, request)
         
   ## Gets weekly average
   # @return   The float for average
   def getAverage(self):
      total = 0 
      for matchup in self.data:
         total += matchup['points']
      return total/len(self.data)
      
   ## Gets total points for a given team
   # @param rosterId   The int for roster ID
   # @return           The float for points scored
   def getPoints(self, rosterId):
      for matchup in self.data:
         if matchup['roster_id'] == rosterId:
            return matchup['points']
            
   ## Determines optimal lineup
   # @param players   The dict for player data
   def setOptimumLineups(self, players):
      for matchup in self.data:
         lineup = {}
         x = sorted(matchup['players_points'].items(), key = lambda x:x[1], reverse = True)
         for player in x:
            if getattr(players, player[0])['position'] == 'QB' and 'QB' not in lineup.keys():
               lineup['QB'] = player[0]
            elif getattr(players, player[0])['position'] == 'RB' and 'RB1' not in lineup.keys():
               lineup['RB1'] = player[0]
            elif getattr(players, player[0])['position'] == 'RB' and 'RB2' not in lineup.keys():
               lineup['RB2'] = player[0]
            elif getattr(players, player[0])['position'] == 'WR' and 'WR1' not in lineup.keys():
               lineup['WR1'] = player[0]
            elif getattr(players, player[0])['position'] == 'WR' and 'WR2' not in lineup.keys():
               lineup['WR2'] = player[0]
            elif getattr(players, player[0])['position'] == 'TE' and 'TE' not in lineup.keys():
               lineup['TE'] = player[0]
            elif getattr(players, player[0])['position'] in ['RB', 'TE', 'WR'] and 'FLEX' not in lineup.keys():
               lineup['FLEX'] = player[0] 
            elif getattr(players, player[0])['position'] == 'K' and 'K' not in lineup.keys():
               lineup['K'] = player[0]
            elif getattr(players, player[0])['position'] == 'DEF' and 'DEF' not in lineup.keys():
               lineup['DEF'] = player[0]
         matchup['optimum'] = {position: matchup['players_points'][player] for position, player in lineup.items()}
         
   ## Gets head to head matchups   
   # @return   The list of tuples
   def getMatchups(self):
      ret = []
      for x in range(len(self.data)):
         matchup = self.data[x]
         for y in range(x + 1, len(self.data)):
            if self.data[y]['matchup_id'] == matchup['matchup_id']:
               ret.append((matchup, self.data[y]))
      return ret
