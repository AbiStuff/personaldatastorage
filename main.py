from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Abishek' and passwordEntry.get()=='2525':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import pdms
    else:
        messagebox.showerror('Error','Please enter correct credentials')



window=Tk()

window.geometry('1941x1280')
window.title('Login System of Personal Data Storge Management System')

# window.resizable(False,False)

bgimage=ImageTk.PhotoImage(file='bg3.jpg')

bgLabel=Label(window,image=bgimage)
bgLabel.place(x=0,y=0)

loginframe=Frame(window,bg='#ccd1d4')
loginframe.place(x=550,y=350)

logoimage=PhotoImage(file='logo1.png')

logolable=Label(loginframe,image=logoimage)
logolable.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user.png')

usernamelabel= Label(loginframe,image=usernameImage,text='Username',compound=LEFT
                     ,font=('times new roman',20,'bold'),bg='#ccd1d4')
usernamelabel.grid(row=1,column=0,pady=10)

usernameEntry=Entry(loginframe,font=('times new roman',20,'bold'),bd=4,fg='black')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)



passwordImage=PhotoImage(file='pass.png')

passwordlabel= Label(loginframe,image=passwordImage,text='Password',compound=LEFT
                     ,font=('times new roman',20,'bold'),bg='#ccd1d4')
passwordlabel.grid(row=2,column=0,pady=10)

passwordEntry=Entry(loginframe,font=('times new roman',20,'bold'),bd=4,fg='black')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginbuttom=Button(loginframe,text='login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',
                   activeforeground='white',cursor='hand2',command=login)
loginbuttom.grid(row=3,column=1,pady=10)


window.mainloop()