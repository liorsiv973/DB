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

team_set = []
athlete_set = []
participation_set = []
medal_set = []
won_set = []

# opens file for ALL olympics table.
teamfile = open("team.csv", 'w', )
teamwriter = csv.writer(teamfile, delimiter=",", quoting=csv.QUOTE_NONE)

athletefile = open("athlete.csv", 'w', )
athletewriter = csv.writer(athletefile, delimiter=",", quoting=csv.QUOTE_NONE)

participationfile = open("participation.csv", 'w', )
participationwriter = csv.writer(participationfile, delimiter=",", quoting=csv.QUOTE_NONE)

medalfile = open("medal.csv", 'w', )
medalwriter = csv.writer(medalfile, delimiter=",", quoting=csv.QUOTE_NONE)

wonfile = open("won.csv", 'w', )
wonwriter = csv.writer(wonfile, delimiter=",", quoting=csv.QUOTE_NONE)

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
    teamfile.close()
    athletefile.close()
    participationfile.close()
    medalfile.close()
    wonfile.close()


# process_row should splits row into the different csv table files
def process_row(row):
    # every line is a list of the features by order
    if row[ID] not in athlete_set:
        athlete_set.append(row[ID])
        athletewriter.writerow(row[ID:TEAM])
    if row[TEAM] not in team_set:
        team_set.append(row[TEAM])
        teamwriter.writerow(row[TEAM:GAMES])

    row_par = row[GAMES:MEDAL]
    row_par.append(row[ID])
    row_par.append(row[TEAM])
    l = [row[ID], row[TEAM], row[GAMES], row[EVENT]]
    if l not in participation_set and row[ID] and row[TEAM]:
        participation_set.append(l)
        participationwriter.writerow(row_par)
    if row[MEDAL] not in medal_set and row[MEDAL]:
        medal_set.append(row[MEDAL])
        medalwriter.writerow([row[MEDAL]])
    row_won = [row[ID], row[TEAM], row[GAMES], row[EVENT], row[MEDAL]]
    if row_won not in won_set and row[MEDAL]:
        won_set.append(row_won)
        wonwriter.writerow(row_won)


# return the list of all tables
def get_names():
    return ["athlete", "team", "participation", "medal", "won"]


if __name__ == "__main__":
    process_file()

