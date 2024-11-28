from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='Rishabh' and PasswordEntry.get()=='12345':
        messagebox.showinfo('Success','Login is Successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong ID or Password')
root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title("Login Page")
image=CTkImage(Image.open('HR-man-.webp'),size=(930,478))
imagelabel=CTkLabel(root,image=image,text='')
imagelabel.place(x=0,y=0)
Heading=CTkLabel(root,text='Employee Management System',bg_color='#FAFAFA',font=('Goudy old style',20,'bold'),text_color='dark blue')
Heading.place(x=20,y=100)

#create input fields
usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username')
usernameEntry.place(x=50,y=150)
PasswordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
PasswordEntry.place(x=50,y=200)

loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=50,y=250)




root.mainloop()
