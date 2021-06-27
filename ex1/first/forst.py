import csv
from io import TextIOWrapper
from zipfile import ZipFile

MAX_LINES = 10000
# Globals
ID = 0
TEAM = 6
GAMES = 8
PARTICIPATE = 12
EVENT = 13
MEDAL = 14

team_dict = []
athlete_dict = []
participation_dict = []
medal_dict = []
won_dict = []

# opens file for ALL olympics table.
team_file = open("team.csv", 'w', )
team_writer = csv.writer(team_file, delimiter=",", quoting=csv.QUOTE_NONE)

athlete_file = open("athlete.csv", 'w', )
athlete_writer = csv.writer(athlete_file, delimiter=",", quoting=csv.QUOTE_NONE)

participation_file = open("participation.csv", 'w', )
participation_writer = csv.writer(participation_file, delimiter=",", quoting=csv.QUOTE_NONE)

medal_file = open("medal.csv", 'w', )
medal_writer = csv.writer(medal_file, delimiter=",", quoting=csv.QUOTE_NONE)

won_file = open("won.csv", 'w', )
won_writer = csv.writer(won_file, delimiter=",", quoting=csv.QUOTE_NONE)


# process_file goes over all rows in original csv file, and sends each row to process_row()
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
    team_file.close()
    athlete_file.close()
    participation_file.close()
    medal_file.close()
    won_file.close()


# process_row should splits row into the different csv table files
def process_row(row):
    # every line is a list of the features by order
    if row[TEAM] not in team_dict:
        team_writer.writerow(row[TEAM:GAMES])
        team_dict.append(row[TEAM])
    if row[ID] not in athlete_dict:
        athlete_writer.writerow(row[:TEAM])
        athlete_dict.append(row[ID])
    if row[GAMES] not in participation_dict:
        participation_writer.writerow(row[GAMES:PARTICIPATE])
        participation_dict.append(row[GAMES])
    if row[EVENT] not in participation_dict:
        participation_writer.writerow(row[PARTICIPATE:MEDAL])
        participation_dict.append(row[EVENT])
    if row[MEDAL] not in medal_dict and row[MEDAL]:
        medal_writer.writerow([row[MEDAL]])
        medal_dict.append(row[MEDAL])

    won_set = [row[ID], row[TEAM], row[GAMES], row[EVENT], row[MEDAL]]
    if row[MEDAL]:
        won_writer.writerow(won_set)
        won_dict.append(won_set)


# return the list of all tables
def get_names():
    return ["teams", "athlete", "participation", "medals", "won"]


if __name__ == "__main__":
    process_file()

