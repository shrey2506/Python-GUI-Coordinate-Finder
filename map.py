from tkinter import *
import webbrowser
basic = Tk()

basic.geometry("200x200")

l1 = Label(basic,text="Custom Map Search")
l1.grid(row=0, columnspan=4)

l2 = Label(basic,text="Latitude")
l2.grid(row=2, column=1)

#n1=StringVar()
e1 = Entry(basic)
e1.grid(row=2, column=3)

l3=Label(basic,text="Longitude")
l3.grid(row=3,column=1)

#n2=StringVar()
e2=Entry(basic)
e2.grid(row=3,column=3)




def glob():
    m1=e1.get()
    m2=e2.get()
    pr = ("https://www.google.com/maps/search/?api=1&query=%s,%s"%(m1,m2))
    webbrowser.open(pr)

b1=Button(basic,text="Search",command=glob)
b1.grid(row=4,column=2)






basic.mainloop()
