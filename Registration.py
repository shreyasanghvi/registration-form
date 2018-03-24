from tkinter import *
from tkinter import messagebox
from sqlite3 import *

user = {'u1':'k'}
flag = False
Count = 0
g = False

#Connection with database
conn = connect('D:event.db')

#Cursor for the database
crsr = conn.cursor()

#usrow
usr = Tk()

#geomtery
usr.geometry('400x400')

Label(usr,text='UserName').grid(row=0,column=0)
uname = Entry(usr)
uname.grid(row=0,column=1)
uname.focus()

one = Label(usr,text='Password')
one.grid(row=1,column=0)
passw = Entry(usr)
passw.grid(row=1,column=1)

def removeform(usr):
    global First,Second,Third,Forth,Fifth,Sixth,Seventh,Eight,fname,lname,Event,sem,Male,Female,contact,email,branch,submit,group,glbl,okk,college,Ninth,Count
    First.grid_forget()
    Second.grid_forget()
    Third.grid_forget()
    Forth.grid_forget()
    Fifth.grid_forget()
    Sixth.grid_forget()
    Seventh.grid_forget()
    Eight.grid_forget()
    fname.grid_forget()
    lname.grid_forget()
    Event.grid_forget()
    sem.grid_forget()
    Male.grid_forget()
    Female.grid_forget()
    contact.grid_forget()
    email.grid_forget()
    branch.grid_forget()
    submit.grid_forget()
    glbl.grid_forget()
    group.grid_forget()
    okk.grid_forget()
    college.grid_forget()
    Ninth.grid_forget()
    
def types(usr):
    global passw,uname,one,ind,grp
    uname.grid_forget()
    passw.grid_forget()
    one.grid_forget()

    if Count>0:
        removeform(usr)
    
    def grp_event():
        global g,group,okk,crsr,glbl
        crsr.execute('CREATE TABLE IF NOT EXISTS Group_events (GroupIndex INTEGER,FirstName TEXT,LastName TEXT,Contact INTEGER,Email TEXT,Branch TEXT,Sem INTEGER,Gender TEXT,Event TEXT,College TEXT)')
        g = True
        #group_index
        if g==True:
            glbl = Label(usr,text="Group Index")
            glbl.grid(row=1,column=0)
            group = Entry(usr,bd=3)
            group.grid(row=1,column=1)
            okk = Button(usr,text='OK',command=ok)
            okk.grid(row=1,column=2)

    def ok():
        global okk
        okk.grid_forget()
        form(usr)
        
    def ind_event():
        global crsr
        crsr.execute('CREATE TABLE IF NOT EXISTS Individual_events (FirstName TEXT,LastName TEXT,Contact INTEGER,Email TEXT,Branch TEXT,Sem INTEGER,Gender TEXT,Event TEXT,College TEXT)')
        form(usr)

    #individual event button
    ind = Button(usr,text="Individual event",command=ind_event,width=15)
    ind.grid(row=0,column=0)
    #group event
    grp = Button(usr,text="Group Event",command=grp_event,width=10)
    grp.grid(row=0,column=1)

    usr.tkraise()

def removetypes(usr):
    global g,grp,ind
    grp.grid_forget()
    ind.grid_forget()
    
def form(usr):
    global First,Second,Third,Forth,Fifth,Sixth,Seventh,Eight,fname,lname,Event,sem,Male,Female,contact,email,branch,submit,Ninth,college,Count

    #remove page 2 contains
    removetypes(usr)
    
    #geometry
    usr.geometry('400x400')

    #Title
    usr.title('Registration')
                     
    #First Name
    First = Label(usr,text='First Name')
    First.grid(row=0,column=0)
    fname = Entry(usr,bd=3)
    fname.grid(row=0,column=1)

    fname.focus()
    
    #Last Name
    Second = Label(usr,text='Last Name')
    Second.grid(row=1,column=0)
    lname = Entry(usr,bd=3)
    lname.grid(row=1,column=1)

    #Contact Number
    Third = Label(usr,text='Contact')
    Third.grid(row=2,column=0)
    contact = Entry(usr,bd=3)
    contact.grid(row=2,column=1)

    #Email Address
    Forth = Label(usr,text='Email')
    Forth.grid(row=3,column=0)
    email = Entry(usr,bd=3)
    email.grid(row=3,column=1)

    #Branch
    Fifth = Label(usr,text='Branch')
    Fifth.grid(row=4,column=0)
    branch = Entry(usr,bd=3)
    branch.grid(row=4,column=1)

    #Sem
    Sixth = Label(usr,text='Sem')
    Sixth.grid(row=5,column=0)
    sem = Entry(usr,bd=3)
    sem.grid(row=5,column=1)
        #e.focus_set()

    #Gender
    Gender = StringVar()
    Seventh = Label(usr,text="Gender")
    Seventh.grid(row=6,column=0)
    
    #Button for Male
    Male = Radiobutton(usr,text="Male",variable=Gender,value="Male")
    Male.grid(row=6,column=1)

    #Button for Female
    Female = Radiobutton(usr,text="Female",variable=Gender,value="Female")
    Female.grid(row=7,column=1)

    #Event drop down menu
    """Event = StringVar()
    Label(usr,text="Event").grid(row=8,column=0)
    Event.set("None")"""

    #event = Listbox(master, yscrollcommand=)
    """event = OptionMenu(usr,Event,"Drive to Campus","C kidaa ++","Pycon","Open House")
    event.config(width=16)
    event.grid(row=8,column=1)
    #event.config(width=20)"""

    #College
    Ninth = Label(usr,text='College')
    Ninth.grid(row=8,column=0)
    college = Entry(usr)
    college.grid(row=8,column=1)
    
    #event
    Eight = Label(usr,text='Event')
    Eight.grid(row=9,column=0)
    Event = Entry(usr)
    Event.grid(row=9,column=1)

    Count += 1

    def sub():
        global g             
        if g:
            if group.get() == "":
                messagebox.showerror("Error","Insert Group Index")
                group.focus()
                return 0
            else:
                try:
                    gi = int(group.get())
                except:
                    messagebox.showerror("Error","Enter number in Group Index")
                    group.focus()

        if fname.get() == "":
            messagebox.showwarning("Warning","Insert First Name")
            fname.focus()
            return 0
        else:
            f = fname.get()
                
        if lname.get() == "":
            messagebox.showwarning("Warning","Insert Last Name")
            lname.focus()
            return 0
        else:
            l = lname.get()
            
        if contact.get() == "":
            messagebox.showwarning("Warning","Insert Contact Number")
            contact.focus()
            return 0
        else:
            try:   
                c = int(contact.get())
            except:
                messagebox.showerror("Error","Enter number")
                contact.delete(0,END)
                contact.focus()
                return 0
                
        if email.get() == "":
            messagebox.showwarning("Warning","Insert Email Address")
            email.focus()
            return 0
        else:
            e = email.get()
            
        if branch.get() == "":
            messagebox.showwarning("Warning","Insert Branch/Std")
            branch.focus()
            return 0
        else:
            b = branch.get()
                
        if sem.get() == "":
            # for message box
            messagebox.showwarning("Warning","Insert Sem")
            sem.focus()
            return 0
        else:
            try:
                s = int(sem.get())
            except:
                messagebox.showerror("Error","Invalid Sem Entry")
                sem.delete(0,END)
                sem.focus()
                return 0

        if Gender.get() == "":
            messagebox.showwarning("Warning","Select Gender")
            return 0
        else:
            gender = Gender.get()

        if str(Event.get()) == "None" or Event.get() == "":
            messagebox.showwarning("Warning","No Event Selected")
            return 0
        else:
            evt = Event.get()

        if college.get() == "":
            messagebox.showwarning("Warning","Insert College")
            college.focus()
            return 0
        else:
            coll = college.get()
            
        try:
            if g == True:
                crsr.execute('INSERT INTO Group_events (GroupIndex, FirstName,LastName,Contact,Email,Branch,Sem,Gender,Event,College) Values(?,?,?,?,?,?,?,?,?,?)',(gi,f.upper(),l.upper(),c,e.lower(),b.upper(),s,gender.upper(),evt.upper(),coll.upper()))
                g = False
                conn.commit()
            else:
                #print (f,l,c,e,b,s,gender,evt,coll)
                crsr.execute('INSERT INTO Individual_events (FirstName,LastName,Contact,Email,Branch,Sem,Gender,Event,College) Values(?,?,?,?,?,?,?,?,?)',(f.upper(),l.upper(),c,e.lower(),b.upper(),s,gender.upper(),evt.upper(),coll.upper()))
                conn.commit()
            #types(usr)
        except:
            messagebox.showerror("Rollback","Inconsist Data")
            conn.rollback()
        types(usr)
    def dele():
        f = fname.get()
        l = lname.get()
        crsr.execute('DELETE FROM Participants WHERE FirstName ="%s"'%(f))
        conn.commit()
        
    #Submit Button
    submit = Button(usr,text="Submit",command=sub,width=30)
    submit.grid(row=10,column=1)

    #Delete Button    
    delete = Button(usr,text="Delete",command=dele,width=6)
    delete.grid(row=4,column=2)

    usr.tkraise()
        
def check():
    u = uname.get()
    p = passw.get()
    if u in user:
        if user[u] == p:
            flag = True
            types(usr)
            f = True
    else:
        messagebox.showerror('username','UserName or Password is incorrect')

ok = Button(usr,text='OK',command=check)
ok.grid(row=2,column=1)
