import sqlite3

class ScoreBot:
    def __init__(self, database, tablename):
        self.db = database
        self.table = tablename

    def getData(self, name, mode="all"):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
    
        if mode == "all":
            cur.execute(f"SELECT * FROM {self.table}")

            rows = cur.fetchall()

            conn.close()

            return rows

        if mode == "individual":
            cur.execute(f"SELECT * FROM {self.table} WHERE name=?", [name])

            rows = cur.fetchall()

            conn.close()

            return rows

    def updateScore(self, name, score):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        try: #If the user does not exist, it just creates a nwe row and sets the score as score
            cur.execute(f"INSERT INTO {self.table}(name, score) VALUES(?, ?)", (name, score))

            conn.commit()

        except sqlite3.IntegrityError: #If the user does exist, it just updates the score.
            oldscore = self.getData(mode="individual", name=name)
            newscore = oldscore[0][1] + score
            cur.execute(f"UPDATE {self.table} SET score = ? WHERE name = ?", [newscore, name])

            conn.commit()

        conn.close()

    def updatePlayer(self, name, mode="add", score=0):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        if mode == "add":
            try:    
                cur.execute(f"INSERT INTO {self.table}(name, score) VALUES(?, ?)", (name, score))

                conn.commit()

            except sqlite3.IntegrityError:
                pass

        if mode == "delete":
            cur.execute(f"DELETE FROM {self.table} WHERE name=?", [name])

            conn.commit()

class MessageKeeperBot:
    def __init__(self, databse, table):
        self.db = databse
        self.table = table

    def getMessage(self, messageid, channelid):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM {self.table} WHERE message=? AND channel=?", (messageid, channelid))

        rows = cur.fetchall()

        conn.close()

        return rows

    def addUser(self, messageid, channelid, userid):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        olduserlist = self.getMessage(messageid, channelid)

        if len(olduserlist) == 0:
            cur.execute(f"INSERT INTO {self.table}(message, channel, users) VALUES(?, ?, ?)", (messageid, channelid, userid))

            conn.commit()

        else:
            newuserlist = olduserlist[0][2] + "," + str(userid)
            cur.execute(f"UPDATE {self.table} SET users = ? WHERE message = ? AND channel = ?", [newuserlist, messageid, channelid])

            conn.commit()

        conn.close()