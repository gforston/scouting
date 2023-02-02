import requests

POINTS_COEF = 0.860 #TOTAL POINTS SCORED (AUTO + TELLY)
HIGH_COEF = 0.389 # NUM PIECES SCORED ON HIGH
MID_COEF = 0 #idk this yet
LOW_COEF = -0.246 # NUM PIECES SCORED ON LOW
AUTOPTS_COEF = 1.034 #TOTAL AUTO POINTS SCORED (TAXI + SCORE + DOCK) 
NUMPIECES_COEF = -0.560 # TOTAL # PIECES SCORED
DROPS_COEF = -0.964 # NUM OF LOST CONTROL PIECES
CONENUM_COEF = 0.181 # NUM OF CONES SCORED
CUBENUM_COEF = 0.116 # NUM OF CUBES SCORED
BALANCED_COEF = 1.369 #POINTS OF BALANCING
UNBALANCED_COEF = 1.008 #POINTS OF NOT BALANCED


POINTS = 18 
HIGH = 6
MID = 0 #idk
LOW = 0
AUTOPTS = 6
NUMPIECES = 10
DROPS = 0
CONENUM = 0
CUBENUM = 0
BALANCED = 12
UNBALANCED = 2
#get these from morscout

TEAM_ADJUST = ((41+42) / 42) * 2.75 #team 1 point ranking + team 2 point ranking /422 * 2.75
TEAMS_AVG = ((22+23) / 42) * 2.75 # average team adjustment

RPW = (POINTS * POINTS_COEF) + (HIGH * HIGH_COEF) + (LOW * LOW_COEF) + (AUTOPTS * AUTOPTS_COEF) + (NUMPIECES * NUMPIECES_COEF) + (DROPS * DROPS_COEF)
+ (CONENUM * CONENUM_COEF) + (CUBENUM * CUBENUM_COEF) + (BALANCED * BALANCED_COEF) + (UNBALANCED * UNBALANCED_COEF) + (TEAM_ADJUST - TEAMS_AVG)

print(TEAM_ADJUST)
print(TEAMS_AVG)
print(RPW + (TEAM_ADJUST - TEAMS_AVG) )

API_KEY = "KXTRTRpyfWN4uXfHnS5iRhNVdWvyKWMRxQeHLSrp1vPxYMICpv02e3U4DVOPi78H"
team_key = "frc1515"
year = "2023"

response = requests.get(f"https://www.thebluealliance.com/api/v3/event/2022cala/rankings", headers={
    "X-TBA-Auth-Key": API_KEY
})
data = response.json()
for team in data["rankings"]:
    if team["team_key"] == team_key:
        print(team["rank"])
        #print(team["team_key"])