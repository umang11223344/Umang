from tkinter import *
from PIL import Image as im
from PIL import ImageTk
import importlib


class Gui:
    root = None
    user_id = None  # this is the _id of the user class

    @staticmethod
    def main():
        Gui.root = Tk()
        Gui.root.title('tkinter -blogging ')
        Gui.root.attributes("-fullscreen", True)
        Gui.login_signup_btn()
        Gui.root.mainloop()

    @staticmethod
    def login_signup_btn():
        def btn(btn_type):
            if btn_type == 'signup':
                frame.pack_forget()
                Gui.login_signup('Signup')
            else:  # login
                frame.pack_forget()
                Gui.login_signup('Login')

        def resize_image(event):  # to make the image fir the entire window
            new_width = event.width
            new_height = event.height

            image = bg.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo

        frame = Frame(Gui.root)  # the main frame
        frame.pack(fill=BOTH, expand=YES)

        bg = im.open('gui/images/bg1.png', 'r')
        photo = ImageTk.PhotoImage(bg)

        label = Label(frame, image=photo)  # adding image to a label and overlaying that label with any widget
        label.place(x=0, y=0, relwidth=1, relheight=1)  # relwidth for filling up the entire window in x and y
        label.bind('<Configure>', resize_image)

        login_frame = Frame(frame, relief='flat')  # add everything in here to show over the image
        login_frame.place(relx=0.4, rely=0.6, anchor=CENTER)

        signup_frame = Frame(frame, relief='flat')  # add everything in here to show over the image
        signup_frame.place(relx=0.6, rely=0.6, anchor=CENTER)

        login_btn = Button(login_frame, text='Login', width=8, bg='#09001a', fg='#943c09', relief='flat',
                           font='Consolas 18 normal', command=lambda: btn('login'), highlightthickness=0)
        login_btn.grid(row=1, column=0, ipady=3)

        signup_btn = Button(signup_frame, text='Signup', width=8, bg='#09001a', fg='#943c09', relief='flat',
                            font='Colsolas 18 normal', command=lambda: btn('signup'), highlightthickness=0)
        signup_btn.grid(row=1, column=1, ipadx=4, ipady=2)

    @staticmethod
    def login_signup(form_type):
        err_ = StringVar()

        def resize_image(event):  # to make the image fir the entire window
            new_width = event.width
            new_height = event.height

            image = bg_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)

            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        def submit():
            if form_type == 'Signup':
                frame.pack_forget()
                name_ = name_entry.get()
                gmail_ = gmail_entry.get()
                password_ = password_entry.get()
                Gui.loged_in_blogs()

            else:  # login
                gmail_ = gmail_entry.get()
                password_ = password_entry.get()
                frame.pack_forget()
                Gui.loged_in_blogs()
        

        frame = Frame(Gui.root)
        frame.pack(fill=BOTH, expand=YES)  # main frame
        bg_image = im.open("gui/images/bg2.jpg")  # the main bg image
        photo = ImageTk.PhotoImage(bg_image)

        label = Label(frame, image=photo)  # adding image to a label and overlaying that label with any widget
        label.place(x=0, y=0, relwidth=1, relheight=1)  # relwidth for filling up the entire window in x and y
        label.bind('<Configure>', resize_image)

        if form_type == 'Signup':
            name = Label(frame, text='Name', font='Consolas 25 normal ', bg='white', fg='#e36fda')  # '#FD5DA8'
            name.place(relx=0.3, rely=0.2)
            name_entry = Entry(frame, font='Consolas 21 normal ', width=20, bg='black', fg='#e36fda',
                               relief='flat', insertbackground='#e36fda', highlightthickness=0)
            name_entry.place(relx=0.4, rely=0.2)

        gmail = Label(frame, text='Gmail', font='Consolas 25 normal ', bg='white', fg='#e36fda')  # '#FD5DA8'
        gmail.place(relx=0.3, rely=0.3)
        gmail_entry = Entry(frame, font='Consolas 21 normal ', width=20, bg='white', fg='#e36fda',
                            relief='flat', insertbackground='#e36fda', highlightthickness=0)
        gmail_entry.place(relx=0.4, rely=0.3)

        password = Label(frame, text='Password', font='Consolas 25 normal ', bg='white', fg='#e36fda')  # '#FD5DA8'
        password.place(relx=0.25, rely=0.4)
        password_entry = Entry(frame, font='Consolas 21 normal ', width=20, bg='white', fg='#e36fda',
                               relief='flat', insertbackground='#e36fda', show='*', highlightthickness=0)
        password_entry.place(relx=0.4, rely=0.4)

        submit_btn = Button(frame, font='Consolas 20 normal', text=form_type, bg='white', fg='#e36fda', relief='flat',
                            command=submit, highlightthickness=0)
        submit_btn.place(relx=0.4, rely=0.5)

        err = Label(frame, textvariable=err_, bg='white', fg='#cf59a0', font='Consolas 20 normal')
        err.place(relx=0.2, rely=0.8)
a = Gui()
a.main()
