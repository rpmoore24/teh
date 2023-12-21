import csv
from common.Matchups import Matchups
from common.Players import Players
from common.Rosters import Rosters
from common.Users import Users

LEAGUE_ID =
START = 1 # week
END = 14 # week

players = Players()
rosters = Rosters(LEAGUE_ID)
users = Users(LEAGUE_ID)

wins = {}
for week in range(START, END + 1):
   matchups = Matchups(LEAGUE_ID, week)
   matchups.setOptimumLineups(players)
   
   file = "optimum_week{}.csv".format(matchups.week)
   csvfile = open(file, 'w')
   csvwriter = csv.writer(csvfile)
   games = matchups.getMatchups()
   for game in games:
      team1 = game[0]
      team1roster = rosters.getRoster(team1['roster_id'])
      team1ownerId = team1roster['owner_id']
      team1owner = users.getUser(team1ownerId)
      team1name = team1owner['metadata']['team_name']
      team1total = sum(team1['optimum'].values())
      
      team2 = game[1]
      team2roster = rosters.getRoster(team2['roster_id'])
      team2ownerId = team2roster['owner_id']
      team2owner = users.getUser(team2ownerId)
      team2name = team2owner['metadata']['team_name']
      team2total = sum(team2['optimum'].values())
      
      if team1['roster_id'] not in wins.keys():
         wins[team1['roster_id']] = 0
      if team2['roster_id'] not in wins.keys():
         wins[team2['roster_id']] = 0
      if team1total > team2total:
         wins[team1['roster_id']] += 1
      else:
         wins[team2['roster_id']] += 1
      
      csvwriter.writerow([None, team1name, team2name])
      csvwriter.writerow(['QB', team1['optimum']['QB'], team2['optimum']['QB']])
      csvwriter.writerow(['RB1', team1['optimum']['RB1'], team2['optimum']['RB1']])
      csvwriter.writerow(['RB2', team1['optimum']['RB2'], team2['optimum']['RB2']])
      csvwriter.writerow(['WR1', team1['optimum']['WR1'], team2['optimum']['WR1']])
      csvwriter.writerow(['WR2', team1['optimum']['WR2'], team2['optimum']['WR2']])
      csvwriter.writerow(['TE', team1['optimum']['TE'], team2['optimum']['TE']])
      csvwriter.writerow(['FLEX', team1['optimum']['FLEX'], team2['optimum']['FLEX']])
      csvwriter.writerow(['K', team1['optimum']['K'], team2['optimum']['K']])
      csvwriter.writerow(['DEF', team1['optimum']['DEF'], team2['optimum']['DEF']])
      csvwriter.writerow(['Total', team1total, team2total])
      csvwriter.writerow([])
      
file = "optimum_records.csv"
csvfile = open(file, 'w')
csvwriter = csv.writer(csvfile)

csvwriter.writerow(['Owner(s)', 'Team', 'Record'])

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
   row.append("{} - {}".format(wins[rosterId], END - wins[rosterId]))
   csvwriter.writerow(row)
