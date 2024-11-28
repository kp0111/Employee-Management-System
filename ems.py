from customtkinter import *
from customtkinter import *
from PIL import Image
from tkinter import messagebox
from tkinter import ttk
import database


#functions
def delete_Aemployee():
    result=messagebox.askyesno('Confirm','Do you really want to delete all the records')
    if result:
        database.deleteall_records()
def Show_all():
    treeview_data()
    Salaryentry.delete(0,END)
    searchbox.set('Search By')


def search_employee():
    if Salaryentry.get()=='':
        messagebox.showerror('error', 'Enter value to search')
    elif searchbox.get()=='Search by':
        messagebox.showerror('error', 'pleae select an option')
    else:
        search_data=database.search(searchbox.get(),Salaryentry.get())
        ftree.delete(*tree.get_children())
        for employee in search_data:
            tree.insert('',END,values=employee)

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to delete')
    else:
        database.delete(identry.get())
        clear()
        messagebox.showerror('Error','Data is deleted')

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to update')
    else:
        database.update(identry.get(),phoneentry.get(),Nameentry.get(),Salaryentry.get(),rolebox.get(),genderbox.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is Updated')
def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        identry.insert(0,row[0])
        Nameentry.insert(0, row[1])
        phoneentry.insert(0, row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        Salaryentry.insert(0,row[5])


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    identry.delete(0,END)
    Nameentry.delete(0,END)
    phoneentry.delete(0,END)
    rolebox.set("Web Developer")
    genderbox.set("Male")
    Salaryentry.delete(0,END)


def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)
def add_employee():
    if identry.get()=='' or phoneentry.get()=='' or Nameentry.get()=='' or Salaryentry.get()=='':
        messagebox.showerror('Error','All Fields are required')
    elif database.id_exists(identry.get()):
        messagebox.showerror('Error','ID already exits')
    elif not identry.get().startswith('EMP'):
        messagebox.showerror('Error', 'Invalid ID format use like EMP1')


    else:
        database.insert(identry.get(),phoneentry.get(),Nameentry.get(),Salaryentry.get(),rolebox.get(),genderbox.get())
        treeview_data()
        clear()
        messagebox.showinfo('success','Data is added')


window=CTk()
window.geometry('930x580+100+100')
window.configure(fg_color='#161C30')
window.title('Employee Managemet System')
window.resizable(False,False)
logo=CTkImage(Image.open('img.png'),size=(930,158))
logolabel=CTkLabel(window,image=logo,text='')
logolabel.grid(row=0,column=0,columnspan=2)
leftframe=CTkFrame(window,fg_color='#161C30')
idlabel=CTkLabel(leftframe,text='ID',font=('ariel',18,'bold'),text_color='white')
idlabel.grid(row=0,column=0,padx=20)

identry=CTkEntry(leftframe,font=('ariel',15,'bold'),width=180)
identry.grid(row=0,column=1,padx=(20))

Namelabel=CTkLabel(leftframe,text='Name',font=('ariel',18,'bold'),text_color='white')
Namelabel.grid(row=1,column=0,padx=20)

Nameentry=CTkEntry(leftframe,font=('ariel',15,'bold'),width=180)
Nameentry.grid(row=1,column=1,padx=(20),pady=15)

phonelabel=CTkLabel(leftframe,text='Phone Number',font=('ariel',18,'bold'),text_color='white')
phonelabel.grid(row=2,column=0,padx=20,pady=15)

phoneentry=CTkEntry(leftframe,font=('ariel',15,'bold'),width=180)
phoneentry.grid(row=2,column=1,padx=(20),pady=(15))

rolelabel=CTkLabel(leftframe,text='Role',font=('ariel',18,'bold'),text_color='white')
rolelabel.grid(row=3,column=0,padx=20,pady=15)

role_options=["Web Developer","Data Scientist","Technical Writer","Network Engineer","Data Analyst","Business Analyst"]
rolebox=CTkComboBox(leftframe,values=role_options,width=180,font=('ariel',15,'bold'),state='readonly')
rolebox.grid(row=3,column=1)
rolebox.set('Web developer')

genderlabel=CTkLabel(leftframe,text='Gender',font=('ariel',18,'bold'),text_color='white')
genderlabel.grid(row=4,column=0,padx=20,pady=15)

gender_options=["Male","Female","Transgender"]
genderbox=CTkComboBox(leftframe,values=gender_options,width=180,font=('ariel',15,'bold'),state='readonly')
genderbox.grid(row=4,column=1)
genderbox.set('Female')

Salarylabel=CTkLabel(leftframe,text='Salary',font=('ariel',18,'bold'),text_color='white')
Salarylabel.grid(row=5,column=0,padx=20,pady=15)

Salaryentry=CTkEntry(leftframe,font=('ariel',15,'bold'),width=180)
Salaryentry.grid(row=5,column=1,padx=(20),pady=(15))
leftframe.grid(row=1,column=0)



rightframe=CTkFrame(window)
rightframe.grid(row=1,column=1)

search_options=["ID","Name","Phone","Gender","Salary"]
searchbox=CTkComboBox(rightframe,values=search_options,width=180,font=('ariel',15,'bold'),state='readonly')
searchbox.grid(row=0,column=0)
searchbox.set('Search by')
Searchentry=CTkEntry(rightframe,font=('ariel',15,'bold'),width=180)
Searchentry.grid(row=0,column=1,padx=(20),pady=(15))

searchbutton=CTkButton(rightframe,text="Search",width=50,command=search_employee)
searchbutton.grid(row=0,column=2)

showbutton=CTkButton(rightframe,text="Show All",width=50,command=Show_all
                     )
showbutton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightframe,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('ID','Name','Phone','Gender','Role','Salary')
tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')
tree.config(show='headings')
tree.column('ID',width=100)
tree.column('Name',width=100)
tree.column('Phone',width=100)
tree.column('Role',width=100)
tree.column('Gender',width=100)
tree.column('Salary',width=100)


style=ttk.Style()
style.configure('Treeview.heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',15,'bold'),rowheight=30,background='#161C30',foreground='white')
buttonFrame=CTkFrame(window,fg_color='#161C30')
scrollbar=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')
buttonFrame.grid(row=2,column=0,columnspan=2)
tree.configure(yscrollcommand==scrollbar.set)

newbutton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newbutton.grid(row=0,column=0,pady=5)

addbutton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addbutton.grid(row=0,column=1,padx=5)

upbutton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
upbutton.grid(row=0,column=2,padx=5)

delbutton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
delbutton.grid(row=0,column=3,padx=5)

delabutton=CTkButton(buttonFrame,text='Delete All Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_Aemployee)
delabutton.grid(row=0,column=4,padx=5)

treeview_data()
window.bind('<ButtonRelease>',selection)
window.mainloop()



