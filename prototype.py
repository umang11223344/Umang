from tkinter import *
from tkinter_api import Gui

bg_ = '#262C3A'
fg = '#B5ECFB'
new_frame = None


def set_frame(value):
    global new_frame
    new_frame = value
# =================================above scrollable blogs header stuff ====================================


header = Label(frame, text='welcome user', font='Consolas 30 normal', bg=bg_, fg=fg)
header.place(x=10, y=30)


def top_button_press(type):
    global frame
    if type == 'create_blog':
        frame.pack_forget()
        Gui.create_blogs()
    elif type == 'browse_blogs':
        frame.pack_forget()
        Gui.browse_all_blogs()
    else:  # back btn
        pass


create_blog_btn = Button(frame, text='Create Blog', bg=fg, fg=bg_, relief='flat', font='Consolas 15 normal',
                         highlightthickness=0, command=lambda: top_button_press('create_blog'))

create_blog_btn.place(x=10, y=100)

browse_all_blogs = Button(frame, text='Browse all blogs', bg=fg, fg=bg_, relief='flat', font='Consolas 15 normal',
                          highlightthickness=0, command=lambda: top_button_press('browse_blogs'))
browse_all_blogs.place(x=180, y=100)

back_btn = Button(frame, text='<', bg=fg, fg=bg_, relief='flat',
                  font='Consolas 15 normal', highlightthickness=0, command=lambda: top_button_press('back'))
back_btn.place(x=410, y=100)

mid_label = Label(frame, text='Your Blogs', font='Consolas 20 normal ', bg=bg_, fg=fg)
mid_label.place(x=10, y=180)

mid_label = Label(frame, text='click on a blog to view your posts ', font='Consolas 14 normal ', bg=bg_, fg=fg)
mid_label.place(x=10, y=215)

# ========================================================scroll area =================================================
container = Frame(frame, bg='#262C3A')  # the main scrollable frame
canvas = Canvas(container, bg='#262C3A', highlightthickness=0, height=500, width=800)
scrollable_frame = Frame(canvas, bg='#262C3A')
scrollable_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.bind('<Button-4>', lambda event: canvas.yview('scroll', -1, 'units'))
canvas.bind('<Button-5>', lambda event: canvas.yview('scroll', 1, 'units'))


def btn_press(a):
    exec("t" + str(a) + '.config(text=a)')


def btn_highlight(a):
    exec("t" + str(a) + '.config(bg=fg)')
    exec("t" + str(a) + '.config(fg=bg_)')


def btn_unhighlight(a):
    exec("t" + str(a) + '.config(bg=bg_)')
    exec("t" + str(a) + '.config(fg=fg)')


for i in range(50):
    temp_frame = ''
    exec('temp_frame = "f" + str(i)')
    exec(temp_frame + '= Frame(scrollable_frame, bg=bg_, highlightthickness=2, highlightbackground=fg)')
    exec(temp_frame + '.bind("<Enter>",lambda event,x=i: btn_highlight(x) )')
    exec(temp_frame + '.bind("<Leave>",lambda event,x=i: btn_unhighlight(x) )')
    exec(temp_frame + '.bind("<Button-1>",lambda event,x=i: btn_press(x) )')
    exec(temp_frame + ".bind('<Button-4>', lambda event: canvas.yview('scroll', -1, 'units'))")
    exec(temp_frame + ".bind('<Button-5>', lambda event: canvas.yview('scroll', 1, 'units'))")
    exec(temp_frame + '.grid()')

    title = ''
    exec('title = "t" + str(i)')
    exec(title + ' = Label(' + temp_frame + f', text="sample title {i}",font="Consolas 18 normal", bg=bg_, fg=fg)')
    exec(title + '.bind("<Button-1>",lambda event,x=i: btn_press(x) )')
    exec(title + '.bind("<Enter>",lambda event,x=i: btn_highlight(x) )')
    exec(title + ".bind('<Button-4>', lambda event: canvas.yview('scroll', -1, 'units'))")
    exec(title + ".bind('<Button-5>', lambda event: canvas.yview('scroll', 1, 'units'))")
    exec(title + '.grid(sticky="w", ipadx=10)')

    m_padding = ''
    exec('m_padding = "p" + str(i)')
    exec(m_padding + ' = Label(' + temp_frame + ', text="", bg=bg_, fg=bg_)')
    exec(m_padding + '.bind("<Enter>",lambda event,x=i: btn_highlight(x) )')
    exec(m_padding + '.bind("<Button-1>",lambda event,x=i: btn_press(x) )')
    exec(m_padding + ".bind('<Button-4>', lambda event: canvas.yview('scroll', -1, 'units'))")
    exec(m_padding + ".bind('<Button-5>', lambda event: canvas.yview('scroll', 1, 'units'))")
    exec(m_padding + '.grid(padx=350, pady=10)')

    description = ''
    exec('description = "d" + str(i)')
    exec(description + ' = Label(' + temp_frame + f', text="sample description {i}"'
                                                  f', font="Consolas 16 normal", bg=bg_, fg=fg)')
    exec(description + '.bind("<Enter>",lambda event,x=i: btn_highlight(x) )')
    exec(description + '.bind("<Button-1>",lambda event,x=i: btn_press(x) )')
    exec(description + ".bind('<Button-4>', lambda event: canvas.yview('scroll', -1, 'units'))")
    exec(description + ".bind('<Button-5>', lambda event: canvas.yview('scroll', 1, 'units'))")
    exec(description + '.grid(sticky="w", padx=10, pady=(0,10))')

    m_padding = ''
    exec('m_padding = "m_p" + str(i)')
    exec(m_padding + ' = Label(scrollable_frame, bg="#262C3A", highlightthickness=0)')
    exec(temp_frame + '.bind("<Enter>",lambda event,x=i: btn_highlight(x) )')
    exec(m_padding + ".bind('<Button-4>', lambda event: canvas.yview('scroll', -1, 'units'))")
    exec(m_padding + ".bind('<Button-5>', lambda event: canvas.yview('scroll', 1, 'units'))")
    exec(m_padding + '.grid(ipady=10, ipadx=355)')

canvas.pack(side="left", fill="both", expand=True)

container.place(x=10, y=300)
