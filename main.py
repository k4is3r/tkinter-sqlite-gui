import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk
from glob import glob

 
class App:
    """ Creando el widget para la wentada"""
    def __int__(self, root):
        self.fields =[]
        self.root = root
        self.label()
        self.entry()
        self.button()
        self.listbox()
        self.db_name_widgets()
        self.tb_name_widgets()
        self.fields_widgets()
        self.btn_create_table()

    def label(self):
        #creating the label for name DB
        self.l = tk.Label(self.root, text="Crear DB [inserte nombre]")
        self.l.pack()

    def entry(self):
        self.db = tk.StringVar()
        self.e = tk.Entry(self.root, textvariable=self.db)
        self.e.pack()

    def button(self):
        #Creating the button for crate DB
        self.b = tk.Button(
			self.root,
			text="Crear DB",
			command= lambda: self.mk_db())
        self.b.pack()

    def listbox(self):
        #Setting the list box for show the bd created
        self.lb = tk.Listbox(self.root)
        self.lb.pack()
        self.show_db()

    def db_name_widgets(self):
        self.lbdname = tk.Label(
            self.root,
            text ="Inserta DB name"
        )
        self.lbdname.pack()
        self.dbn = tk.StringVar()
        self.edb = tk.Entry(
            self.root,
            textvariable=self.dbn)
        self.edb.pack()

    def tb_name_widgets(self):
        self.ltbname = tk.Label(
            self.root,
            text="Ingresa nombre para Tabla")
        self.ltbname.pack()
        

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
