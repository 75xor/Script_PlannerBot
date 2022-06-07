from tkinter import *
from tkinter.ttk import *
from tkcalendar import *
from datetime import *
d = datetime.now()

root = Tk()
root.title('Planner Bot')
root.geometry("600x400")

cal = Calendar(root,selectmode="day",year=d.year,month=d.month,day=d.day)
cal.pack(padx=20,pady=20,fill="both",expand=True)

def grab_date():
    my_label.config(text="Today's Date is "+cal.get_date())

but = Button(root,text="get Date",command=grab_date)
but.pack(pady=20)

my_label = Label(root,text="")
my_label.pack(pady=20)

root.mainloop()
