import re

class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goals = 0

    def add_points(self, points):
        self.points += points
    
    def add_goals(self, goals):
        self.goals += goals

    def __str__(self):
        return f"{self.name} {self.points}"


def creat_team(team_name, teams_list):
    if not team_name in list(map(lambda t: t.name, teams_list)):
        team = Team(team_name)
        teams_list.append(team)
        return team

    return list(filter(lambda t: t.name == team_name, teams_list))[0]
    

code = input()
if '?' in code:
    code = code.replace('?', '\\?')

data = input()
teams_list = []
while data != 'final':
    teams_pattern = r'(?<={code})[A-Za-z]*(?={code})'
    pattern = teams_pattern.format(code = code)

    teams = re.findall(pattern, data)
    correct_named_teams = list(map(lambda t: t.upper()[::-1], teams))

    team_1 = creat_team(correct_named_teams[0], teams_list)
    team_2 = creat_team(correct_named_teams[1], teams_list)

    scores_pattern = r'\d+:\d+'
    result_as_str = re.findall(scores_pattern, data)[0].split(':')
    result_int = list(map(int, result_as_str))

    if result_int[0] > result_int[1]:
        team_1.add_points(3)
    elif result_int[0] < result_int[1]:
        team_2.add_points(3)
    else:
        team_1.add_points(1)
        team_2.add_points(1)

    team_1.add_goals(result_int[0])
    team_2.add_goals(result_int[1])
    
    data = input()

sorted_teams = sorted(teams_list, key=lambda t: (-t.points, t.name))
top_3 = sorted(teams_list, key=lambda t: (-t.goals, t.name))[:3]

print('League standings:')
[print(f"{index+1}. {team}") for index, team in enumerate(sorted_teams)]

print('Top 3 scored goals:')
[print(f"- {team.name} -> {team.goals}") for team in sorted(top_3, key=lambda t: (t.goals), reverse=True)]