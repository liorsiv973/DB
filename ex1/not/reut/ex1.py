import csv
from io import TextIOWrapper
from zipfile import ZipFile

MAX_LINES = 10000
ID = 0
TEAM = 6
GAMES = 8
EVENT = 13
MEDAL = 14

athlete_l = []
team_l = []
game_l = []
sport_l = []
medal_l = []
play_l = []
won_l = []

athlete = open("athlete.csv", 'w')
athlete_w = csv.writer(athlete, delimiter=",", quoting=csv.QUOTE_NONE)
team = open("teams.csv", 'w')
team_w = csv.writer(team, delimiter=",", quoting=csv.QUOTE_NONE)
game = open("game.csv", 'w')
game_w = csv.writer(game, delimiter=",", quoting=csv.QUOTE_NONE)
sport = open("sports.csv", 'w')
sport_w = csv.writer(sport, delimiter=",", quoting=csv.QUOTE_NONE)
medal = open("medals.csv", 'w')
medal_w = csv.writer(medal, delimiter=",", quoting=csv.QUOTE_NONE)
play = open("play.csv", 'w')
play_w = csv.writer(play, delimiter=",", quoting=csv.QUOTE_NONE)
won = open("won.csv", 'w')
won_w = csv.writer(won, delimiter=",", quoting=csv.QUOTE_NONE)


# process_file goes over all rows in original csv file, and sends each row to process_row()
# DO NOT CHANGE!!!
def process_file():
    counter = 0
    with ZipFile('athlete_events.csv.zip') as zf:
        with zf.open('athlete_events.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:
                # pre-process : remove all quotation marks from input and turns NA into null value ''.
                row = [v.replace(',','') for v in row]
                row = [v.replace("'",'') for v in row]
                row = [v.replace('"','') for v in row]
                row = [v if v != 'NA' else "" for v in row]
                # in 'Sailing', the medal winning rules are different than the rest of olympic games, so they are discarded.
                if row[12] == "Sailing":
                    continue
                # In all years but 1956 summer, olympic games took place in only one city. we clean this fringe case out of the data.
                if row[9] == '1956' and row[11] == 'Stockholm':
                    continue
                # This country is associated with two different noc values, and is discarded.
                if row[6] == 'Union des Socits Franais de Sports Athletiques':
                    continue
                process_row(row)
                counter += 1
                if counter == MAX_LINES:
                    break
    athlete.close()
    team.close()
    game.close()
    sport.close()
    medal.close()
    play.close()
    won.close()


# process_row should splits row into the different csv table files
def process_row(row):
    if row[ID] not in athlete_l:
        athlete_w.writerow(row[:6])
        athlete_l.append(row[ID])
    if row[TEAM] not in team_l:
        team_w.writerow(row[6:8])
        team_l.append(row[TEAM])
    if row[GAMES] not in game_l:
        game_w.writerow(row[8:12])
        game_l.append(row[GAMES])
    if row[EVENT] not in sport_l:
        sport_w.writerow(row[12:14])
        sport_l.append(row[EVENT])
    if row[MEDAL] not in medal_l and row[MEDAL]:
        medal_w.writerow([row[14]])
        medal_l.append(row[MEDAL])

    play_index = [row[ID], row[TEAM], row[GAMES], row[EVENT]]
    won_index = [row[ID], row[TEAM], row[GAMES], row[EVENT], row[MEDAL]]

    if play_index not in play_l:
        play_w.writerow(play_index)
        play_l.append(play_index)
    if row[MEDAL] and won_index not in play_l:
        won_w.writerow(won_index)
        won_l.append(won_index)




# return the list of all tables
def get_names():
    return ["athlete", "teams", "game", "sports", "medals", "play", "won"]


if __name__ == "__main__":
    process_file()