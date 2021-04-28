import sqlite3

class Databasein:
    
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, name text, i1 text, i2 text, q text)")
        self.conn.commit()
        

    def addrec(self,name,i1,i2,q):
        self.cur.execute("INSERT INTO inventory VALUES (NULL,?,?,?,?)",(name,i1,i2,q))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM inventory")
        rows=self.cur.fetchall()
        return rows

    def searchrec(self,name=""):
        self.cur.execute("SELECT * FROM inventory WHERE name=?", (name,))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM inventory WHERE id=?",(id,))
        self.conn.commit()
    
        
    def update(self,id,name,i1,i2,q):
        self.cur.execute("UPDATE inventory SET name=?, i1=?, i2=?, q=? WHERE id=?",(name,i1,i2,q,id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

con = sqlite3.connect("SE_PROJECT/inventory.db")
cur = con.cursor()
statement = "SELECT username, password FROM users"
cur.execute(statement)
print(cur.fetchall())
#addrec("pasta","mayo","sauce",5)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))

