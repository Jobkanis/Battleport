import sqlite3



class Database:
    def __init__ (self):
        self.connection = sqlite3.connect('battleport.db')
        self.c = self.connection.cursor()

    def create_table(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS players (name TEXT, wins REAL, losses REAL)")

    def data_entry(self, name):
        entry = True
        self.c.execute("SELECT name FROM players")
        for row in self.c.fetchall():
            if row[0] == name:
                entry = False
                break

        if entry == True:
            wins = 0
            losses = 0
            self.c.execute("INSERT INTO players (name, wins, losses) VALUES (?, ?, ?)", (name, wins, losses))
            self.connection.commit()

    def data_update(self, playername, playerwins, playerlosses):
        self.c.execute("UPDATE players SET wins = (?), losses = (?) WHERE name = (?)", (playerwins, playerlosses, playername))
        self.connection.commit()

    def player_win(self, name):
        self.c.execute("SELECT * FROM players WHERE name = (?)", [name])
        for row in self.c.fetchall():
            wins = row[1] + 1
            break

        self.c.execute("UPDATE players SET wins = (?) WHERE name = (?)", (wins, name))
        self.connection.commit()

    def player_lose(self, name):
        self.c.execute("SELECT * FROM players WHERE name = (?)", [name])
        for row in self.c.fetchall():
            losses = row[2] + 1
            break

        self.c.execute("UPDATE players SET losses = (?) WHERE name = (?)", (losses, name))
        self.connection.commit()

database = Database()
database.create_table()
database.c.close()
database.connection.close()