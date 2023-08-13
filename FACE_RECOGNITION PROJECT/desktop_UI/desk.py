import customtkinter as ctk
import tkinter



root=ctk.CTk()

ctk.set_default_color_theme("green")

root.geometry('1520x880')
root.title('FAce_recognition')

#heading frame
frame1=ctk.CTkFrame(root,width=1520,height=80)
frame1.pack()
#heading frame title
title_label=ctk.CTkLabel(frame1,height=80,width=1520,bg_color="blue",text="Face Recognition Database",font=ctk.CTkFont(size=30,weight='bold'))
title_label.pack()

#navigation bar
frame_nav=ctk.CTkFrame(root,width=1400,height=50)
frame_nav.pack(padx=(10),pady=(10,10))
#navigation buttons

nav_button_addface=ctk.CTkButton(frame_nav,width=20,height=5,bg_color="blue",text="Add Face",font=ctk.CTkFont(size=30,weight='bold'))
nav_button_addface.pack(pady=(0))

nav_button_adddata=ctk.CTkButton(frame_nav,width=20,height=5,bg_color="blue",text="Add Face",font=ctk.CTkFont(size=30,weight='bold'))
nav_button_adddata.pack(pady=(0,0))

root.mainloop()