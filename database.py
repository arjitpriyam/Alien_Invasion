import sqlite3
from sqlite3 import Error

class Database():

    def __init__(self):
        self.conn = sqlite3.connect("score.db")
        self.user_name=""
        self.high_score=0
        self.query = ""
        self.c= self.conn.cursor()

    def open(self):
        self.conn = sqlite3.connect("score.db")

    def close(self):
        self.conn.close()

    def check(self,username):
        username="'"+username+"'"
        self.query = "SELECT username FROM Players WHERE username= " + username
        self.c.execute(self.query)
        data=self.c.fetchone()
        if data is None:
            return True
        else:
            return False

    def create_table(self):
        self.c.execute("""CREATE TABLE Players (
                            username text,
                            password text,
                            high_score integer)""")

        self.conn.commit()

    def add_player(self, username,password):
        username = "'" + username + "'"
        password = "'" + password + "'"
        self.query="INSERT INTO Players (username,password,high_score) VALUES ("+username+","+password+",0)"
        print(self.query)
        self.c.execute(self.query)
        self.conn.commit()

    def update_high_score(self,username,highscore):
        username = "'" + username + "'"
        highscore=str(highscore)
        print(highscore)
        self.query="UPDATE Players SET high_score ="+highscore+" WHERE username= "+username
        self.c.execute(self.query)
        self.conn.commit()

    def get_highscore(self,username):
        username = "'" + username + "'"
        self.query="SELECT high_score FROM Players WHERE username= "+username
        self.c.execute(self.query)
        high=self.c.fetchone()[0]
        return high

    def check_password(self,username,password):
        username = "'" + username + "'"
        self.query="SELECT password FROM Players WHERE username= "+username
        self.c.execute(self.query)
        pas=self.c.fetchone()[0]
        if (password==pas):
            return True
        else:
            return False


#db=Database()
#db.update_high_score("abcd",100)
#db.get_highscore("abcd")
#db.create_table()
#db.close()
#db.update_high_score("anushka","100")
#hs=db.get_highscore("anushka")
#print(hs)
#print(db.check("anushka"))