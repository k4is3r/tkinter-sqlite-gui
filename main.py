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

class Window:
    """ Creando el widget para la wentada"""

    def __init__(self):
        self.win = tk.Tk()
        self.label()
        self.entry()
        self.button()
        self.listbox()

    def label(self):
        self.l = tk.Label(self.win, text="Crear DB [inserte nombre]")
        self.l.pack()

    def entry(self):
        self.db = tk.StringVar()
        self.e = tk.Entry(self.win, textvariable=self.db)
        self.e.pack()

    def button():
        self.b = tk.Button(self.win, text="Crear DB", command= lambda: create(self))
        self.b.pack()
    
    def listbox():
        pass     
