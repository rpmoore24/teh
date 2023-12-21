import csv
from common.Matchups import Matchups
from common.Rosters import Rosters
from common.Users import Users

LEAGUE_ID =
START = 1 # week
END = 14 # week

rosters = Rosters(LEAGUE_ID)
users = Users(LEAGUE_ID)

wins = {}
season = []
for week in range(START, END + 1):
   matchups = Matchups(LEAGUE_ID, week)
   avg = matchups.getAverage()
   season.append(matchups)
   
   for team in matchups.data:
      if team['roster_id'] not in wins.keys():
         wins[team['roster_id']] = 0
      if team['points'] > avg:
         wins[team['roster_id']] += 1

csvfile = open('weekly_average.csv', 'w')
csvwriter = csv.writer(csvfile)

fields = ['Owner(s)', 'Team']
for week in range(START, END + 1):
   fields.append('Week {}'.format(week))
fields.append('Record')
csvwriter.writerow(fields)

for rosterId in wins.keys():
   row = []
   roster = rosters.getRoster(rosterId)
   ownerId = roster['owner_id']
   owner = users.getUser(ownerId)
   owners = owner['display_name']
   if roster['co_owners'] is not None:
      for coOwner in roster['co_owners']:
         user = users.getUser(coOwner)
         owners += ", " + user['display_name']
   row.append(owners)
   row.append(owner['metadata']['team_name'])
   for matchups in season:
      row.append(matchups.getPoints(rosterId))
   row.append("{} - {}".format(wins[rosterId], END - wins[rosterId]))
   csvwriter.writerow(row)

   row = [None, "Average"]
   for matchups in season:
      row.append(matchups.getAverage())
   csvwriter.writerow(row)