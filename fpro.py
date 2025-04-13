from tkinter import*
import tkinter as ttk
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pyodbc
import datetime as dt


try:
    conn_str=(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
              r'DBQ=D:\Programming Languages\python\final project day\final project\fproDB.accdb;')

    conn=pyodbc.connect(conn_str)
    print("connection stablished")   
    
    cursor=conn.cursor()
except pyodbc.Error as e:
    print("Error is connection",e)





def selection():
    selected=str(var.get())  
    #lblgender.config(text=selected)
    entgender.delete(0,END)
    entgender.insert(END,selected)
    

   
def submit():
    if entindxno.get()=='' or entfname.get()=='' or entfname.get()=='' or spage.get()=='' or entgender.get()=='' or entmail.get()=='' or entwno.get()=='' or cbpro.get()=='' or cbscl.get()=='':
        tkinter.messagebox.showerror("Data Error","Fill All Blanks")
        


    else:
        no=entindxno.get()
        fname=entfname.get()
        lname=entlname.get()
        age=spage.get()
        gender=entgender.get()
        mail=entmail.get()
        wnumber=entwno.get()
        City=cbpro.get()
        school=cbscl.get()

        cursor.execute("insert into student(Index,FirstName,LastName,Age,Gender,Email,WhatsappNo,City,School)\
                   values(?,?,?,?,?,?,?,?,?)",no,fname,lname,age,gender,mail,wnumber,City,school)
        tkinter.messagebox.showinfo("Add new data","Add new record Successfully")

        conn.commit()


def yesbtn():
    
    #btnsubmit.configure(state=NORMAL)
    btnsubmit["state"]=NORMAL



    
def search():
    yesbtn.configure(state=DISABLED)
    btnsubmit["state"]=DISABLED
    no=entindxno.get()
    try:
        if no !="":
            q="select*from student where Index=?"
            cursor.execute(q,(no,))
            row=cursor.fetchone()
            Index=row[0]
            FirstName=row[1]
            LastName=row[2]
            Age=row[3]
            Gender=row[4]    
            mail=row[5]
            WhatsappNo=row[6]
            City=row[7]
            School=row[8]
            entfname.delete(0,END)
            entfname.insert(END,FirstName)
            entlname.delete(0,END)
            entlname.insert(END,LastName)
            spage.delete(0,END)
            spage.insert(END,Age)
            entgender.delete(0,END)
            entgender.insert(END,Gender)
            entmail.delete(0,END)
            entmail.insert(END,mail)    
            entwno.delete(0,END)
            entwno.insert(END,WhatsappNo)
            cbpro.delete(0,END)
            cbpro.insert(END,City)
            cbscl.delete(0,END)
            cbscl.insert(END,School)
        else:     
            tkinter.messagebox.showerror("Error Input","Please Input \n index Number")
            yesbtn.configure(state=NORMAL)
            entindxno.delete(0,END)
            entfname.delete(0,END)
            entlname.delete(0,END)
            spage.delete(0,END)
            entgender.delete(0,END)
            rbtnmale.deselect()
            rbtnfemale.deselect()
            entmail.delete(0,END)
            entwno.delete(0,END)
            cbpro.delete(0,END)
            cbscl.delete(0,END)
    except:
        tkinter.messagebox.showinfo("Search Record","Input correct \n Index Number")
        yesbtn.configure(state=NORMAL)
        entindxno.delete(0,END)
        entfname.delete(0,END)
        entlname.delete(0,END)
        spage.delete(0,END)
        entgender.delete(0,END)
        rbtnmale.deselect()
        rbtnfemale.deselect()
        entmail.delete(0,END)
        entwno.delete(0,END)
        cbpro.delete(0,END)
        cbscl.delete(0,END)
    
def clear():
    yesbtn.configure(state=NORMAL)
    entindxno.delete(0,END)
    entfname.delete(0,END)
    entlname.delete(0,END)
    spage.delete(0,END)
    entgender.delete(0,END)
    rbtnmale.deselect()
    rbtnfemale.deselect()
    entmail.delete(0,END)
    entwno.delete(0,END)
    cbpro.delete(0,END)
    cbscl.delete(0,END)

    
def exitbtn():
    myexit=tkinter.messagebox.askyesno("Warning","Are you want to exit")
    if myexit==1:
        conn.close()
        win.destroy()
    

def addtotxtfile():
    if entindxno.get()=='' or entfname.get()=='' or entfname.get()=='' or spage.get()=='' or entgender.get()=='' or entmail.get()=='' or entwno.get()=='' or cbpro.get()=='' or cbscl.get()=='':
        tkinter.messagebox.showerror("Data Error","Fill All Blanks")


    else:
        open("text.txt","w").close()
        text = "Index - "+entindxno.get()+ "\n"+"First Name - "+entfname.get() + "\n" +"Last Name - "+ entlname.get() + "\n" +"Age - "+  spage.get() +  "\n" +"Gender - "+  entgender.get() + "\n"+"Email Adress - "+  entmail.get() + "\n"+"Whatsapp Number - "+  entwno.get() +"\n"+"City - "+  cbpro.get() + "\n"+"School - "+  cbscl.get() + "\n"+ "\n"
        with open("text", "a") as f:
            f.write(text)


        tkinter.messagebox.showinfo("Add new details","Successfully Add this details to text file")     

def display():
    cursor.execute("select * from student")
    result=cursor.fetchall()
    if len(result)!=0:
        memrecords.delete(*memrecords.get_children())
        for row in result[0:]:
            memrecords.insert("",END,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
        
    conn.commit()


def update():
    

    no=entindxno.get()
    fname=entfname.get()
    lname=entlname.get()
    age=spage.get()
    gender=entgender.get()
    mail=entmail.get()
    wnumber=entwno.get()
    City=cbpro.get()
    school=cbscl.get()
    
    cursor.execute("update student set FirstName=?,LastName=?,Age=?,Gender=?,Email=?,WhatsappNo=?,City=?,School=? where Index=?",(fname,lname,age,gender,mail,wnumber,City,school,no))
    tkinter.messagebox.showinfo("Update data","Update Successfully")




    
root=Tk()
root.title("Login Form")
root.geometry("500x275+500+250")
root.resizable(0,0)
root.configure(bg="black")


date = dt.datetime.now()
# Create Label to display the Date
labeldate=Label(root, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10",bg="black",fg="silver")
labeldate.place(x=350,y=250)



#def loginform():
try:
    conn_str=(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
              r'DBQ=D:\Programming Languages\python\final project day\final project\fproDB.accdb;')

    conn=pyodbc.connect(conn_str)
    print("connection stablished")   
    
    cursor=conn.cursor()
except pyodbc.Error as e:
    print("Error is connection",e)


def entrybtn():
   
    if entid.get() == '2004' and entname.get() == 'madhura':
        tkinter.messagebox.showinfo("Login", "Login successfully")
        root.destroy()  # Destroy the login window
        
    else:
        idn = entid.get()
        name = entname.get()
        cursor.execute("insert into invalidlogin(username,password) values(?,?)", name, idn)
        tkinter.messagebox.showerror("Login", "Invalid Username or Password")
        conn.commit()

'''def lgnexit():
    exitme=tkinter.messagebox.askyesno("Exit","Are you Want To Exit")
    if exitme==1:
        conn.close()
        root.destroy()'''

def lgnclear():
    entname.delete(0,END)
    entid.delete(0,END)    

lblname=Label(root,text="UserName:",font="none 15",bg="#005456",fg="white")
lblname.place(x=50,y=10)
entname=Entry(root,font="none 15",width=35)
entname.place(x=50,y=60)


lblid=Label(root,text="Password:",font="none 15",bg="#005456",fg="white")
lblid.place(x=50,y=110)
entid=Entry(root,font="none 15",width=35,show="*")
entid.place(x=50,y=160)


lgnbtn=Button(root,text="Login",command=entrybtn,font="none 15",bg="cadet blue")
lgnbtn.place(x=50,y=210)
root.bind("<Return>",lambda event:entrybtn())

lgnclrbtn=Button(root,text="Clear",command=lgnclear,font="none 15",bg="cadet blue")
lgnclrbtn.place(x=125,y=210)
root.bind("<Escape>",lambda event:lgnclear())


#lgnbtn=Button(root,text="Close",command=lgnexit,font="none 15",bg="cadet blue")
#lgnbtn.place(x=125,y=210)
#root.bind("<Escape>",lambda event:lgnexit())


    

root.mainloop()
        
win=Tk()
win.title("DB1pythonform")
win.geometry("1525x725+0+40")
win.configure(bg="#708090")
win.resizable(0,0)

date = dt.datetime.now()
# Create Label to display the Date
labeldate= Label(win, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10",bg="#708090",fg="black")
labeldate.place(x=1000,y=700)

btnup=Button(win,text="Update",font="none 15",width="10",bg="darkgray",command=update)
btnup.place(x=925,y=50)

btndis=Button(win,text="Display",font="none 15",width="10",height=1,bg="darkgray",command=display)
btndis.place(x=1075,y=50)



#showing database details
viewframe=Frame(win,bd=5,width=520,height=150,relief=RIDGE,bg="cadet blue")
viewframe.place(x=615,y=100)

scroll_y=Scrollbar(viewframe,orient=VERTICAL)
memrecords=ttk.Treeview(viewframe,height=28,columns=("Index","FirstName","LastName","Age","Gender","Email","WhatsappNo","City","School"),yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)

memrecords.heading("Index",text="Index")
memrecords.heading("FirstName",text="FirstName")
memrecords.heading("LastName",text="LastName")
memrecords.heading("Age",text="Age")
memrecords.heading("Gender",text="Gender")
memrecords.heading("Email",text="Email")
memrecords.heading("WhatsappNo",text="WhatsappNo")
memrecords.heading("City",text="City")
memrecords.heading("School",text="School")

memrecords["show"]="headings"
memrecords.column("Index",width=50,anchor=W)
memrecords.column("FirstName",width=70,anchor=W)
memrecords.column("LastName",width=70,anchor=W)
memrecords.column("Age",width=30,anchor=CENTER)
memrecords.column("Gender",width=45,anchor=CENTER)
memrecords.column("Email",width=180,anchor=CENTER)
memrecords.column("WhatsappNo",width=80,anchor=CENTER)
memrecords.column("City",width=100,anchor=CENTER)
memrecords.column("School",width=240,anchor=CENTER)

memrecords.pack(fill=BOTH,expand=1)




lbltitle=Label(win,text="Student Record System",bg="#708090",fg="white")
Font_tuple = ( "none",30,"bold","italic","underline")
lbltitle.configure(font = Font_tuple)
lbltitle.place(x=100,y=20)


lblindxno=Label(win,text="Index Number:",font="none 15",bg="#708090",fg="white")
lblindxno.place(x=20,y=100)
entindxno=Entry(win,font="none 15",width=15)
entindxno.place(x=200,y=100)

lblfname=Label(win,text="First Name:",font="none 15",bg="#708090",fg="white")
lblfname.place(x=20,y=150)
entfname=Entry(win,font="none 15",width=35)
entfname.place(x=200,y=150)

lbllname=Label(win,text="Last Name:",font="none 15",bg="#708090",fg="white")
lbllname.place(x=20,y=200)
entlname=Entry(win,font="none 15",width=35)
entlname.place(x=200,y=200)


lblage=Label(win,text="Student Age:",font="none 15",bg="#708090",fg="white")
lblage.place(x=20,y=250)
spage=Spinbox(win,font="none 15",width="2",from_=5,to=20)
spage.place(x=200,y=250)

var=StringVar()
lblgender=Label(win,text="Gender:",font="none 15",bg="#708090",fg="white")
lblgender.place(x=20,y=300)
rbtnmale=Radiobutton(win,text="Male",font="none 15",variable=var,value="Male",bg="#708090",command=selection)
rbtnmale.place(x=200,y=300)
rbtnfemale=Radiobutton(win,text="Female",font="none 15",variable=var,value="Female",bg="#708090",command=selection)
rbtnfemale.place(x=300,y=300)
entgender=Entry(win,font="none 15",width=10)
entgender.place(x=450,y=305)
 

lblmail=Label(win,text="Email Address:",font="none 15",bg="#708090",fg="white")
lblmail.place(x=20,y=350)
entmail=Entry(win,font="none 15",width=35)
entmail.place(x=200,y=350)

lblwno=Label(win,text="whatsapp number:",font="none 15",bg="#708090",fg="white")
lblwno.place(x=20,y=400)
entwno=Entry(win,font="none 15",width=35)
entwno.place(x=200,y=400)


places = [
    "Polonaruwa",
    "Kaduruwela",
    "Hingurakgoda",
    "Minneriya",
    "Bakamuna",
    "Aralaganwila",
    "Medirigiriya",
    "Giritale",
    "Elahera",
    "Jayantipura",
    "Galamuna",
    "Lankapura",
    "Sungavila",
    "Manampitiya",
    "Siripura",
    "Welikanda",
    "Dimbulagala",
    "Thambala",
    "Pulastigama"
]


schools = [
    "Royal Central College, Polonnaruwa",
    "Thopawewa National School, Polonnaruwa",
    "Polonnaruwa Muslim Central College, Kaduruwela",
    "Ananda Balika National School, Hingurakgoda",
    "Minneriya National School, Minneriya",
    "Medirigiriya National School, Medirigiriya",
    "Diulankadawala Central College, Diulankadawala",
    "Mahasen National School, Bakamuna",
    "Vilayaya Nationala School, Aralaganwila",
    "Polonnaruwa Sungavil Muslim Maha Vidyalaya"
]




lblpro=Label(win,text="City:",font="none 15",bg="#708090",fg="white")
lblpro.place(x=20,y=450)
cbpro=ttk.Combobox(win,font="none 15",width="15",values=places)
cbpro.place(x=200,y=450)

lblscl=Label(win,text="School:",font="none 15",bg="#708090",fg="white")
lblscl.place(x=20,y=500)
cbscl=ttk.Combobox(win,font="none 15",width=35,values=schools)
cbscl.place(x=200,y=500)


yesbtn=Button(win,text="Yes",font="none 10",bg="darkgray",command=yesbtn)
yesbtn.place(x=440,y=550)

lblcheck=Label(win,text="The Above Details Are True:-",font="none 15",bg="#708090",fg="white")
lblcheck.place(x=175,y=550)


btnsubmit=Button(win,text="Submit",font="none 15",width="10",bg="darkgray",state=DISABLED,command=submit)
btnsubmit.place(x=100,y=600)

btnsrh=Button(win,text="Search",font="none 15",width="10",bg="darkgray",command=search)
btnsrh.place(x=100,y=650)
win.bind("<Return>",lambda event:search())

btnclr=Button(win,text="Clear",font="none 15",width="10",bg="darkgray",command=clear)
btnclr.place(x=240,y=600)

btnclr=Button(win,text="Exit",font="none 15",width="10",bg="darkgray",fg="red",command=exitbtn)
btnclr.place(x=240,y=650)
win.bind("<Escape>",lambda event:exitbtn())

btnaddtotxtfile=Button(win,text="Add This"+ "\n"+"Details to Text File",font="none 15",width="15",height=3,bg="darkgray",command=addtotxtfile)
btnaddtotxtfile.place(x=380,y=600)



display()

win.mainloop()

