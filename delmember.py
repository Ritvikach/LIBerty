
from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()


class delmember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Delete Member")

        self.resizable(False, False)
        ###############################Frames################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # bottom frame
        self.bottomFrame = Frame(self, height=600, bg='#708d8d')
        self.bottomFrame.pack(fill=X)
        # heading,image
        heading = Label(self.topFrame, text=' Delete Member', font=' arial 30 bold', fg="#51702c", bg='white')
        heading.place(x=210, y=60)


        ################################################entries and labels########3

        # member name
        self.lbl_name = Label(self.bottomFrame, text='Name:', font='arial 10 bold', bg="#c4b48c", fg="black")
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, 'PLEASE ENTER MEMBER NAME')
        self.ent_name.place(x=150, y=45)
        ##phone
        self.lbl_phone = Label(self.bottomFrame, text=' Phone:', font='arial 10 bold', bg="#c4b48c", fg="black")
        self.lbl_phone.place(x=40, y=80)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_phone.insert(0, 'PLEASE ENTER PHONE NUMBER')
        self.ent_phone.place(x=150, y=85)
        # button
        button = Button(self.bottomFrame, text='Delete Member', command=self.delmember, fg='white', bg="#51702c")
        button.place(x=270, y=200)
        button2 = Button(self.bottomFrame, text='Delete Member')
        button.place(x=210, y=200)

    def delmember(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()

        if name and phone != "":
            try:
                query = "DELETE FROM 'MEMBERS' (member_name,member_phone) VALUES(?,? )"
                cur.execute(query, (name, phone))
                con.commit()
                messagebox.showinfo("Success", "Successfully removed from database")
            except:
                messagebox.showerror("ERROR", "Can't delete from database")

        else:
            messagebox.showerror("ERROR", "Fields cant be empty")
