from datetime import *
from tkinter import *




def get_age():
    age = datetime.now().year - int(age_entry.get())
    user_age.set(f'You are {age} year old!')


# setting
root = Tk()

root.geometry('320x530')
root.title('Age')
root.resizable(width=False, height=False)
root.configure(bg='gray15')

root.iconbitmap(r'icon.ico')


user_name = StringVar()
user_age = StringVar()
# frames
# how old are you frame
how_old_frame = Frame(root, width=320, height=50, bg='dark slate gray')
how_old_frame.pack(side=TOP)

# border frame 1

border_frame = Frame(root, width=320, height=5, bg='DarkSeaGreen3')
border_frame.pack(side=TOP)

# enter age frame

enter_age_frame = Frame(root, width=320, height=120, bg='plum4')
enter_age_frame.pack(side=TOP)

# border frame 2

border_frame = Frame(root, width=320, height=5, bg='DarkSeaGreen3')
border_frame.pack(side=TOP)

# age entry frame

age_entry_frame = Frame(root, width=320, height=70, bg='dark slate gray')
age_entry_frame.pack(side=TOP)

# border frame 3

border_frame = Frame(root, width=320, height=5, bg='white')
border_frame.pack(side=TOP)

# out put frame

output_frame = Frame(root, width=320, height=50, bg='DarkSeaGreen3')
output_frame.pack(side=TOP)

# border frame 4

border_frame = Frame(root, width=320, height=5, bg='white')
border_frame.pack(side=TOP)

# eye img frame

eye_frame = Frame(root, width=320, height=280, bg='gray17')
eye_frame.pack(side=TOP)


# entry

# age entry

age_entry = Entry(age_entry_frame, width=20)
age_entry.place(x=110, y=25)


# Labels
# how old img label

how_old_img = PhotoImage(file='how_old.png')
how_old_img_label = Label(how_old_frame, image=how_old_img,
                          width=320, height=50, bg='dark slate gray')
how_old_img_label.place(x=2)

# enter age img label

enter_age_img = PhotoImage(file='enter_age.png')
enter_age_img_label = Label(enter_age_frame, image=enter_age_img,
                            width=320, height=100, bg='plum4')
enter_age_img_label.place(x=0, y=10)


# age entry label

age_entry_label = Label(age_entry_frame, text='Year of Birth: ',
                        bg='dark slate gray', font=('Tahoma'))
age_entry_label.place(x=7, y=22)

# out put label

output_label = Label(output_frame, textvariable=user_age, width=30,
                     height=2,  font=('Tahoma'), bg='papaya whip', fg='gray17')
output_label.place(x=22, y=3)

# eye image label
frameCnt = 12
eye_img = [PhotoImage(file='girl.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = eye_img[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    eye_img_label.configure(image=frame)
    root.after(100, update, ind)

eye_img_label = Label(eye_frame, width=320, height=270)
eye_img_label.place(x=0)
root.after(0, update, 0)
# Buttons

submit_button = Button(age_entry_frame, text='Submit', font=(
    'Tahoma'), bg='DarkSeaGreen3', command=lambda: get_age())
submit_button.place(x=245, y=14)


root.mainloop()
