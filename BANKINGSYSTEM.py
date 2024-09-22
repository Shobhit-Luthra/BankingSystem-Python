import mysql.connector as con
import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk 

mycon=con.connect(
    host="localhost",
    user="root",
    password="1234",
    database="d1")
cursor =mycon.cursor(buffered=True)
obj=mycon.cursor()
 

def go_to_next_element(event):
    event.widget.tk_focusNext().focus()

def Exit():
   nw.destroy()
    
def repass():
    obj.reset()
    q="select* from user_pass"
    obj.execute(q)
    for i in obj:
        il=ctk.CTkInputDialog(text="Enter username",title="Reset password")
        k=il.get_input()
        if k==i[0]:
            iz=ctk.CTkInputDialog(text="What is your favorute animal?",title="Enter Security Question Answer")
            p=iz.get_input()
            if i[2]==p:
                ic=ctk.CTkInputDialog(text="Enter New Password",title="Enter New Password")
                r=ic.get_input()
                ia=ctk.CTkInputDialog(text="Renter New Password",title="Renter New Password")
                o=ia.get_input()
                if r==o:
                    v="update user_pass set Password=%s where Username=%s;"
                    obj.reset()
                    l=(r,k)
                    obj.execute(v,l)
                    mycon.commit()
                    tkinter.messagebox.showinfo("Sucessfuly Changed Password","Sucessfuly Changed Password")
                    
def register():
    global a
    a=username.get()
    b=password.get()
    c=con_pass.get()
    d=squestion.get()
    if b==c:
        q="insert into user_pass values(%s,%s,%s)"
        v=(a,b,d)	
        obj.execute(q,v)
        obj.reset()
        q2="insert into bank values(%s,0)"
        v1=(a,)
        obj.execute(q2,v1)
        mycon.commit()
        tkinter.messagebox.showinfo("Sucessfuly Registerd","Sucessfuly Registerd")

def login():
    global e
    e=username1.get()
    f=password1.get()
    q="select* from user_pass"
    obj.execute(q)
    for i in obj:
            if e==i[0] and f==i[1]:
                tkinter.messagebox.showinfo("Sucessfuly Logged in","Sucessfuly Logged in")
                app.destroy()
                newwin()
                break
                         
def newwin():
    global nw
    nw=ctk.CTk()
    nw.title("Home Page")
    nw.geometry('500x500')
    nw.grid_columnconfigure(0, weight=1)
    nw.grid_columnconfigure(1, weight=1)
    nw.grid_columnconfigure(2, weight=1)
    nw.grid_rowconfigure(0, weight=1)
    nw.grid_rowconfigure(1, weight=1)
    nw.grid_rowconfigure(2, weight=1)
    nw.grid_rowconfigure(3, weight=1)
    nw.grid_rowconfigure(4, weight=1)
    nw.grid_rowconfigure(5, weight=1)
    nw.grid_rowconfigure(6, weight=1)
    nw.grid_rowconfigure(7, weight=1)
    button2=ctk.CTkButton(nw,text="Check Balance",command=balance)
    button2.grid(row=2, column=1, padx=10, pady=10, sticky="")
    button3=ctk.CTkButton(nw,text="Withdraw Money",command=withdraw)
    button3.grid(row=3,column=1,padx=10, pady=10, sticky="")
    button4=ctk.CTkButton(nw,text="Deposit Money",command=deposit)
    button4.grid(row=4,column=1,padx=10, pady=10, sticky="")
    button5=ctk.CTkButton(nw,text="Return to Login",command=Exit)
    button5.grid(row=5,column=1,padx=10, pady=10, sticky="")
    nw.mainloop()

def balance():
    obj.reset()
    q1="select* from bank"
    obj.execute(q1)
    for i in obj:
            if e==i[0]:
                c=i[1]
                tkinter.messagebox.showinfo("Bank Balance:",c)
                break
            

def withdraw():
    obj.reset()
    q="select* from bank"
    obj.execute(q)
    for i in obj:
        if e==i[0]:
            c=i[1]
            im=ctk.CTkInputDialog(text="Enter amount to be withdrawn",title="Withdraw money")
            z=int(im.get_input())
            w=c-z
            if w>0:
                n="update bank set Balance=%s where Username=%s;"
                l=(w,e)
                obj.reset()
                obj.execute(n,l)
                tkinter.messagebox.showinfo("Bank Balance left:",c)
                mycon.commit()
            else:
                tkinter.messagebox.showinfo("Error")


def deposit():
    obj.reset()
    q="select* from bank"
    obj.execute(q)
    for i in obj:
        if e==i[0]:
            d=i[1]
            ik=ctk.CTkInputDialog(text="Enter amount to be deposit",title="Deposit money")
            z=int(ik.get_input())
            d=d+z
            x="update bank set Balance=%s where Username=%s;"
            l=(d,e)
            obj.reset()
            obj.execute(x,l)
            tkinter.messagebox.showinfo("Bank Balance:",d)
            mycon.commit()

root=ctk.CTk()
app=ctk.CTk()
app.title("Bank")
app.geometry('500x500')
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)
app.grid_columnconfigure(4, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)
app.grid_rowconfigure(5, weight=1)
app.grid_rowconfigure(6, weight=1)
app.grid_rowconfigure(7, weight=1)
ctk.set_default_color_theme("dark-blue") 
ctk.set_appearance_mode("dark")

my_tab = ctk.CTkTabview(master=app)
my_tab.grid(column=2,row=0,padx=20, pady=20)
tab1=my_tab.add("Register")
tab2=my_tab.add("Login")

def entry_1_return_key_event(event):
    register()

username=ctk.CTkEntry(tab1,placeholder_text="Enter your Name",width=300,height=30)
username.bind('<Return>', go_to_next_element)
username.grid(row=1,column=2,padx=10, pady=10)
password=ctk.CTkEntry(tab1,placeholder_text="Enter password",width=300,height=30)
password.configure(show="*")
password.grid(row=2,column=2,padx=10, pady=10)
password.bind('<Return>', go_to_next_element)
con_pass=ctk.CTkEntry(tab1,placeholder_text="Renter password",width=300,height=30)
con_pass.configure(show="*")
con_pass.bind('<Return>', go_to_next_element)
con_pass.grid(row=3,column=2,padx=10, pady=10)
squestion=ctk.CTkEntry(tab1,placeholder_text="Security Question:What is your favourite Animal?",width=300,height=30)
squestion.bind('<Return>', entry_1_return_key_event)
squestion.grid(row=4,column=2,padx=10, pady=10)
button=ctk.CTkButton(tab1, text="Register",command=lambda:register())
button.grid(row=5, column=2, padx=10, pady=10, sticky="")

def entry_2_return_key_event(event):
    login()

username1=ctk.CTkEntry(tab2,placeholder_text="Enter your Name",width=300,height=30)
username1.bind('<Return>', go_to_next_element)
username1.grid(row=1,column=2,padx=10, pady=10)
password1=ctk.CTkEntry(tab2,placeholder_text="Enter password",width=300,height=30)
password1.bind('<Return>', entry_2_return_key_event)
password1.configure(show="*")
password1.grid(row=2,column=2,padx=10, pady=10)
button1=ctk.CTkButton(tab2, text="Login",command=login)
button1.grid(row=5, column=2, padx=10, pady=10, sticky="")
button5=ctk.CTkButton(tab2,text="Reset Password",command=repass)
button5.grid(row=6,column=2,padx=10, pady=10, sticky="")

app.mainloop()
