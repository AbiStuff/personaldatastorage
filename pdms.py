from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas


# functionality part

def iexit():
    result=messagebox.askyesno('Comfirm','Do you want to exit')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='csv')
    indexing=persontable.get_children()
    newlist=[]
    for index in indexing:
        content=persontable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Pancard','Adhar','Licence','Added date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Details is saved succesfully')



def toplevel(title,button_text,command):
    global idEntry,nameEntry,mobileEntry,emailEntry,addressEntry,genderEntry,dobEntry,number1Entry,number2Entry,number3Entry,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    mobileLabel = Label(screen, text='MobileNo', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    mobileEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    number1Label = Label(screen, text='PanNumber', font=('times new roman', 20, 'bold'))
    number1Label.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    number1Entry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    number1Entry.grid(row=7, column=1, pady=15, padx=10)

    number2Label = Label(screen, text='AdharNumber', font=('times new roman', 20, 'bold'))
    number2Label.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    number2Entry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    number2Entry.grid(row=8, column=1, pady=15, padx=10)

    number3Label = Label(screen, text='licenceNumber', font=('times new roman', 20, 'bold'))
    number3Label.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    number3Entry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    number3Entry.grid(row=9, column=1, pady=15, padx=10)

    person_button = ttk.Button(screen, text=button_text, command=command)
    person_button.grid(row=10, columnspan=2, pady=15)
    if title=='Update the Person Data':
        indexing = persontable.focus()

        content = persontable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(1, listdata[1])
        mobileEntry.insert(2, listdata[2])
        emailEntry.insert(3, listdata[3])
        addressEntry.insert(4, listdata[4])
        genderEntry.insert(5, listdata[5])
        dobEntry.insert(6, listdata[6])
        number1Entry.insert(7, listdata[7])
        number2Entry.insert(8, listdata[8])
        number3Entry.insert(9, listdata[9])






def update_data():

    query='update details set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,PanNumber=%s,AdharNumber=%s,LicenceNUmber=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),mobileEntry.get(),emailEntry.get(),addressEntry.get(),
                            genderEntry.get(),dobEntry.get(),number1Entry.get(),number2Entry.get(),number3Entry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id{idEntry.get()} id modified successfully',parent=screen)
    screen.destroy()
    show_person()

def show_person():
    query = 'select *from details'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    persontable.delete(*persontable.get_children())
    for data in fetched_data:
        persontable.insert('', END, values=data)


def delete_person():
    indexing =persontable.focus()
    print(indexing)
    content=persontable.item(indexing)
    content_id=content['values'][0]
    query='delete from details where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select *from details'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    persontable.delete(*persontable.get_children())
    for data in fetched_data:
        persontable.insert('',END,values=data)





def search_data():
    query='select *from details where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s '
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),mobileEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    persontable.delete(*persontable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        persontable.insert('',END,values=data)


def add_data():
    if idEntry.get() == '' or nameEntry.get() == '' or mobileEntry.get() == '' or emailEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '' or number1Entry.get() == '' or number2Entry.get() == '' or number3Entry.get() == '':
        messagebox.showerror('Error', 'All fields are required', parent=screen)
    else:
        try:
            query = 'insert into details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (
                idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(),
                genderEntry.get(), dobEntry.get(), number1Entry.get(), number2Entry.get(), number3Entry.get(), date, time))
            con.commit()


            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clear the form?',
                                         parent=screen)
            screen.destroy()
            if result:
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                mobileEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
                number1Entry.delete(0, END)
                number2Entry.delete(0, END)
                number3Entry.delete(0, END)

            query = 'select * from details'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            persontable.delete(*persontable.get_children())
            for data in fetched_data:
                persontable.insert('', END, values=data)

            messagebox.showerror('Error', 'ID cannot be repeated', parent=screen)
        except Exception as e:

            messagebox.showerror('Error', f'An error occurred: {str(e)}', parent=screen)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password='Abi@sql')
            mycursor=con.cursor()
            messagebox.showinfo('Success','Database Connection is successful',parent=connectWindow)
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query="create database personaldatamanagement"
            mycursor.execute(query)
            query="use personaldatamanagement"
            mycursor.execute(query)
            query=('create table details(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),'
                   'address varchar(100),gender varchar(20),dob varchar(20),PanNumber bigint,AdharNumber int,'
                   'LicenceNumber int,date varchar(50),time varchar(50))')
            mycursor.execute(query)
        except:
            query='use personaldatamanagement'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection is successful',parent=connectWindow)
        connectWindow.destroy()
        addpersonButton.config(state=NORMAL)
        searchpersonButton.config(state=NORMAL)
        deletepersonButton.config(state=NORMAL)
        updatepersonButton.config(state=NORMAL)
        showpersonButton.config(state=NORMAL)
        exportpersonButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title("Database Connection")
    connectWindow.resizable(0,0)


    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0 ,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='Username', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)


    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)


count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count] #s
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date:{date}\nTime:{time}')
    datetimeLabel.after(1000,clock)

# GUI part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')
root.geometry('1941x1280+0+0')
root.title('Personal Data Storage Management System ')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s="Personal Data Storage Management System"
sliderLabel=Label(root,font=('arial',25,'italic','bold'),width=50)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text="Connect to Database",command=connect_database)
connectButton.place(x=1300,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='person.png')
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addpersonButton=ttk.Button(leftFrame,text='Add Person Data',width=25,state=DISABLED,command=lambda : toplevel('Add The Person Data','ADD',add_data))
addpersonButton.grid(row=1,column=0,pady=20)

searchpersonButton=ttk.Button(leftFrame,text='Search Person Data',width=25,state=DISABLED,command= lambda : toplevel('Search The Person Data','SEARCH',search_data))
searchpersonButton.grid(row=2,column=0,pady=20)

deletepersonButton=ttk.Button(leftFrame,text='Delete Person Data',width=25,state=DISABLED,command=delete_person)
deletepersonButton.grid(row=3,column=0,pady=20)

updatepersonButton=ttk.Button(leftFrame,text='Update Person Data',width=25,state=DISABLED,command=lambda : toplevel('Update the Person Data','UPDATE',update_data))
updatepersonButton.grid(row=4,column=0,pady=20)

showpersonButton=ttk.Button(leftFrame,text='Show Person Data',width=25,state=DISABLED,command=show_person)
showpersonButton.grid(row=5,column=0,pady=20)

exportpersonButton=ttk.Button(leftFrame,text='Export Person Data',width=25,state=DISABLED,command=export_data)
exportpersonButton.grid(row=6,column=0,pady=20)

exitpersonButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitpersonButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root )
rightFrame.place(x=300,y=80,width=1200,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

persontable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender','D.O.B','Number1',
                                             'Number2','Number3','Added Date','Added Time'),
                                             xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)


scrollBarX.config(command=persontable.xview)
scrollBarY.config(command=persontable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

persontable.pack(fill=BOTH,expand=1)

persontable.heading('Id',text='Id')
persontable.heading('Name',text='Name')
persontable.heading('Mobile',text='Mobile No')
persontable.heading('Email',text='Email')
persontable.heading('Address',text='Address')
persontable.heading('Gender',text='Gender')
persontable.heading('D.O.B',text='D.O.B')
persontable.heading('Number1',text='PanNumber')
persontable.heading('Number2',text='AdharNumber')
persontable.heading('Number3',text='LicenceNumber')
persontable.heading('Added Date',text='AddedDate')
persontable.heading('Added Time',text='AddedTime')


persontable.column('Id',width=100,anchor=CENTER)
persontable.column('Name',width=300,anchor=CENTER)
persontable.column('Mobile',width=200,anchor=CENTER)
persontable.column('Email',width=400,anchor=CENTER)
persontable.column('Address',width=400,anchor=CENTER)
persontable.column('Gender',width=150,anchor=CENTER)
persontable.column('D.O.B',width=150,anchor=CENTER)
persontable.column('Number1',width=200,anchor=CENTER)
persontable.column('Number2',width=250,anchor=CENTER)
persontable.column('Number3',width=250,anchor=CENTER)
persontable.column('Added Date',width=200,anchor=CENTER)
persontable.column('Added Time',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=30,font=('arial',12,'bold'),background='white',fieldbackground='white')

style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='red')



persontable.config(show='headings')


root.mainloop()