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
        self.tbn = tk.StringVar()
        self.etb = tk.Entry(
            self.root,
            textvariable= self.tbn
        )
        self.etb.pack()

    def fields_widgets(self):
        self.lflname = tk.Label(
            self.root,
            text="""
            Ingrese los nombres y tipos de los campos
            seguidos por una coma, uno por uno selecionando
            uno por cada campo
            """
        )
        self.lflname.pack()
        self.vfl = tk.StringVar()
        self.efl = tk.Entry(
            self.root,
            textvariable= self.vfl
        )
        self.efl.pack()
        self.bfl = tk.Button(
            self.root,
            text="Crear campo",
            command= lambda : self.mk_fl()
        )
        self.bfl.pack()

    def btn_create_table(self):
        self.btb = tk.Button(
            self.root,
            text="Crear Tabla",
            command = lambda : self.mk_tb(self.dbn, self.tbn)
        )
        self.btb.pack()


    def mk_db(self):
        db = self.e.get()
        if db.endswith(".db"):
            pass
        else:
            db = db + ".db"
        try:
            conn = lite.connect(db)
            if db in self.lb.get(0, tk.END):
                pass
            else:
                self.lb.insert(tk.END, db)
            return conn
        except Error as e:
            print(e)
        finally:
            self.db.set("")
            conn.close()

    def show_db(self):
        for file in glob("*.db"):
            self.lb.insert(tk.END, file)

    def mk_fl(self):
        self.fields.append(self.efl.get())
        self.vfl.set("")

    def mk_tb(self, dbn, tbn):
        self.conn = lite.connect(dbn.get())
        self.cur = self.conn.cursor()
        self.fields = "".join(self.fields)
        self.cur.execute("""Crear tabla {} ({});""".format(tbn,self.fields))
        self.fields = []
        self.conn.close()



root = tk.Tk()
win  = App(root)
root.mainloop()
