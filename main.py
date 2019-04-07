from tkinter import *
from database import Database
from tkinter import messagebox
from alien_invasion import alien_invasion

db=Database()
al=alien_invasion()
def update():
   username=("%s"%(e1.get()))
   password=("%s"%(e2.get()))
   if((db.check(username))==True):
      db.add_player(username,password)
      master.quit()
      al.run_game(username)
   else:
      if(((db.check(username)))==False):
         if((db.check_password(username,password))==True):
            print("Login successful")
            master.quit()
            al.run_game(username)
         else:
            messagebox.showinfo("Registration Error", "Incorrect Password, Try Again")


master = Tk()
master.title("Registration")
Label(master, text="Username").grid(row=0)
Label(master, text="Password").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Login', command=update).grid(row=4, column=1, sticky=W, pady=4)


mainloop( )
db.close()