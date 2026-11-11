#backend
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movie1.db")

def MovieData():
    con=sqlite3.connect(DB_PATH) 
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Movie_ID text,Movie_Name text,Release_Date text,Director text,[Cast] text,Budget text,Duration text,Rating text)")
    con.commit()
    con.close()
    
def AddMovieRec(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating):
    con=sqlite3.connect(DB_PATH)    
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)", (Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()

def ViewMovieData():
    con=sqlite3.connect(DB_PATH)    
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteMovieRec(id):    
    con=sqlite3.connect(DB_PATH)    
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()  

def SearchMovieData(Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):  
    con=sqlite3.connect(DB_PATH)    
    cur=con.cursor()
    conditions = []
    params = []
    fields = [("Movie_ID", Movie_ID), ("Movie_Name", Movie_Name), ("Release_Date", Release_Date),
              ("Director", Director), ("[Cast]", Cast), ("Budget", Budget),
              ("Duration", Duration), ("Rating", Rating)]
    for col, val in fields:
        if val != "":
            conditions.append(f"{col}=?")
            params.append(val)
    if conditions:
        query = "SELECT * FROM book WHERE " + " OR ".join(conditions)
        cur.execute(query, tuple(params))
    else:
        cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateMovieData(id,Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):
    con=sqlite3.connect(DB_PATH)    
    cur=con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?,Movie_Name=?,Release_Date=?,Director=?,[Cast]=?,Budget=?,Duration=?,Rating=? WHERE id=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating,id))
    con.commit()
    con.close()

MovieData()


