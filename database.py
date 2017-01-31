import sqlite3


connection = sqlite3.connect('battleport.db')
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS players (name TEXT, wins REAL, losses REAL)")

def data_entry(name):
    entry = True
    c.execute("SELECT name FROM players")
    for row in c.fetchall():
        if row[0] == name:
            entry = False
            break

    if entry == True:
        wins = 0
        losses = 0
        c.execute("INSERT INTO players (name, wins, losses) VALUES (?, ?, ?)", (name, wins, losses))
        connection.commit()

def data_update(playername, playerwins, playerlosses):
    c.execute("UPDATE players SET wins = (?), losses = (?) WHERE name = (?)", (playerwins, playerlosses, playername))
    connection.commit()

def player_win(name):
    c.execute("SELECT * FROM players WHERE name = (?)", [name])
    for row in c.fetchall():
        wins = row[1] + 1
        break

    c.execute("UPDATE players SET wins = (?) WHERE name = (?)", (wins, name))
    connection.commit()

def player_lose(name):
    c.execute("SELECT * FROM players WHERE name = (?)", [name])
    for row in c.fetchall():
        losses = row[2] + 1
        break

    c.execute("UPDATE players SET losses = (?) WHERE name = (?)", (losses, name))
    connection.commit()


create_table()
c.close()
connection.close()