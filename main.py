import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk
from glob import glob

def create(obj):
    db = obj.e.get()
    
    if db[-3] == ".db":
        pass
    else:
        db = db + ".db"
    try:
        conn = lite.connect(db)
        return conn
    except Error as e:
        print(e)

    finally:
        conn.close()
        odj.lb.insert(tk.END, db)
        obj.db.set("")

 
