from tkinter import *
import os
def restart():
    os.system("shutdown/s/t 5")
def restart_time():
    os.system("shutdown/r/t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown/s/t 1")

st=Tk()
st.title("Shut down app")
st.geometry("500x500")
st.config(bg="skyblue")

r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold" ),
                relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=100)

rt_button=Button(st,text="Restart Time",font=("Time New Roman",10,"bold" ),
                 relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=100)

rl_button=Button(st,text="Log-Out",font=("Time New Roman",10,"bold" ),
                 relief=RAISED,cursor="plus",command=logout)
rl_button.place(x=150,y=270,height=50,width=100)

rs_button=Button(st,text="Shut-Down",font=("Time New Roman",10,"bold" ),
                 relief=RAISED,cursor="plus",command=shutdown)
rs_button.place(x=150,y=370,height=50,width=100)

st.mainloop()