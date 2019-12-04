import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk
from glob import glob

 
class App:
    """ Creando el widget para la wentada"""

    def __init__(self, root):
        self.root = root
        #creating the label for name DB
        self.l = tk.Label(self.win, text="Crear DB [inserte nombre]")
        self.l.pack()
        #Setting the var
        self.e_string_var = tk.StringVar()
        self.e = tk.Entry(self.root, textvariable=self.e_string_var)
        self.e.pack()
        #Creating the button for crate DB
        self.b = tk.Button(
			self.root,
			text="Crear DB",
			command= lambda: self.mk_db(self))
        self.b.pack()
        #Setting the list box for show the bd created
        self.lb = tk.Listbox(self.win)
        self.lb.pack()
        self.show_db()
    #funtion to create the DB
    def mk_db(self):
        db = self.e.get()
        if db.endswith(".db"):
            pass
        else:
            db = db + ".db"
        try:
            conn = lite.connect(db)
            self.lb.insert(tk.END, db)
            self.e_string_var.set("")
            return conn
        except Error as e:
            print(e)
        finally:
            conn.close()
    #Funtion to shwo DB in the listbox
    def show_db(self):
        for file in glob("*.db"):
            self.lb.insert(tk.END, file)


root = tk.Tk()
app = App(root)
root.mainloop()