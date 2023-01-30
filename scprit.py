import requests

API_KEY = "KXTRTRpyfWN4uXfHnS5iRhNVdWvyKWMRxQeHLSrp1vPxYMICpv02e3U4DVOPi78H"
team_key = "frc1515"
year = "2023"

# response = requests.get(f"https://www.thebluealliance.com/api/v3/team/{team_key}/events/{year}", headers={
#     "X-TBA-Auth-Key": API_KEY
# })
# data = response.json()
# for event in data:
#     print(event['address'])

# response2 = requests.get(f"https://www.thebluealliance.com/api/v3/team/{team_key}/event/2022cala/matches", headers={
#     "X-TBA-Auth-Key": API_KEY
# })

# array = []
# data2 = response2.json()
# for x in data2:
#     array.append(x['alliances']['blue']['score'])

# array.remove(8)
# print(sum(array) / len(array))

response = requests.get(f"https://www.thebluealliance.com/api/v3/event/2022cala/matches", headers={
    "X-TBA-Auth-Key": API_KEY
})
team_key = "frc1515"
data = response.json()

climbs = []
taxis = []
for match in data:
    if(team_key in match['alliances']['blue']['team_keys'] or team_key in match['alliances']['red']['team_keys']):
        isRed = team_key in match['alliances']['red']['team_keys']
        alliance = "red" if isRed else "blue"
        team_position = match['alliances'][alliance]['team_keys'].index(team_key) + 1

        climb = match['score_breakdown'][alliance][f"endgameRobot{team_position}"]
        taxi = match['score_breakdown'][alliance][f"taxiRobot{team_position}"]
        climbs.append(climb)
        taxis.append(taxi)

output = ""
for climb, taxi in zip(climbs, taxis):
    output += f"{climb},{taxi}\n"

with open('sheet.csv', 'w') as f:
    f.write(output)
        



