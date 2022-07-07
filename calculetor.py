from tkinter import *
root=Tk()
root.geometry("498x300")
root.title('Calculetor')
#justify="right"
#x.set(x.get()+q)
#evel(z)

x=StringVar()
e=Entry(root,font=("Arial",35),width=19,justify="right",textvariable=x)
e.grid(columnspan=4)
root.configure(bg="black")

def show(q):
  x.set(x.get()+q)

def ans():
  z=x.get()
  x.set(eval(z))

def cal():
  x.set("")

b1=Button(root,text="7",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("7"))
b1.grid(pady=3,row=1,column=0)
b2=Button(root,text="8",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("8"))
b2.grid(pady=3,row=1,column=1)
b3=Button(root,text="9",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("9"))
b3.grid(pady=3,row=1,column=2)
b4=Button(root,text="+",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("+"))
b4.grid(pady=3,row=1,column=3)


b5=Button(root,text="4",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("4"))
b5.grid(pady=0,row=2,column=0)
b6=Button(root,text="5",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("5"))
b6.grid(pady=0,row=2,column=1)
b7=Button(root,text="6",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("6"))
b7.grid(pady=0,row=2,column=2)
b8=Button(root,text="-",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("-"))
b8.grid(pady=0,row=2,column=3)


b9=Button(root,text="1",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("1"))
b9.grid(pady=3,row=3,column=0)
b10=Button(root,text="2",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("2"))
b10.grid(pady=3,row=3,column=1)
b11=Button(root,text="3",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("3"))
b11.grid(pady=3,row=3,column=2)
b12=Button(root,text="*",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("*"))
b12.grid(pady=3,row=3,column=3)


b13=Button(root,text="C",font=("Arial",20),width=7,bg="gray",fg="white",command=cal)
b13.grid(pady=0,row=4,column=0)
b14=Button(root,text="0",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("0"))
b14.grid(pady=0,row=4,column=1)
b15=Button(root,text="=",font=("Arial",20),width=7,bg="gray",fg="white",command=ans)
b15.grid(pady=0,row=4,column=2)
b16=Button(root,text="/",font=("Arial",20),width=7,bg="gray",fg="white",command=lambda:show("/"))
b16.grid(pady=0,row=4,column=3)

root.mainloop()
