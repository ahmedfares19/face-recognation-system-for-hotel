import sqlite3

class UsersDatabase():
    def __init__(self):
        self.datafile = sqlite3.connect('UsersData.db')
        self.cur = self.datafile.cursor()
        self.create_table()


    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT ,NID TEXT)")
        self.datafile.commit()

    def UserNames(self):
        self.cur.execute("SELECT name FROM users")
        li = list(self.cur.fetchall())
        lis = []
        for x in li:
            lis.append(str(x[0]))
        return lis


    def InsertUser(self, username, password):
        d = self.cur.execute("SELECT name FROM users WHERE name = ?",(username,))
        li = list(d.fetchall())
        if(len(li) == 0):
            self.cur.execute('INSERT INTO users VALUES(?,?)', (username, password,))
            self.datafile.commit()
            return True
        return False


    def deleteUser(self,name):
        self.cur.execute('DELETE FROM users WHERE name = ?',(name,))
        self.datafile.commit()

    def LogIN(self,username , pas):
        d = self.cur.execute("SELECT name FROM users WHERE name = ?", (username,))
        li = list(d.fetchall())
        d1 = self.cur.execute("SELECT password FROM users WHERE name = ?", (username,))
        li1 = list(d1.fetchall())
        if len(li) == 1 and li1[0][0]==pas:
            return True
        else:
            return False


#######################################****************************************************####################################



class ResidentDatabase():
    def __init__(self):
        self.datafile = sqlite3.connect('ResidentData.db')
        self.cur = self.datafile.cursor()
        self.create_table1()


    def create_table1(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS resident(Room TEXT , PersonNum TEXT ,Name TEXT ,NID TEXT , StrDate TEXT , StrTime TEXT ,EndDate TEXT , endTime TEXT)")
        self.datafile.commit()


    def resNames(self):
        self.cur.execute("SELECT name FROM users")
        li = list(self.cur.fetchall())
        lis = []
        for x in li:
            lis.append(str(x[0]))
        return lis


    def InsertResident(self, NID, name , room , personnum , strdate ,strtime ,enddate,endtime,):
        d = self.cur.execute("SELECT NID FROM resident WHERE NID = ?",(NID,))
        li = list(d.fetchall())
        d1 = self.cur.execute("SELECT Room FROM resident WHERE Room = ?", (room,))
        li2 = list(d1.fetchall())
        d3 = self.cur.execute("SELECT PersonNum FROM resident WHERE PersonNum = ?", (personnum,))
        li3 = list(d3.fetchall())
        if(len(li) == 0 and len(li2) == 0 and len(li3) == 0):
            self.cur.execute('INSERT INTO resident VALUES(?,?,?,?,?,?,?,?)', (room, personnum,name,NID,strdate,strtime,enddate,endtime,))
            self.datafile.commit()
            return True
        return False


    def deleteres(self,NID):
        self.cur.execute('DELETE FROM users WHERE name = ?',(NID,))
        self.datafile.commit()



